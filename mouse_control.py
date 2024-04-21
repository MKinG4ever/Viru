import os
import time
import random as rnd
import pyautogui as pg

dly = time.sleep
cmd = os.system

def main():
  """ powered from pyAutoGUI modules """
	w, h = pg.size()
	x, y = pg.position()	
	print(f'width:{w} | height:{h}')
	print(f'x:{x} | y:{y}')
	goCenter(1.5)
	print('I\'m Done.\n')
	dly(1)
	print('GO Jump..')
	jump(10)
	input('Press ENTER')


def goCenter(interval=0):
	w, h = pg.size()
	c = {'w':w//2, 'h':h//2}
	pg.moveTo(c['w'],c['h'],interval)
	return c['w'], c['h']


def randomPosition():
	w, h = pg.size()
	x = rnd.randint(1, w-1)
	y = rnd.randint(1, h-1)
	return x, y


def trap():
	x1, y1 = pg.position()
	x2, y2 = pg.position()
	while x2 == x1 or y2 == y1:
		x2, y2 = pg.position()
	x = x2-x1  # abs(x2-x1)
	y = y2-y1  # abs(y2-y1)
	# print(f'X({x1}, {x2} = {x}) | Y({y1}, {y2} = {y})')
	return x, y


def jump(jumps=1):
	for _ in range(jumps):
		x, y = trap()
		r = rnd.randint(3,9) * 3.149264 + 1
		pg.moveRel(x*r, y*r)


def trackIt(moves=100):
	locations = [pg.position()]
	for _ in range(moves):
		x, y = trap()
		locations.append((x, y))
	return locations
	

def repeatIt(locations):
	f, *others = locations
	fx, fy = f
	pg.moveTo(fx, fy)
	for loc in others:
		x,y = loc
		pg.moveRel(x, y, 0.1)


if __name__ == '__main__':
    main()
