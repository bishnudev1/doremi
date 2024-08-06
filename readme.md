# DoremiAI

DoremiAI is a Streamlit-based research assistant application that allows users to query documents and retrieve intelligent responses using large language models (LLMs). The application integrates Together AI and Hugging Face for LLM functionalities, providing a seamless and beautiful user experience.

## Features

- Load and embed documents from URLs.
- Query embedded documents using advanced AI models.
- Beautiful and responsive UI.
- Built-in support for Hugging Face and Together AI.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/DoremiAI.git
    cd DoremiAI
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory and add your Together AI API key and Hugging Face token:

    ```plaintext
    TOGETHER_API_KEY=your_together_api_key
    HF_TOKEN=your_hugging_face_token
    ```

## Usage

1. **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

2. **Open your browser and navigate to:**

    ```plaintext
    http://localhost:8501
    ```

3. **Use the application:**

    - **Load and Embed Documents:**
        - Enter URLs (comma-separated) into the provided text area.
        - Click the "Load and Embed Documents" button.
    
    - **Query the Documents:**
        - Enter your query into the text input.
        - Click the "Get Answer" button to retrieve the response and sources.

## Project Structure

- **.env**: Environment variables for API keys.
- **requirements.txt**: List of dependencies required by the project.
- **app.py**: Streamlit UI components and interaction logic.
- **llm_helper.py**: Helper methods for loading documents, embedding, and querying.

## Example Use Case

1. **Load and Embed Documents:**

    - Enter the URL "https://www.moneycontrol.com/stocksmarketsindia/" into the text area.
    - Click "Load and Embed Documents".

2. **Query the Documents:**

    - Enter "What is the price of Bitcoin?" into the query input.
    - Click "Get Answer" to retrieve the response and relevant sources.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any features, bug fixes, or enhancements.

## License

This project is licensed under the MIT License.
