game_tracker
============

Little script to track NFL games with spreads.

Usage: 

    ./game_tracker.py bet [bet bet bet ...]

Each bet is a team name (e.g. "NYG" or "JAC") plus a spread (e.g. "+3.5" or "-1")

Group parlay bets into individual arguments to have them delineated in the output, e.g.

    ./game_tracker.py "NYG+3 GB-4" IND-7

Output looks like:

    --------------------------------------------------
     GB -3    (lose)  GB 13 - 21 BUF [Final]
     NE -8.5  (win)  MIA 13 - 41 NE  [Final]
    IND -7    (push) HOU 10 - 17 IND [Final]
    --------------------------------------------------
    PIT -3    (win)  PIT 27 - 20 ATL [Final]
    CIN +2.5  (win)  CIN 30 -  0 CLE [Final]
    CAR -3.5  (lose)  TB 17 - 19 CAR [Final]
    --------------------------------------------------
    NYG -7    (win)  WAS 13 - 24 NYG [Final]
    --------------------------------------------------
    DEN -4    (win)  DEN 22 - 10 SD  [Q4 03:56]
    TEN +3.5  (lose) NYJ 16 - 11 TEN [Q4 03:09]
    DET -7.5  (lose) MIN 14 - 16 DET [Q4 03:20]
    SEA -10   (push)  SF  7 - 17 SEA [Q4 09:17]
    --------------------------------------------------
    TEN -3.5  (lose) NYJ 16 - 11 TEN [Q4 03:09]
    CIN -3.5  (win)  CIN 30 -  0 CLE [Final]
    --------------------------------------------------