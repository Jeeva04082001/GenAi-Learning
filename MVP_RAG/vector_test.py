#page 3

from config import engine

search= engine.similarity_search("college name", k=3)

print(search)


