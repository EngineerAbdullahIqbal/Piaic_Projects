from crewai.flow import Flow, start
from multi_ai_agent.crews.multi_crew.multi_crew import MultiCrew


class multi_crew_flow(Flow):

    @start()
    def multi_crew(self):
        output = MultiCrew().crew().kickoff(
            inputs=
              {"problem": "take a lecture about AI and explain it to a student named '{topic}' and ask questions about '{topic}'.",
               "topic": "AI"
              })
        return output.raw
    
def kickoff():
    flow = multi_crew_flow()
    flow.kickoff()