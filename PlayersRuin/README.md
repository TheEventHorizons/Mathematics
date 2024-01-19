# Ruin Simulation README

This repository contains a Python script for simulating a gambling game between two players and analyzing the ruin scenario. The game involves two players, each starting with an initial amount of money. The players take turns betting, and the winner of each round gains money while the loser loses money. The game continues until one of the players goes broke.

## Prerequisites

Make sure you have the following libraries installed:

- numpy
- matplotlib

You can install these libraries using the following command:

```bash
pip install numpy matplotlib
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/TheEventHorizons/Players-Ruin.git
cd Players-Ruin
```

2. Run the script:

```bash
python ruin_simulation.py
```

The script simulates the gambling game using a biased coin and outputs the number of rounds played until one of the players goes broke. Additionally, it provides a visual representation of the players' fortunes throughout the simulation.

## Script Overview

- `ruin_simulation.py`: The main Python script.
- `README.md`: This README file providing instructions and an overview of the script.

## Simulation Function

- `simulate_ruin(player_a_amount, player_b_amount, win_probability)`: Simulates the ruin of two players in a gambling game and returns the number of rounds played.

## Visualization Function

- `simulate_ruin_visual(player_a_amount, player_b_amount, win_probability)`: Simulates the ruin of two players in a gambling game with a biased coin and visualizes the results using matplotlib.

## Parameters

Adjust the following parameters in the script:

- `player_a_amount`: Initial amount of money for player A.
- `player_b_amount`: Initial amount of money for player B.
- `win_probability`: Probability of winning a bet (biased coin).

Feel free to experiment with different initial amounts and win probabilities to observe how they affect the ruin scenario.

For a simple explanation of how the classification works, visit my [scientific outreach website](https://theeventhorizons.com/toss-a-coin/) for accessible content on the topic.

Happy simulating!