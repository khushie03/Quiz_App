from crewai import Agent 
from tools import serp_tool
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    verbose=True,
    temperature=0.5,
    google_api_key="LAIzaSyDM9xdKD9JDW_wu6p1gnCraUK3Ds-DPNc"
)

question_generator = Agent(
    role="Question Generator from a topic",
    goal="""Get the relevant questions based on a topic : {topic} in the format of Multiple Choice Questions
    for every question create {numberofquestions} based on the difficulty level of the question : {level}.
    Select questions such that among all the options only one option is correct.
    Format:
    **Question :**\n\nQuestion?\n\n(A) OptionA\n(B) OptionB\n(C) OptionC\n(D) OptionD\n\nResult: A,B,C,D
    """,
    llm=llm,
    verbose=True,
    memory=True,
    backstory=(
        "Based on the topic given to you, you need to create the number of questions asked for "
        "based on the difficulty level of the questions."
    ),
    tools=[],
)

previous_history_generator = Agent(
    role="Question Generator from a topic based on previous history",
    goal="""Get the relevant questions based on a topic : {topic} in the format of Multiple Choice Questions.
    For every question create {numberofquestions} based on the difficulty level of the question : {level}.
    Also, take user responses :  {responses} into account, and based on the mistakes made by the user,
    suggest similar questions related to it.
    Select questions such that among all the options only one option is correct.
    Format:
    **Question :**\n\nQuestion?\n\n(A) OptionA\n(B) OptionB\n(C) OptionC\n(D) OptionD\n\nResult: A,B,C,D
    """,
    llm=llm,
    verbose=True,
    memory=True,
    backstory=(
        "By analyzing the previous history of the user, you have to create questions "
        "so that the user can work better on their weak areas."
    ),
    tools=[],
)

additional_information = Agent(
    role="Provide necessary information to answer the question",
    goal="Based on the question : {question} specified, provide all the information necessary to answer the question. "
         "Make sure to provide a summarized view of information in around 200 words.",
    llm=llm,
    verbose=True,
    memory=True,
    backstory="By carefully analyzing the question, provide all the necessary information needed to answer it in a summarized form.",
    tools=[],
)

study_material = Agent(
    role="Provide all the relevant study material for a topic",
    goal="Provide all the relevant study material for a topic : {topic}, including links, snippets, and other research papers.",
    llm=llm,
    verbose=True,
    memory=True,
    tools=[serp_tool] 
)
