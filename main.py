def save_render(format='jpeg'):
  filename = str(zoom) + '_' + str(x_count) + 'x' + str(y_count) + '_render'
  pg.image.save(sc, 'renders/' +filename+'.'+format)
  
def select_extension(format=1):
  if format == '' or save_format == '1': return 'jpeg'
  if format == '2': return 'png'
  if format == '3': return 'bmp' 

import sys
import pygame as pg

pg.init()

fps = 60
clock = pg.time.Clock()

# Define values

size = 100              # Pixel distance beten dots. Shouldnt be changed
count = 2               # Amount of dots for each direction
x_count, y_count = 0, 0 # Amount of dots for each row/column
zoom = 1                # Zoom
rendering = True        # Are we saving the render?
save_format = 'bmp'     # Which format are we using to save the render? (png/jpeg)
positions = []          # List of dots position

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
  if count   < 2 and count != 0: count = 2
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

print('Figure size: ' + str(width-1) + 'x' + str(height-1))
if rendering: print('\nRender will be done once you close the program.')
sc = pg.display.set_mode((width, height))
 
# Program loop
while True:
  sc.fill((255, 255, 255))
  
  # Render the lines
  for x in range(len(positions)):
    for y in range(len(positions)):
      pg.draw.line(sc, (0,0,0), positions[x], positions[y])

  if rendering:
    save_render(save_format)
    rendering = False

  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      sys.exit()

  pg.display.flip()
  clock.tick(fps)