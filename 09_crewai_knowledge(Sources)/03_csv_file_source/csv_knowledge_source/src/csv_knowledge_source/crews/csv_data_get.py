from crewai import Agent, Task, Crew, Process
from crewai.knowledge.source.csv_knowledge_source import CSVKnowledgeSource
from crewai import LLM
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

my_llm = LLM(
    model=os.getenv('MODEL'),
    api_key=os.getenv("GEMINI_API_KEY")
)

google_embedder = {
    'provider': 'google',
    'config': {
        'model': "models/text-embedding-004",
        'api_key': os.getenv('GEMINI_API_KEY')
    }
}

csv_knowledge_source = CSVKnowledgeSource(
    name="csv_file_knowledge_source",
    file_paths=['Extended_Company_FAQ.csv'] # Fixed path
)

agent = Agent(
    role="User Profile Expert",
    goal="Extract and analyze user information from {path}",
    backstory="Specialist in user behavior analysis and preference mapping",
    verbose=True,
    allow_delegation=False,
    llm=my_llm,
)

task = Task(
    description="Analyze user data at {path} to answer: {question} and also memorize the user question",
    expected_output="Structured response with verified information",
    agent=agent,
)

crew = Crew(
    memory=True,
    agents=[agent],
    tasks=[task],
    verbose=True,
    process=Process.sequential,
    knowledge_sources=[csv_knowledge_source],
    embedder=google_embedder
)

def kickoff():
    result = crew.kickoff(
        inputs={
            "question": "what is my first question.",
            'path': "Knowledge\Extended_Company_FAQ.csv",
        }
    )
    print(result)