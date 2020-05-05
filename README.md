# Battle-Py!
*Battle-Py! is a rendition of the classic *Battleship* board game, created with Python 3.
* Copywright and intellectual property of *Battleship* belongs to Milton Bradley, Inc. 
<img src="https://images-na.ssl-images-amazon.com/images/I/91bDu7cDe4L._AC_SL1500_.jpg" width="200" align="right"><br>
# Rules of Battle-Py
## Game Objective
The object of Battle-Py is to try and sink all of the bot's ships before the bot sinks all of your ships. All of the other bot's ships are somewhere on his/her board.  You try and hit them by inputting the coordinates of one of the squares on the board.  The bot player then tries to hit your ships by providing coordinates.  Neither you nor the bot can see the other's board so you must try to guess where they are.  Each board in the physical game has two grids:  the lower (horizontal) section for the player's ships and the upper part (vertical during play) for recording the player's guesses.

## Starting a New Game
To begin the game, navigate to the src folder and enter this command<br>
```
CS224\src> python game.py
```
To begin the game in testing mode, which places the player's ships for you and shows the computer's ship placements, type this command into the same directory<br>
```
CS224\src> python game.py test
```
Each player places the 5 ships somewhere on their board.  The ships can only be placed vertically or horizontally. Diagonal placement is not allowed. No part of a ship may hang off the edge of the board.  Ships may not overlap each other.  No ships may be placed on another ship. <br>

Once the guessing begins, the players may not move the ships.<br>

The 5 ships are:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).  

## Playing the Game
Player's take turns inputting coordinates. The opponent responds with "hit" or "miss" as appropriate.  Both players should mark their board with pegs:  red for hit, white for miss (this is done automatically within the program). For example, if you call out F6 and your opponent does not have any ship located at F6, your opponent would respond with "miss".  You record the miss F6 by placing a white peg on the lower part of your board at F6.  The bot then records the miss.<br>

When all of the squares that one your ships occupies have been hit, the ship will be sunk. In the physical game, a red peg is placed on the top edge of the vertical board to indicate a sunk ship. <br>

As soon as all of either the player or the bot's ships have been sunk, the game ends.

# Program Structure
***

To run the program, the user must first install *termcolor*. This can be done using the following command in the project's src folder:
```
CS224\src> pip install termcolor
```

## game.py - Game driver, responsible for implementing core functionality.
### Dependencies: player.py, bot.py

class Game
| Method        | Parameters  |  Function  |
| :------------- |:-------------| :-----|
| __play_game__      | *self*<br> player : player instance<br> bot : bot instance that will compete against player | Runs the game by creating boards for player and bot, requests guesses from the player and outputs a version of the board afterwards. |
| __main__  | *self* | Requests player name, runs *play_game()* |

## bot.py - Creates the automated player which competes with the user.<br>
### Dependencies: termcolor.colored

class Bot
| Method        | Parameters  |  Function  |
| :------------- |:-------------| :-----|
| __init__      | *self* | Creates a clean board for the bot which plays against the player |
| __print_board__  | *self* |   Prints the opponent's board |
| __get_hidden_board__ | *self* | Provides the user with a view of the opponent's board |
| __update_clean_board__ | *self*<br>x : x-coord<br>y : y-coord | Update opponent's board with new coordinate inputs |


## player.py - Creates a player object. Contains methods for retrieving and evaluating guesses.<br>
### Dependencies: termcolor.colored, ship.py

class Player
| Method        | Parameters  |  Function  |
| :------------- |:-------------| :-----|
| __init__      | *self*<br>name : player name (taken via user input) | Initializes a new Player object, creates a blank board |
| __get_board__  | *self* |  Returns the player's board |
| __print_board__ | *self* | Print method that provides a printed board in the console |
| __make_guess__ | *self*<br>x : x-coord<br>y : y-coord<br>opponent : opponent location | Updates the board based on player input, checks opponent position to determine if it was a hit/miss |
| __create_board__ | *self* | Creates newly updated board following guess, checks for valid inputs |


## ship.py - Creates a ship object with associated rules and characteristics. <br>
### No dependencies, independent class

class Ship
| Method        | Parameters  |  Function  |
| :------------- |:-------------| :-----|
| __init__      | *self*<br>x : x-coord<br>y : y-coord<br> orientation : which direction the ship is facing<br>length : the length of the ship<br>board : board object to reference when placing the ship | Initializes the ship object |
| __set_cells__  | *self*<br>x : x-coord<br>y : y-coord<br> orientation : which direction the ship is facing<br>length : the length of the ship<br>board : board object to reference when placing the ship  | Sets the location and positioning of a ship |
| __is_ship_sunk__ | *self* | Returns boolean for whether or not a ship is sunk |
| __hit__ | *self*<br>x : x-coord<br>y : y-coord | If ship is hit, it's cells will be removed from the cell grid. Else, do nothing. |

class Cell, subclass of Ship<br>
Cell object, used to create a grid for ships to be placed on.

| Method        | Parameters  |  Function  |
| :------------- |:-------------| :-----|
| __init__ | *self*<br>x : x-coordinate<br>y : y-coordinate | Initialize the Cell object
| __str__ | *self* | Returns a string representation of the Cell object. |



## Acknowledgements
Created for Spring CS 224, Mathias<br>
**Authors:** Max Ahola, Douglas Krouth, Alyssa Oswald, Maxx Persin<br>
**Rules for Battleship** sourced from https://www.cs.nmsu.edu/~bdu/TA/487/brules.htm
