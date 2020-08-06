number = input("Type Numbers That You want to convert into Roman Numerals : ")

RomanNumerals = {
    "1" : "I",
    "2" : "II",
    "3" : "III",
    "4" : "IV",
    "5" : "V",
    "6" : "VI" ,
    "7" : "VII",
    "8" : "VIII",
    "9" : "IX",
    "10" : "X",
    "0"  : "*(There is no ZERO in ROMAN NUMERALS)*"

}

output_Roman_Numerals = " "
for i in number :
    output_Roman_Numerals += RomanNumerals.get( i , " ") + " "

print(output_Roman_Numerals)