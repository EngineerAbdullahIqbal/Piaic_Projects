from crewai.flow import Flow , start , listen
from litellm import completion 
from dotenv import load_dotenv , find_dotenv

load_dotenv(find_dotenv())

class SimpleOrchestrationFlow(Flow):

    model = "gemini/gemini-2.0-flash"

    @start()
    def write_Essay(self):
        output = completion(
            model=self.model,
            messages=[{
                "role": "user",
                "content": "Write an essay on the importance of AI in 2025."
            }],
        )
        essay =  output['choices'][0]['message']['content']
        print(f"Essay: {essay}")
        return essay
    
    @listen("write_Essay")
    def summarize_Essay(self, essay):
        output = completion(
            model=self.model,
            messages=[{
                "role": "user",
                "content": f"Summarize the essay: {essay}"
            }],
        )
        summary =  output['choices'][0]['message']['content']
        print(f"Summary: {summary}")
        return summary
    
    @listen("summarize_Essay")
    def write_Conclusion(self, summary):
        output = completion(
            model=self.model,
            messages=[{
                "role": "user",
                "content": f"Write a conclusion for the essay: {summary}"
            }],
        )
        conclusion =  output['choices'][0]['message']['content']
        print(f"Conclusion: {conclusion}")
        return conclusion
    

def kickoff():
    flow = SimpleOrchestrationFlow()
    final_output = flow.kickoff()
    print(f"Final Output: {final_output}")

def plot():
    flow = SimpleOrchestrationFlow()
    flow.plot()
