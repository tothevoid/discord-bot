from threading import Timer
import random as rnd

class VotingService:
    def __init__(self):
        self.__voting_ready = False
        self.__film_name_dict = {}
    
    def StartVoting(self, time:float, afterVotingMethod = None):
        timer = Timer(time, self.CloseVoting, [afterVotingMethod])
        timer.start()
        self.voting_ready = True
        

    def CloseVoting(self, callback):
        print("Voting close!")
        
        for key, value in self.__film_name_dict.items():
            print(key,"\t\t",value)

        key, result = rnd.choice(list(self.__film_name_dict.items()))        
        print("\nWin: ", key, "\tFilm:", result)
        if (callable(callback)):
            callback(key, result)
    
    def AddVote(self, user_name, film_name):
        self.__film_name_dict[user_name] = film_name

if (__name__ == "__main__"):
    print("test")
    service = VotingService()
    service.StartVoting(1,print)
    service.AddVote("user1", "film3")
    service.AddVote("user2", "film1")
    service.AddVote("user2", "film2")
    service.AddVote("user3", "film2")
    service.AddVote("user4", "film4")
    service.AddVote("user1", "film3")
