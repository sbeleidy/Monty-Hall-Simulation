import random

def runOnce():
    doors = [1,2,3]
    successDoor = doors[random.randint(0,2)]
    
    # The failing doors are the ones that are in the list after removing
    # the success state door
    doors.remove(successDoor)
    failDoors = doors

    # Choose a door to show
    shownDoor = failDoors[random.randint(0,1)]

    # Remaining doors are the other fail door and the success door
    failDoors.remove(shownDoor)
    remainingDoors = [failDoors[0],successDoor]

    chosenDoor = remainingDoors[random.randint(0,1)]
    

    # Record data depending on what was initially chosen
    if chosenDoor == successDoor:
        chosenSuccess = 1
        chosenFail = 0
    else:
        chosenSuccess = 0
        chosenFail = 1

    # Return all data that may be needed for later analysis
    return [chosenSuccess, chosenFail, chosenDoor, successDoor, shownDoor]


def run(n,printResults):
    counter = 0
    chosenSuccessTotal = 0
    chosenFailTotal = 0

    #Count the times each door is chosen, success, shown
    chosenCount = [0,0,0]
    successCount = [0,0,0]
    shownCount = [0,0,0]

    #Run n times
    while counter < n:
        data = runOnce()

        chosenSuccessTotal += data[0]
        chosenFailTotal += data[1]

        chosenCount[data[2]-1]+=1
        successCount[data[3]-1]+=1
        shownCount[data[4]-1]+=1
        

        if printResults:
            print "Chose:",data[2]
            print "Showed:",data[4]
            print "Success:",data[3]

            if data[0]>data[1]:
                print "Chosen was correct"
            else:
                print "Switch was correct"
            
        counter +=1

    print "Chosen success:",chosenSuccessTotal
    print "Chosen fail:", chosenFailTotal
    print "Door 1 was chosen", chosenCount[0],"times, successful",successCount[0],"times and shown", shownCount[0],"times."
    print "Door 2 was chosen", chosenCount[1],"times, successful",successCount[1],"times and shown", shownCount[1],"times."
    print "Door 3 was chosen", chosenCount[2],"times, successful",successCount[2],"times and shown", shownCount[2],"times."

run(10000000,False)
