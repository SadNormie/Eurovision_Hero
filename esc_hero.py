import random
import time

def finalists(): #A function for making finalists
    grand_final = []
    p = 0
    print('''Hello, and welcome to Eurovision Hero :)
    please write every participating country.
    Should you wish to delete the last country you wrote, write "delete" 
    When you are done, press 'enter' on your keyboard
    ''') #Welcome message

    '''This loop asks the user to add their countries of choice to a list
    which will be used as the participants in the "grand final" of Eurovision Hero"'''

    while True: #A while loop that lets the user add countries and press 'enter', when they're finished
        print('\n')
        add_country = input() 
        if add_country == '': 
            break

        elif add_country == 'delete': 
            print(grand_final[-1], 'was deleted from the list!')
            grand_final.pop()
            print("\nYour list:")
            for x in range(len(grand_final)):
                print(grand_final[x])
            p -= 1
            

        elif p >= 26: 
            print("Sorry, but you can't add any more countries!") 

        else:
            grand_final.append(add_country) 
            print("\nYour list:")
            for x in range(len(grand_final)):
                print(grand_final[x])
            p += 1 
    return grand_final
def jury(): #A function for making the jury and the televote
    jury_loop = True
    the_jury = []
    the_televote = []
    while jury_loop == True:
        same_as_grand_final = input()
        if same_as_grand_final == 'no':
            the_jury = participants.copy()
            jury_loop = False
        elif same_as_grand_final == 'yes':
            while True:
                print('\n')
                add_jury = input() 
                if add_jury == '':
                    jury_loop = False 
                    break
                elif add_jury == 'delete': 
                    print(the_jury[-1], 'was removed from the jury!')
                    the_jury.pop()
                    print("\nYour jury:")
                    for x in range(len(the_jury)):
                        print(the_jury[x])
                    
                else:
                    the_jury.append(add_jury) 
                    print("\nYour jury:")
                    for x in range(len(the_jury)):
                        print(the_jury[x])
        else:
            print('invalid input, try again')

    the_televote = list(the_jury)
    random.shuffle(the_jury)
    random.shuffle(the_televote)
    return the_jury, the_televote


def brain(): #The function running Eurovision_Hero
    global participants
    participants = finalists()
    print('Do you want to make your own jury?\n\nyes\nno\n')
    the_jury, the_televote = jury()
    for y in range(len(participants)):
        odds = [63, 42, 19, 10, 8, 7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
        points = [1, 2, 3, 4, 5, 6, 7, 8, 10, 12]
        odds_by_participant = [[participant, odds[index]] for index, participant in enumerate(participants)]
        winners = []
        value = 0 
        for x in range(len(odds_by_participant)):
            odds_by_participant[x].append(value)
            value += odds_by_participant[x][1]
            odds_by_participant[x].append(value)
        jury_currently_voting = the_jury[y]

        stopper = len(odds_by_participant)
        if len(odds_by_participant) >= 11:
            stopper = 11
        while len(winners) < stopper - 1:
            casting_vote = random.randrange(0, value)
            for x in range(len(odds_by_participant)):
                if casting_vote > odds_by_participant[x][2] and casting_vote < odds_by_participant[x][3] and odds_by_participant[x][0] not in winners and odds_by_participant[x][0] not in jury_currently_voting:
                    winners.append(odds_by_participant[x][0])
                

        winners.reverse()
        for p in range(len(winners)):
            if p == 0:
                time.sleep(0.25)
                print(points[p], "point goes to", winners[p])
            elif p == 9:
                input("")
                print(winners[p], "gets ", points[p], "points from ", jury_currently_voting + "!")
            else:
                time.sleep(0.25)
                print(points[p], "points goes to", winners[p])
        input("")

            
        
            

brain()


    


    










    
    