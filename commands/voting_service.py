from threading import Timer
import random as rnd

class VotingService:
    def __init__(self):
        self.__voting_started = False
        self.__film_name_dict = {}
    
    def start_voting(self, time:float, voting_callback = None):
        timer = Timer(time, self.close_voting, [voting_callback])
        timer.start()
        self.__voting_started = True

    def close_voting(self, callback):
        print("Voting ended!")
        
        for key, value in self.__film_name_dict.items():
            print(key, "\t\t",value)

        key, result = rnd.choice(list(self.__film_name_dict.items()))        
        print("\nToday's film: ", key, "\tFilm:", result)
        if (callable(callback)):
            callback(key, result)
    
    def add_vote(self, user_name, film_name):
        self.__film_name_dict[user_name] = film_name