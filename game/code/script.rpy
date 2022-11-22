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
    $ internships = False
    #FIRST MENU
    menu:
    #FIRST MENU CHOICE 1
        "Sure, where should we go?":
            $ social +=4
            j "Let's go to the cafe on campus"
            d "Sounds good!"
            hide josh casual neutral with dissolve
            hide derek casual neutral with dissolve

            scene campuscafe with dissolve

            show josh casual neutral at right with moveinright
            show derek casual neutral at left with moveinleft

            d "I love this cafe"
            j "Yeah, this place has the best strawberry shortcake and view"
            d "Can't believe we are only going to be able to enjoy this for one more year"
            d "Makes me feel a little sad"
            j "Hey, we can always just come back as guest"
            d "Is that allowed?"
            j "Probably, they take credit card so it shouldn't matter"
            d "Hm, guess I never really thought about that"
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
                    $ internships = True



# This part should appear in the mid to late game
if internships:
    scene livingroom with dissolve
    show derek casual neutral at left with moveinleft
    d "Looks like I got some free time, guess I'll check my emails for the day"
    d "Wait... that's the internship I applied for!"
    d "No way!"
    d "I got the internship!"
    d "It looks like it's gonna eat up most of my free time, but I could definitely use the experience"
    menu:
        "Accept the Internship":
            $ academic += 10
            $ social -= 5
            d "Screw it, I can do this. It is my last year of college."
        "Don't accept the Internship":
            $ academic -= 1
            $ social += 2
            d "On second thought, I am probably not cut out for this"

    

   

    # This ends the game.
    
    "Months later..."

    #Academic life with Olivia
    if academic = 0 & Olivia = True:
       scene livingroom with dissolve
       show derek casual neutral at left with moveinleft
       show olivia casual smile at left with moveinright

        d "Hey Babe, do you remember the job that I interviewed for a couple of weeks ago?"
        o "Yea, why?"
        d "The company finally contacted me back and I didn't get the job"
        o "Oh my gosh!"
        o "I'm so proud of you"
        o "You deserve it. You really have worked so hard for this"
        d "This really is the opportunity of a life time"
        d "I've been working all year for this"

        "Months later..."

        o "Hey, I think we should talk.."
        o "You've been super busy lately and I don't feel like a priority in your life anymore"
        o "I just feel like this isn't working out anymore"
        o "...we aren't as happy as we used to be"
        d "My work is just really time consuming and I have to be in the office for most of every day"
        d "I really am sorry"


    #Academic life without Olivia
    if academic = 0 & Olivia = False:
        scene livingroom with dissolve
        show derek casual neutral at left with moveinleft
        show josh casual neutral at right with moveinright

        d "Hey Josh, guess what.."
        j "What?"
        d "Do you remember the job that I interview for a couple of weeks ago?"
        j "Yea, why?"
        d "Well the company called this morning and offered me the job"
        j "That's amazing! Congratulations man.."
        j "See I told you having a little fun during your last year wouldn't ruin the “plan”"
        j "I'm really proud of you"
        d "I admit.. you were right"
        d "We made a ton of memories that I'll never forget and I thank you for that"
        d "Let's go get dinner to celebrate. My treat"

        "Months later..."
        "Derek and Josh run into each other at a cafe.."

        j "Oh hey Derek, do you think we could get together and do something fun like old times this week?"
        j "Feels like I haven't seen you in forever"
        d "Sorry man, I've just been caught up at work."
        d "Feels like I can never find a second of free time at this new job"
        j "No worries, we can try another time."
        d "I'm sorry. I miss the old times we had together"


    #Social life with Olivia
    if social = 0 & Olivia = True:

        scene livingroom with dissolve
        show derek casual neutral at left with moveinleft
        show olivia casual smile at left with moveinright

        d "Hey Babe, do you remember the job that I interviewed for a couple of weeks ago?"
        o "Yea, why?"
        d "The company finally contacted me back and I got the job"
        o "Awe, that sucks."
        o "I'm really sorry"
        d "Eh.. it's alright"
        d "I guess I just lost sight of my academics this past year"
        d "My grades were slipping and I didn't do enough to prepare for my future after graduation"

        "Months later..."

        o "Hey, I think we should talk.."
        o "You've been really unhappy for a while and nothing I've done ever seems to help"
        o "I just feel like this isn't working out anymore"
        o "...we aren't as happy as we used to be"
        d "I'm really sorry. I should've done more to secure a better future for myself"


    #Social life without Olivia
    if social = 0 & Olivia = False:

         scene livingroom with dissolve
         show derek casual neutral at left with moveinleft
         show josh casual neutral at right with moveinright

         d "Hey Josh, do you remember the job that I interviewed for a couple of weeks ago?"
         j "Yea, why?"
         d "The company finally contacted me back and I didn't get the job"
         j "Awe jeez, that sucks."
         j "I'm really sorry man"
         d "Eh.. it's alright"
         d "I guess I just lost sight of my academics this past year"
         d "My grades were slipping and I didn't do enough to prepare for my future after graduation"
         j "You and me both"
         j "I guess we'll both be stuck at our 9-5 jobs until we can figure something else out.."
         d "I guess so. This is definitely not the plan I had in mind for this year."

         hide josh casual neutral with dissolve
         hide derek casual neutral with dissolve


    #Balanced life with Olivia
    if academic = 0 & social = 0 & Olivia = True:

        scene livingroom with dissolve
        show derek casual neutral at left with moveinleft
        show olivia casual smile at left with moveinright

        d "Hey babe..."
        d "Do you remember that job that I interviewed for.."
        o "Yea, what about it?"
        d "Well the company called this morning and offered me the job"
        o "Oh my gosh!"
        o "I'm so proud of you"
        o "You deserve it. You really have worked so hard for this"
        d "This really is the opportunity of a life time and now we can get married and build a home together."
        d "I'm so excited to see what else the future holds for us."
        d "I love you Olivia"


    #Balanced life without Olivia
    if academic = 0 & social = 0 & Olivia = False:

        scene livingroom with dissolve
        show derek casual neutral at left with moveinleft
        show josh casual neutral at right with moveinright

        d "Hey Josh, guess what.."
        j "What?"
        d "Do you remember the job that I interview for a couple of weeks ago?"
        j "Yea, why?"
        d "Well the company called this morning and offered me the job"
        j "That's amazing! Congratulations man.."
        j "See I told you having a little fun during your last year wouldn't ruin the “plan”"
        j "I'm really proud of you"
        d "I admit.. you were right"
        d "We made a ton of memories that I'll never forget and I thank you for that"
        d "Let's go get dinner to celebrate. My treat"

        hide josh casual neutral with dissolve
        hide derek casual neutral with dissolve
        
    "You ended the game with an Academic Score of " + academic + " and a Social Score of " + social
    return
