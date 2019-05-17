import requests
usd=input("enter currency in USD")
url="https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=b4550d8eb9b5df5ba921"
response = requests.get(url)
jsondata = response.json()
print(jsondata)
print("INR= ",jsondata['USD_INR']*float(usd))