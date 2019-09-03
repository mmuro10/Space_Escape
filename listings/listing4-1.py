#Escape - A Python Adventure
# by Sean McManus 
#Typed in by Marco Muro

import time, random, math

###############
## VARIABLES ##
###############

WIDTH = 800 #window size
HEIGHT = 800

#PLAYER varibles
PLAYER_NAME = "Marco"
FRIEND1_NAME = "Amanda"
FRIEND2_NAME = "Leo"
current_room = 31 #Start room 

top_left_x = 100
top_left_y = 150

DEMO_OBJECTS = [images.floor, images.pillar, images.soil]

#########
## MAP ##
#########

MAP_WIDTH = 5
MAP_HEIGHT = 10
MAP_SIZE = MAP_WIDTH * MAP_HEIGHT

GAME_MAP = [["Room 0 - where unused objects are kept", 0,0,False,False]]

outdoor_rooms = range(1,26)
for planetsectors in range(1,26): #rooms 1 to 25 are generated here
    GAME_MAP.append(["The dusty planet surface",13,13,True,True])

GAME_MAP += [
    #["Room name", height, width, Top exit?, Right exit?]
    ["The airlock",13,5,True,False], # room 26
    ["The enineeringlab",13,13,False,False], # room 27
    ["Poodle Mission Control",9,13,False,True], # room 28
    ["The viewing gallery",9,15,False,False], # room 29
    ["The crew's' bathroom",5,5,False,False], # room 30
    ["The airlock entry bay",7,11,True,True], # room 31
    ["Left elbow room",9,7,True,False], # room 32
    ["Right elbow room",7,13,True,True], # room 33
    ["The Science lab",13,13,False,True], # room 34
    ["The green house",13,13,True,False], # room 35
    [PLAYER_NAME + "'s sleeping quarters", 9,11,False,False], # room 36
    ["West corridor",15,5,True,True], #room 37
    ["The briefing room",7,13,False,True], #room 38
    ["The crews community room",11,13,True,False], #room 39
    ["Main Mission Control",14,14,False,False],# room 40
    ["The sick bay",12,7,True,False], # room 41
    ["West corridor",9,7,True,False], # room 42
    ["Utilities control room",9,9,False,True],# room 43
    ["Systems engineering bay",9,11,False,False], # room 44
    ["Security portal to Mission Control",7,7,True,False], #room 45
    [FRIEND1_NAME + "'s sleeping quarters",9,11,True,True], #room 46
    [FRIEND2_NAME + "'s sleeping quarters",9,11,True,True], #room 47
    ["The pipeworks",13,11,True,False], #room 48
    ["The chief scientist's office",9,7,True,False], #room 49
    ["The robot workshop",9,11,True,False]#room 50
    ]
#Simple sanity check on map above to check data entry
assert len(GAME_MAP)-1 == MAP_SIZE, "Mape siae and GAME_MAP don't match"