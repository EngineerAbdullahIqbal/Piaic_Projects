from crewai import Agent , Task , Crew , Process , LLM
from crewai.knowledge.source.crew_docling_source import CrewDoclingSource
from dotenv import load_dotenv , find_dotenv
import os

load_dotenv(find_dotenv())  


google_embader = {
    'provider':'google',
    'config':{
        'model':'models/text-embedding-004',
        'api_key': os.getenv('GEMINI_API_KEY')
    }
}

llm1 = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=os.getenv('GEMINI_API_KEY')
)


docling_source = CrewDoclingSource(
    file_paths=[
        "https://medium.com/one-minute-machine-learning/attention-is-all-you-need-2017-one-minute-summary-f3c7509f2144",
        "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"
    ]
)


agent = Agent(
    role="About Paper",
    goal="You know Every Thing About Paper reading",
    backstory="YOu are master in Understanding Paper and there content.",
    verbose=True,
    allow_delegation=False,
    llm=llm1
)

task = Task(
    description="Answer The following questions about paper and there content '{question}'",
    expected_output="An Answer The Questions",
    agent=agent
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    knowledge_sources=[docling_source],
    process=Process.sequential,
    Memory=True,
    embedder=google_embader
)


def kickoff():
    output = crew.kickoff(inputs={"question":"What is Transformers?"})
    print(output)
