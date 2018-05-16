
class Sender:        
    
    @abstractmethod
    def __init__(self,server_details):
        pass
        
    @abstractmethod
    def send(self,message):
        pass
        
         
