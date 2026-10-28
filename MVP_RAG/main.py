#page 4

from config import llm,engine
from langchain.tools import tool
from langchain.agents import create_agent

user_question = " what is her email"
@tool
def person_kb(user_question):
    "Need to user for the resume knowledge base"
    
    
    print("running tool")
    return engine.similarity_search(user_question, k=3)

# def chatbot(user_question):
    
#     search_content = person_kb(user_question=user_question)

#     system_prompt = """
#     Your name is sam, you are a helpful assistant for users,
#     answer in crisp and nicely

#     User asked this:
#     {user_question}
    
#     the context you have is:
#     {search_content}



#     """
    
#     response = llm.invoke(system_prompt)
    
#     return response.content

# answer=chatbot(user_question)

# print(answer)

def chatbot(user_question):
    system_prompt = """
    Your name is sam, you are a helpful assistant for users,
    answer in crisp and nicely with the context give for you
    """
    agent = create_agent(
        model=llm,
        system_prompt=system_prompt,
        tools=[person_kb],
        debug=True
    )
    response = agent.invoke({"messages":user_question})
    return response["messages"][-1].content

answer=chatbot(user_question)
print(answer)

