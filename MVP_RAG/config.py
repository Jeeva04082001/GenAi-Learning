# LLM model, embedding model, Chroma Engine

#page 2


from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()
import os 
gemini_api_key = os.getenv("GEMINI_API_KEY_RAG")
llm = ChatGroq(model="openai/gpt-oss-120b")

# res=llm.invoke("whta is your name")
# print(res)

embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2",api_key=gemini_api_key)

# print(len(embedding.embed_query("what is your name")))

engine = Chroma( 
        embedding_function=embedding,
        collection_name="MVP-RAG",
        persist_directory="chroma.db"

)

