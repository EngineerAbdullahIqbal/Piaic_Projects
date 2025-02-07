from crewai.flow.flow import Flow , start , listen
import time

class SimpleFlow(Flow):

    @start()
    def start(self):
        print("Start Running..")
        time.sleep(2)

    @listen(start)
    def listen1(self):
        print("After Starting Now Listening..")
        time.sleep(2)

    @listen(listen1)
    def listen2(self):
        print("Listening Again..")


def kickoff():
    obj = SimpleFlow()
    obj.kickoff()

def plot():
    obj = SimpleFlow()
    obj.plot()