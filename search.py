import json

#query = "Hp warna merah ram 1gb"
exdic = {"Warna" : "Red", "RAM" : "2 GB"} #nanti dictionarynya nambahin attribut lg sesuai query

with open("samsung.json") as json_data:
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
					continue
			if att == "RAM":
				if int(data[brand][phone]["RAM"][0:1]) < int(exdic["RAM"][0:1]):
					cocok = False
					continue
			#if att == "ScreenSize":
			#if att == "ScreenType":
			#if att == "Price":
			#if att == "CPU":
			#if att == "GPU":
			#if att == "Storage":
			#if att == "OS":
			#if att == "Battery":
			#if att == "Camera":
			#if att == "Berat":
			#if att == "Tebal":
			#if att == "Fingerprint Reader":
			#if att == "Misc":

		if cocok:
			arr.append(phone)

print(arr)