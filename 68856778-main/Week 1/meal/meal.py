def main():
    time = input("What time is it?: ").strip()
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        quit()

def convert(time):
    if time.endswith("a.m."): #time = "10:00 a.m."
        time = time.split(' a.m.') #time = ['10:00', ' ']
        time = time[0].split(':') #time = ['10', '00']

        #Explanation of [0]:
        #When the Time Ends with "a.m." or "p.m.":
        #The split method is used to separate the time string at the " a.m." or " p.m." part.
        #For example, if time is "10:30 a.m.", after time.split(' a.m.'), you get a list ['10:30', ''].
        #The [0] is used to select the first element of the list, which is '10:30'.
        #The code then splits '10:30' at the colon ':', resulting in ['10', '30'].

        #When the Time Does Not End with "a.m." or "p.m.":
        #The else block handles times that don't end with "a.m." or "p.m.".
        #Here, the code directly splits the time string at the colon ':'.
        #For example, if time is '14:45', splitting it at the colon results in ['14', '45'].

        #TLDR: It's a split within a split so you need to specify which part of the splitted parts you want to split

        return round(int(time[0]) + int(time[1])/60)

        #Not all of the numbers can be divided and will end up going on infinitely after the decimal point
        #So you need to make an ending point
        #In this case, the division ends after it calculates the 2nd number after the decimal point
        #I think you need to do this because that way it would cause less confusion in the future

    elif time.endswith("p.m."):
        time = time.split('p.m.')
        time = time[0].split(':')
        return round(12 + int(time[0]) + int(time[1])/60, 2)
    else:
        time = time.split(':')
        return round(int(time[0]) + int(time[1])/60, 2)

if __name__ == "__main__":
    main()
