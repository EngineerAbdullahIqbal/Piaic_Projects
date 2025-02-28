from crewai.flow import Flow , start , listen 
from litellm import completion
from dotenv import load_dotenv , find_dotenv
import random

load_dotenv(find_dotenv())

# Define the flow class
class PromptChainingFlow(Flow):

    model = "gemini/gemini-1.5-flash"
    Dishes = ["biryani", "Beef" , "Chicken" , "Karai" , "Pulao" , "Korma" , "Nihari" , "Haleem" , "Karahi" , "Kofta"]
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
        self.select_dishes = result
        print(f"User selected the dish: {self.select_dishes}")
        return self.select_dishes
        
         
    

    @listen(select_dish)
    def make_recipe(self , dish):
        output = completion(
            model= self.model,
            messages=[
                {"role": "user" , 
                 "content": f"Write a complete recipe of the dish {dish}"}
            ],
        )
        recipe = output['choices'][0]['message']['content']
        print(f"Recipe for {self.select_dishes} is: {recipe}")
        return recipe
    
    @listen(make_recipe)
    def tips(self , dish):
        output = completion(
            model= self.model,
            messages=[
                {"role": "user" , 
                 "content": f"Give 5 tips to surve {dish} for guests"}
            ],
        )
        tips = output['choices'][0]['message']['content']
        print(f"Recipe for {self.select_dishes} is: {tips}")
        return tips
    

def kickoff():
    flow = PromptChainingFlow()
    final_output = flow.kickoff()
    print(final_output)

def plot():
    flow = PromptChainingFlow()
    flow.plot()




