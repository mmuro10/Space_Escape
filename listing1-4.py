
#Space_Escape
#by Sean McManus
#www.sean.co.uk / www.nostarch.com
#This is a test
import time, random, math

WIDTH = 800
HEIGHT = 600
player_x = 600
player_y = 85

def draw():
    screen.blit(images.backdrop,(0,0))
    screen.blit(images.mars,(50,50))
    screen.blit(images.astronaut,(player_x,player_y))
    screen.blit(images.ship,(550,50))
    
def game_loop():
    global player_x, player_y
    if keyboard.right:
        player_x += 2
    elif keyboard.left:
        player_x -= 2
    elif keyboard.up:
        player_y -= 2   
    elif keyboard.down:
        player_y += 2

clock.schedule_interval(game_loop, .01)
  