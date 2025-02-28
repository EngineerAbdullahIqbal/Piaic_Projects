from crewai.flow import Flow , start , listen , router
from litellm import completion
from dotenv import load_dotenv , find_dotenv
import random

load_dotenv(find_dotenv())

class RoutingFlow(Flow):

    model = "gemini/gemini-1.5-flash"
    Dishes = ["biryani", "Beef" , "Chicken"]
    select_dishes = random.choice(Dishes)

    @start()
    def select_dish(self):
        output = completion(
            model= self.model,
            messages=[
                {"role": "user" , 
                 "content": f"Select one random dish from the menu: {self.select_dishes}"}
            ],
        )
        result = output['choices'][0]['message']['content']
        self.state['biryani'] = 'biryani' in result.lower()
        self.state['Beef'] = 'Beef' in result.lower()
        self.state['Chicken'] = 'Chicken' in result.lower()
        self.state['Karai'] = 'Karai' in result.lower()
        self.state['Pulao'] = 'Pulao' in result.lower()
        print(f"User selected the dish: {result}")
        return result
        
    @router(select_dish)
    def route_dish(self):
        if self.state.get('biryani'):
            return "biryani"
        elif self.state.get('Beef'):
            return "Beef"
        else:
            return "Chicken"
        
        
    @listen('biryani')
    def joke_about_biryani(self):
        output = completion(
            model= self.model,
            messages=[
                {"role": "user" , 
                 "content": "write a joke about biryani"}
            ],
        )
        result = output['choices'][0]['message']['content']
        print(f"About biryani: {result}")
        return result
    
    @listen('Beef')
    def history_of_beef(self):
        output = completion(
            model= self.model,
            messages=[
                {"role": "user" , 
                 "content": "tell me the history of beef"}
            ],
        )
        result = output['choices'][0]['message']['content']
        print(f"About beef: {result}")
        return result
    
    @listen('Chicken')
    def benifits_of_chicken(self):
        output = completion(
            model= self.model,
            messages=[
                {"role": "user" , 
                 "content": "explain the benefits of eating chicken"}
            ],
        )
        result = output['choices'][0]['message']['content']
        print(f"About chicken: {result}")
        return result
    
    
    
    
def kickoff():
    flow = RoutingFlow()
    final_output = flow.kickoff()
    print(final_output)

def plot():
    flow = RoutingFlow()
    flow.plot()
    

    
