# Welp, I just threw everything I learned in this section out of the window for this problem.
# As well as completely ignoring the problem by using a dictionary for the months instead of a list.
# Hint to my future self the next time I do this problem: You can use try and except statemnets. The main errors that go into
# the except statement are ValueError and KeyError. You use if statements as well. Finally, you can split something twice with
# different separaters by splitting what was already split before.

months_list = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"

def main():
    while True:
        date = input("Date: ")

        if "," in date:
            date = date.split(" ")
            day = date[1].strip(",")
            month = date[0]
            year = date[2]
            if 1 <= int(day) <= 31 and month in months_list and 1 <= int(year) <= 9999:
                break
            else:
                continue
        elif "/" in date:
            date = date.split("/")
            month = date[0]
            day = date[1]
            year = date[2]
            if 1 <= int(day) <= 31 and 1 <= int(month) <= 12 and 1 <= int(year) <= 9999:
                break
            else:
                continue

    year = str(year_converter(year))
    month = str(month_converter(month))
    day = str(day_converter(day))

    print(year + "-" + month + "-" + day)

def year_converter(s):
    if 1 <= int(s) <= 9999:
        # Yeah I think instead of converting variables between int and str over and over
        # again I could've just make it stay as an int by using this f-string "print(f"{n:02}")".
        # If n is a single digit, it will be prefixed with 0. That way, it's easier to format the
        # day, month, and year values instead of using a convoluted if statement.
        if len(s) < 4:
            zeroes = 4 - len(s)
            s = "0"*zeroes + s
            return s
        else:
            return s

def month_converter(s):
    if s in months_list:
        for i in months_list:
            if i == s:
                return months_list[i]
    else:
        if len(s) == 1:
            s = "0" + s
            return s
        else:
            return s

def day_converter(s):
    if 1 <= int(s) <= 9:
        s = "0" + str(s)
        return s
    else:
        return s

main()
