#!/usr/bin/python

import os, re, sys, time
import nflgame

valid_teams = set([ t[0] for t in nflgame.teams ])

class Bet:
  def __init__(self, raw):
    match = re.match(r'([a-zA-Z]{2,3})([+-][0-9\.]+)', raw)
    if not match:
      raise SyntaxError('Could not parse bet: "%s"' % raw)
    if match.group(1) not in valid_teams:
      raise SyntaxError('Unknown team: "%s"\n(valid teams: %s)' % (match.group(1), valid_teams))
    (self.team, self.spread) = match.groups([1, 2])

  def __str__(self):
    return '%s %s' % (self.team, self.spread)
  def __repr__(self): return self.__str__()

def parse_bets(input):
  # list of lists, to support parlays
  bet_groups = []
  for p in input:
    bet_groups.append([ Bet(b) for b in p.split(' ') ])

  return bet_groups


def check_bets(bet_groups):
  year, week = nflgame.live.current_year_and_week()
  all_games = nflgame.games(year, week=week, started=False)

  os.system('clear')

  index = {}
  for game in all_games:
    index[game.home] = (game.score_home - game.score_away, game)
    index[game.away] = (game.score_away - game.score_home, game)

  out = ''
  for group in bet_groups:
    out += '--------------------------------------------------\n'
    for bet in group:
      if bet.team in index:
        (diff, game) = index[bet.team]
        score = diff + float(bet.spread)
        if str(game.time) == 'Pregame': mark = '(pre) '
        elif score == 0:                mark = '(push)'
        elif score < 0:                 mark = '(lose)'
        else:                           mark = '(win) '

        out += '%3s %-5s %s %3s %2d - %2d %-3s [%s]\n' % (bet.team, bet.spread, mark, game.away, game.score_away, game.score_home, game.home, game.time)
      else:
        out += '%3s %-5s (unstarted)\n' % (bet.team, bet.spread)

  out += '--------------------------------------------------\n'

  return out


def main():
  usage = """%prog% bet [bet bet bet ...]
   "bets" is a list of bets
   Each bet is a team name (e.g. "NYG" or "JAC") plus a spread (e.g. "+3.5" or "-1")
   Group parlay bets into individual arguments to have them delineated in the output, e.g.
      %prog% "NYG+3 GB-4" IND-7
  """

  if len(sys.argv) < 2:
    print usage
    sys.exit(1)

  bet_groups = parse_bets(sys.argv[1:])

  while True:
    print check_bets(bet_groups)
    time.sleep(60)


if __name__ == '__main__':
  main()
