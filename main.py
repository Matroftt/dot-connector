def save_render(format='jpeg'):
  filename = get_name()
  pg.image.save(sc, 'renders/' +filename+'.'+format)
def get_name():
  filename = str(zoom) + '_' + str(x_count) + 'x' + str(y_count) + '_render'
  return filename
  
def select_extension(format='1'):
  if format == '1': return 'jpeg'
  if format == '2': return 'png'
  if format == '3': return 'bmp'

  if format == '':  return 'jpeg'

import sys
import pygame as pg

pg.init()

fps = 60
clock = pg.time.Clock()

# Define values

# Fractal values
size = 100              # Pixel distance beten dots. Shouldnt be changed
count = 2               # Amount of dots for each direction
x_count, y_count = 0, 0 # Amount of dots for each row/column
zoom = 1                # Zoom
positions = []          # List of dots position

# Rendering values
save_format = 'jpeg'       # Which format are we using to save the render? (png/jpeg/bmp)
bg_color = (255, 255, 255) # Color of the background

# Booleans
rendering = True  # Are we saving the render?
oversized = False # Is the image way too big to be drew in window?
window = True     # Generate pygame window or no?


# Are you inserting values through console or through code?
use_console = 1

if use_console:
  square = int(input('Are you making a rectangle grid or a square grid? (0/1) '))
  
  if square:
    count = int(input('How much there should be dots for each direction: '))
    
  else:
    count = 0
    x_count = int(input('How much there should be dots for each row: '))
    y_count = int(input('How much there should be dots for each column: '))
  
  zoom = float(input('How much you want to zoom the grid? (Type 1 to not zoom) '))
  rendering = bool(input('Are you saving the render (0/1): '))
  if rendering: save_format = input('In which format are you saving the render?\n1 or empty - jpeg\n2 - png\n3 - bmp\n')
  save_format = select_extension(save_format)
  
  # We are not making grids with only one dot
  if count   < 2 and  count != 0: count = 2
  if x_count < 2 and square != 1: x_count = 2
  if y_count < 2 and square != 1: y_count = 2

x_count += count
y_count += count

# Get all possible positions for this grid
for x in range(x_count):
  for y in range(y_count):
    positions.append((x * size/zoom, y * size/zoom))

# Calculate screen size
width =  size*(x_count)/zoom-size/zoom+1
height = size*(y_count)/zoom-size/zoom+1

print('[Info] Figure size: ' + str(width-1) + 'x' + str(height-1))
print('[Info] Filename: '+get_name()+'.'+save_format)
if rendering: print('\n[Progress] Rendering process has been started...')

# Check if PC is able to render given figure
try:
  sc = pg.Surface((round(width),round(height)))
except:
  print('[FATAL] Out of memory!')
  sys.exit()
  
if width > 5000 and height > 5000:
  print('[WARNING]  Image size is too large, it wont be drew in the pygame window')
  display = pg.display.set_mode((100, 100))
  oversized = True
else:
  display = pg.display.set_mode((width, height))

# Program loop
while True:
  sc.fill(bg_color)
  
  # Render the lines
  for x in range(len(positions)):
    for y in range(len(positions)):
      pg.draw.line(sc, (0,0,0), positions[x], positions[y])

  if rendering:
    print('[Progress] Lines have been rendered')

    save_render(save_format)
    
    print('[Progress] Render is done')
    rendering = False
  
  
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()
  
  if oversized == False:
    display.blit(sc, (0,0))
  pg.display.flip()

  clock.tick(fps)