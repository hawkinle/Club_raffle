import random
import pandas as pd

def draw_raffle(participants):
    # Ensure there are at least 2 participants
    if len(participants) < 2:
        print("Not enough participants for the draw.")
        return

    # Create copies of participants for main and secondary draws
    main_draw = participants.copy()
    secondary_draw = participants.copy()

    # Calculate the number of weeks in 4 months (approximately 17 weeks)
    weeks = 17

    # Prepare a list to store the results
    results = []

    for week in range(weeks):
        # If all participants have had a turn, reset the list
        if not main_draw:
            main_draw = participants.copy()
        if not secondary_draw:
            secondary_draw = participants.copy()

        # Select a main and a secondary person
        main_person = main_draw.pop(0)
        secondary_person = secondary_draw.pop(0)

        # Store the result of the draw
        results.append([week+1, main_person, secondary_person])

    # Convert the results to a DataFrame and print it
    df = pd.DataFrame(results, columns=["Week", "Main Person", "Secondary Person"])
    print(df)

# List of participants
participants = ["Leith", "Jack", "Shelly", "Phil", "Dave","Dan", "Jason","Simon"]

# Shuffle the participants list to ensure randomness
random.shuffle(participants)

draw_raffle(participants)
