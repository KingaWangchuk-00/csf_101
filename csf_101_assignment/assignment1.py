# Rock-Paper-Scissors game based on the given problem statement

def get_computer_play(opponent_play):
    """Determines the computer's play based on the opponent's play."""
    if opponent_play == 'A':
        return 'rock'
    elif opponent_play == 'B':
        return 'paper'
    else:
        return 'scissors'

def get_my_play(opponent_play, desired_outcome):
    """Determines my play based on the opponent's play and desired outcome."""
    if desired_outcome == 'Y':
        return opponent_play

    if desired_outcome == 'X':
        if opponent_play == 'A':
            return 'scissors'
        elif opponent_play == 'B':
            return 'rock'
        else:
            return 'paper'

    if desired_outcome == 'Z':
        if opponent_play == 'A':
            return 'paper'
        elif opponent_play == 'B':
            return 'scissors'
        else:
            return 'rock'

def calculate_score(my_play, opponent_play, outcome):
    """Calculates the score based on my play, opponent's play, and the outcome."""
    shape_score = 0
    if my_play == 'rock':
        shape_score = 1
    elif my_play == 'paper':
        shape_score = 2
    else:
        shape_score = 3

    if outcome == 'X':
        return shape_score

    if outcome == 'Y':
        return shape_score + 3

    return shape_score + 6

def main():
    """The main function to run the game."""
    game_data = [
        ('A', 'Y'),
        ('B', 'X'),
        ('C', 'Z'),
    ]

    total_score = 0
    for opponent_play, desired_outcome in game_data:
        my_play = get_my_play(opponent_play, desired_outcome)
        computer_play = get_computer_play(opponent_play)
        outcome = 'Y' if my_play == opponent_play else ('X' if desired_outcome == 'Z' else 'Z')
        round_score = calculate_score(my_play, opponent_play, outcome)
        print(f"Round: My play {my_play.capitalize()} vs. Computer play {computer_play.capitalize()}. "
              f"Outcome: {outcome}. Score: {round_score}.")
        total_score += round_score

    print(f"\nTotal score: {total_score}")

if __name__ == "__main__":
    main()


# Rock-Paper-Scissors game using dictionaries

def calculate_score(my_play, opponent_play, outcome):
    """Calculates the score based on my play, opponent's play, and the outcome."""
    shape_points = SHAPING_POINTS[my_play]
    outcome_points = OUTCOME_POINTS[outcome]
    return shape_points + outcome_points

def get_my_play(opponent_play, desired_outcome):
    """Determines my play based on the opponent's play and desired outcome."""
    if desired_outcome == 'Y':
        return opponent_play

    if desired_outcome == 'X':
        return LOSE_MAP[opponent_play]

    return WIN_MAP[opponent_play]

def main():
    """The main function to run the game."""
    GAME_DATA = [
        ('A', 'Y'),
        ('B', 'X'),
        ('C', 'Z'),
    ]

    total_score = 0
    for opponent_play, desired_outcome in GAME_DATA:
        my_play = get_my_play(opponent_play, desired_outcome)
        round_score = calculate_score(my_play, opponent_play, 'Y' if my_play == opponent_play else ('X' if desired_outcome == 'Z' else 'Z'))
        print(f"Round: My play {my_play.capitalize()} vs. Computer play {opponent_play.capitalize()}. "
              f"Outcome: draw if same, lose if X, win if Z. Score: {round_score}.")
        total_score += round_score

    print(f"\nTotal score: {total_score}")

# Define the dictionaries
SHAPING_POINTS = {'rock': 1, 'paper': 2, 'scissors': 3}
OUTCOME_POINTS = {'X': 0, 'Y': 3, 'Z': 6}
LOSE_MAP = {'A': 'scissors', 'B': 'rock', 'C': 'paper'}
WIN_MAP = {'A': 'paper', 'B': 'scissors', 'C': 'rock'}

if __name__ == "__main__":
    main()







    # Rock-Paper-Scissors game using a class

class RPSGame:
    """A class to represent the Rock-Paper-Scissors game."""

    def __init__(self):
        """Initializes the game with the required dictionaries."""
        self.shaping_points = {'rock': 1, 'paper': 2, 'scissors': 3}
        self.outcome_points = {'X': 0, 'Y': 3, 'Z': 6}
        self.lose_map = {'A': 'scissors', 'B': 'rock', 'C': 'paper'}
        self.win_map = {'A': 'paper', 'B': 'scissors', 'C': 'rock'}

    def calculate_score(self, my_play, opponent_play, outcome):
        """Calculates the score based on my play, opponent's play, and the outcome."""
        shape_points = self.shaping_points[my_play]
        outcome_points = self.outcome_points[outcome]
        return shape_points + outcome_points

    def get_my_play(self, opponent_play, desired_outcome):
        """Determines my play based on the opponent's play and desired outcome."""
        if desired_outcome == 'Y':
            return opponent_play

        if desired_outcome == 'X':
            return self.lose_map[opponent_play]

        return self.win_map[opponent_play]

def main():
    """The main function to run the game."""
    game = RPSGame()
    GAME_DATA = [
        ('A', 'Y'),
        ('B', 'X'),
        ('C', 'Z'),
    ]

    total_score = 0
    for opponent_play, desired_outcome in GAME_DATA:
        my_play = game.get_my_play(opponent_play, desired_outcome)
        round_score = game.calculate_score(my_play, opponent_play, 'Y' if my_play == opponent_play else ('X' if desired_outcome == 'Z' else 'Z'))
        print(f"Round: My play {my_play.capitalize()} vs. Computer play {opponent_play.capitalize()}. "
              f"Outcome: draw if same, lose if X, win if Z. Score: {round_score}.")
        total_score += round_score

    print(f"\nTotal score: {total_score}")

if __name__ == "__main__":
    main()