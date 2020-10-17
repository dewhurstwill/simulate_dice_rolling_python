######################################################
#                                                    #
#  A simple program to calculate the probability of  #
#     rolling 2 1s (snake eyes) on a pair of dice.   #
#                                                    #
######################################################

# Importing the random module, this will be used to 
# simulate a dice roll, random number between 1-6
import random

# Setting a variable to be used as a counter for
# the total number of rolls taken
total_rolls = 0
# Number of times to run the test, before calculating
# the probability
times_to_roll = 1000

# Function to roll a dice
def roll_dice():
  # Roll a dice (Generate random number between
  # 1 and 6)
  result = random.randint(1,6)
  # If the total_rolls is divisible by 2 the
  # roll was done by Dice 2 
  if (total_rolls % 2) == 0:
    print('Dice 2: ', result)
  # Otherwise it was Dice 1
  else:
    print('Dice 1: ', result)
  # Return the result of the dice roll
  return result

# Run the test x times
for i in range(times_to_roll):
  while True:
    # Increment the total_rolls by 1
    total_rolls += 1
    # Roll 2 dice and save the results to die1 & die2
    die1,die2 = roll_dice(),roll_dice()
    # If both dice roll a 1, break out of the loop
    if die1 == 1 and die2 == 1:
      break
  
  # Print the total_rolls taken
  print('Number of rolls taken: ', total_rolls)
  # Print the current loop number
  print('Current loop number: ', i+1)
  # Print a line break
  print('')
# Calculate the probability
probability = total_rolls/times_to_roll
# Print the probability as a fraction
print('Probability of rolling snake eyes: 1/{0:.0f}'.format(probability))
# Calculate the probability as a percentage
probability_percentage = 1 / probability * 100
# Print the probability as a percentage
print('Probability {:.1f}%'.format(probability_percentage))
