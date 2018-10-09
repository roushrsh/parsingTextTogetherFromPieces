# parsingTextTogetherFromPieces
#FibonnaciPuzzle.Re-CreatingPageFromPieces
#Was a fun challenge

#Soroush Hajizadeh

import math #Import needed tools
import sys
while 1:
    try:
        fullMixedText = sys.stdin.readline() #read line given to us.
    except KeyboardInterrupt:
        break #break if interuppted

    if not fullMixedText:
        break #break if nothing given

    listOfText = fullMixedText.split(";") #Split text into list to be processed



    def checkForOverlapCount(partA, partB):  #Checks to see if there are overlaps
        for x in range (min(len(partA), len(partB)), 1, -1):  #Start at largest possibility and go down.
            if ((partA[-x:] == partB[:x])):
                return (x) #if found from A to B, return large sum
            if ((partB[-x:] == partA[:x])):
                return (x) #have to check other ends, return length from B to A
        return False  #If no match, then return False.

    def doOverLaps(partA, partB):  #Actually does the merging
        for x in range (min(len(partA), len(partB)), 1, -1): #Same as before, except now we're confident there is an overlap, we perform and return our result
            if ((partA[-x:] == partB[:x])):
                return(partA + partB[x:])
            elif ((partB[-x:] == partA[:x])):
                return(partB+partA[x:])

    while(len(listOfText) > 0): #our loop to go through the list, and merge them until there's only one left
        heldPosition = [0,0]   #where the longest item is, as we want the BEST fit possible
        for x in range (1, len(listOfText)):   #we want our first item to be always the full text, so we check all items after against it

            positionScore = checkForOverlapCount(listOfText[0], listOfText[x])  #Check for overlap, if there is, get a score
            if (positionScore != False):   #if there IS an overlap proceed
                if (heldPosition[0] < positionScore): #Save position of overlap assuming it's larger than previously found ones
                    heldPosition[0] = positionScore
                    heldPosition[1] = x

        listOfText[0]= str(doOverLaps(listOfText[0], listOfText[(heldPosition[1])]))  #Merge our first item with the found largest overlap


        if (heldPosition[0] == 0):  #If there are no more overlaps left, then break
            break
        del listOfText[(heldPosition[1])] #remove the one we merged into the first, making the list smaller


    print listOfText[0] #print out the final large text
