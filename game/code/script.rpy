# The Fate of Choice

# The game starts here.

label start:

    scene livingroom with dissolve

    show derek casual neutral at left with moveinleft

    d "I can’t believe we’re starting our last semester of college.."
    d "I feel like it was just yesterday that we graduated high school together"

    show josh casual neutral at right with moveinright
    
    j "I know right"
    j "All this time together and you still haven’t gotten the full college experience.."
    j "We can’t waste the time we have left"
    d "I just want to make sure I graduate with a plan"
    j "You’ve spent every second of your time and energy on this “plan” since the day we stepped foot on this campus..."
    j "A little distraction won’t ruin the “plan”"
    j "You’re only 22..."
    j "You’ve got to live a little"
    d "I know... You’re right"
    j "We’re going to make it happen"
    j "Me and you..."
    j "We’re going to give you your final college experience this year"
    j "But hey, I’m going to go get some breakfast"
    j "You want to come with?"

    $ social = 0
    $ academic = 0

    #FIRST MENU
    menu:
    #FIRST MENU CHOICE 1
        "Sure, where should we go?":
            $ social +=1
            j "Let's go to the cafe on campus"
            d "Sounds good!"

            hide josh casual neutral with dissolve
            hide derek casual neutral with dissolve

            scene campuscafe with dissolve

            show josh casual neutral at right with moveinright
            show derek casual neutral at left with moveinleft

            d "I love this cafe"

        #FIRST MENU CHOICE 2
        "Not today, I should catch up on some work before class":
            $ academic += 1
            j "No worries, maybe another day"
            j "I'll see you later in class"

            hide josh casual neutral with dissolve

            "What should I do now?"

            #SECOND MENU
            menu:
                #SECOND MENU CHOICE 1
                "work on homework":
                    "Let's do it"

                #SECOND MENU CHOICE 2
                "look for internships":
                    "Let's do it"






    

   

    # This ends the game.

    return
