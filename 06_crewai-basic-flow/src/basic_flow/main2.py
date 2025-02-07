from crewai.flow.flow import Flow , start , listen , router
import random


class CricketFunFact(Flow):

    @start()
    def SelectPlayer(self):
        print("Assalam-O-alikum!")
        Players = ["Babar Azam", "Shadab Khan","Saim Ayub"]

        select_player = random.choice(Players)
        self.state['player'] = select_player


    @router(SelectPlayer)
    def select_city(self):
        
        if self.state['player']=='Babar Azam':
            return 'Babar Azam'
        elif self.state['player']=='Shadab Khan':
            return 'Shadab Khan'
        else:
            return 'Saim Ayub'
        
    @listen('Babar Azam')
    def f1(self):
        # print(f"Write some fun fact about {self.state['player']} player.")
        return f"Write some fun fact about {self.state['player']} player."
    
    @listen('Shadaab Khan')
    def f2(self, player):
        # print(f"Write some fun fact about {self.state['player']} city.")
        return f"Write some fun fact about {self.state['player']} city."
    
    @listen('Saim Ayub')
    def f3(self, player):
        # print(f"Write some fun fact about {self.state['player']} city.")
        return f"Write some fun fact about {self.state['player']} city."

def kickoff():
    obj = CricketFunFact()
    result = obj.kickoff()
    print(result)

def plot():
    obj = CricketFunFact()
    obj.plot()
    
