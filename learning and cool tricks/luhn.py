# Learn how to work with numbers and strings by implementing the Luhn algorithm
    
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1] # [ 1st character : last character : step ]
    odd_digits = card_number_reversed[::2] # [ default : default : show every other ]
    for i in odd_digits:
        sum_of_odd_digits += int(i)
    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2] # [ int location 1 : default : every other ]
    for i in even_digits:
        number = int(i)*2 # times every even digit by 2
        if number >= 10:
            number = (number // 10)+(number%10) # adds(number - last digit & last digit of number {123 = 12+3 = 15})
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits    
    return 0 == total%10 # check if the total is a multiple of 10

def main():
    card_number = "4111-1111-4555-1142"
    card_translation = str.maketrans({'-':'',' ':''}) # removes any dashes or spaces from the number (useful) into a translation table
    translated_card_number = card_number.translate(card_translation) # turns the translation table into a string
    if verify_card_number(translated_card_number):
        print("VALID!") 
    else: 
        print("INVALID!")


main()