## The script of the game goes in this file.

## These transforms account for the widescreen format of the game, placing the
## characters slightly in from the edges.
## The negative xzoom flips a sprite horizontally.

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

define e = Character('Eileen')

define red = Character('Red', color='#b70505')

image red main = "red_idle.png"

## The game starts here.

label start:

    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    scene bg room

    ## This shows a character sprite. A placeholder is used, but you can replace
    ## it by adding a file named "eileen happy.png" to the images directory.
    
    show red main at leftish

    ## These display lines of dialogue.

    "Hello, world."
    
    red "Hey!!"
    
    show red main as red2 at rightish

    red "Who are you??"

    e "Once you add a story, pictures, and music, you can release it to the world!"

    ## This ends the game.

    return
