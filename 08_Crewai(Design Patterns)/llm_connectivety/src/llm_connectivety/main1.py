from crewai.flow import Flow, start, listen
from llm_connectivety.crews.dev_crew.dev_crew import DevCrew


class DevFlow(Flow):
    @start()
    def code_writer_crew(self):
        output = DevCrew().crew().kickoff(inputs= 
                                   {"problem": "Write a Simple Python Code Without python type hints and solve the given '{problem}'."}
                                )
        return output.raw
    
def kickoff():
    flow = DevFlow()
    flow.kickoff()