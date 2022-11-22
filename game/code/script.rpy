#ALL CHARACTERS ARE CURRENTLY HASHED OUT BECAUSE THE GAME WON'T RUN WITH THEM

# The Fate of Choice

# The game starts here.

label start:

    scene livingroom with dissolve

    show derek casual neutral at left with moveinleft

    d "I can’t believe we’re starting our last semester of college.."
    d "I feel like it was just yesterday that we graduated high school together"

    #show josh casual neutral at right with moveinright
    
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
            #hide josh casual neutral with dissolve
            #hide derek casual neutral with dissolve

            scene campuscafe with dissolve

            #show josh casual neutral at right with moveinright
            #show derek casual neutral at left with moveinleft

            d "I love this cafe"
            j "Yeah, this place has the best strawberry shortcake and view"
            d "Can't believe we are only going to be able to enjoy this for one more year"
            d "Makes me feel a little sad"
            j "Hey, we can always just come back as guests"
            d "Is that allowed?"
            j "Probably, they take credit card so it shouldn't matter"
            d "Hm, guess I never really thought about that"

            "Some time passes and the two finish eating their breakfast..."

            d "What time is it?"
            j "10:30.."
            j "Oh shoot, 10:30... we have to have to head to class"
            d "Oh yea, you're right. We should go now so we're not late"

            #hide josh casual neutral with dissolve
            #hide derek casual neutral with dissolve


        #FIRST MENU CHOICE 2
        "Not today, I should catch up on some work before class":
            $ academic += 1
            j "No worries, maybe another day"
            j "I'll see you later in class"

            #hide josh casual neutral with dissolve
            #hide derek casual neutral with dissolve

            scene bedroomday with dissolve
            #show derek casual neutral at left with moveinleft

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

            return

            #hide derek casual neutral with dissolve

            "Some time passes..."

            scene livingroom with dissolve
            #show derek casual neutral at left with moveinleft
            #show josh casual neutral at right with moveinright

            d "How was your breakfast?"
            j "It was great!"
            j "The campus cafe actually has some really good food"
            j "I wish you would've came, you would've loved it"
            d "You're probably right but I wanted to catch up on things before class"
            d "Speaking of class..."
            d "It's 10:30, so we should probably head to class now"
            j "Yea, you're right"
            j "Let me grab my bag"

            #hide josh casual neutral with dissolve
            #hide derek casual neutral with dissolve

    return

    scene classroom with dissolve
    #show derek casual neutral at left with moveinleft
    #show josh casual neutral at right with moveinright

    "The two arrive to class.."

    d "Looks like our professor is running late today"
    j "You're right..."
    j "He 10 minutes late right now"
    j "You know what that means right?"
    d "What..?"
    j "If our professor doesn't show up in 5 more minutes, then we get to leave"
    d "That's not even a real thing.."
    d "You know that right.."
    j "It may not be to everyone else, but it is to me"
    j "I say we skip if he doesn't show up in 5 more minutes"
    d "Eh... I don't know if that's a good idea"
    d "We're supposed to be learning some important stuff today"

    "10 minutes go by.."

    j "I gave it 10 minutes instead of 5.."
    j "I say we skip"
    d "I'm not sure.."
    d "We have a test coming up soon and I don't think I understand these topics fully"
    j "Oh come on.."
    j "It's only on class"
    j "We can study later"

    menu:
        "Not today.. I should try and learn a little more before this test"
            $ academic += 5
            $ social -= 2

            j "Maybe another day then.."
            j "We still have to get you to live a little this year"
            d "I know, I know..."
            d "I think I just really need to stay in class today"
            d "I'll do something another day"
            d "I'll see you later?"
            j "Yea, let's do something fun tonight"

            "The professor finally shows up and class finishes.."

            d "Hey Mr.Murphy, I'm having a hard time understanding some of the topics that we went over in class today"
            pm "No worries, I'm always here to help"
            pm "What can I do to help you understand a little better?"
            d "I was wondering if you could send me the powerpoints that we went over today and some practice problems for me to work through"
            pm "Absolutely! I'll email you it all during my office hours today"
            d "Great, thank you so much"
            d "I really appreciate the help"
            pm "Of course, I'm always willing to help my students"
            pm "I also want to thank you for showing up to class today"
            pm "I've noticed a lot of students skipping lately"
            d "It's my last year so I can't give up now"
            pm "Well keep up to good work!"

            scene livingroom with dissolve

            "He goes home and some time passes by..."

            j "How was class?"
            d "It was alright"
            d "I'm still confused about some of the topics that are going to be on the test so I asked for some extra help"
            j "Don't worry, you'll be ready for it next week"
            d "It's 3:00pm, should we head to study group?"
            d "We're supposed to go over some topics that'll be on the test next week"
            j "I mean I skipped so I didn't really have any intention to go today"
            j "You shouldn't go either"
            j "The test isn't until next week"


        "Okay, fine.. I'll go but just this once"
            $ academic -= 3
            $ social += 5

            j "Yay!"
            j "Let's go do something fun"
            d "Sounds good to me"
            d "I hope we don't miss too much important information today"
            j "Don't stress about it"
            j "We're going to be fine"
            j "Let's go pick up some lunch then bring it back to the apartment and binge watch our Netflix show"
            d "Alright, let's do it"

            scene livingroom with dissolve

            "They pick up food and finish watching their tv show.."

            d "I love this show"
            d "I can't believe they're not making anymore seasons"
            j "Me neither, I'm going to be upset when we finally finish it for good"
            d "Good thing we saved a few episodes to watch later"
            d "Hey, what time is it?"
            j "Uh, looks like it's 3:00pm"
            d "Shouldn't we be heading to study group?"
            j "I mean we skipped the actual class.."
            j "Might as well finish it off by not going to the study group either"
            d "Eh... but we might learn something important during study group today"
            d "We're supposed to be going over some stuff for our test next week"
            j "We can always figure it out later"
            j "The test isn't until next week"

    return

    menu:
        "Eh.. I think I'll go"
            $ social += 2
            $ academic += 2





        "You're right.. I'll skip it today"
            $ social += 2
            $ academic += 2













