Length = game.ask_for_number("Input an value for the length")
Breath = game.ask_for_number("Input an value for the breath")
Perimeter = 2 * (Length + Breath)
Area = Length * Breath
game.splash("The area of the rectangle is " + str(Area) + ", and the perimeter is " + str(Perimeter))