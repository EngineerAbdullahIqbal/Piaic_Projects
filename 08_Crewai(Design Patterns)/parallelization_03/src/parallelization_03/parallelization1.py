from crewai.flow import Flow , start , listen , or_
from litellm import completion
from dotenv import load_dotenv , find_dotenv

load_dotenv(find_dotenv())

class ParallelizationFlow(Flow):
    
    model = "gemini/gemini-1.5-flash"

    @start()
    def select_topic(self):
        response = completion(
            model=self.model,
            messages=[{
                "role": "user",
                "content": "Select a topic for a lecture for a student who is learning Python."
            }]
        )
        lecture = response['choices'][0]['message']['content']
        print(f"Selected Topic: {lecture}")
        return lecture
    
    @start()
    def explain_topic(self):
        response = completion(
            model=self.model,
            messages=[{
                "role": "user",
                "content": f"Explain the topic in a way a student can understand. given by the lecturer'."
            }]
        )
        explanation = response["choices"][0]["message"]["content"].strip()
        print(f"Explanation: {explanation}")
        return explanation
    
    @listen(or_("select_topic", "explain_topic"))
    def aggregate(self, lecture):

        print(f"Aggregated: {lecture}")

        return lecture
    

def kickoff():
    flow = ParallelizationFlow()
    output = flow.kickoff()
    print(output)

def plot():
    flow = ParallelizationFlow()
    flow.plot()


        
