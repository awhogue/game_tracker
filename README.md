game_tracker
============

Little script to track NFL games with spreads.

Usage: 
    ./game_tracker.py bet [bet bet bet ...]

"bets" is a list of bets

Each bet is a team name (e.g. "NYG" or "JAC") plus a spread (e.g. "+3.5" or "-1")

Group parlay bets into individual arguments to have them delineated in the output, e.g.

    ./game_tracker.py "NYG+3 GB-4" IND-7
