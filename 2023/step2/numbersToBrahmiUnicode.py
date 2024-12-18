import re

input = input("Enter numbers separated by spaces: ")

def convert_to_ksatrapa_brahmi_numerals(input):
    """
    Converts Arabic numerals in input to Ksatrapa Brahmi numerals in Unicode.
    U+11052 		𑁒 	&#69714; &#x11052; 	BRAHMI NUMBER ONE
    U+11053 		𑁓 	&#69715; &#x11053; 	BRAHMI NUMBER TWO
    U+11054 		𑁔 	&#69716; &#x11054; 	BRAHMI NUMBER THREE
    U+11055 		𑁕 	&#69717; &#x11055; 	BRAHMI NUMBER FOUR
    U+11056 		𑁖 	&#69718; &#x11056; 	BRAHMI NUMBER FIVE
    U+11057 		𑁗 	&#69719; &#x11057; 	BRAHMI NUMBER SIX
    U+11058 		𑁘 	&#69720; &#x11058; 	BRAHMI NUMBER SEVEN
    U+11059 		𑁙 	&#69721; &#x11059; 	BRAHMI NUMBER EIGHT
    U+1105A 		𑁚 	&#69722; &#x1105a; 	BRAHMI NUMBER NINE
    U+1105B 		𑁛 	&#69723; &#x1105b; 	BRAHMI NUMBER TEN
    U+1105C 		𑁜 	&#69724; &#x1105c; 	BRAHMI NUMBER TWENTY
    U+1105D 		𑁝 	&#69725; &#x1105d; 	BRAHMI NUMBER THIRTY
    U+1105E 		𑁞 	&#69726; &#x1105e; 	BRAHMI NUMBER FORTY
    U+1105F 		𑁟 	&#69727; &#x1105f; 	BRAHMI NUMBER FIFTY
    U+11060 		𑁠 	&#69728; &#x11060; 	BRAHMI NUMBER SIXTY
    U+11061 		𑁡 	&#69729; &#x11061; 	BRAHMI NUMBER SEVENTY
    U+11062 		𑁢 	&#69730; &#x11062; 	BRAHMI NUMBER EIGHTY
    U+11063 		𑁣 	&#69731; &#x11063; 	BRAHMI NUMBER NINETY
    U+11064 		𑁤 	&#69732; &#x11064; 	BRAHMI NUMBER ONE HUNDRED
    """
    numerals = {'0': 'ERROR', '1': '\U00011052', '2': '\U00011053', '3': '\U00011054', '4': '\U00011055',
                '5': '\U00011056', '6': '\U00011057', '7': '\U00011058', '8': '\U00011059', '9': '\U0001105A', 
                '10': '\U0001105B', '20': '\U0001105C', '30': '\U0001105D', '40': '\U0001105E', '50': '\U0001105F',
                '60': '\U00011060', '70': '\U00011061', '80': '\U00011062', '90': '\U00011063', '100': '\U00011064'}
    # input is delimited by spaces. Keep all characters including spaces, but convert numbers to Brahmi numerals.
    # return re.sub(r'(\d+)', lambda m: numerals[m.group()], input)
    return re.sub(r'(\d+)', lambda m: numerals[m.group()], input)

def convert_to_arabic_numerals(input):
    numerals = {'\U00011052': '1', '\U00011053': '2', '\U00011054': '3', '\U00011055': '4',
                '\U00011056': '5', '\U00011057': '6', '\U00011058': '7', '\U00011059': '8', '\U0001105A': '9',
                '\U0001105B': '10', '\U0001105C': '20', '\U0001105D': '30', '\U0001105E': '40', '\U0001105F': '50',
                '\U00011060': '60', '\U00011061': '70', '\U00011062': '80', '\U00011063': '90', '\U00011064': '100'}
    # input is delimited by spaces. Keep all characters including spaces, but convert brahmi numerals to numbers.

    return re.sub(r'(\U00011052|\U00011053|\U00011054|\U00011055|\U00011056|\U00011057|\U00011058|\U00011059|\U0001105A|\U0001105B|\U0001105C|\U0001105D|\U0001105E|\U0001105F|\U00011060|\U00011061|\U00011062|\U00011063|\U00011064)', lambda m: numerals[m.group()], input)

# Save the result to a file called "output.txt"
with open("converted_brahmi.txt", "w") as f:
    f.write(convert_to_ksatrapa_brahmi_numerals(input))

with open("converted_arabic.txt", "w") as f:
    f.write(convert_to_arabic_numerals(input))