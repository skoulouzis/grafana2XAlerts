from abc import ABCMeta, abstractmethod

class Sender:        
    
    def __init__(self,server_details):
        self.server_details = server_details
        
    @abstractmethod
    def send(self,message):
        pass
        
         