# This part should appear in the mid to late game
if internships:
    scene livingroom with dissolve
    #show derek casual neutral at left with moveinleft
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
        #show derek casual neutral at left with moveinleft
        #show olivia casual smile at left with moveinright

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
        return


    #Academic life without Olivia
    if academic = 0 & Olivia = False:
        scene livingroom with dissolve
        #show derek casual neutral at left with moveinleft
        #show josh casual neutral at right with moveinright

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
        return


    #Social life with Olivia
    if social = 0 & Olivia = True:
        scene livingroom with dissolve
        #show derek casual neutral at left with moveinleft
        #show olivia casual smile at left with moveinright

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
        return


    #Social life without Olivia
    if social = 0 & Olivia = False:

        scene livingroom with dissolve
        #show derek casual neutral at left with moveinleft
        #show josh casual neutral at right with moveinright

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

        #hide josh casual neutral with dissolve
        #hide derek casual neutral with dissolve
        return


    #Balanced life with Olivia
    if academic = 0 & social = 0 & Olivia = True:

        scene livingroom with dissolve
        #show derek casual neutral at left with moveinleft
        #show olivia casual smile at left with moveinright

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
        return


    #Balanced life without Olivia
    if academic = 0 & social = 0 & Olivia = False:

        scene livingroom with dissolve
        #show derek casual neutral at left with moveinleft
        #show josh casual neutral at right with moveinright

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

        #hide josh casual neutral with dissolve
        #hide derek casual neutral with dissolve
        return

    #"You ended the game with an academic score of "  + academic + " and a social score of " + social + "."
    return
