# 361-microservice
A microservice that will return stock information. This microservice uses python's socket module as a communication pipe.

## 2A. HOW TO REQUEST DATA:
  1. Start the microservice's server and client files by typing the following into two separate terminals.
```
python server.py
```
```
python client.py
```
  2. Once the two processes are running, the server is waiting for instructions from the client and the client asks for an input stating: 'Enter a stock ticker or type 'close' to turn off:'. There are two possible things to put in the client's input: a ticker or the word 'close'.
  3. If the user types 'close', the client will send it to the server and it will turn off the server and client processes. However, if the client is given a stock ticker, the server will verify if the ticker is a valid ticker.

## 2B. HOW TO RECEIVE DATA:
1. Once the server receives a ticker, it will verify if the ticker is a valid ticker or not.
2. The server will then format result either as an error or stock information and send it back to the client.
3. The client will receive a result in dictionary format using the pickle module. 

## 2C. UML SEQUENCE DIAGRAM:

## EXAMPLES OF RUNNING MICROSERVICE:

### SUCCESSFUL RUN:
### TICKER NAME TOO LONG ERROR:
### INVALID TICKER ERROR:

### API LIMIT ERROR: 
yfinance data will be returned but the api data will show an error message. 



