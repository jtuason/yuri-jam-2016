## The script of the game goes in this file.

## These transforms account for the widescreen format of the game, placing the
## characters slightly in from the edges.
## yalign set to 1.0 snaps the image and its anchor to the bottom of the screen.
## The negative xzoom flips a sprite horizontally.

## Initialization block

init:
    
    ## Transforms
    
    transform leftish:
        xpos .1
        yalign 1.0
    transform rightish:
        xpos .6
        yalign 1.0
        xzoom -1.0
    transform rightmost:
        xpos 1.05
        yalign 1.0
        xzoom -1.0
    transform rightFlipped:
        xpos .75
        yalign 1.0
        xzoom -1.0
    transform  saoirseRight:
        xpos .7
        yalign 1.0
        xzoom 1.0
    transform rightishFlipped:
        xpos .6
        yalign 1.0
        xzoom 1.0
    transform leftShort:
        xpos .1
        yalign 1.0
        zoom .8
    transform centerLeftShort:
        xpos .2
        yalign 1.0
        zoom .8  
    transform centerShort:
        xpos .3
        yalign 1.0
        zoom .8
    transform centerRightish:
        xpos .55
        yalign 1.0
        xzoom -1.0
        
    ## Variables
    
    $ metSaorgaine = False
    $ metGieda = False


## Transitions

define fastDissolve = Dissolve(.25)

## Characters

define red = Character('Red', color='#b70505')
define britta = Character('Britta', color='#ff3300')
define miralda = Character('Miralda', color='#cc3399')
define gieda = Character('Gieda', color='#6699ff')
define saoirse = Character('Saoirse', color='#912c3f')
define morgaine = Character('Morgaine', color='#498425')


## Images

## Backgrounds
image foodStalls = "bg_foodStalls.png"
image cornMaze = "bg_cornfield.png"
image frontGate = "bg_carnivalEntrance.png"

## CGs

## Character expressions

## Red
image red neutral = "red_neutral.png"

## Miralda
image miralda neutral = "miralda_neutral.png"
image miralda frown = "miralda_frown.png"
image miralda angry = "miralda_angry.png"
image miralda uncomfortable = "miralda_uncomfortable.png"
image miralda amused = "miralda_amused.png"
image miralda cheerful = "miralda_cheerful.png"
image miralda devious = "miralda_devious.png"
image miralda wistful = "miralda_wistful.png"
image miralda puzzled = "miralda_puzzled.png"

## Gieda
image gieda neutral = "gieda_neutral.png"
image gieda frown = "gieda_frown.png"
image gieda alarm = "gieda_alarm.png"
image gieda blush = "gieda_blush.png"
image gieda angryBlush = "gieda_angryBlush.png"
image gieda smile = "gieda_smile.png"
image gieda angry = "gieda_angry.png"

## Britta
image britta neutral = "britta_neutral.png"
image britta laughing = "britta_laughing.png"
image britta angry = "britta_angry.png"
image britta uncomfortable = "britta_uncomfortable.png"
image britta frown = "britta_frown.png"
image britta grin = "britta_grin.png"
image britta puzzled = "britta_puzzled.png"
image britta surprised = "britta_surprised.png"
image britta devious = "britta_devious.png"
image britta eyeroll = "britta_eyeroll.png"

## Saoirse
image saoirse neutral = "saoirse_neutral.png"
image saoirse cheerful = "saoirse_cheerful.png"
image saoirse flustered = "saoirse_flustered.png"
image saoirse angry = "saoirse_angry.png"
image saoirse eyeroll = "saoirse_eyeroll.png"
image saoirse crestfallen = "saoirse_crestfallen.png"
image saoirse sad = "saoirse_sad.png"
image saoirse surprised = "saoirse_surprised.png"
image saoirse playful = "saoirse_playful.png"
image saoirse hopeful = "saoirse_hopeful.png"
image saoirse smiling = "saoirse_smiling.png"
image saoirse frown = "saoirse_frown.png"

## Morgaine
image morgaine neutral = "morgaine_neutral.png"
image morgaine surprised = "morgaine_surprised.png"
image morgaine eyeroll = "morgaine_eyeroll.png"
image morgaine smirk = "morgaine_smirk.png"
image morgaine smiling = "morgaine_smiling.png"
image morgaine angry = "morgaine_angry.png"
image morgaine annoyed = "morgaine_annoyed.png"
image morgaine sad = "morgaine_sad.png"



