import json

print("Mau cari HP yang seperti apa?\n")
query = str(input("=> "))
print(query)

data_query = query.split(" ")

list_stopword = []
stopword = open("stopword.txt","r") #open stopword file
for word in stopword :
    list_stopword.append((word.split("\n")[0]))

fixed_query = []

for word in data_query :
    if(not word.lower() in list_stopword) :
        fixed_query.append(word.lower())

print(fixed_query)

exdic = {}
brand_search = ""

for index, spec in enumerate(fixed_query) :
    if(spec == "samsung" ) :
        brand_search = "Samsung"
    elif(spec == "oneplus") :
        brand_search = "OnePlus"
    elif (spec == "iphone") :
        brand_search = "Iphone"
    elif (spec == "xiaomi") :
        brand_search = "Xiaomi"
    elif (spec == "asus") :
        brand_search = "Asus"
    elif(spec == "harga" or spec == "harganya") :
        price = fixed_query[index+1]
        try: 
            value = int(price)
            if(value <= 1000) :
                following = fixed_query[index+2]

                if(following == "jt" or following == "juta") :
                    exdic["Price"] = value * 1000000
                elif(following.lower() == "ribu" or following.lower() == "rebu") :
                    exdic["Price"] = value * 100000
            else :
                exdic["Price"] = value
        except ValueError:
            if(price == "dibawah") :
                price = fixed_query[index+2]
                try :
                    value = int(price)
                    if(value <= 1000) :
                        following = fixed_query[index+3]
                        if(following.lower() == "jt" or following.lower() == "juta") :
                            exdic["PriceMax"] = value * 1000000
                        elif(following.lower() == "ribu" or following.lower() == "rebu") :
                            exdic["PriceMax"] = value * 100000
                except ValueError : 
                    pass
    elif (spec == "murah") :
        exdic["PriceMax"] = "3000000"
    
#query = "Hp warna merah ram 1gb"
#exdic = {"Warna" : "Blue", "RAM" : "2 GB", "Battery": "2000 mAh", "Fingerprint Reader" : 1, "Berat": "150"} #nanti dictionarynya nambahin attribut lg sesuai query

with open('data.json') as json_data:
	data = json.load(json_data)

print(exdic)
arr = [] #array isinya hp yang sesuai query

#loop every brand
for brand in data:
	if(brand_search != "" and brand_search != brand) :
		continue
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
				if (int(data[brand][phone]["Price"][4:]) - int(exdic["Price"]) >= 1000000 or int(data[brand][phone]["Price"][4:]) - int(exdic["Price"]) <= -1000000):
					cocok = False
					break
			if att == "PriceMax":
				if (int(data[brand][phone]["Price"][4:]) > int(exdic["PriceMax"])) :
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
			arr.append(brand + ";" + phone)


for phone in (arr) :
	brand = phone.split(";")
	print("------------------------------" + brand[1] + "------------------------------------")
	for spec in (data[brand[0]][brand[1]]) :
		if(spec == "Camera") :
			for camera_spec in (data[brand[0]][brand[1]][spec]) :
				print(camera_spec + ": " + data[brand[0]][brand[1]][spec][camera_spec])
		elif (spec == "Fingerprint Reader" or spec == "Dualsim") :
			if(data[brand[0]][brand[1]][spec	] == 1) :
				print(spec + ": Yes")
			else :				
				print(spec + ": No")
		else :
			print(spec + ": " + data[brand[0]][brand[1]][spec])
