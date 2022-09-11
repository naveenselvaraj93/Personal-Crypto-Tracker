# importing the requests library
import requests
import pandas as pd
import time


def stats():
	final_l_or_p=0
	current_val=0
	df_samples = pd.read_excel(r'Portfolio.xlsx', engine='openpyxl')

	val=df_samples.to_dict('list')
	total_coins=len(val['Coin'])
	

	for i in range(0,total_coins):
		name=val['Coin'][i]
		holding=val['Holding'][i]
		invested=val['Invested'][i]
		print("")
		print("-"*35)
		print("Name of the coins is",name)
		print("-"*35)
		print("")
		print("Holding for",name,"is",holding)
		print("Investment for",name,"is",invested)
		c_price=get_price(name)
		print("Current price for",name,"is",c_price)
		print("Current holdings value till now",current_val)
		print()
		current_val=current_val+float(holding)*c_price
		final_l_or_p=final_l_or_p+invested
	print("Total holding is",current_val)
	print("Total Invested",final_l_or_p)
	print("")
	print(current_val-final_l_or_p)

def get_price(name):
	time.sleep(5)
	try:
		# api-endpoint
		URL = "https://api.coingecko.com/api/v3/simple/price?ids="+name+"&vs_currencies=inr"

		r = requests.get(url = URL)

		# extracting data in json format
		data = r.json()
		print(data)
		current_price=data[name]['inr']
		return current_price
	except Exception as e: 
		print(e)
stats()