## The game starts here.

label start:
    
    scene frontGate


    show miralda neutral at centerRightish
    with dissolve
    miralda "And here we are! Fall Fling Hallow’s Eve Carnival. That wasn’t too bad a drive, now, was it?" 


    show britta frown at left
    with easeinleft
    britta "If you don’t mind a billion miles of corn in every direction, yeah, it was great."


    miralda "I find the country aesthetic quite charming, actually. In small doses." 


    show britta neutral
    britta "Oh, hey, looks like they have a list of attractions here."
    show britta puzzled
    britta "Hmm… a pumpkin patch, a corn maze, some rides, a ton of stalls for crafts and food... "
    show britta neutral
    britta "Ooh, and a costume competition!"
    show britta grin
    britta "Hope they’ve got a ’hottest costume’ category, ’cause I’ve got that shit in the bag."
    show britta neutral
    britta "Get it? ’Cause I’m a devil? Ha ha."


    show miralda amused
    miralda "Oh, sweetie."
    miralda "If anyone’s going to win the ’hottest costume’ category, it’s going to be me." 


    britta "In your dreams, you old broad! They only give that award to conventionally attractive twenty-somethings."


    miralda "Oh, darn. That rules us both out, doesn’t it?"


    show britta angry
    britta "Fuck off, mom." 


    show miralda neutral
    miralda "Before we visit any attractions, we should make a plan of attack."
    miralda "Should we do that first, or should we refuel with a quick bite?" 


    menu:
        extend "" # extra line
        
        "Let’s make a plan.":

            show britta neutral
            britta "I’ve got no idea what we’re doing, so let’s get all strategic and shit."


            show miralda neutral
            miralda "Fair enough. Let’s go in and find a map or guide. I have our tickets right here." 


            jump meetGieda


        "Plans are for nerds. Let’s eat!" if not metSaorgaine:

            show britta neutral
            britta "I’m craving some crappy carnival food. I’m gonna find a candied apple stand and shove every one of them up my asshole." 


            show miralda neutral
            miralda "I’m fond of hard cider, myself."
            miralda "Let’s not dawdle, then. I have our tickets right here." 


            jump meetSaorgaine

label meetGieda:
    
    $ metGieda = True
    
    scene foodStalls


    show miralda puzzled at left
    with fade
    miralda "Hmm… I’m not seeing a map anywhere."
    miralda "Wait as second, is that…?"


    show gieda neutral at rightishFlipped
    with dissolve
    gieda "..."


    show miralda neutral
    miralda "Well, look who it is. I thought I recognized those oversized biceps." 


    show gieda angry
    gieda "Excuse me? Have we—"
    show gieda alarm
    gieda "Wait… Miralda? Good gods, is that you?"


    show britta eyeroll at center
    with easeinleft
    britta "Oh, great."


    show miralda neutral
    miralda "Gieda Dreng. It’s been a while, hasn’t it? I haven’t seen you in—Britta, sweetie, how old are you?"
    miralda "Nineteen? Twenty?" 


    show britta angry
    britta "Ugh, mom! I’m twenty-three!"


    show miralda cheerful
    show britta angry behind miralda, gieda
    miralda "Twenty-three! Funny how a few drinks can make you forget a few years, isn’t it?"
    miralda "Time really does fly. You hardly look a day uglier, Gieda!" 


    show gieda frown
    gieda "I’m flattered." 


    britta "The hell are you doing here anyway, Dreng? Don’t you have a fire to put out?" 


    show gieda neutral
    gieda "Not at the moment, but these jack-o-lanterns do present a fire hazard. Can’t hurt to have a firefighter on hand." 
    gieda "Actually, Alice asked me to come. She and her family should be scattered around the carnival by now."


    show miralda amused
    miralda "She considers you family? What a sweetheart."


    show britta eyeroll
    britta "What a nerd." 
    show britta neutral
    britta "Where is she, anyway? Charming some hapless maiden?" 


    gieda "I’m not sure. She didn’t mention where we should meet." 


    show miralda neutral
    miralda "Why don’t you spend some time with us, then? It must be a little lonely wandering alone in a sea of screaming children." 


    show britta frown
    britta "Mom, no." 


    show gieda frown
    gieda "With you? I’d rather not." 


    show miralda frown
    miralda "Oh, don’t be like that. What, are you still upset about that little falling out?" 
    show miralda neutral
    miralda "Why, it’s been over twenty years, Gieda! You’re not one to hold a grudge that long, are you?"


    show gieda angry
    gieda "A ’falling out’? Is that what you–"
    show gieda frown
    gieda "No, you know what? We aren’t discussing this. I didn’t come here to open old wounds." 


    show miralda frown
    miralda "Still as over-serious as ever, I see. Some things never change." 


    britta "Great, we’ve established that Gieda Dreng is the most emotionally constipated woman on earth. Can we go?" 


    gieda "That might be for the best." 


    miralda "Fine. Let’s go, Britta. Pick a direction for us." 


    menu:
        extend "" # extra line
        
        "I’m starving. Time for some greasy carnival food!" if not metSaorgaine:
            show britta neutral
            britta "All this drama is making me hungry. Let’s go eat!"
            show miralda frown
            miralda "Agreed. Lead the way, sweetheart." 


            jump meetSaorgaine


        "Let’s check out that corn maze.":
            show britta puzzled
            britta "Huh… looks like a bunch of people are gathered outside the corn maze. Let’s check it out."
            show miralda puzzled
            miralda "The corn maze? Well, all right. I’ll follow your lead." 


            jump cornmazeStart

