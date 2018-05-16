from senders.sender import *
import json

class RabbitmqSender(Sender):
        
    def send(self, grafana_alert_message):
        grafana_alert = json.loads(grafana_alert_message)    
        print grafana_alert
        print grafana_alert["ruleId"]
        print grafana_alert["state"]
        
         
