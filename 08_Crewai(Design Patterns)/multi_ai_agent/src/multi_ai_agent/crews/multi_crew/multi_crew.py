from crewai import Agent , Crew , Task , Process 
from crewai.project import CrewBase , agent , task , crew
import os
from dotenv import load_dotenv , find_dotenv
from crewai import LLM


load_dotenv(find_dotenv())

llm_key = LLM(os.getenv("GEMINI_API_KEY"))
llm_model = LLM(os.getenv("MODEL"))

@CrewBase
class MultiCrew:

    
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def senior_lecturer(self)->Agent:
        return Agent(
            config=self.agents_config['senior_lecturer'],
            llm=llm_model,
            llm_key=llm_key,
        )
    
    @agent
    def smart_student(self)->Agent:
        return Agent(
            config=self.agents_config['smart_student'],
            llm=llm_model,
            llm_key=llm_key,
        )
    
    @agent
    def researcher(self)->Agent:
        return Agent(
            config=self.agents_config['researcher'],
            llm=llm_model,
            llm_key=llm_key,
        )
    
    @task
    def take_lecture(self)->Task:
        return Task(
            config=self.tasks_config["take_lecture"],
            llm=llm_model,
            llm_key=llm_key,

        )
    
    @task
    def question_about_lecture(self)->Task:
        return Task(
            config=self.tasks_config["question_about_lecture"],
            llm=llm_model,
            llm_key=llm_key,
        )
    
    @task
    def research_about_question(self)->Task:
        return Task(
            config=self.tasks_config["research_about_question"],
            llm=llm_model,
            llm_key=llm_key,
        )

    @crew
    def crew(self)->Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
