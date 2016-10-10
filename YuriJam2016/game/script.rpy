## The script of the game goes in this file.

## These transforms account for the widescreen format of the game, placing the
## characters slightly in from the edges.
## yalign set to 1.0 snaps the image and its anchor to th ebottom of the screen.
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


## Characters

define red = Character('Red', color='#b70505')
define britta = Character('Britta', color='#ff3300')
define miralda = Character('Miralda')
define gieda = Character('Gieda')
define saoirse = Character('Saoirse')
define morgaine = Character('Morgaine')


## Images

## Backgrounds

## CGs

## Character expressions

## Red
image red neutral = "red_idle.png"
image red larger = "red002.png"

## Miralda
image miralda neutral = "red002.png"
image miralda smug = "red002.png"
image miralda cheerful = "red002.png"

## Gieda
image gieda angry = "red002.png"
image gieda shock = "red002.png"
image gieda frown = "red002.png"

## Britta
image britta eyeroll = "red002.png"
image britta angry = "red002.png"
image britta frown = "red002.png"


## The game starts here.

label start:

    scene bg room
    
    "Hello, world."
    
    show red neutral at leftish
    red "Hey!!"
    
    show red larger as red2 at rightish
    red "Who are you?"
    
    britta "Who the fuck are YOU??"
    
    menu:
        "I'm Red?":
            britta "Oh okay."
            
        "idk":
            britta "Get out of here!"
    
    britta "Anyway."

    show miralda smug
    miralda "Well, look who it is. I thought I recognized those oversized biceps." 

    show gieda angry
    gieda "Excuse me? Have we—"
    show gieda shock
    gieda "Wait… Miralda? Good gods, is that you?"

    show britta eyeroll
    britta "Oh, great." 

    show miralda neutral
    miralda "It’s been a while, hasn’t it? I haven’t seen you in—Britta, sweetie, how old are you?"
    miralda "Nineteen? Twenty?" 

    menu:
        "Ugh, mom! I’m twenty-three!":
            show britta angry
            britta "Ugh, mom! I’m twenty-three!"
            show miralda cheerful
            miralda "Twenty-three! Funny how a few drinks can make you forget a few years, isn’t it?"

        # show britta frown
        "I’m just gonna leave before this gets weird.":
            show miralda neutral
            miralda "Sigh! Fine, go play with your little friends. Mommy has some catching up to do."

    show miralda cheerful
    miralda "Incredible how a few decades can fly by. You hardly look a day uglier!" 

    show gieda frown
    gieda "I’m flattered." 

    
    ## This ends the game.

    return
