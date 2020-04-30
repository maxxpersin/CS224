# Battle-Py!
*Battle-Py! is a rendition of the classic *Battleship* board game, created with Python 3.
* Copywright and intellectual property of *Battleship* belongs to Milton Bradley, Inc. 
<img src="https://images-na.ssl-images-amazon.com/images/I/91bDu7cDe4L._AC_SL1500_.jpg" width="200" align="right"><br>
# Program Structure
***

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
**Authors:** Max Ahola, Douglas Krouth, Alyssa Oswald, Maxx Persin
