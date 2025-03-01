# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year=int(input("Greetings! What is your year of origin? ")) # RR: removing the extra '='
# and changing the quote and correcting the parenthesis

if year <= 1900: # RR: adding ':'
    print ("Woah, that's the past!") # RR: changing the quotes
elif year > 1900 and year < 2020: # RR: '&&' to 'and'
    print ("That's totally the present!")
else: # RR: changing elif to else
    print ("Far out, that's the future!!")
