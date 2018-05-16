# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from message_relay import *
from senders.rabbitmq_sender import *

if __name__ == "__main__":
    port = 8081
    
    server = HTTPServer(('', port), MessageRelay,)
    server.serve_forever()
