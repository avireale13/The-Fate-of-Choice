#ALL CHARACTERS ARE CURRENTLY HASHED OUT BECAUSE THE GAME WON'T RUN WITH THEM

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

    show derek eyebrow up at left with dissolve

    d "I know... You’re right"

    show derek casual neutral at left with dissolve

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

            show derek smile at left with dissolve

            d "Sounds good!"
            hide josh casual neutral with dissolve
            hide derek smile with dissolve

            scene campuscafe with dissolve

            show josh casual neutral at right with moveinright
            show derek smile no teeth at left with moveinleft

            d "I love this cafe"

            show derek casual neutral at left with dissolve

            j "Yeah, this place has the best strawberry shortcake and view"

            show derek sad at left with dissolve

            d "Can't believe we are only going to be able to enjoy this for one more year"
            d "Makes me feel a little sad"
            j "Hey, we can always just come back as guests"
            d "Is that allowed?"

            show derek casual neutral at left with dissolve

            j "Probably, they take credit card so it shouldn't matter"
            d "Hm, guess I never really thought about that"

            "Some time passes and the two finish eating their breakfast..."

            d "What time is it?"
            j "10:30.."

            show derek concerned at left with dissolve

            j "Oh shoot, 10:30... we have to have to head to class"
            d "Oh yea, you're right. We should go now so we're not late"

            hide josh casual neutral with dissolve
            hide derek concerned neutral with dissolve


        #FIRST MENU CHOICE 2
        "Not today, I should catch up on some work before class":

            show derek sad at left with dissolve

            $ academic += 1
            j "No worries, maybe another day"

            show derek casual neutral at left with dissolve

            j "I'll see you later in class"

            hide josh casual neutral with dissolve
            hide derek casual neutral with dissolve

            scene bedroomday with dissolve
            show derek casual neutral at left with moveinleft

            "What should I do now?"

            #SECOND MENU
            menu:
                #SECOND MENU CHOICE 1
                "work on homework":
                    show derek smile at left with dissolve
                    "Let's do it"

                #SECOND MENU CHOICE 2
                "look for internships":
                    show derek smile at left with dissolve
                    "Let's do it"
                    $ internships = True


            hide derek smile with dissolve

            "Some time passes..."

            scene livingroom with dissolve
            show derek casual neutral at left with moveinleft
            show josh casual neutral at right with moveinright

            d "How was your breakfast?"
            j "It was great!"
            j "The campus cafe actually has some really good food"
            j "I wish you would've came, you would've loved it"

            show derek sad at left with dissolve

            d "You're probably right but I wanted to catch up on things before class"
            d "Speaking of class..."
            d "It's 10:30, so we should probably head to class now"

            hide derek casual neutral with dissolve

            j "Yea, you're right"
            j "Let me grab my bag"

            hide josh casual neutral with dissolve
            hide derek casual neutral with dissolve


    scene classroom with dissolve
    show derek casual neutral at left with moveinleft
    show josh casual neutral at right with moveinright

    "The two arrive to class.."

    d "Looks like our professor is running late today"
    j "You're right..."
    j "He 10 minutes late right now"
    j "You know what that means right?"
    d "What..?"
    j "If our professor doesn't show up in 5 more minutes, then we get to leave"

    show derek eyebrow up at left with dissolve

    d "That's not even a real thing.."
    d "You know that right.."
    j "It may not be to everyone else, but it is to me"
    j "I say we skip if he doesn't show up in 5 more minutes"

    show derek concerned at left with dissolve

    d "Eh... I don't know if that's a good idea"
    d "We're supposed to be learning some important stuff today"

    show derek casual neutral with dissolve

    "10 minutes go by.."

    j "I gave it 10 minutes instead of 5.."
    j "I say we skip"

    show derek concerned at left with dissolve

    d "I'm not sure.."
    d "We have a test coming up soon and I don't think I understand these topics fully"
    j "Oh come on.."
    j "It's only on class"
    j "We can study later"

    menu:
        "Not today.. I should try and learn a little more before this test":
            $ academic += 5
            $ social -= 2

            j "Maybe another day then.."
            j "We still have to get you to live a little this year"

            show derek casual neutral at left with dissolve

            d "I know, I know..."
            d "I think I just really need to stay in class today"
            d "I'll do something another day"
            d "I'll see you later?"
            j "Yea, let's do something fun tonight"

            hide josh casual neutral at right with dissolve
            hide derek casual neutral at left with dissolve

            "The professor finally shows up and class finishes.."

            show derek casual neutral at left with dissolve

            #add teacher character sprite here

            d "Hey Mr.Murphy, I'm having a hard time understanding some of the topics that we went over in class today"
            pm "No worries, I'm always here to help"
            pm "What can I do to help you understand a little better?"
            d "I was wondering if you could send me the powerpoints that we went over today and some practice problems for me to work through"
            pm "Absolutely! I'll email you it all during my office hours today"

            show derek smile at left with dissolve

            d "Great, thank you so much"
            d "I really appreciate the help"

            show derek casual neutral at left with dissolve

            pm "Of course, I'm always willing to help my students"
            pm "I also want to thank you for showing up to class today"
            pm "I've noticed a lot of students skipping lately"
            d "It's my last year so I can't give up now"
            pm "Well keep up to good work!"

            hide derek casual neutral at left with dissolve

            "He goes home and some time passes by..."

            scene livingroom with dissolve

            show derek casual neutral at left with moveinleft
            show josh casual neutral at right with moveinright

            j "How was class?"

            show derek concerned at left with dissolve

            d "It was alright"
            d "I'm still confused about some of the topics that are going to be on the test so I asked for some extra help"
            j "Don't worry, you'll be ready for it next week"

            show derek casual neutral at left with dissolve

            d "It's 3:00pm, should we head to study group?"
            d "We're supposed to go over some topics that'll be on the test next week"
            j "I mean I skipped so I didn't really have any intention to go today"
            j "You shouldn't go either"
            j "The test isn't until next week"


        "Okay, fine.. I'll go but just this once":
            $ academic -= 3
            $ social += 5

            j "Yay!"
            j "Let's go do something fun"
            d "Sounds good to me"

            show derek concerned at left with dissolve

            d "I hope we don't miss too much important information today"
            j "Don't stress about it"

            show derek casual neutral at left with dissolve

            j "We're going to be fine"
            j "Let's go pick up some lunch then bring it back to the apartment and binge watch our Netflix show"
            d "Alright, let's do it"

            hide derek casual neutral at left with dissolve
            hide josh casual neutral at right with dissolve

            scene livingroom with dissolve

            "They pick up food and finish watching their tv show.."

            show derek casual neutral at left with moveinleft
            show josh casual neutral at right with moveinright

            d "I love this show"

            show derek sad at left with dissolve

            d "I can't believe they're not making anymore seasons"
            j "Me neither, I'm going to be upset when we finally finish it for good"

            show derek casual neutral at left with dissolve

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


    menu:
        "Eh.. I think I'll go":
            show derek eyebrow up at left with dissolve
            $ social += 2
            $ academic += 2

            d "I really want to make sure I'm ready for that test"
            j "I'll see you later tonight then"
            j "I think I'm going to head to the gym for a little"

            show derek casual neutral at left with dissolve

            d "Alright, I'm going to head out now so I'm not late"
            d "I'll see you when I get home"

            hide derek casual neutral at left with dissolve

            "He heads to study group then comes home.."

            show derek casual neutral at left with moveinleft

            j "How was study group?"
            d "It was actually kind of fun and I learned a lot"
            d "We played games that kind of helped me understand some things that I was confused about"
            d "You  should come with me next time"
            j "Yea, maybe next time"
            j "Sounds like it was a good time"
            d "I definitely enjoyed it"
            d "But hey, I'm kind of tired so I'm going to head to bed"
            j "Alright, I'll see you in the morning"

        "You're right.. I'll skip it today":
            $ social += 2
            $ academic += 2

            show derek concerned at left with dissolve

            d "Don't let me slip on studying next week"

            show derek casual neutral at left with dissolve

            d "But for now, let's just finish our show"
            d "Might as well finish it off since we only have a few left"
            j "You're right"
            j "Let's do it"

            hide derek casual neutral at left with dissolve
            hide josh casual neutral at right with dissolve

            "The two finish their show and off to bed.."

            show derek casual neutral at left with moveinleft
            show josh casual neutral at right with moveinright


    j "So I heard there's going to be a party tonight and I think we should definitely go"

    show derek concerned at left with dissolve

    d "Ah I don't know, I haven't actually been to a real college party before"
    j "That's exactly why we should go"
    j "It's all part of getting the full college experience"
    j "This would be a great start"
    d "I'm not sure, let me at least think about it first"
    j "Fine"
    j "You can think about it but I still expect you to say yes when I ask you later"
    d "We'll see about that"

    show derek casual neutral at left with dissolve

    j "Well in the mean time, I'm thinking about going to the gym.."
    j "Want to come with?"

    menu:
        "Sure, why not":
            $ social += 2

            d "Sounds fun"
            d "Let me go get ready really quick"
            j "Alright, I'll make us some breakfast so we can eat before we go"
            j "Are eggs and some toast good?"
            d "Sounds good to me"

            "They eat breakfast and the two go to the gym together"

            hide derek casual neutral at left with dissolve
            hide josh casual neutral at right with dissolve

            scene gym with dissolve

            show derek casual neutral at left with moveinleft
            show josh casual neutral at right with moveinright

            j "See that wasn't so bad"
            d "I feel like I haven't been to the gym in a really long time"
            d "I'm definitely going to be sore tomorrow but I'm glad I came"
            j "We should make it a regular thing"
            j "I like having a partner to spot me"
            d "Yea, let's do it again this week"
            d "I need something to keep me in shape"

            hide derek casual neutral at left with dissolve
            hide josh casual neutral at right with dissolve

            "The two get lunch and bring it home.."


        "Not today":
            $ social -= 1

            show derek concerned at left with dissolve

            d "I'm not feeling up to it today, but maybe another day"
            j "Alright, no worries"
            j "I go often so you're always welcome to come with"
            j "I'm going to head out now so I'll see you later"

            show derek casual neutral at left with dissolve

            d "Sounds good"

            hide derek casual neutral at left with dissolve
            hide josh casual neutral at right with dissolve

            scene bedroomevening with dissolve

            show derek casual neutral at left with moveinleft

            "What should I do now?"

            menu:
                "Study for the upcoming test":
                    $ academic += 1

                    show derek smile at left with dissolve

                    d "Let's do it"

                    show derek casual neutral at left with dissolve

                    d "I should really catch up on my notes before this test"

                    hide derek casual neutral at left with dissolve

                    "He studies and learns a few new topics before his exam next week"


                "Make breakfast and watch some tv":
                    show derek smile at left with dissolve

                    d "Let's do it"

                    show casual neutral at left with dissolve

                    d "I'm starved and I could use some chill time"

                    hide casual neutral at left with dissolve

                    "He makes breakfast and relaxes at home"

            scene livingroom with dissolve

            show derek casual neutral at left with moveinleft
            show josh casual neutral at right with moveinright

            d "How was the gym?"
            j "It was good"
            j "It would been a perfect day for you to come"
            d "Why's that?"
            j "I didn't have to wait for a single machine that I needed"
            j "It was super empty today"

            show derek sad at left with dissolve

            d "Darn"
            d "I'll have to go next time"

            hide derek sad at left with moveinleft
            hide josh casual neutral at right with moveinright

            "The two pick up lunch and bring it back home.."


    scene livingroom with dissolve

    show derek casual neutral at left with moveinleft
    show josh casual neutral at right with moveinright

    j "So about that party tonight.."
    j "We're definitely going right?"

    show derek concerned at left with dissolve

    d "I still don't know"
    d "Parties aren't really my scene"
    j "Come on.."
    j "You have to"
    j "It's all part of getting the full experience"

    menu:
        "I'm just not feeling it tonight":
            j "Oh come on.."
            j "We've got to get you out"
            d "I just don't feel like it tonight"
            j "Well promise me you'll at least go to one before we graduate"
            d "Eh.. maybe one party"

            show derek casual neutral at left with dissolve

            j "You better go to at least one"
            d "I can't promise but I'll definitely think about it more next time"
            d "Just let me know how it goes tonight"
            j "I will when I get back"
            j "I'm going to get ready now and head out"
            d "Alright, I'll see you later"

            hide josh casual neutral at right with dissolve

            "What should I do now?"

            menu:
                "Make some dinner and study for next weeks exam":
                    $ academic += 1
                    $ social -= 2

                    show derek smile at left with dissolve

                    d "Let's do it"

                    hide derek smile at left with dissolve

                    "He makes food, studies, then heads too bed for the night.."
                    $ social -= 3

                    scene bedroomnight with dissolve

                "Order dinner to the apartment then head to bed":

                    show derek smile at left with dissolve

                    d "Let's do it"

                    hide derek smile at left with dissolve

                    "He orders dinner then heads to bed for the night.."

                    scene bedroomnight with dissolve


            scene livingroom with dissolve

            show derek casual neutral at left with moveinleft
            show josh casual neutral at right with moveinright

            d "So how was the party last night?"
            j "It was super fun"
            j "I really wish you would've come with last night"
            j "You'll definitely have to come with next time"
            d "I thought about it last night and I'm thinking I might actually"
            j "I can promise you that the party was definitely more fun than whatever you were doing last night"
            d "You're honestly probably right"

        "Fine, I'll go":
            $ social += 5
            j "Heck yea!"

            show derek casual neutral at left with dissolve

            j "We're going to have so much fun tonight"
            j "I'm going to go shower and get ready to go"
            d "Sounds good, I'll go get ready too"
            j "Alright, so after I'll order us a quick snack before we leave"
            j "How does pizza sound?"
            d "Sounds good to me"

            hide derek casual neutral at left with dissolve
            hide josh casual neutral at left with dissolve

            "The two get ready,eat, then head to the party"

            scene bedroomnight with dissolve

            scene livingroom with dissolve

            hide derek casual neutral at left with dissolve
            hide josh casual neutral at left with dissolve

            d "I have to admit, yesterday was actually pretty fun"
            j "See"
            j "I told you it would be fun"
            d "You were right"







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

        hide derek casual neutral at left with dissolve
        hide olivia casual smile at left with dissolve

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

        hide derek casual neutral at left with dissolve
        hide josh casual neutral at right with disssolve

        "Months later..."
        "Derek and Josh run into each other at a cafe.."

        j "Oh hey Derek, do you think we could get together and do something fun like old times this week?"
        j "Feels like I haven't seen you in forever"
        d "Sorry man, I've just been caught up at work."
        d "Feels like I can never find a second of free time at this new job"
        j "No worries, we can try another time."


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

        hide derek casual neutral at left with dissolve
        hide olivia casual smile at left with dissolve

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

        hide derek casual neutral at left with dissolve
        hide olivia casual smile at left with dissolve


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

    #"You ended the game with an academic score of "  + academic + " and a social score of " + social + "."
    return
