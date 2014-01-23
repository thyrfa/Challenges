#!/bin/python
# Head ends here
import random
def calculate_bid(player,pos,first_moves,second_moves):
    player1=100
    player2=100
    tie=True
    for i in range(len(first_moves)):
        if (first_moves[i]>second_moves[i]):
            player1-=first_moves[i]
        elif (first_moves[i]==second_moves[i]):
            if (tie):
                player1-=first_moves[i]
                tie=(not tie)
            else:
                player2-=second_moves[i]
                tie=(not tie)
        else:
            player2-=second_moves[i]
    if (player==1):
        ours=player1
        theirs=player2
        onetowin=9
        wewin=1
    else:
        theirs=player1
        ours=player2
        tie=(not tie)
        onetowin=1
        wewin=9
    if (ours==0):
        return 0
    state1=False
    state2=False
    state3=False
    state4=False
    if ((ours>=theirs) and tie):
        state1=True
    elif ((ours>=theirs) and (not tie)):
        state2=True
    elif (ours>theirs):
        state3=True
    elif (ours<theirs):
        state4=True
    if (pos==onetowin and state1):
        return theirs
    elif (pos==onetowin and state2):
        return theirs+1
    elif (pos==wewin):
        return ours
    wewindistance=abs(wewin-pos+1)
    theywindistance=abs(onetowin-pos+1)
    towin=int(ours/(abs(wewin-pos)+1))-1
    theywin=int(theirs/(abs(onetowin-pos)+1))-1
    if (towin<=0):
        if (ours>=1):
            return 1
        else:
            return 0
    if (towin>theirs):
        return towin
    if (pos==5):
        return (ours/5)
    if (pos==wewin and state1):
        return theirs
    elif (pos==wewin and state2):
        return theirs+1
    elif (pos==wewin):
        return ours
    return towin
# Tail starts here
#gets the id of the player
player = input()

scotch_pos = input()         #current position of the scotch

first_moves = [int(i) for i in raw_input().split()]
second_moves = [int(i) for i in raw_input().split()]
bid = calculate_bid(player,scotch_pos,first_moves,second_moves)
print bid