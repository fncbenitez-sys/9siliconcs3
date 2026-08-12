zodiacSigns = [
"Rat (鼠 / Shǔ)",
"Ox (牛 / Niú)",
"Tiger (虎 / Hǔ)",
"Rabbit (兔 / Tù)",
"Dragon (龙 / Lóng)",
"Snake (蛇 / Shé)",
"Horse (马 / Mǎ)",
"Goat (羊 / Yáng)",
"Monkey (猴 / Hóu)",
"Rooster (鸡 / Jī)",
"Dog (狗 / Gǒu)",
"Pig (猪 / Zhū)",
] # zodiac sign array makes things easier

birthYear = int(input("Enter your birth year: ")) # asks for user's birth year
 
if birthYear > 1899: #makes sure that the birth year is on or after 1900
    index = (birthYear-1900)%12 #I chose to subtract 1900 because it gives a smaller number to use %
    print(f'Your Chinese Zodiac Sign is: {zodiacSigns[index]}') # gets the remainder and assigns it as the index
else:
    print("We only take birth years after 1899...") # eeror message
