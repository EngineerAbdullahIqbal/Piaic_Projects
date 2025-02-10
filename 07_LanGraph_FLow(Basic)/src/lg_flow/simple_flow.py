from langgraph.func import task, entrypoint
from dotenv import load_dotenv, find_dotenv
from litellm import completion
import os


_:bool = load_dotenv(find_dotenv())
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
langsmith_api_key  = os.getenv("langsmith_api_key ")


@task
def function1():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[
            {"role": "user", "content": "generate any random city name from pakistan only."}
        ],
        api_key=GOOGLE_API_KEY
    )
    city_name = response["choices"][0]["message"]["content"]
    print("step 1 generate city name", city_name)
    return city_name

@task
def function2(city_name):
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[
            {"role": "user", "content": f"write fun factors about {city_name} city."}
        ],
        api_key=GOOGLE_API_KEY
    )
    fun_fact = response["choices"][0]["message"]["content"]
    print("step 2 generate fun fact")
    return fun_fact

@task
def function3(fun_fact):
    with open("fun_fact.md", "w") as f:
        f.write(fun_fact)

    print("step 3save file")

@entrypoint()
def run_flow(input={}):
    city =function1().result()
    fun_fact = function2(city).result()
    function3(fun_fact)

def run_prompt_chaining_flow() -> None:
    run_flow.invoke({})