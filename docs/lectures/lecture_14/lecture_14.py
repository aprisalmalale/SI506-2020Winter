# Lecture 14 Exercise

# 01. Write functions
# 02. Call functions
# 03. Orchestrate execution flow from main()
# 04. Work with dictionaries
# 05. Bonus: leverage enumerate() index values


def calculate_points(record):
    """Calculate league points per provided team record.
    Points are earned as follows: win 3 points, draw 1 point
    loss 0 points.

    Parameters:
        record (list): list of wins, draws, and losses

    Returns
        int: total league points earned
    """

    pass


def place_in_standings(standings, team):
    """Update league standings. List order is
    determined by team points. Last place team
    is appended to list not inserted.

    Parameters:
        standings (list): current standings
        team (dict): team to be inserted/appended to list

    Return:
        list: updated standings
    """

    pass


def standings_to_str(standings):
    """Format standings list as string. Use enumerate()
    index value both to display place. Ties receive the
    same place value.

    Format: "<place>. <team name> (<points>)\n"

    Parameters:
        standings (list): team standings

    Returns:
        str: formatted string representation of list
    """

    pass


def main():
    """Program entry point. Generate English Priemer League
    team standings list sorted by total points earned.

    Orchestrate workflow by calling functions that perform
    the following tasks:

      1) calculate League points for each team based on record.
         record: [<wins>, <draws>, <losses>]
      2) generate new standings list sorted by points. Ties
         receive the same place value.
      3) provide a string representation of the new list.
      4) print string to screen

    Parameters:
        None

    Returns:
        None
    """

    # Standings (alpha sort)
    # List: <wins>, <draws>, <losses>
    premier_league = {
        'Arsenal': [8,13,6],
        'Aston Villa': [7,4,16],
        'Bournemouth': [7,5,15],
        'Brighton': [6,10,11],
        'Burnley': [11,4,12],
        'Chelsea': [13,5,9],
        'Crystal Palace': [8,9,10],
        'Everton': [10,6,11],
        'Leicester City': [15,5,7],
        'Liverpool': [26,1,0],
        'Manchester City': [18,3,6],
        'Manchester United': [11,8,8],
        'Newcastle': [8,7,12],
        'Norwich City': [4,6,17],
        'Sheffield United': [10,10,7],
        'Southampton': [10,4,13],
        'Tottenham': [11,7,9],
        'Watford': [5,9,13],
        'West Ham': [6,6,15],
        'Wolverhampton': [9,12,6]
    }

    standings = [] # accumulator

    for key, val in premier_league.items():
        # Calculate points
        points = 0 # FIX ME

        # New team record
        team = {} # dict literal

        # Seed standings list
        if not standings:
            standings.append(team)

        # Sort standings
        if team not in standings:
            standings = None # FIX ME

        # print(key, points)

    # Format output
    to_str = None # FIX ME
    print(to_str)


if __name__ == '__main__':
    main()