label meetSaorgaine:
    
    $ metSaorgaine = True
    
    scene foodStalls


    show saoirse cheerful at leftish
    with fade
    saoirse "Morgaine! Morgaine, hi. I-wow."


    show morgaine surprised at rightish
    with fastDissolve
    morgaine "Saoirse?"
    morgaine "What are you doing here?"


    saoirse "Are you a witch tonight? Somehow, I thought you’d be hairier."


    show morgaine neutral
    morgaine "Ah, no. Not tonight."
    morgaine "I save that costume for...special occasions."


    show saoirse smiling
    saoirse "Well, you still look nice, even though it’s kind of a bummer."


    morgaine "You wore the red hood on purpose, then."


    show saoirse cheerful
    saoirse "I sure did. And I have a whole slew of wolf jokes up my sleeves, this time."
    show saoirse playful
    saoirse "Why, grandmother, what big teeth you have!"


    show morgaine eyeroll
    morgaine "Original."
    morgaine "I’m surprised you didn’t come dressed as a virgin."


    show saoirse neutral
    saoirse "That was one time."
    saoirse "In middle school."
    saoirse "For a play."


    show morgaine smirk
    morgaine "And you looked so very precious."


    saoirse "I regret inviting you to that so much."


    morgaine "I would have had to go either way, for Atreo. Mother wouldn’t have let me skip it."
    morgaine "I hope you find comfort in the knowledge that nothing would have saved you."


    show saoirse eyeroll
    saoirse "Okay, slow your roll, you generic fantasy villain."


    show morgaine smiling
    morgaine "Who even says that, anymore?"


    show saoirse smiling
    saoirse "You’re one to talk. I learned it from you."


    # "A moment passes, then Morgaine’s smile drops. She checks her phone, then gazes searchingly into the crowd."
    show morgaine neutral
    "..."
    show morgaine eyeroll
    "..."
    show morgaine sad
    "..."

    show saoirse hopeful
    show morgaine neutral
    saoirse "So...how have you been?"


    show morgaine neutral
    morgaine "Fine."


    show saoirse smiling
    saoirse "I wasn’t sure you’d actually be here."
    saoirse "It honestly seemed just as likely that you’d spend the night alone in that pit you call a bedroom."


    morgaine "Interesting that you’d say that. I have particularly vivid memories of a certain spoiled little girl begging me to help complete her chores."


    show saoirse cheerful
    saoirse "How strange! Did you ever say no?"


    morgaine "You know perfectly well that I didn’t."


    show saoirse smiling
    saoirse "You were very sweet to me, back then. I always wanted to be around you."


    morgaine "..."
    morgaine "Why are you here, Saoirse?"


    show saoirse neutral
    saoirse "I thought maybe we could talk, for once."


    morgaine "Atreo’s supposed to meet me in five minutes. Can’t this wait?"


    saoirse "I’d love to, if I had any guarantee that we’d meet later. You’ve been so hard to find, lately. It almost makes me think you’re avoiding me."


    morgaine "That’s because I was."
    morgaine "I didn’t think we needed to talk about anything else."


    show saoirse crestfallen
    saoirse "Ah…"
    show saoirse neutral
    saoirse "I’m not sure I agree."


    morgaine "Okay."
    morgaine "Well, I’m not doing this tonight."


    saoirse "Atreo’s not coming."


    morgaine "Wh-"
    morgaine "..."
    morgaine "Tell me you didn’t."


    saoirse "...I’m sorry."


    show morgaine angry
    morgaine "Oh, outstanding."


    show saoirse sad
    saoirse "It was the only way you’d talk to me!"
    saoirse "You don’t return my texts, you don’t answer my calls, and you don’t open your door when I knock on it. What else were we supposed to do?"


    morgaine "Wow, I’m not sure. Maybe respect my space and not involve my brother?"


    saoirse "I didn’t. He involved himself."
    saoirse "He’s just as sick of you tiptoeing around me as I am."


    morgaine "Well, glad your breakup didn’t affect your collective inability to stay out of my lane."


    show saoirse angry
    saoirse "You kissed me, remember?"
    saoirse "Where was your lane then?"


    show britta neutral at centerShort
    with easeinleft
    britta "Yo, this tea is great and all, but could you maybe please perchance get the fuck out of my way?"


    show saoirse angry at left
    with easeinright
    show morgaine angry at right
    with easeinleft
    saoirse "Excuse me?"


    britta "The popcorn stall. You’re standing right in front of it."
    britta "I like having something to munch on when I eavesdrop, you know?" 


    show miralda neutral at leftish
    with easeinleft
    show britta behind miralda, saoirse, morgaine
    miralda "Morgaine, dear! I didn’t expect to see you out of the house, let alone at an amusement park."
    miralda "You should have told me you were coming; we could have dressed to match!" 


    show morgaine neutral
    morgaine "It was a last minute decision."
    morgaine "Besides, I have a feeling we wouldn’t pair very well."


    miralda "Hmm… yes, I suppose dumpy swamp witch and sexy enchantress are two entirely different beasts." 
    show miralda cheerful
    miralda "We’ll just have to settle for the tried and true ’witch and familiar’ combination!" 


    show saoirse neutral at center
    with easeinleft
    saoirse "If you had just come as a werewolf like you were supposed to…"
    
    show morgaine neutral at rightmost
    with easeinleft
    morgaine "Considering I had no idea you were going to be here, I fail to see how that sentiment holds any value."


    show miralda devious at left
    with easeinright
    miralda "Costume missteps notwithstanding, you look absolutely delicious, Saoirse. I could just gobble you up!" 


    show saoirse flustered at rightFlipped
    with easeinleft
    saoirse "Ah, that’s...um...kind of you."


    show britta frown at centerLeftShort
    with easeinleft
    britta "Mom, you know these clowns?" 


    show miralda neutral
    miralda "Sweetheart, I know everyone worth knowing." 


    show saoirse neutral
    saoirse "I’m Saoirse, by the way. I don’t think we’ve met."


    show britta puzzled
    britta "’Saoirse’? Uh, how do you pronounce that, exactly?"


    show saoirse frown
    saoirse "..."
    saoirse "You literally just said it."


    show morgaine smirk
    morgaine "I’m Morgaine."


    show britta grin
    britta "Britta Morne! Pleased to meetcha." 


    show saoirse surprised
    saoirse "I didn’t know you had a daughter, Miralda."


    show miralda wistful
    miralda "Sigh! Far too many, in fact. And this one’s the worst."  


    show britta neutral
    britta "Well, she’s not wrong." 


    show miralda neutral
    miralda "You know, Saoirse…"
    miralda "For all that we’ve spoken, I feel as though we don’t know each other very well." 
    show miralda devious
    miralda "Why don’t we find somewhere more private and see if we can’t get a little closer?"


    show saoirse cheerful
    saoirse "Oh, I’d love that!"
    saoirse "Why don’t we ride the ferris wheel? That seems like a great place to chat."


    show miralda cheerful
    miralda "That sounds perfect!"
    show miralda devious 
    miralda "I have so many things I’ve been meaning to share with you." 


    show saoirse surprised
    saoirse "Wow, really?"
    saoirse "That’s so sweet."


    show morgaine annoyed
    morgaine "Are you real right now, Saoirse?"


    show saoirse neutral at saoirseRight
    with easeinright
    saoirse "What? It’s nice."
    saoirse "At least someone wants to spend time with me, for a change."


    show morgaine neutral
    morgaine "If I promise that we’ll talk before the night is over, will you please not follow any predatory older women into dark, isolated places?"


    show miralda frown
    miralda "Oh, don’t be a killjoy, Morgaine. I’m just having a little fun!" 


    morgaine "..."
    morgaine "Right."


    show saoirse crestfallen:
        xzoom -1.0
    saoirse "Wait. So does this mean neither of you will ride the ferris wheel with me?"


    show britta grin
    britta "I don’t count as an older predatory woman, right? I’ll go!" 


    show morgaine annoyed
    morgaine "Look, just stick with me for now, all right?"


    show saoirse neutral:
        xzoom 1.0
    saoirse "Not if you’re going to have that attitude all night."


    show morgaine neutral
    morgaine "..."
    morgaine "You’re right. I’m sorry."
    morgaine "Can we just-?"
    morgaine "You were right, earlier. We do need to talk. But can we just make the best of this for now?"
    morgaine "It would make me feel better if we stuck together."


    show saoirse smiling
    saoirse "Yeah, okay. We can do that. We can just...have fun, for now."
    show saoirse neutral
    saoirse "But you have to promise me we’ll talk, later. Don’t avoid me again."
    show saoirse sad
    saoirse "I’ve really missed you."


    show morgaine sad
    morgaine "Yeah…"
    morgaine "I…"
    morgaine "I promise."


    show saoirse cheerful:
        xzoom -1.0
    saoirse "Good! Now hold my hand so we don’t get separated."


    show britta laughing
    britta "Gayyyyyy"


    show morgaine neutral
    morgaine "..."


    show miralda neutral
    miralda "Well, if you two are heading off, we should do the same."
    miralda "Where should we go next, dear?" 


    menu:
        extend "" # extra line
        
        "Let’s find a map and figure out what we’re doing next." if not metGieda:
            show britta neutral
            britta "We should do that planning thing we mentioned earlier. You know, scope out the scene."
            show miralda neutral
            miralda "Good idea. I’ll feel better when we have a plan under our collective belt." 
            miralda "But first, hand me some of that popcorn, won’t you?"
            britta "What? No! Get your own, you cheapskate!" 


            jump meetGieda


        "Let’s check out that corn maze.":
            show britta puzzled
            britta "Huh… looks like a bunch of people are gathered outside the corn maze. Let’s check it out."
            show miralda puzzled
            miralda "The corn maze? Well, all right. I’ll follow your lead." 


            jump cornmazeStart


