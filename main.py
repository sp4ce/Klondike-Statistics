import argparse
import csv
import matplotlib
import os.path
import pylab
import random
import subprocess
import sys
import time

#set line width
pylab.rcParams['lines.linewidth'] = 6
#set font size for titles
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.major.size'] = 5
#set size of numbers on y-axis
pylab.rcParams['ytick.major.size'] = 5
#set size of markers
pylab.rcParams['lines.markersize'] = 10
# XKCD style
matplotlib.pyplot.xkcd()

# Path to the solver application.
SOLVER = 'KlondikeSolver'
SOLVER_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'solver')
if not os.path.isfile(os.path.join(SOLVER_DIR, SOLVER)):
    print "Please run `cd solver` and then `make` to compile the solver"
    exit()

# Argument parser.
parser = argparse.ArgumentParser(description='Klondike Statistics')

# The number of game for the simulation.
parser.add_argument('--games', dest='games', type=int, default=10,
                    help='The number of random games (default to 10)')

# The number of cards to draw from the deck.
parser.add_argument('--draw', dest='draw', type=int, default=1,
                    help='Number of cards to draw (default to 1).')

# Display only the given file and does not run simulation.
parser.add_argument('--display', dest='display', type=str, default=None,
                    help='Display only the given file (default to None).')

# Parse the args.
args = parser.parse_args()

# Statistics file
if args.display == None:
    stats_dir = os.path.join(os.path.dirname(os.path.realpath(__file__), 'statistics'))
    stats = os.path.join(stats_dir, "stats_%s.csv" % (time.strftime("%d%m%Y%H%M%S")))

    # Run the games and collect the result.
    for i in range(0, args.games):
        # Generate a random game number.
        game = random.randint(0, sys.maxint / 2)

        # Call the solver on this game.
        subprocess.call([os.path.join(SOLVER_DIR, SOLVER), '-g', str(game),
                        '-dc', str(args.draw), '-o', str(2), '-st', stats])
else:
    stats = args.display

reader = csv.reader(open(stats, 'r'))
for row in reader:
    print row
