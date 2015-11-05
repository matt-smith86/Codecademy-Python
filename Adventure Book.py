def mansion():
    print "You've just entered the mansion!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Abuse Room, prepare to be tortured!"
    elif answer == "right" or answer == "r":
        print "Of course this is the exit, you escaped!"
    else:
        print "You didn't pick left or right! Try again."
        mansion()

mansion()
