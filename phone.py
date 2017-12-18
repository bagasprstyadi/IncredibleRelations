import json
import re

def query(text) :

	# print("What kind of phone you're searching?\n")
	# query = str(input("=> "))
	# data_query = re.split("[-/() ,]", query)

	query = text
	data_query = re.split("[-/() ,]", query)

	with open('data.json') as json_data:
		data = json.load(json_data)

	my_boolean_index = {}

	for brand in data :
		for phone in data[brand] :
			my_boolean_index[phone] = dict()
			my_boolean_index[phone][brand.lower()] = 1
			for part in phone.split(" ") :
				my_boolean_index[phone][part.lower()] = 1
			#my_boolean_index[phone]
			for spec in data[brand][phone] :
				my_boolean_index[phone][spec.lower()] = 1
				try :
					spesific = data[brand][phone][spec]
					spesific_2 = re.split('[-/(), ]', spesific)
					for word in spesific_2 :
						if word != "" :
							
							if spec in ["RAM", "Storage"] :
								if(not word.lower() in ["gb","mm","g"]) :
									my_boolean_index[phone][word.lower() + " gb"] = 1
								else :
									my_boolean_index[phone][word.lower()] = 1
							elif spec in ["Tebal"] :
								if(not word.lower() in ["gb","mm","g"]) :
									my_boolean_index[phone][word.lower() + " mm"] = 1
								else :
									my_boolean_index[phone][word.lower()] = 1
							elif spec in ["Berat"] :
								if(not word.lower() in ["gb","mm","g"]) :
									my_boolean_index[phone][word.lower() + " g"] = 1
								else :
									my_boolean_index[phone][word.lower()] = 1
							elif spec in ["ScreenSize"] :
								if(not word.lower() in ["inches"]) :
									my_boolean_index[phone][word.lower() + " inches"] = 1
								else :
									my_boolean_index[phone][word.lower()] = 1
							else :
								my_boolean_index[phone][word.lower()] = 1

				except TypeError :
					for camera in data[brand][phone][spec] :
						spesific = data[brand][phone][spec][camera]
						spesific_2 = re.split('[-/(), ]', spesific)
						for word in spesific_2 :
							if word != "" :
								if(not word.lower() in ["mp"]) :
									my_boolean_index[phone][word.lower() + " mp"] = 1
								else :
									my_boolean_index[phone][word.lower()] = 1

	# for phone in my_boolean_index :
	# 	print(phone)
	# 	print(my_boolean_index[phone])
	# 	print()

	list_stopword = []
	stopword = open("stopword.txt","r") #open stopword file

	for word in stopword :
		list_stopword.append((word.split("\n")[0]))

	fixed_query = []
	
	for word in data_query :
		if(not word.lower() in list_stopword and word.lower() != "") :
			fixed_query.append(word.lower())

	print(fixed_query)

	list_added = []
	prefix = ""

	for phone in my_boolean_index :
		add = True
		for index, query in enumerate(fixed_query) :
			prefix = ""
			try : 
				prefix = fixed_query[index+1]
				query = float(query)
				if(prefix in ["mm","inches"]) :
					a = 1
				elif(prefix in ["g", "gb", "mb"]) :
					query = int(query)
				else :
					query = str(int(query))
					prefix = ""
			except ValueError :
				prefix = ""
			except IndexError :
				prefix = ""
			if(prefix != "") :
				q = str(query) + " " + prefix
				# print(q)
				if q in my_boolean_index[phone] :
					next
				else :
					add = False
					break
			else:
				# print(query)
				if query in my_boolean_index[phone] :
					next
				else :
					add = False
					break
		if add :
			list_added.append(phone)

	print(list_added)
	return list_added
	# for brand in data :
	# 	for phone in data[brand] :
	# 		if phone in list_added :
	# 			print(phone)
	# 			print("---------------------")
	# 			for spec in data[brand][phone] :
	# 				if(spec != "Camera") :
	# 					print(spec + " : " + data[brand][phone][spec])
	# 				else :
	# 					for camera in data[brand][phone][spec]:
	# 						print(camera + " : " + data[brand][phone][spec][camera])
