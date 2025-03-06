from crewai import Agent , Task , Crew , Process
from crewai.project import CrewBase , agent , task , crew
from dotenv import load_dotenv , find_dotenv
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
from crewai import LLM
import os

load_dotenv(find_dotenv())
my_llm = LLM(
    model=os.getenv("MODEL"),
    api_key=os.getenv("GEMINI_API_KEY"),
)

# Knowledge sources

pdf_knowledge_source = PDFKnowledgeSource(
    name="pdf_knowledge_source",
    file_paths=["Company_FAQ.pdf"],
)

# Provider Added 
google_embeder = {
    'provider': 'google',
    'config': {
         "model": "models/text-embedding-004",
         "api_key": os.getenv('GEMINI_API_KEY')
    }
}



@CrewBase
class RAGDataCrew:

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def insight_miner(self) -> Agent:
        return Agent(
            config=self.agents_config["insight_miner"],                        
            llm=my_llm,
        )
    
    @agent
    def knowledge_navigator(self) -> Agent:
        return Agent(
            config=self.agents_config["knowledge_navigator"],
            llm=my_llm,
        )

    @task
    def document_intelligence(self) -> Task:
        return Task(
            config=self.tasks_config["document_intelligence"],
        )
    
    @task
    def precision_qa(self) -> Task:
        return Task(
            config=self.tasks_config["precision_qa"],
        )


    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=True,
            knowledge_sources=[pdf_knowledge_source],
            embedder=google_embeder , # Remove the brackets []
    )
