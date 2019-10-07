#Nana Aba Turkson
#hw3.py
#29/09/2019 to 7/10/2019


#Part 1:Note to frequency
def noteToFreq(note):
    '''this function convert note to frequency by calling the createMiniOctaves function to converts
    specific octaves to corresponding frequency'''
    a4 = 440 #frequency of A (common value is 440Hz)
    letter = note[0]
    octave = int(note[1])

    if letter == 'A':
        return createMiniOctaves(octave)
    elif letter == 'B':
        return createMiniOctaves(octave) * (2 ** (2/12))
    elif letter == 'G':
        return createMiniOctaves(octave) * (2 ** (-2/12))
    elif letter == 'F':
        return createMiniOctaves(octave) * (2 ** (-4/12))
    elif letter == 'E':
        return createMiniOctaves(octave) * (2 ** (-5/12))
    elif letter == 'D':
        return createMiniOctaves(octave) * (2 ** (-7/12))
    else:
        return createMiniOctaves(octave) * (2 ** (-9/12))


def createMiniOctaves(octave):
    '''this function takes octave as an argument and returns its corresponding frequency'''
    a4 = 440 #frequency of A (coomon value is 440Hz)
    if octave == 8:
        return a4 * (2**4)
    elif octave == 7:
        return a4 * (2**3)
    elif octave == 6:
        return a4 * (2**2)
    elif octave == 5:
        return a4 * 2
    elif octave == 4:
        return a4
    elif octave == 3:
        return a4 / 2
    elif octave == 2:
        return a4 *  (2** (-2))
    elif octave == 1:
        return a4 *  (2**(-3))
    else:
        return a4 * (2**(-4))



#Part 2:Calendering
def isLeapYear(year):
    '''this function takes a year as its only argument and returns True is the year is
    a leap and False if it is not'''

    if year % 4 == 0: #divisible by 4? if yes it should return a remainder of 0
        if year % 100 == 0:#a year is a leapYear if and only if when divisible by 100, it would also be divisible by 400
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def numberOfDays(year, month):
    ''' this function takes two argument and returns the number of days in the specified month'''
    if month == 4 or month == 6 or month == 9 or month ==11:#these months only have 30 days
        return 30
    elif month == 2:#this is to return the number of days in february based on whether is it a leapYear or not
        if(isLeapYear(year) == True):
            return 29
        else:
            return 28
    else:
        return 31


def nextDay(year, month, day):
    '''this function takes 3 arguments and returns 3 values representing the next day
    after the specified year, month and day.'''

    #if the days are more than the required days in a month and also the month number
    #is more than the 12, it should return 0 indicating an error
    if(day > numberOfDays(year, month) or month > 12):
        return 0

    if(day == numberOfDays(year, month)):
        if(month == 12):
            print('1')
            return year + 1, 1, 1
        else:
            print('2')
            return year, month + 1, 1
    else:
        print('3')
        return year, month, day + 1



#Part 3: Baby Sitting
def babySitting(startinghour, startingmin, endinghour, endingmin):
    '''this function takes 3 argument and returns the total amount of money earned according to your pay schedule'''

    #computations to calculate the number of hours
    end_total_num_of_hours = endinghour + (endingmin / 60)
    start_total_num_of_hours = startinghour + (startingmin / 60)


    if(end_total_num_of_hours < 19.75):
        #calculating money earned before 7:45
        difference = end_total_num_of_hours - start_total_num_of_hour
        money_earned = (difference * 12)
        return money_earned

    elif (end_total_num_of_hours >= 19.75 and end_total_num_of_hours < 22.50 ):
        #calculating money earned after or 7:45 and before 10:30
        if(start_total_num_of_hours >= 19.75):
            #calculating money earned when the starting time is after or 7:45
            difference = end_total_num_of_hours - start_total_num_of_hours
            money_earned = (difference * 6)
            return money_earned

        else:
            #calculating money earned when the starting time is before 7:45
            standard_hours = 45/60 + 19
            first_half_hours = standard_hours - start_total_num_of_hours
            first_earned_money = first_half_hours * 12
            second_half_hours = end_total_num_of_hours - standard_hours
            second_earned_money = second_half_hours * 6
            money_earned = first_earned_money + second_earned_money
            return money_earned
    else:
        #calculating money earned before midnight
        if(end_total_num_of_hours > 24.0): #return 0 if the end time is more than midnight
            return 0

        #calculating money earned when the starting time is after or 10:30
        if(start_total_num_of_hours >= 22.50):
            difference = end_total_num_of_hours - start_total_num_of_hours
            money_earned = (difference * 17)
            return money_earned

        #calculating money earned when the starting time is after or 7:45 and before 10:30
        elif(start_total_num_of_hours >= 19.75 and start_total_num_of_hours < 22.50):
            standard_hours = 30/60 + 22
            first_half_hours = standard_hours - start_total_num_of_hours
            first_earned_money = first_half_hours * 6
            second_half_hours = end_total_num_of_hours - standard_hours
            second_earned_money = second_half_hours * 17
            money_earned = first_earned_money + second_earned_money
            return money_earned

        #calculating money earned when the starting time is before 7:45
        else:
            first_standard_hours = 45/60 + 19
            second_standard_hours = 30/60 + 2
            first_half_hours = first_standard_hours - start_total_num_of_hours
            first_earned_money = first_half_hours * 12
            second_half_hours = second_standard_hours - first_standard_hours
            second_earned_money = second_half_hours * 6
            third_half_hours = end_total_num_of_hours - second_standard_hours
            third_earned_money = third_half_hours * 17
            money_earned = first_earned_money + second_earned_money + third_earned_money
            return money_earned
