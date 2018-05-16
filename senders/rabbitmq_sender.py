from senders.sender import *

class RabbitmqSender(Sender):
        
    def send(self, grafana_alert):
        print grafana_alert
        print grafana_alert["ruleId"]
        print grafana_alert["state"]
        
         
