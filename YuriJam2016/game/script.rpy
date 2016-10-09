## The script of the game goes in this file.

## These transforms account for the widescreen format of the game, placing the
## characters slightly in from the edges.
## The negative xzoom flips a sprite horizontally.

## Transforms

init:
    transform leftish:
        xpos .1
        yalign 1.0
    transform rightish:
        xpos .6
        yalign 1.0
        xzoom -1.0


## Declare characters used by this game. The color argument colorizes the name
## of the character.

## Characters

#  define e = Character('Eileen')

define red = Character('Red', color='#b70505')
define britta = Character('Britta', color='#ff3300')
define miralda = Character('Miralda')
define gieda = Character('Gieda')
define saoirse = Character('Saoirse')
define morgaine = Character('Morgaine')

## Images

image red main = "red_idle.png"

## The game starts here.

label start:

    scene bg room
    
    show red main at leftish

    "Hello, world."
    
    red "Hey!!"
    
    show red main as red2 at rightish

    red "Who are you?"
    
    britta "Who the fuck are YOU??"
    
    ## This ends the game.

    return
