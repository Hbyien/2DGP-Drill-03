from pico2d import *
import math

open_canvas()


grass = load_image('grass.png')
boy = load_image('character.png')


def draw_boy(x, y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.01)


def run_top():
    print('Top')

    for x in range(0, 800, 10):
        
        draw_boy(x, 550)        
    pass

def run_right():
    print('Right')
    for y in range(600, 0, -10):
        
        draw_boy(750,y)
    pass

def run_bottom():
    print('Bottom')
    for x in range(800,0, -10):
        
        draw_boy(x, 50)
    pass

def run_left():
    print('Left')
    for y in range(0, 600, 10):
        
        draw_boy(50,y)
    pass


def run_left_line():
    print('left line')

    for x in range(0, 400, 10):
        y= 3/2*x
        draw_boy(x,y)
    pass

def run_right_line():
    print('right line')
    for x in range(400, 800, 10):
        y= 2 * x*-1 +1600
        draw_boy(x,y)
    pass


def run_triangle():
    print('Triangle')

    run_bottom()
    run_left_line()
    run_right_line()
    pass


def run_rectangle():
    print('Rect')

    
    run_bottom()
    run_left()
    run_top()
    run_right()
    
    pass

def run_circle():
    print('Circle')

    r = 300
    cx = 800//2
    cy = 600//2
    for d in range(-90,270):

        x = r* math.cos(math.radians(d)) +cx
        y = r*math.sin(math.radians(d))+cy
        
        draw_boy(x,y)
    pass

while(True):
    run_circle()
    run_rectangle()
    run_triangle()
    


close_canvas()
