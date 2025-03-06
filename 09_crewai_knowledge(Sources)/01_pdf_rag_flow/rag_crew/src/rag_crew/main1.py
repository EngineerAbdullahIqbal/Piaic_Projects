from crewai.flow import Flow , start
from rag_crew.crews.rag_data_crew.rag_crew import RAGDataCrew


class RagFlow(Flow):

    @start()
    def get_data(self):
        result = RAGDataCrew().crew().kickoff(inputs={"data_path": "Knowledge/Company_FAQ.pdf",
                                                      "question": "What are your shipment times?"})
        
        return result.raw

def kickoff():
    final_result = RagFlow()
    final_result.kickoff()