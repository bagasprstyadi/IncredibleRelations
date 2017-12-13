import pygame as pg

pg.init()
screen = pg.display.set_mode((640, 700))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 32)

def title():
	tag = pg.image.load('title.png')
	screen.blit(tag,(120,30))
	
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
	

def showResult(cpu, ram, gpu, storage, screensize, screentype, os, price, battery, camera, warna, berat, tebal, fingerprint, misc):
	printCPU(cpu)
	printRAM(ram)
	printGPU(gpu)
	printSTORAGE(storage)
	printSCREENSIZE(screensize)
	printSCREENTYPE(screentype)
	printOS(os)
	printPRICE(price)
	printBATTERY(battery)
	printCAMERA(camera)
	printWARNA(warna)
	printBERAT(berat)
	printTEBAL(tebal)
	printFING(fingerprint)
	printMISC(misc)

class InputBox:

	def __init__(self, x, y, w, h, text=''):
		self.rect = pg.Rect(x, y, w, h)
		self.color = COLOR_INACTIVE
		self.text = text
		self.txt_surface = FONT.render(text, True, self.color)
		self.active = False

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
			if self.active:
				if event.key == pg.K_RETURN:
					self.text = ''
				elif event.key == pg.K_BACKSPACE:
					self.text = self.text[:-1]
				else:
					self.text += event.unicode
				# Re-render the text.
				self.txt_surface = FONT.render(self.text, True, self.color)

	def update(self):
		# Resize the box if the text is too long.
		width = max(200, self.txt_surface.get_width()+10)
		self.rect.w = width

	def draw(self, screen):
		# Blit the text.
		screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
		# Blit the rect.
		pg.draw.rect(screen, self.color, self.rect, 2)



def main():
	clock = pg.time.Clock()
	input_box1 = InputBox(210, 100, 200, 32)
	done = False

	while not done:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				done = True
			print(pg.mouse.get_pos())
			input_box1.handle_event(event)

		input_box1.update()

		screen.fill((30, 30, 30))
		input_box1.draw(screen)
		
		title()
		showResult("Iphone X","a","a","a","a","a","a","a","a","a","a","a","a","a","a")
		pg.display.flip()
		clock.tick(30)


if __name__ == '__main__':
	main()
	pg.quit()