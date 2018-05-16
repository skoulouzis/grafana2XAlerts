from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser

from senders.rabbitmq_sender import *

class MessageRelay(BaseHTTPRequestHandler):
        
    def do_POST(self):
        request_path = self.path
        request_headers = self.headers
        content_length = request_headers.getheaders('content-length')
        length = int(content_length[0]) if content_length else 0
        alert_message = self.rfile.read(length)        
        sender = self.get_sender()
        sender.send(alert_message)
        sender = None
        self.send_response(200)
        
        
    def get_sender(self):
        server_details = {}
        server_details["host"] = ""
        server_details["port"] = ""
        return RabbitmqSender(server_details)