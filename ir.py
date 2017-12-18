import pygame as pg
import json
import re

with open('data.json') as json_data:
	data = json.load(json_data)

my_boolean_index = {}

for brand in data :
	for phone in data[brand] :
		my_boolean_index[phone] = dict()
		my_boolean_index[phone][brand.lower()] = 1
		my_boolean_index[phone][phone.lower()] = 1
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

pg.init()
screen = pg.display.set_mode((1600, 900))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)

def title():
	tag = pg.image.load('title.png')
	screen.blit(tag,(600,80))
	
def text_objects(text, font):
	text = text.upper()
	textSurface = font.render(text, True, COLOR_INACTIVE)
	return textSurface, textSurface.get_rect()

def printCPU(cpu):
	text = 'CPU : ' + cpu
	spec = pg.font.Font('freesansbold.ttf', 23)
	TextSurf, TextRect = text_objects(text, spec)
	TextRect.center = (310, 285)
	screen.blit(TextSurf, TextRect) 
	
def printRAM(ram):
	text = 'RAM : ' + ram
	spec = pg.font.Font('freesansbold.ttf', 23)
	TextSurf, TextRect = text_objects(text, spec)
	TextRect.center = (310, 310)
	screen.blit(TextSurf, TextRect) 
	
def printGPU(gpu):
	text = 'GPU : ' + gpu
	spec = pg.font.Font('freesansbold.ttf', 23)
	TextSurf, TextRect = text_objects(text, spec)
	TextRect.center = (310, 335)
	screen.blit(TextSurf, TextRect)
	
def printSTORAGE(storage):
	text = 'STORAGE : ' + storage
	spec = pg.font.Font('freesansbold.ttf', 23)
	TextSurf, TextRect = text_objects(text, spec)
	TextRect.center = (310, 360)
	screen.blit(TextSurf, TextRect)
	
def printSCREENSIZE(screensize):
	text = 'SCREENSIZE : ' + screensize
	spec = pg.font.Font('freesansbold.ttf', 23)
	TextSurf, TextRect = text_objects(text, spec)
	TextRect.center = (310, 385)
	screen.blit(TextSurf, TextRect)
	
def printSCREENTYPE(screentype):
	text = 'SCREENTYPE : ' + screentype
	spec = pg.font.Font('freesansbold.ttf', 23)
	TextSurf, TextRect = text_objects(text, spec)
	TextRect.center = (310, 410)
	screen.blit(TextSurf, TextRect) 
	
def printOS(os):
	text = 'OS : ' + os
	spec = pg.font.Font('freesansbold.ttf', 23)
	TextSurf, TextRect = text_objects(text, spec)
	TextRect.center = (310, 435)
	screen.blit(TextSurf, TextRect)
	
def printPRICE(price):
	text = 'PRICE : ' + price
	spec = pg.font.Font('freesansbold.ttf', 23)
	TextSurf, TextRect = text_objects(text, spec)
	TextRect.center = (310, 457)
	screen.blit(TextSurf, TextRect)
	
def printBATTERY(battery):
	text = 'BATTERY : ' + battery
	spec = pg.font.Font('freesansbold.ttf', 23)
	TextSurf, TextRect = text_objects(text, spec)
	TextRect.center = (310, 480)
	screen.blit(TextSurf, TextRect)
	
def printCAMERA(camera):
	text = 'CAMERA : ' + camera
	spec = pg.font.Font('freesansbold.ttf', 23)
	TextSurf, TextRect = text_objects(text, spec)
	TextRect.center = (310, 503)
	screen.blit(TextSurf, TextRect)
	
def printWARNA(warna):
	text = 'WARNA : ' + warna
	spec = pg.font.Font('freesansbold.ttf', 23)
	TextSurf, TextRect = text_objects(text, spec)
	TextRect.center = (310, 525)
	screen.blit(TextSurf, TextRect)
	
def printBERAT(berat):
	text = 'BERAT : ' + berat
	spec = pg.font.Font('freesansbold.ttf', 23)
	TextSurf, TextRect = text_objects(text, spec)
	TextRect.center = (310, 547)
	screen.blit(TextSurf, TextRect)
	
