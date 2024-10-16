import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.llms.groq import Groq
from urllib.parse import urlparse, parse_qs
from streamlit_option_menu import option_menu
from llama_index.embeddings.openai import OpenAIEmbedding
from dotenv import load_dotenv

load_dotenv()
Settings.embed_model = OpenAIEmbedding(api_key=os.getenv('OPENAI_API_KEY'))
Settings.llm = Groq(model="llama3-70b-8192", api_key=os.getenv("GROQ_API_KEY"))

def infoBot(prompt):
    # Read documents from the reader
    print("Loading documents...")
    
    docs = SimpleDirectoryReader("data").load_data()
    print(f"Loaded {len(docs)} documents.")

    # Create the index
    print("Creating the index...")
    index = VectorStoreIndex.from_documents(docs)
    print("Index created.")

    # Set up the query engine
    query_engine = index.as_query_engine()
    response = query_engine.query(prompt)
    # Print the response
    print("Response: ")
    print(response)
    return response
