from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from pypdf import PdfReader

#Resume analyzer using RAG and LLM
#Retrive the data from file / RAG - Document loading
def extract_pdf(file):
    reader = PdfReader(file)
    text =" " #str type
    for page in reader.pages:
        text +=page.extract_text()
    return text

# Splitting Document
def split_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    return splitter.split_text(text)

#Embedding & Vector storage
def create_vector_text(text):
    chunks = split_text(text)
    docs = [Document(page_content=c) for c in chunks]
    embedding = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
    vectorstore = FAISS.from_documents(docs, embedding)
    return vectorstore
