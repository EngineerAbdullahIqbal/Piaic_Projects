from crewai.flow.flow import Flow , start , listen # Importing the Flow class and the decorators
from litellm import completion # Importing the completion function from the litellm module

api_key = "AIzaSyBGKU70IqteZ9jVg7WHLuLnr30UfRCG9Mg"

class CityFunFact(Flow):

    @start()
    def genertate_random_city(self):
        result = completion(
            model="gemini/gemini-1.5-flash",
            api_key=api_key,
            messages=[{"content":"Generate any random city name From Pakistan",
                       "role":"user"}]
        )
        city = result['choices'][0]['message']['content']
        print(f"City Name: {city}")
        return city
    
    @listen(genertate_random_city)
    def genertate_fun_fact(self , city_name):
        result = completion(
            model="gemini/gemini-2.0-flash-exp",
            api_key=api_key,
            messages=[{"content":f"Write some FunFAct About {city_name} City",
                       "role":"user"}]
        )
        fun_fact = result['choices'][0]['message']['content']
        print(f"City Name: {fun_fact}")
        self.state['fun_fact'] = fun_fact

    @listen(genertate_fun_fact)
    def save_fun_fact(self):
        with open('fun_fact.md' , 'w') as f:
            f.write(self.state['fun_fact'])
            return self.state['fun_fact']

def kickoff():
    obj = CityFunFact()
    result = obj.kickoff()
    print(result)


def plot():
    obj = CityFunFact()
    obj.plot()