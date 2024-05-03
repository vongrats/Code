"""
Project:  Basic Text Role Playing Game (RPG)
Author:   Sam Vongratana
Notes:    A basic text based adventure. Mechanics inspired by Zork from the days of old...
          Prison Break. Get out of prison without wandering guards seeing you.
#!/bin/python3
"""

###   Initialization
inventory = []    # Inventory, initially empty
room_desc = True  # Verbose room descriptions by default. Turn to False for Brief descriptions.
action_list = ['brief', 'get', 'go', 'verbose']    # list of possible actions
go_list = ['n', 'e', 'w', 's', 'u', 'd', 'ne', 'nw', 'se', 'sw']    # List of possible directions

###   Define
def showInstructions():
    #print a main menu and the commands
    print('''========
Commands:
  go [direction], get [item], brief/verbose''')

def showStatus():
    #print the player's current status
    print('---------------------------')
    print('You are in ' + currentRoom + '.')
    if room_desc == True :
        print(rooms[currentRoom]['desc'])
        print('You can go: ', rooms[currentRoom]['opening'])
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    if (currentRoom == 'Courtyard') and (any('flare' not in s for s in inventory)):
        print('You need the flare to escape!')    
    print("---------------------------") 

#a dictionary linking a room to other rooms
rooms = {
        'Cell 1' : {
            'desc' : 'You are in a bleak cell.',
            'opening' : 'E',
            'east' : 'Block A', 'e' : 'Block A',
            'item' : 'key'},
        'Cell 2' : {
            'desc' : 'You are in an empty cell.',
            'opening' : 'S',
            'south' : 'Block A', 's' : 'Block A'},
        'Cell 3' : {
            'desc' : 'You are in an empty cell.',
            'opening' : 'N',
            'north' : 'Block A', 'n' : 'Block A'},
        'Cell 4' : {
            'desc' : 'You are in an empty cell.',
            'opening' : 'S',
            'south' : 'Block B', 's' : 'Block B'},
        'Cell 5' : {
            'desc' : 'You are in an empty cell.',
            'opening' : 'N',
            'north' : 'Block B', 'n' : 'Block B',
            'item' : 'keycard'},
        'Cell 6' : {
            'desc' : 'You are in an empty cell.',
            'opening' : 'S',
            'south' : 'Block C', 's' : 'Block C'},
        'Block A' : {
            'desc' : 'You are in a cell block hallway. There are cells north, south and west.',
            'opening' : 'N, S, E, W',
            'west' : 'Cell 1', 'w' : 'Cell 1',
            'north' : 'Cell 2', 'n' : 'Cell 2',
            'south' : 'Cell 3', 's' : 'Cell 3',
            'east' : 'Block B', 'e' : 'Block B'},
        'Block B' : {
            'desc' : 'You are in a cell block hallway. There are cells north and south.',
            'opening' : 'N, S, E, W',
            'west' : 'Block A', 'w' : 'Block A',
            'north' : 'Cell 4', 'n' : 'Cell 4',
            'south' : 'Cell 5', 's' : 'Cell 5',
            'east' : 'Block C', 'e' : 'Block C'},
        'Block C' : {
            'desc' : 'You are in a cell block hallway. There is a cell north and guard room south',
            'opening' : 'N, S, E, W',
            'west' : 'Block B', 'w' : 'Block B',
            'north' : 'Cell 6', 'n' : 'Cell 6',
            'south' : 'Guard Office', 's' : 'Guard Office',
            'east' : 'Hall', 'e' : 'Hall',
            'item' : 'locked door'},
        'Guard Office' : {
            'desc' : 'You are in guard\'s office.',
            'opening' : 'N',
            'north' : 'Block C', 'n' : 'Block C',
            'item' : 'guard'},
        'Hall' : {
            'desc' : 'You are in a plain hallway.',
            'opening' : 'W, S',
            'west' : 'Block C', 'w' : 'Block C',
            'south' : 'Courtyard', 's' : 'Courtyard',
            'item' : 'flare'},
        'Courtyard' : {
            'desc' : 'You are in an outdoor courtyard. There is the sound of a helecopter in the distance.',
            'opening' : 'N',
            'north' : 'Hall', 'n' : 'Hall'}
         }

###   Main
print('''========
Prison Break
========
You were in the wrong place at the wrong time. Innocent until proven guilty, my arse. 
You find yourself in a Russian prison and will be executed tomorrow for a crime 
you didn't commit. Find a way to the courtyard, drop a flare and get yourself 
out of there before the guards find you. Good luck!...''')

#start the player in the Hall
currentRoom = 'Cell 1'
showInstructions()

#loop forever
while True:

    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':  
        move = input('>')
    
    move = move.lower().split()

    if (move[0] not in action_list) and (move[0] not in go_list):
        print('You can\'t do that!')

    if move[0] == 'brief':
        room_desc = False  
    if move[0] == 'verbose':
        room_desc = True  
    
    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    if move[0] in go_list:
        #check that they are allowed wherever they want to go
        if move[0] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[0]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')
    
    #if they type 'get' first
    if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print('Got ' + move[1] + '!')
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

 
    #player loses if they enter a room with a monster
    if 'item' in rooms[currentRoom] and 'guard' in rooms[currentRoom]['item']:
        print('Guards caught you... GAME OVER!')
    
        play_again = input("Play again? (y/n): ")
        if (play_again.lower() != "y") or (play_again.lower() != "yes"):
            break

    #player wins is they get to the garden with the key and potion
    if (currentRoom == 'Courtyard') and (any('flare' in s for s in inventory)):
        
 #       if ('flare' in 'Courtyard'['item']):
        print('The flare signals a helecopter to come get you!')
        print('A ladder drops in front of you and you climb up.')
        print('Congratulations! You escaped the prison... YOU WIN!')
        break