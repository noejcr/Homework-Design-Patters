def count_to(count):
    """Our iterator implementation"""

    #our list
    numbers_in_german = ["cins", "zwei", "drei", "vier", "funf"]

    #our built-in iterator
    #Creates a tuple such as (1, "eins")
    iterator = zip(range(count), numbers_in_german)

    #Iterate trough our iterable list
    #Extract the German numbers
    #Put them in a generator called number
    for position, number in iterator:

        #Returns a 'generator' containing numbers in German
        yield number


#Let's that the generator returned by our iterator
for num in count_to(3):
    print("{}".format(num))

for num in count_to(4):
    print("{}".format(num))
