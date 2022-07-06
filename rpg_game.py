#!/usr/bin/python3
import sys
import os
'''LB's RPG Game'''

inventory = []
       

def showInstructions():
    print('''
LB  RPG GAME
OBJECTIVE: ESCAPE THE CASTLE
--------
Actions:
    GO [north, south, east, west, up, down]
    GET [item]
    USE [item]
    LOOK
    INV/INVENTORY
Type 'help' at any time! Type 'q' to quit!''')

def playerinfo():
    print('')
    print('YOU ARE IN THE ' + currentRoom + '.')
    print('=================================')
    print('Inventory :', str(inventory))
    print('=================================')


def showStatus(): # display the player's status
 #   if 'desc' in rooms[currentRoom]:
 #       print(rooms[currentRoom]['desc'])
    if 'item' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'] + rooms[currentRoom]['item_status'] + '.')
#    print('=================')


rooms = {
        'HALL' : {
            'south' : 'KITCHEN',
            'east' : 'DINING ROOM',
            'item' : 'dagger',
            'item_status' : ' inside of a display case. It is unlocked',
            'desc' : 'You are trapped in the hall of a large mysterious castle. The walls are blackened from some ancient fire & the blood of past adventurer\'s. You get the feeling you are being watched & that danger is near. To the east'
            },
        'KITCHEN' : {
            'north' : 'HALL',
            'down' : 'BASEMENT',
            'desc' : 'You are in what was once a kitchen. Nests made of human bones are draped across every countertop. There is a large hole in the floor. Where it leads you have no idea.'
            },
        'BASEMENT' : {
            'spell' : 'fireball',
            'desc' : 'You are in a stinking basement with an earthen floor. You can\'t even see your hand in front of your face. You are likely to be attacked. Luckily you see a flashlight',
            'randenc' : '0',
            'item' : 'flashlight',
            'item_status' : 'in the corner of the room',
            'up': 'KITCHEN',
            'north' : 'UNDERGROUND TUNNEL'
            },
        'DINING ROOM' : {
            'west' : 'HALL',
            'south' : 'GARDEN',
            'north' : 'PANTRY',
            'desc' : 'You are in the dining room. The table is set for an elegant party but is covered a blanket of dust. Sleeping bats cling to the chandelier. North is a dark pantry. South lies the garden. West returns to the hall.',
            'randenc' : '0',
            'item' : 'potion',
            'item_status' : ' hiding among the bottles of wine. It is cherry red in color'
            },
        'GARDEN' : {
            'north' : 'DINING ROOM',
            'desc' : 'You are in the garden, but you don\'t see anywhere to go'
            },
        'PANTRY' : {
            'south' : 'DINING ROOM',
            'up' : 'ROOFTOP',
            'desc' : 'You made it to the pantry. The ladder in here seems out of place...',
            'item' : 'cake ',
            'item_status' : 'sitting on the cabinet',
            },
        'UNDERGROUND TUNNEL' : {
            'south' : 'BASEMENT',
            'up' : 'LADDER',
            'desc' : 'You are in the tunnel & there seems to be a ladder',
            'item' : 'key',
            'item_status' : ' laying on the floor',
            },
        'ROOFTOP' : {
            'desc' : 'You\'e reached the roof and are close to escaping. You see a jetpack',
            'south' : 'PANTRY',
            'item' : 'jetpack',
            'item_status' : ' on the edge of the roof..'
            },
        'SECRET DOOR' : {
            'down' : 'LADDER',
            'desc' : 'You have found the secret door which what lives behind it is unknown. It could be freedom or it could be despair. If you choose to proceed is your decision',
            },
        'LADDER' : {
            'south' : 'UNDERGROUND TUNNEL',
            'up' : 'SECRET DOOR',
            'randenc' : '0'
            }
        }

currentRoom = 'HALL'   # player start location

os.system('clear') # start game with a fresh screen
showInstructions()     # show instructions to the player

while True:   # MAIN INFINITE LOOP
    playerinfo()
    showStatus()

    if rooms[currentRoom] == 'SECRET DOOR':
        if 'key' in inventory:
            print("The strange  door seems to be locked...")

    # ask the player what they want to do
    move = ''
    while move == '':
        move = input('>') # so long as the move does not
        # have a value. Ask the user for input

    move = move.lower().split() # make everything lower case because directions and items require it, then split into a list
    os.system('clear') # clear the screen
    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            if 'desc' in rooms[currentRoom]:
                print(rooms[currentRoom]['desc'])
            # if YES that direction exists, then assign your new current room to the VALUE of the key the user entered
        else:
            print("YOU CAN'T GO THAT WAY!")
    if move[0] == 'use':
        if move[1].lower() == 'potion' and 'potion' in inventory:
            print("You drink from the potion. Your health has been restored!")
            print("Your potion magically refills itself! Handy!")
            player_health = 20
        if move[1].lower() == 'key' and 'key' in inventory:
                print("The key unlocked the door!")
                print("You've escaped from the dangerous castle & are free!")
                sys.exit()
        if move[1].lower() == 'jetpack' and 'jetpack' in inventory:
                print("The jetpack has fuel!")
                print("You fly away from the castle & escape!")
                sys.exit()
    if move[0] == 'get':
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]] # add item to inv
            print(move[1].capitalize() + ' received!') # msg saying you received the item
            del rooms[currentRoom]['item'] # deletes that item from the dictionary

        else:
            print('YOU CANNOT GET ' + (move[1].upper()) + '!')

    if move[0] == 'look':
        if 'desc' in rooms[currentRoom]:
            print(rooms[currentRoom]['desc']) # print the look description
        else:
            print('You can\'t see anything.')

    elif move[0] == 'help':
        showInstructions()

    elif move[0] in ['q', 'quit]']:
        print("Are you sure you want to quit? Yes/No")
        quit_query = input('>')
        if quit_query.lower() in ['y', 'yes']:
            print("Thanks for playing!")
            sys.exit()
        else:
            pass
