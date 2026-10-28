#page 1

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import engine

#1. data load

loader = PyPDFLoader(r"D:\JEEVA\GENAI\MVP_RAG\Resume.pdf")
text = loader.load()
# print(len(text))

#2. chunking

data_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 800,
    chunk_overlap=100
)

chunk = data_splitter.split_documents(text)
# print(chunk)
# print(len(chunk))

engine.add_documents(chunk)






