from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai import LLM
import os

llm1_model = LLM(os.getenv("MODEL"))
llm_key = LLM(os.getenv("GEMINI_API_KEY"))


@CrewBase
class DevCrew:
    """Dev Crew"""
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def junior_coder(self) -> Agent:
        return Agent(
            config=self.agents_config["junior_coder"],
            llm=llm1_model,
            llm_key=llm_key,
        )
    

    @agent
    def senior_coder(self) -> Agent:
        return Agent(
            config=self.agents_config["senior_coder"],
            llm=llm1_model,
            llm_key=llm_key,
        )
    
    @task
    def write_code(self) -> Task:
        return Task(
            config=self.tasks_config["code_writer"],
            llm=llm1_model,
            llm_key=llm_key,
        )

    @task
    def code_imporover(self) -> Task:
        return Task(
            config=self.tasks_config["code_improver"],
            llm=llm1_model,
            llm_key=llm_key,
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )