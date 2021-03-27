name = input('What is your name?: ')
kilometers = float(input('What is the distance in km?: '))
miles = round(kilometers / 1.609, 2)
print(f"Hello {name.capitalize()}! Your distance is {kilometers} km or {miles} miles!")

