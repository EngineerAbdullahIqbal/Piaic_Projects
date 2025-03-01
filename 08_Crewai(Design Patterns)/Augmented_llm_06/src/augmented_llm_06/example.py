from crewai import Agent , Task , Crew , Process
from dotenv import load_dotenv , find_dotenv
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
from crewai import  LLM
import os


load_dotenv(find_dotenv())

llm1 = LLM(
    model="gemini/gemini-2.0-flash",
)

google_embedder = {
    "provider": "google",
    "config": {
         "model": "models/text-embedding-004",
         "api_key": os.getenv('GEMINI_API_KEY'),
         }
}

content="Abdullah is An Agentic AI Engineer Live In Pakistan he is 18 yeras old."
knowledge_source = StringKnowledgeSource(
    content=content
)


agent = Agent(
    role="About user",
    goal="Answer About user",
    backstory="You are a master at understanding people and their preferences",
    llm=llm1,
    verbose=True,
    allow_delegation=False
)

task = Task(
    description="Answer folowing questions about user questions: {question}",
    expected_output="An Answer to the question",
    agent=agent
)

crew = Crew(
    memory=True,
    agents=[agent],
    tasks=[task],
    verbose=True,
    process=Process.sequential,
    knowledge_sources=[knowledge_source], # Enable knowledge by adding the sources here. You can also add more sources to the sources list.
    embedder=google_embedder,
)

def kickoff():
    output = crew.kickoff(inputs={"question": "Where Abdullah Live and how old he is."})
    print(output) 

