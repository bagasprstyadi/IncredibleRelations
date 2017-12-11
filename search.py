import json

#query = "Hp warna merah ram 1gb"
exdic = {"Warna" : "Blue", "RAM" : "2 GB", "Battery": "2000 mAh", "Fingerprint Reader" : 1, "Berat": "150"} #nanti dictionarynya nambahin attribut lg sesuai query

with open('data.json') as json_data:
	data = json.load(json_data)

arr = [] #array isinya hp yang sesuai query

#loop every brand
for brand in data:
	#loop every phone in that brand
	for phone in data[brand]:
		cocok = True
		#loop every attribut in exdic
		for att in exdic:
			if att == "Warna":
				if exdic["Warna"].lower() not in data[brand][phone]["Warna"].lower():
					cocok = False
					break
			if att == "RAM":
				if int(data[brand][phone]["RAM"][0:1]) < int(exdic["RAM"][0:1]):
					cocok = False
					break
			#if att == "ScreenSize":
			#if att == "ScreenType":
			if att == "Price":
				if int(data[brand][phone]["Price"][4:] > int(exdic["Price"])):
					cocok = False
					break
			if att == "CPU":
				if exdic["CPU"].lower() not in data[brand][phone]["CPU"].lower():
					cocok = False
					break
			if att == "GPU":
				if exdic["GPU"].lower() not in data[brand][phone]["GPU"].lower():
					cocok = False
					break
			if att == "Storage":
				if int(data[brand][phone]["Storage"][0:1]) < int(exdic["Storage"][0:1]):
					cocok = False
					break
			if att == "OS":
				if exdic["OS"].lower() not in data[brand][phone]["OS"].lower():
					cocok = False
					break
			if att == "Battery":
				token = data[brand][phone]["Battery"].lower().split()
				battery = 0
				for i in range(len(token)):
					if token[i] == "mah":
						battery = int(token[i-1])
						break
				if battery < int(exdic["Battery"][0:4]):
					cocok = False
					break
			#if att == "Camera":
			if att == "Berat":
				token = data[brand][phone]["Berat"].split()
				if float(token[0]) > float(exdic["Berat"]):
					cocok = False
					break
			if att == "Tebal":
				token = data[brand][phone]["Tebal"].split()
				if float(token[0]) > float(exdic["Berat"]):
					cocok = False
					break
			if att == "Fingerprint Reader":
				if data[brand][phone]["Fingerprint Reader"] == 0:
					cocok = False
					break
			#if att == "Misc":

		if cocok:
			arr.append(phone)

print(arr)