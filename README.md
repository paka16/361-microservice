# 361-microservice

This microserve uses yfinance and an api to return stock data when given a ticker. 
SERVER
CLIENT
```
import sockets
import json
import pickle
```
When given a viable ticker, the microservice will return its previous 5 day history, symbol, company, and country. 
If an unviable ticker is given, it will return an error message.
If 25 requests have been met, only yfinance data will be returned. 
If 'close' is sent from the client, it will shut off the microservice's server. 

Successful Case:

Failed Case:



