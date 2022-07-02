let Length = game.askForNumber("Input an value for the length")
let Breath = game.askForNumber("Input an value for the breath")
let Perimeter = 2 * (Length + Breath)
let Area = Length * Breath
game.splash("The area of the shape is " + Area + ", and the perimeter is " + Perimeter)
