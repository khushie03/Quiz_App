from crewai import Agent 
from tools import *
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-pro",
                             verbose=True,
                             temperature=0.5,
                             google_api_key="AIzaSyDM9xdKD9JDW_wu6Lp1gnCraUK3Ds-DPNc")

question_generator = Agent(
    role = "Question Generator from a topic",
    goal = """Get the relevant questions based on a topic : {topic} in the format of Multiple Choice Questions
    for every question create {numberofquestions} based on the difficulty level of the question : {level}
    Select questions such that among all the option only one option is correct
    in the format : **Question :**\n\nQuestion?\n\n(A) OptionA\n(B) OptionB\n(C) OptionC\n(D) OptionD\n\nResult: A,B,C,D
    """ ,
    llm = llm,
    verbose = True ,
    memeory = True,
    backstory = ("Based on the topic given to you , you need to create the number of questions asked for based on the difficulty level of the questions"),
    tools = [],
)

previous_history_generator = Agent(
    role = "Question Generator from a topic based on previous history",
    goal = """Get the relevant questions based on a topic : {topic} in the format of Multiple Choice Questions
    for every question create {numberofquestions} based on the difficulty level of the question : {level}
    As well take user responses :  {responses} ,into account and basis on the mistakes made by user
    suggest similar question related to it
    Select questions such that among all the option only one option is correct
    in the format : **Question :**\n\nQuestion?\n\n(A) OptionA\n(B) OptionB\n(C) OptionC\n(D) OptionD\n\nResult: A,B,C,D
    """ ,
    llm = llm,
    verbose = True ,
    memeory = True,
    backstory = ("So here basically by analyzing the previous history of the user you have to create the question so that a user is anle to work better on its weak area"),
    tools = [],
)

additional_information = Agent(
    role = "Provide neccessary information to answer the question",
    goal = "Based on the question : {question} specified provide all the information neccessary in order to answer the question . Make sure to provide a summarized view of information in around 200 words",
    llm = llm,
    verbose = True,
    memory = True ,
    backstory = "By carefully analyzing the question provide all the neccessary information needed to answer that question in a summarized form",
    tools = [],
)

study_material = Agent(
    role = "Provide all the relevant study material for a topic",
    goal = "So here you need to provide all the relevant for a topic : {topic}that links snippets and other research papers",
    llm= llm,
    verbose = True ,
    memory = True , 
    tools = []
)


