# Super Squares

Super Squares is a tool that allows anyone to generate and randomly assign Super Bowl squares.

## Prerequisites 

Before you begin, ensure you have met the following requirements:

- You have read the documentation

## Installing Super Squares

To install Super Squares, follow these steps on all OS devices:

1. Install using the following command: `pip install supersquares`
2. Import the package with: `from supersquares import squares`

## Functions Overview 

### Square Stats 

The `square_stats()` function prints information about a created Squares instance. This information incluces the number of rows and columns. The default number of rows and columns is 10. There is no default value for the minimum or maximum number of squares per player. Unless otherwise specified, the team associated with the number of rows is the AFC and the NFC team aligns with the columns. The default cost per square is $5.00 and the payouts are 15% for Q1 and Q3, 30% for Q2, and 40% for Q4.

The square_stats() function does not take any input. 

### Add Player

To add a player to the Squares instance, use the `add_player()` function. This function takes a player name as a string and the number of squares as an integer. Only unique names will be accepted. If there are minimum or maximum square requirements, they must be met. There must be enough available squares for a player to be added.

### Assign Squares

Use `assign_squares()` to give each player randomized squares corresponding to the number they purchased. This function does not take any input. 

### Assign Empty Squares

The `assign_empty_squares()` function can be used to randomly assign any blank squares to players already in the pool and does not take any variables as input. 

### Get Player Squares

Use the `print_squares()` function to generate a tabulated format of the squares and save the grid as a .csv file called "squares.csv". No input is needed to print the squares.

### Payout 

Each player has squares associated with their name. To get the squares assigned to a specific player, user the `get_player_squares()` function, which takes the player name string as input.

## Usage Example

1. Create a Squares() instance with the desired parameters and store it in a variable.
	Input: 
	```
	squares_example = Squares(cost_per_square = 10, 
							team_a = "Pawnee", 
							team_b = "Eagleton",
							min_squares = 1,
							q1 = 10, 
							q3 = 10, 
							q4 = 50)
	```
2. View the specifications of the grid 
	Input: 
	```
	squares_example.square_stats()
	```
	Output: 
	```
	Number of rows: 10
	Number of columns: 10
	Minimum number of squares: 1
	Maximum number of squares: None
	Team A: Pawnee
	Team B: Eagleton
	Cost per square: $10
	Total pot: $1000
		Q1 payout: 10%, $100.0
		Halftime payout: 30%, $300.0
		Q3 payout: 10%, $100.0
		Final Score payout: 50%, $500.0
	Total squares: 100
	```
3. Add new users to the pool. Note: the entered number of squares must be available in the pool. Players must have unique names. 
	Input: 
	```
	squares_example.add_player("Leslie", 10)
	squares_example.add_player("Ben", 15)
	squares_example.add_player("Ron", 10)
	squares_example.add_player("Ann", 10)
	squares_example.add_player("Donna", 15)
	squares_example.add_player("April", 5)
	squares_example.add_player("Tom", 10)
	squares_example.add_player("Chris", 10)
	squares_example.add_player("Andy", 10)
	squares_example.add_player("Jerry", 5)
	```
4. Assign squares to all of the players at once 
	Input: 
	```
	squares_example.assign_squares()
	```
5. Check the squares assigned to a specific user 
	Input: 
	```
	squares_example.get_player_squares("Leslie")
	```
	Output: 
	```
	Leslie has the following squares: [(4, 9), (2, 8), (3, 9), (7, 6), (2, 6), (6, 8), (2, 2), (8, 2), (5, 3), (6, 6)]
	```
6. Print the grid
	Input:
	```
	squares_example.print_squares()
	```
	Output: 
	```
			0           1           2           3           4           5           6           7           8           9
			Eagleton    Eagleton    Eagleton    Eagleton    Eagleton    Eagleton    Eagleton    Eagleton    Eagleton    Eagleton
	------  ----------  ----------  ----------  ----------  ----------  ----------  ----------  ----------  ----------  ----------
	0       Ben         Ann         Donna       Chris       Andy        Chris       Ron         Ben         Chris       Donna
	Pawnee
	1       Ron         Tom         Tom         Chris       Ann         April       Ann         Andy        Ben         Ann
	Pawnee
	2       Ben         Chris       Leslie      Donna       Ron         Donna       Leslie      Ron         Leslie      April
	Pawnee
	3       Chris       Ann         Chris       Chris       Ben         Tom         Donna       Andy        Andy        Leslie
	Pawnee
	4       April       Andy        Donna       Ron         Donna       Jerry       Ann         Ron         Ben         Leslie
	Pawnee
	5       Donna       Ann         Ben         Leslie      Ben         Andy        Donna       April       Ben         Tom
	Pawnee
	6       Tom         Tom         Ben         Ben         Jerry       Tom         Leslie      Ron         Leslie      Donna
	Pawnee
	7       Chris       Donna       Ben         Ann         Ben         Andy        Leslie      Ron         Donna       Ron
	Pawnee
	8       Donna       Andy        Leslie      Tom         Jerry       April       Ron         Ann         Jerry       Ben
	Pawnee
	9       Tom         Andy        Donna       Andy        Chris       Tom         Donna       Ann         Jerry       Ben
	Pawnee
	```
7. Enter the score at the end of each quarter 
	Input:
	```
	squares_example.payout(7, 28, 1)
	```
	Output: 
	```
	The Q1 winner is Donna with the (7, 8) square. They win $100.0!
	```

## FAQ

### What variables can be modified?
- Number of rows (default = 10)
- Number of columns (default = 10)
- Minimum number of squares (default = None)
- Maximum number of squares (default = None)
- Team A Name (default = AFC)
- Team B Name (default = NFC)
- Cost per squares (default = $5.00)
- Quarter 1 payout percentage (default = 15%)
- Halftime payout percentage (default = 30%)
- Quarter 3 payout percentage (default = 15%)
- Final score payout percentage (default = 40%)

### Why can't I manually choose squares?
Accoring to [sportingnews.com](https://www.sportingnews.com/us/nfl/news/super-bowl-squares-grid-2023-best-numbers/ltur0ayv6wvsdkyjjk2cnmdo), the most frequently occuring squares are (0,0), (0, 3), (3, 0), (0, 7), (7, 0), (3, 7) and (7, 3). Squares are assigned randomly to fairly distribute squares with a greater chance of winning.

## Contact
If you want to contact me, you can reach me at slpardes@syr.edu.

## License
This project uses the following license: MIT License.
