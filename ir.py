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
	
def showResult(cpu, ram, gpu, storage, screensize, screentype, os, price, battery, camera, warna, berat, tebal, fingerprint, misc):
	text = 'CPU 				= ' + cpu + '\n'
	text = text + 'RAM 					= ' + ram + '\n'
	text = text + 'GPU 					= ' + gpu + '\n'
	text = text + 'STORAGE 				= ' + storage + '\n'
	text = text + 'SCREENSIZE 			= ' + screensize + '\n'
	text = text + 'SCREENTYPE 			= ' + screentype + '\n'
	text = text + 'OS 					= ' + os + '\n'
	text = text + 'PRICE 				= ' + price + '\n'
	text = text + 'BATTERY 				= ' + battery + '\n'
	text = text + 'CAMERA 				= ' + camera + '\n'
	text = text + 'COLOR 				= ' + warna + '\n'
	text = text + 'BERAT		 		= ' + berat + '\n'
	text = text + 'TEBAL 				= ' + tebal + '\n'
	text = text + 'FINGERPRINT READER 	= ' + fingerprint + '\n'
	text = text + 'MISC 				= ' + misc
	spec = pg.font.Font('freesansbold.ttf', 23)
	TextSurf, TextRect = text_objects(text, spec)
	TextRect.center = (30, 30)
	screen.blit(TextSurf, TextRect)
	

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
			input_box1.handle_event(event)

		input_box1.update()

		screen.fill((30, 30, 30))
		input_box1.draw(screen)
		
		title()
		showResult("a","a","a","a","a","a","a","a","a","a","a","a","a","a","a")
		pg.display.flip()
		clock.tick(30)


if __name__ == '__main__':
	main()
	pg.quit()