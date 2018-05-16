import json
import pika
from senders.sender import *

class RabbitmqSender(Sender):
    
    def __init__(self, server_details):
        self.rabbit_port = server_details['port']
        self.rabbit_host = server_details['host']
        self.user = server_details['user']
        self.password = server_details['password']
        
        
    def init_connection(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.rabbit_host))
        self.channel = self.connection.channel()
        self.channel.confirm_delivery()
        self.channel.queue_declare(queue=self.q_name, durable=True)        
#        self.channel.exchange_declare(exchange='alerts', exchange_type='direct')

        
    def send(self, grafana_alert_message):
        grafana_alert = json.loads(grafana_alert_message)    
        
        ruleId = str(grafana_alert["ruleId"])
        self.q_name = ruleId
        state = grafana_alert["state"]
        
        self.init_connection()
        

        self.channel.basic_publish(exchange='',
                                   routing_key=self.q_name,
                                   body=grafana_alert_message)
         
        self.connection.close()
        
         
