import numpy as np
import matplotlib.pyplot as plt

def simulate_ruin(player_a_amount, player_b_amount, win_probability):
    """
    Simulates the ruin of two players in a gambling game and returns the number of rounds played.
    
    Args:
        player_a_amount (int): Initial amount of money for player A.
        player_b_amount (int): Initial amount of money for player B.
        win_probability (float): Probability of winning a bet.
        
    Returns:
        int: Number of rounds played until one of the players goes broke.
    """
    rounds = 0
    
    while player_a_amount > 0 and player_b_amount > 0:
        # Simulate a round of the game
        if np.random.rand() < win_probability:
            player_a_amount += 1  # Player A wins
            player_b_amount -= 1  # Player B loses
        else:
            player_a_amount -= 1  # Player A loses
            player_b_amount += 1  # Player B wins
        
        rounds += 1
    
    return rounds

def simulate_ruin_visual(player_a_amount, player_b_amount, win_probability):
    """
    Simulates the ruin of two players in a gambling game with a biased coin and visualizes the results.
    
    Args:
        player_a_amount (int): Initial amount of money for player A.
        player_b_amount (int): Initial amount of money for player B.
        win_probability (float): Probability of winning a bet.
    """
    player_a_history = [player_a_amount]
    player_b_history = [player_b_amount]
    rounds = 0
    
    while player_a_amount > 0 and player_b_amount > 0:
        # Simulate a round of the game with a biased coin
        if np.random.rand() < win_probability:
            player_a_amount += 1  # Player A wins
            player_b_amount -= 1  # Player B loses
        else:
            player_a_amount -= 1  # Player A loses
            player_b_amount += 1  # Player B wins
        
        rounds += 1
        player_a_history.append(player_a_amount)
        player_b_history.append(player_b_amount)
    
    # Plot the results
    plt.plot(player_a_history, label='Geralt fortune')
    plt.plot(player_b_history, label='Casino fortune')
    plt.xlabel('Rounds')
    plt.ylabel('Amount')
    plt.title('Players Ruin Simulation (Balanced Coin)')
    plt.legend()
    plt.grid()
    plt.show()

# Parameters
player_a_amount = 1000  # Initial amount of money for player A
player_b_amount = 100000  # Initial amount of money for player B
win_probability = 0.5  # Probability of winning a bet (biased coin)

# Perform the simulation and get the number of rounds played
rounds_played = simulate_ruin(player_a_amount, player_b_amount, win_probability)
print("Number of rounds played:", rounds_played)

# Perform the simulation and visualize the results
simulate_ruin_visual(player_a_amount, player_b_amount, win_probability)
