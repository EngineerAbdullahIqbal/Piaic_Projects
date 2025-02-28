from crewai.flow import Flow , start , listen
from litellm import completion
from dotenv import load_dotenv , find_dotenv

load_dotenv(find_dotenv())

class EvaluatorFlow(Flow):

    model="gemini/gemini-1.5-flash"

    @start()
    def simple_essay(self):
        output = completion(
            model =self.model,
            messages=[{
                "role": "user",
                "content": "Write a short essay about the history of the AI , With some mistakes"
            }]
        )
        esaay = output['choices'][0]['message']['content']
        print(f"Simple Essay : {esaay}")
        return esaay
    
    @listen('simple_essay')
    def improve_essay(self,esaay):
        output = completion(
            model =self.model,
            messages=[{
                "role": "user",
                "content": f"Improve the following essay : {esaay}"
            }]
    )         
        improved_essay = output['choices'][0]['message']['content']
        print(f"Improved Essay : {improved_essay}")
        return improved_essay
    
    @listen('improve_essay')
    def summarize_essay(self,improved_essay):
        output = completion(
            model =self.model,
            messages=[{
                "role": "user",
                "content": f"Summarize the following essay : {improved_essay}"
            }]
    )         
        summary = output['choices'][0]['message']['content']
        print(f"Summary : {summary}")
        return summary
    
    @listen('summarize_essay')
    def evaluate_essay(self,summary):
        output = completion(
            model =self.model,
            messages=[{
                "role": "user",
                "content": f"Rate the following essay : {summary}"
            }]
    )         
        rating = output['choices'][0]['message']['content']
        print(f"Rating : {rating}")
        return rating
        
    @listen('evaluate_essay')
    def final_essay(self,rating):
        output = completion(
            model =self.model,
            messages=[{
                "role": "user",
                "content": f"MAke improvements and Finalize the following essay After rating : {rating}"
            }]
    )         
        final_essay = output['choices'][0]['message']['content']
        print(f"Final Essay : {final_essay}")
        return final_essay


def kickoff():
    flow = EvaluatorFlow()
    final_result = flow.kickoff()
    print(final_result)

def plot():
    flow = EvaluatorFlow()
    flow.plot()