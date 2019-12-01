#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Simple local HTTP server for communication with Arduino board

usage: python server.py 
'''

import serial
import struct
from socketserver import ThreadingMixIn
from http.server import HTTPServer, SimpleHTTPRequestHandler

port = None
port_name = '/dev/ttyACM0'

class BoardHandler(SimpleHTTPRequestHandler):
    
    def log_message(self, format, *args):
        return

    def do_GET(self):
        global port
        s = self.path.split('/')
        if 'cmd' in s: 
            for c in s[2]:
                port.write(struct.pack('B', ord(c)))
            
            resp = 'ok'
            message = resp.encode()
            self.request.send(message)
        else:
            SimpleHTTPRequestHandler.do_GET(self)


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

def http_server():
    try:
        server = ThreadedHTTPServer(('127.0.0.1', 1111), BoardHandler) 
        server.daemon_threads = True
        print( "HTTP Server at port 1111, ^C to exit")
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()


if __name__ == '__main__':
    port = serial.Serial(port_name, 115200)
    http_server()