def printTEBAL(tebal):
	text = 'TEBAL : ' + tebal
	spec = pg.font.Font('freesansbold.ttf', 23)
	TextSurf, TextRect = text_objects(text, spec)
	TextRect.center = (310, 570)
	screen.blit(TextSurf, TextRect)
	
def printFING(fingerprint):
	text = 'FINGERPRINT READER : ' + fingerprint
	spec = pg.font.Font('freesansbold.ttf', 23)
	TextSurf, TextRect = text_objects(text, spec)
	TextRect.center = (310, 590)
	screen.blit(TextSurf, TextRect)
	
def printMISC(misc):
	text = 'MISC : ' + misc
	spec = pg.font.Font('freesansbold.ttf', 23)
	TextSurf, TextRect = text_objects(text, spec)
	TextRect.center = (310, 610)
	screen.blit(TextSurf, TextRect)
	

def showResult(text,spec):
	if spec == "CPU" :
		printCPU(text)
	elif spec == "RAM" :
		printRAM(text)
	elif spec == "GPU" :
		printGPU(text)
	elif spec == "Storage" :
		printSTORAGE(text)
	elif spec == "ScreenSize" :
		printSCREENSIZE(text)
	elif spec == "ScreenType" :
		printSCREENTYPE(text)
	elif spec == "OS" :
		printOS(text)
	elif spec == "Price" :
		printPRICE(text)
	elif spec == "Battery" :
		printBATTERY(text)
	elif spec == "Camera" :
		printCAMERA(camera)
	elif spec == "Color" :
		printWARNA(text)
	elif spec == "Weight" :
		printBERAT(text)
	elif spec == "Thick" :
		printTEBAL(text)
	elif spec == "Censors" :
		printFING(text)
	elif spec == "Misc" :
		printMISC(text)

class InputBox:
	def __init__(self, x, y, w, h, text=''):
		self.rect = pg.Rect(x, y, w, h)
		self.color = COLOR_INACTIVE
		self.text = text
		self.txt_surface = FONT.render(text, True, self.color)
		self.active = False
		self.list_result = list()

	def handle_event(self, event):
		if event.type == pg.MOUSEBUTTONDOWN:
			# If the user clicked on the input_box rect.
			if self.rect.collidepoint(event.pos):
				# Toggle the active variable.
				self.active = not self.active
			else:
				self.active = False
				# Change the current color of the input box.
				self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
		if event.type == pg.KEYDOWN:
			# print(pg.key.name(event.key))
			if self.active:
				if event.key == pg.K_RETURN:
					self.list_result = query(self.text)
					self.text = ''
				elif event.key == pg.K_BACKSPACE:
					self.text = self.text[:-1]
				else:
					self.text += event.unicode
				# Re-render the text.
				self.txt_surface = FONT.render(self.text, True, self.color)
		

	def update(self):
		# Resize the box if the text is too long.
		width = max(1000, self.txt_surface.get_width()+10)
		self.rect.w = width

	def draw(self, screen):
		# Blit the text.
		screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
		# Blit the rect.
		pg.draw.rect(screen, self.color, self.rect, 2)

	def getListResult(self) :
		return self.list_result

def query(text) :

	fixed_query = []	
	query = text
	data_query = re.split("[-/() ,]",query)

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
	
	return list_added
	
def main():
	clock = pg.time.Clock()
	input_box1 = InputBox(300, 150, 800, 32)
	done = False

	while not done:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				done = True
			# print(pg.mouse.get_pos())
			input_box1.handle_event(event)
		result = input_box1.getListResult()
		if(len(result) != 0) :
			for brand in data :
				for phone in data[brand] :
					if phone in result :
						# print(phone)
						# print("---------------------")
						for spec in data[brand][phone] :
							if(spec != "Camera") :
								showResult(data[brand][phone][spec], spec)
								pg.display.update()
								# print(spec + " : " + data[brand][phone][spec])
							else :
								for camera in data[brand][phone][spec]:
									showResult(data[brand][phone][spec][camera], spec)
									pg.display.update()
									
		input_box1.list_result = []			
		input_box1.update()

		screen.fill((30, 30, 30))
		input_box1.draw(screen)
		
		title()
		# print(camera + " : " + data[brand][phone][spec][camera]
		pg.display.flip()
		clock.tick(30)

if __name__ == '__main__':
	main()
	pg.quit()
