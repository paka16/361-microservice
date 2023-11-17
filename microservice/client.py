# MODULE
import socket
import json
import pickle

# CONSTANTS
HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

while True:
    stock = input("Enter a stock ticker or type 'close' to turn off: ") # The End-User's stock

    if 3 <= len(stock) <= 5:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("DEBUG - Client: Microservice Communication Pipe Running.")
            s.connect((HOST, PORT))
    
            print(f"Sending message to server: {stock}")
            # uses .sendall to send the message to the server

            

            s.sendall(bytes(stock, encoding="utf-8"))
            if stock == "close":
                print("DEBUG - CLIENT:  Shutting Off")
                break
            # s.sendall(b"{message}")
            # reads the server's reply
            data = s.recv(4096)
            data_load = pickle.loads(data)
            
        print(f" data_load: {data_load}")
        

    else:
        print("Enter a viable ticker!")

##############################################################################

