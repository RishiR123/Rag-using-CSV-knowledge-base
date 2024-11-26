from langchain_community.document_loaders.csv_loader import CSVLoader
import google.generativeai as gemini
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os

# Settings our Model
load_dotenv()
api = os.getenv("google")

gemini.configure(api_key=api)

model = gemini.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("hi im zakariya")
response.text

# Loading the Csv - Knowledge base
loader = CSVLoader(file_path="data.csv", source_column="input")
data = loader.load()

# embeddings setup
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api, task_type="retrieval_query")

# Text chunks into embeddings
# Will take around 1 - 5 mins depending on the CPU/GPU
text_data = [doc.page_content for doc in data]
vectors = [embeddings.embed_query(text) for text in text_data]

# Vector Database
vectordb = Chroma.from_texts(
    texts=text_data,  
    embedding=embeddings,
    persist_directory="rova_db"  
)

# Cosine Similarity search
query = input("Enter the question: ")
search_results = vectordb.similarity_search(query, k=3)

print(search_results)

# Combine search results as context
combined_context = "\n\n".join([res.page_content for res in search_results])

# Make it a single prompt to avoid type error
final_prompt = f"User's Query: {query}\n\nContext:\n{combined_context}\n\nProvide a concise, human-like response based on the context above."

# Directly pass the query and context to the model
response = model.generate_content(final_prompt)

# Extract generated text
generated_text = response.candidates[0].content.parts[0].text

print("Generated Text:", generated_text)
