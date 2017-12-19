from tkinter import *
import json
import re

def click() :
	for button in list_button :
		button.destroy()
	entered_text = textentry.get()
	result = query(entered_text)
	init_x = 0.1
	init_y = 0.5
	x_counter = 0
	for phone in result :
		add_phone(phone, init_x, init_y)
		init_x += 0.2
		x_counter += 1
		if(x_counter > 4) :
			init_y += 0.05
			init_x = 0.1
			x_counter = 0

def add_phone(name, x, y) :
	new_button = Button (window, text=name, width=30, command=lambda m=name: click_about(m))
	new_button.place(relx=x, rely=y, anchor="center")
	list_button.append(new_button)

def click_about(name) :
	toplevel = Toplevel()
	toplevel.geometry("1280x720")
	toplevel.configure(background="light blue")
	label1 = Label(toplevel, text="Detail Spesification", font="none 16 underline", fg="white", bg="light blue").place(relx=.5, rely=.1, anchor="center")
	
	init_x = 0.3
	init_y = 0.20

	for brand in data :
		for phone in data[brand] :
			label1 = Label(toplevel, text=name, font="none 14 bold", fg="white", bg="light blue").place(relx=.5, rely=.15, anchor="center")
			if phone == name :
				for spec in data[brand][phone] :
					if(spec != "Camera") :
						Label(toplevel, text=spec + ": " + data[brand][phone][spec], font="none 12 bold", fg="black", bg="light blue").place(relx=init_x, rely=init_y, anchor="w")
					else :
						for camera in data[brand][phone][spec]:
							Label(toplevel,text=spec + " " + camera +  ": " + data[brand][phone][spec][camera], font="none 12 bold", fg="black", bg="light blue").place(relx=init_x, rely=init_y, anchor="w")
					init_y += 0.035

def query(text) :

	# print("What kind of phone you're searching?\n")
	# query = str(input("=> "))
	# data_query = re.split("[-/() ,]", query)

	query = text
	data_query = re.split("[-/() ,]", query)

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



window = Tk()
window.title("Find Your Spec")
window.configure(background="light blue")
window.geometry('1280x720')
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(2, weight=1)

photo1 = PhotoImage(file="title.png")
Label(window, image=photo1).place(relx=.5, rely=.1, anchor="center")

textentry = Entry(window, width=150, bg="white")
textentry.place(relx=.5, rely=.25, anchor="center")

Label (window, text ="Type your description !", bg="light blue", fg="white", font="none 16 bold").place(relx=.5, rely=.2, anchor="center")

Button (window, text="SEARCH", width=30, command=click).place(relx=.5, rely=.30, anchor="center")
list_button = list()
Label (window, text="Search Results", bg="light blue", fg="white", font="none 16 underline").place(relx=.5, rely=.35, anchor="center")

window.resizable(False,False)
window.mainloop()