label cornmazeStart:
    scene cornMaze
    with fade

    show britta surprised at leftShort
    with dissolve
    britta "Wow, looks like half the fair is here."


    show miralda puzzled at rightish
    miralda "It looks as though they only just opened the maze to visitors." 
    miralda "I’ve also heard this is the biggest corn maze in the tristate area, which explains the crowd." 


    show britta neutral
    britta "Oh, hey, there are some rules posted here."
    britta "’1. Please monitor all children under the age of 13 at all times.’"
    britta "’2. Do not walk through the maze walls.’"
    britta "’3. Please travel in groups no smaller than three.’"
    show britta frown
    britta "’Groups no smaller than three’? That’s a weird rule." 


    show miralda neutral
    miralda "We’d best find another friend, then." 


    show britta devious
    britta "A friend, huh? Guess this is where we split."


    show miralda amused
    miralda "You’d leave your own mother behind? You really are a wretch." 


    show britta neutral
    britta "Well, you know, the apple doesn’t fall far from the huge bitch."
    britta "Let’s see… looks like my choices of partners are…" 


    show miralda neutral
    miralda "Wait, Britta! You can’t choose your partners now!"


    show britta puzzled
    britta "Huh? Why the hell not?"


    miralda "Because this is only the demo version! The player will have to wait until the full version is out to progress any further!" 


    show britta surprised
    britta "Oh, shit, you’re right!"
    show britta neutral
    britta "*Ahem* Hey, folks! Tune in when the full version is released if you want me to harass my friends (and enemies) into dating!"


    miralda "There will be drama! Comedy! Heartbreak! Young love! Old flames!" 


    britta "Don’t we have some awkward dads in here too, somewhere?" 


    miralda "Awkward fathers! Hot mothers! Ungrateful daughters!" 


    show britta frown
    britta "They get it, mom." 
    show britta neutral
    britta "Oh, and even after the full release, we’ll probably see some additional pairings and endings added over time." 
    show britta uncomfortable
    britta "Uh, not that I know what that means, since I’m a fictional character stuck in a video game."
    show britta neutral
    britta "Anyway, thanks for playing! And Happy Halloween!" 

    
    ## This ends the game.

    return
