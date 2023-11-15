# echo-server.py

# API
# website: https://www.alphavantage.co/ 
API_KEY = 'N8P69WL8ZKN99ZS2'

# MODULES:
import requests
import socket
import yfinance as yf
import json
import pickle

# CONSTANTS
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

waiting = True
print("DEBUG - SERVER: Microservice Communication Pipe Running.")

while waiting:
    print("DEBUG: Waiting for ticker...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            
            while True:
                # receiving message from the client
                incoming = conn.recv(1024).decode("utf-8")
                print(f"Receiving Data from Client: {incoming}")
                
                if not incoming:
                    print("DEBUG - SERVER: Empty data sent from client.")
                    break


                else: 
                    data = incoming
                    print(f"data: {data}")

                    if len(data) == 0:
                        print("Waiting for ticker...")
                    
                    elif data == "close":
                        waiting = False
                        conn.sendall(b'SERVER CLOSED')
                        break

                    else:
                        # get the ticker information:
                        # yfinance
                        # last 5 days worth of information
                        history = yf.download(data, period="5d")

                        # stock api information
                        # get all stock info
                        url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={data}&apikey={API_KEY}'
                        r = requests.get(url)
                        j = r.json()
                        # print(f"j = {j}") -> prints the whole company overview of the ticker.
                    

                        if j != {}:
                            # send the whole data or just a couple things? 
                            if "Information" in j:
                                format_info = {
                                    "yf_data" : history,
                                    'stock_info': "Error: API LIMIT HIT"
                                }
                            else:
                                stock_info = {
                                    "Symbol": j["Symbol"],
                                    "Name": j["Name"],
                                    "Country": j["Country"]
                                }
                                # print(stock_info)

                                format_info = {
                                    "yf_data": history,
                                    "stock_info": stock_info
                                    }

                            data_dump = pickle.dumps(format_info)
                            # edit this portion too with the information to send back.
                            # sends the data back to the client? 
                            print(f"Sending from the Server")
                            conn.sendall(data_dump)
                    
                        else:
                            not_viable = {
                                'Error': 'Not a viable ticker!'
                            }
                            not_viable = pickle.dumps(not_viable)
                            conn.sendall(not_viable)
print("DEBUG: MICROSERVICE SERVER: OFF")
    
    

############################################################################
# data = "IBM"
# history = yf.download(data, period='5d')
# print(history)
            