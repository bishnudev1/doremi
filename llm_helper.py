import os
import together
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms.base import LLM
from pydantic import Field
import textwrap
from dotenv import load_dotenv
from huggingface_hub import login

load_dotenv()

TOGETHER_API_KEY = os.getenv('TOGETHER_API_KEY')
HF_TOKEN = os.getenv('HF_TOKEN')

login(token=HF_TOKEN)

together.api_key = TOGETHER_API_KEY

# LLM Class
class LLAMA(LLM):
    model_name: str = Field()
    temperature: float = Field(default=0.4)

    def __init__(self, model, temperature=0.4):
        super().__init__(model_name=model, temperature=temperature)

    def _call(self, prompt, stop=None):
        output = together.Complete.create(
            prompt=prompt,
            model=self.model_name,
            temperature=self.temperature,
        )
        return output["choices"][0]["text"]

    @property
    def _llm_type(self):
        return "custom"

# Helper functions
def wrap_text_preserve_newlines(text, width=110):
    lines = text.split('\n')
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]
    return '\n'.join(wrapped_lines)

# Load and embed documents into Chroma
def load_and_embed_documents(urls):
    loader = UnstructuredURLLoader(urls=urls)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    
    embeddings = HuggingFaceInstructEmbeddings(
        model_name='hkunlp/instructor-xl',
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )
    
    db = Chroma.from_documents(texts, embeddings)
    return db

# Query responses
def query_responses(db, query, model_name="togethercomputer/llama-2-70b-chat", temperature=0.5):
    llm = LLAMA(model=model_name, temperature=temperature)
    retriever = db.as_retriever()
    rag = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    return rag(query)

def process_llm_response(llm_response):
    wrapped_result = wrap_text_preserve_newlines(llm_response['result'])
    return wrapped_result
