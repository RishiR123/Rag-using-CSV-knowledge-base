# Project Name: Knowledge Chatbot using Google Gemini and LangChain

## Description

This project implements a knowledge chatbot using Google Gemini and LangChain, leveraging embeddings, CSV file loading, and vector search capabilities to generate human-like responses based on provided data.

The goal of this project is to integrate various libraries like LangChain and Google Generative AI to create a conversational interface capable of handling queries and providing accurate responses based on CSV data.

## Features

- **CSV Data Loader**: Loads knowledge base from CSV files.
- **Google Gemini Model**: Utilizes the Gemini-1.5 model for content generation.
- **LangChain Integration**: Uses LangChain to create and manage embeddings.
- **Vector Search**: Implements cosine similarity search for fetching relevant responses from the knowledge base.

## Requirements

- Python 3.8+ (i used python 3.12.3 as it is being most stable as of now)
- `langchain_community`
- `google-generativeai`
- `dotenv`
- `langchain_google_genai`


## Installation

Follow these steps to set up the project locally:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/Rag-using-CSV-knowledge-base.git
    cd your-repository
    ```

2. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file and add your Google API key:

    ```bash
    GOOGLE_API_KEY=your-api-key-here
    ```

4. Run the project:

    ```bash
    jupyter notebook
    ```

    Navigate to the notebook file and run the cells to interact with the chatbot.

## Usage

1. **Load CSV Data**: Load knowledge data into the chatbot by uploading a CSV file containing questions and responses.

2. **Query the Chatbot**: Once the data is loaded, you can query the chatbot for responses. The chatbot will use vector search to find the best possible match for the query.

3. **Adjust Model**: Modify the model and API settings by configuring the `google-generativeai` API key and selecting a model like `gemini-1.5-flash`.

## Author

- **Author**: Zakariya (Rishi R)
- **GitHub**: [Rishi123](https://github.com/RishiR123)
- **Email**: [rishiininternet@Gmail.com]

