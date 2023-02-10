import random
from tabulate import tabulate as tb

class Squares:
    """
    This is the Squares class! Use it to create your Super Bowl squares. 
    
    Unless otherwise specified, the number of rows and columns are each set to ten, creating a 10x10 grid. 
    
    It is optional to set the minimum or maximum number of squares a player can purchase. 

    By default, the team associated with the rows in the grid is the AFC. The team associated with the columns is the NFC. These values can be overwritten. 
 
    The adjustable cost per square is $5.00.
    
    The payout percentage are set to be 15% for quarters 1 and 3, 30% for quarter 2 (halftime), and 40% of the pot for quarter 4 (the final score). These values can be updated as well.
    """

    def __init__(
        self,
        n_rows=10,
        n_cols=10,
        min_squares=None,
        max_squares=None,
        team_a="AFC",
        team_b="NFC",
        cost_per_square=5,
        q1=15,
        q2=30,
        q3=15,
        q4=40,
    ):

        self.n_rows = n_rows
        self.n_cols = n_cols
        self.min_squares = min_squares
        self.max_squares = max_squares
        self.team_a = team_a
        self.team_b = team_b
        self.cost_per_square = cost_per_square
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4

        self.squares_pool = {(i, j): None for i in range(n_rows) for j in range(n_cols)}
        self.squares_dict = {}
        self.player_dict = {}

        self.total_pot = self.cost_per_square * (self.n_rows * self.n_cols)

        # check that manually entered quarter percentages add up to 100% exactly
        if (q1 + q2 + q3 + q4) != 100:
            raise ValueError("Error: Quarter payouts must add up to 100%.")

    def square_stats(self):
        """
        The square_stats() function prints information about a created Squares instance.
        This information incluces the number of rows and columns. The default number of rows and columns is 10.
        There is no default value for the minimum or maximum number of squares per player.
        Unless otherwise specified, the team associated with the number of rows is the AFC and the NFC team aligns with the columns.
        The default cost per square is $5.00 and the payouts are 15% for Q1 and Q3, 30% for Q2, and 40% for Q4.
        """
        print(f"Number of rows: {self.n_rows}")
        print(f"Number of columns: {self.n_cols}")
        print(f"Minimum number of squares: {self.min_squares}")
        print(f"Maximum number of squares: {self.max_squares}")
        print(f"Team A: {self.team_a}")
        print(f"Team B: {self.team_b}")
        print(f"Cost per square: ${self.cost_per_square}")
        print(f"Total pot: ${self.total_pot}")
        print(f"\tQ1 payout: {self.q1}%, ${self.total_pot *(self.q1/100)}")
        print(f"\tHalftime payout: {self.q2}%, ${self.total_pot *(self.q2/100)}")
        print(f"\tQ3 payout: {self.q3}%, ${self.total_pot *(self.q3/100)}")
        print(f"\tFinal Score payout: {self.q4}%, ${self.total_pot *(self.q4/100)}")
        print(f"Total squares: {len(self.squares_pool)}")

    def add_player(self, name: str, n_squares: int):
        """
        To add a player to the Squares instance, use the add_player() function.
        This function takes a player name as a string and the number of squares as an integer. 
        Only unique names will be accepted. 
        If there are minimum or maximum square requirements, they must be met.
        There must be enough available squares for a player to be added.
        """

        # check that the player name is unique
        if name in self.player_dict:
            print(
                f"Error: {name} has already been added to the pool. Please enter a unique player name."
            )
            return

        # check that the player meets the optional minimum squares criteria
        elif self.min_squares != None and n_squares < self.min_squares:
            print(
                f"Error: {name} has not met the minimum number of squares for this pool. The minimum number of squares per player is {self.min_squares}"
            )
            return

        # check that the player meets the optional maximum squares criteria
        elif self.max_squares != None and n_squares > self.max_squares:
            print(
                f"Error: {name} has exceeded the maximum number of squares for this pool. The maximum number of squares per player is {self.max_squares}"
            )
            return

        # check that there are enough available squares for the player to join the pool
        elif (sum(self.player_dict.values()) + n_squares) > (self.n_rows * self.n_cols):
            print(
                f"Error: Not enough available squares. {name} asked for {n_squares} squares but there are {(self.n_rows * self.n_cols) - sum(self.player_dict.values())} remaining squares."
            )
            return

        # add the player to the pool with their desired number of squares
        else:
            player_squares = []
            self.player_dict[name] = n_squares
            print(f"{name} added to the pool with {n_squares} squares")

    def assign_squares(self, assign_empty_squares=True):
        """
        Use assign_squares() to give each player randomized squares corresponding to the number they purchased.
        """
        # for each player, assign them the number of random squares that they purchased
        for player, n_squares in self.player_dict.items():

            for i in range(n_squares):
                square = random.choice(list(self.squares_pool.keys()))
                self.squares_pool.pop(square)
                self.squares_dict[square] = player

    def assign_empty_squares(self):
        """
        The assign_empty_squares() function can be used to randomly assign any blank squares to players already in the pool. 
        """

        player_list = list(self.player_dict.keys())

        for i in range(len(self.squares_pool.keys())):
            if len(player_list) == 0:
                player_list = list(self.player_dict.keys())
            else:
                player = random.choice(player_list)
                player_list.remove(player)

            square = random.choice(list(self.squares_pool.keys()))

            self.squares_pool.pop(square)
            self.squares_dict[square] = player

    def print_squares(self):
        """
        Use the print_squares() function to generate a tabulated format of the squares and save the grid as a .csv file called "squares.csv". 
        """

        # create an empty grid using the number of rows and columns (optionally) specified
        output = [[(None) for _ in range(self.n_rows)] for _ in range(self.n_cols)]

        # order the squares dictionary
        for key, value in sorted(self.squares_dict.items()):
            i = key[0]
            j = key[1]
            output[i][j] = value

        # append the team name to the index
        rowIDs = [f"{i}\n{self.team_a}" for i in range(self.n_rows)]

        # create a table from the assigned squares
        table = tb(
            output,
            headers=[f"{i}\n{self.team_b}" for i in range(self.n_cols)],
            showindex=rowIDs,
            tablefmt="simple",
        )

        text_file = open("squares.csv", "w")
        text_file.write(table)
        text_file.close()

        print(table)

    def get_player_squares(self, name):
        """
        Each player has squares associated with their name. 
        To get the squares assigned to a specific player, user the get_player_squares() function, which takes the player name string (already entered in the pool) as input.
        """

        if name not in self.player_dict:
            print(
                f"Error: Please enter a user who already has squares. {name} does not have any squares."
            )
            return
        else:
            # enter user name, get their squares
            squares_list = []

            for key, value in self.squares_dict.items():
                if value == name:
                    squares_list.append(key)

            print(f"{name} has the following squares: {squares_list}")

    def payout(self, team_a_score: int, team_b_score: int, quarter: int):
        """
        To determine the payout at the end of each quarter, run the payout() function. 
        Enter the score of the AFC team, the score of the NFC team, and the quarter of the game to get the winning player and the amount of money they have won.  
        """

        # enter the score and the quarter to get the winner and payout
        team_a_digit = int(repr(team_a_score)[-1])
        team_b_digit = int(repr(team_b_score)[-1])

        winner = self.squares_dict.get((team_a_digit, team_b_digit))

        # calculate payout depending on the quarter

        if quarter == 1:
            payout = self.total_pot * (self.q1 / 100)
        if quarter == 2:
            payout = self.total_pot * (self.q2 / 100)
        if quarter == 3:
            payout = self.total_pot * (self.q3 / 100)
        if quarter == 4:
            payout = self.total_pot * (self.q4 / 100)

        print(
            f"The Q{quarter} winner is {winner} with the ({team_a_digit}, {team_b_digit}) square. They win ${payout}!"
        )