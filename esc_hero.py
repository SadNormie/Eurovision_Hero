import time
import random
import participating_countries

def brain(): #The function running Eurovision_Hero
  
    odds = ["31.5%", "21%", "9.5%", "5%", "4%", "3.5%", "3%", "2.5%", "2%", "1.5%", "1%", "1%", "1%", "1%", "1%", "1%", "1%", "1%", "1%", "1%", "1%", "1%", "1%", "1%", "1%", "0.5%"]
    
    
    
    the_jury, the_televote, participants = participating_countries.jury(participating_countries.finalists())
    print('''\nNow you are ready for the voting process.
As you may have noticed, you haven't had the opportunity to add a televote.
Don't worry, though! The program will automatically make a televote equal to the jury.
As of Eurovision 2023, the program will also automatically add "Rest of the world" as a member of the televote.

Press "enter" to continue''')
    input("")
    print("This program gives points based on an odds based system. The countries you wrote has the following chance of getting 12 points from the jury, with the assumption, that 26 participants are present:")
    time.sleep(10)
    for e in range(len(participants)):
        print(participants[e], odds[e])
        time.sleep(0.5)
    print('''\nPress "enter" to continue''')
    input("")
    random.shuffle(the_jury), random.shuffle(the_televote)
    for y in range(len(the_jury)):
        odds = [63+random.randrange(-61, 32), 
                42+random.randrange(-40, 21), 
                19+random.randrange(-17, 10), 
                10+random.randrange(-8, 5), 
                8+random.randrange(-6, 4), 
                7+random.randrange(-5, 4), 
                6+random.randrange(-4, 3), 
                5+random.randrange(-3, 3), 
                4+random.randrange(-2, 2), 
                3+random.randrange(-1, 2), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                1+random.randrange(0, 1)]
        
        points = [1, 2, 3, 4, 5, 6, 7, 8, 10, 12]
        odds_by_participant = [[participant, odds[index]] for index, participant in enumerate(participants)]
        winners = []
        value = 0 
        jury_currently_voting = the_jury[y]
        if "Greece" in participants and "Cyprus" == jury_currently_voting:
            for w in range(len(participants)):
                if "Greece" in odds_by_participant[w][0]:
                    odds_by_participant[w][1] = 10000
                    break
        elif "Cyprus" in participants and "Greece" == jury_currently_voting:
            for w in range(len(participants)):
                if "Cyprus" in odds_by_participant[w][0]:
                    odds_by_participant[w][1] = 10000
                    break
        elif "Armenia" in participants and "Azerbaijan" == jury_currently_voting:
            for w in range(len(participants)):
                if "Armenia" in odds_by_participant[w][0] and len(participants) > 11:
                    odds_by_participant[w][0] = jury_currently_voting
                    break
        elif "Azerbaijan" in participants and "Armenia" == jury_currently_voting:
            for w in range(len(participants)):
                if "Azerbaijan" in odds_by_participant[w][0] and len(participants) > 11:
                    odds_by_participant[w][0] = jury_currently_voting
                    break

            
        for x in range(len(odds_by_participant)):
            odds_by_participant[x].append(value)
            value += odds_by_participant[x][1]
            odds_by_participant[x].append(value)
        

        stopper = len(odds_by_participant)
        if len(odds_by_participant) >= 11:
            stopper = 11
        while len(winners) < stopper - 1:
            casting_vote = random.randrange(0, value)
            for x in range(len(odds_by_participant)):
                if casting_vote > odds_by_participant[x][2] and casting_vote < odds_by_participant[x][3] and odds_by_participant[x][0] not in winners and odds_by_participant[x][0] not in jury_currently_voting:
                    winners.append(odds_by_participant[x][0])
                

        winners.reverse()
        print("Now calling", jury_currently_voting + "!\n")
        for p in range(len(winners)):
            if p == 0:
                time.sleep(0.25)
                print(points[p], "point goes to", winners[p])
            elif p == 9:
                input("")
                print(jury_currently_voting, "gives", points[p], "points to", winners[p] + "!")
            else:
                time.sleep(0.25)
                print(points[p], "points goes to", winners[p])
        input("")
    print("The Jury has given their votes!\n\n Now it's time to see what viewers has voted:")
    input("")
    for i in range(100):
        random.shuffle(participants)
    the_televote.append("Rest of the world")

    for y in range(len(the_televote)):
        odds = [63+random.randrange(-61, 32), 
                42+random.randrange(-40, 21), 
                19+random.randrange(-17, 10), 
                10+random.randrange(-8, 5), 
                8+random.randrange(-6, 4), 
                7+random.randrange(-5, 4), 
                6+random.randrange(-4, 3), 
                5+random.randrange(-3, 3), 
                4+random.randrange(-2, 2), 
                3+random.randrange(-1, 2), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                2+random.randrange(0, 1), 
                1+random.randrange(0, 1)]
        points = [1, 2, 3, 4, 5, 6, 7, 8, 10, 12]
        odds_by_participant = [[participant, odds[index]] for index, participant in enumerate(participants)]
        winners = []
        value = 0 
        televote_currently_voting = the_televote[y]
        if televote_currently_voting == "Rest of the world":
            for i in range(100):
                random.shuffle(participants)
        if "Armenia" in participants and "Azerbaijan" == televote_currently_voting:
            for w in range(len(participants)):
                if "Armenia" in odds_by_participant[w][0] and len(participants) > 11:
                    odds_by_participant[w][0] = televote_currently_voting
                    break
        elif "Azerbaijan" in participants and "Armenia" == televote_currently_voting:
            for w in range(len(participants)):
                if "Azerbaijan" in odds_by_participant[w][0] and len(participants) > 11:
                    odds_by_participant[w][0] = televote_currently_voting
                    break
        
        for x in range(len(odds_by_participant)):
            odds_by_participant[x].append(value)
            value += odds_by_participant[x][1]
            odds_by_participant[x].append(value)
        

        stopper = len(odds_by_participant) - 1
        if televote_currently_voting == "Rest of the world" and len(odds_by_participant) < 11:
            stopper = len(odds_by_participant)
        elif len(odds_by_participant) >= 11:
            stopper = 11 - 1
        while len(winners) < stopper:
            casting_vote = random.randrange(0, value)
            for x in range(len(odds_by_participant)):
                if casting_vote > odds_by_participant[x][2] and casting_vote < odds_by_participant[x][3] and odds_by_participant[x][0] not in winners and odds_by_participant[x][0] not in televote_currently_voting:
                    winners.append(odds_by_participant[x][0])
        

        winners.reverse()
        print("Now calling", televote_currently_voting + "!\n")
        for p in range(len(winners)):
            if p == 0:
                time.sleep(0.25)
                print(points[p], "point goes to", winners[p])
            elif p == 9:
                input("")
                print(televote_currently_voting, "gives", points[p], "points to", winners[p] + "!")
            else:
                time.sleep(0.25)
                print(points[p], "points goes to", winners[p])
        input("")
    print("You did it! Now add your scores to scorewiz.com and make your scoreboard :)")

brain()


    


    










    
    