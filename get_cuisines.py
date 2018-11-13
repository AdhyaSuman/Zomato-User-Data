import requests
import json
import sys
import time

url = "https://developers.zomato.com/api/v2.1/restaurant?res_id="
api_key = "24ec4ae067064a2f7a53bfacf05c7a5b" 
with open ('in.txt', "r") as myfile:
	for line in myfile.readlines():
		arr = line.split(',')
		rest_id = arr[1]
		headers={"user-key": api_key}
		time.sleep(2)
		response = requests.get(url+rest_id,headers=headers)
		json_obj = response.json()
		#print(response.json())
		#print(json_obj["code"])
		with open('cuisines.csv',"a") as f:
			if response.status_code == 200:
				print (rest_id + ', ' + arr[0] + "," + json_obj["name"] + ", " + json_obj["cuisines"])
				f.write(rest_id + ', ' + arr[0] + "," + json_obj["name"] + ", " + json_obj["cuisines"]+"\n")
			else:
				print (rest_id  + ', ' + arr[0] + ', Error Code = ' + str(response.status_code))
				f.write(rest_id  + ', ' + arr[0] + ', Error Code = ' + str(response.status_code)+"\n")
			
			
