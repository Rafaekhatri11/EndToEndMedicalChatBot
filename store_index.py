from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")

# os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
index_name="medical-bot"
pinecone_store = PineconeVectorStore(embedding=embeddings, pinecone_api_key=PINECONE_API_KEY, index_name=index_name)
docsearch=pinecone_store.from_texts(
[t.page_content for t in text_chunks],
embeddings,
index_name=index_name,
)   


