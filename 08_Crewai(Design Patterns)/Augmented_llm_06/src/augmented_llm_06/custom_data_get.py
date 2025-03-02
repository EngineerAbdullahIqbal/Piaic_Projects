import os
from crewai import Crew, Process , Task , Agent
from mem0 import MemoryClient
from crewai import LLM
from dotenv import load_dotenv , find_dotenv

load_dotenv(find_dotenv())


my_llm = LLM(
    model='gemini/gemini-1.5-flash',
    api_key=os.getenv('GOOGLE_API_KEY'),
)

# Set environment variables for Mem0
os.environ["MEM0_API_KEY"] = os.getenv("MEM0_API_KEY")
# Step 1: Record preferences based on past conversation or user input
client = MemoryClient()
# messages = [
#     {"role": "user", "content": "Hi there! I'm planning a vacation and could use some advice."},
#     {"role": "assistant", "content": "Hello! I'd be happy to help with your vacation planning. What kind of destination do you prefer?"},
#     {"role": "user", "content": "I am more of a beach person than a mountain person."},
#     {"role": "assistant", "content": "That's interesting. Do you like hotels or Airbnb?"},
#     {"role": "user", "content": "I like Airbnb more."},
# ]
# client.add(messages, user_id="Abdulllah")

# Step 2: Create a Crew with User Memory

# Create an agent with the knowledge store
agent = Agent(
    role="About User",
    goal="You know everything about the user.",
    backstory="""You are a master at understanding people and their preferences.""",
    verbose=True,
    allow_delegation=False,
    llm=my_llm,
)
task = Task(
    description="Answer the following questions about the user: {question}",
    expected_output="An answer to the question.",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    process = Process.sequential,
    verbose=True,
    memory=True,
    memory_config={
        "provider": "mem0",
        "config": {"user_id": "Abdullah"},
    }
)

def kickoff():
    output = crew.kickoff(inputs={"question": "What is your favorite vacation destination?"})
    print(output)