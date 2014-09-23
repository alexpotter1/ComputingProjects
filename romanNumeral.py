__author__ = '09-Potter-A'

RomanNumerals = (('M', 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1))

def intRoman(i):
    if i >= 1 and i < 4000:
        output = ""
        for numeral, number in RomanNumerals: # iterate through the tuple pairs in list
            while i >= number: # whilst input number is greater than the numbers stored in the tuple
                output += numeral # the numeral is stored in the output
                i -= number # finds remainder by subtracting input by tuple numbers
        return "The Roman Numeral is %s" % output
    else:
        return "Number is too large or is negative! :("








print(intRoman(int(input("Please input your integer between 1 and 3999: "))))





