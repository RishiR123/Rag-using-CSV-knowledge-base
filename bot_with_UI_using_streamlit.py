import streamlit as st
from langchain_community.document_loaders.csv_loader import CSVLoader
import google.generativeai as gemini
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api = os.getenv("google")

# Configure the Gemini API
gemini.configure(api_key=api)

# Model selection
model = gemini.GenerativeModel("gemini-1.5-flash")

# Streamlit UI
st.title("CSV-Based AI Assistant")
st.sidebar.header("Configuration")
csv_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if csv_file:
    # Load CSV Knowledge Base
    st.sidebar.success("CSV file loaded successfully!")
    loader = CSVLoader(file_path=csv_file.name, source_column="input")
    data = loader.load()

    # Display dataset preview
    st.write("### Preview of the Knowledge Base")
    st.dataframe(data[:5])

    # Setup embeddings
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=api,
        task_type="retrieval_query"
    )

    # Create vectors and vector database
    st.info("Generating embeddings, this may take a few minutes...")
    text_data = [doc.page_content for doc in data]
    vectors = [embeddings.embed_query(text) for text in text_data]

    vectordb = Chroma.from_texts(
        texts=text_data,
        embedding=embeddings,
        persist_directory="rova_db"
    )
    st.success("Vector database created!")

    # Query Section
    st.write("### Ask a Question")
    query = st.text_input("Enter your question:")
    if st.button("Get Answer") and query:
        # Perform similarity search
        search_results = vectordb.similarity_search(query, k=3)
        combined_context = "\n\n".join([res.page_content for res in search_results])

        # Construct the final prompt
        final_prompt = (
            f"User's Query: {query}\n\nContext:\n{combined_context}\n\n"
            "Provide a concise, human-like response based on the context above."
        )

        # Generate response
        response = model.generate_content(final_prompt)
        generated_text = response.candidates[0].content.parts[0].text

        #

