import matplotlib
import pylab

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

statesMoves = []
moves1 = []
moves2 = []
statesHelper = []
helper = []
file = open('solver/output.txt')
for line in file:
    if line.startswith('moves: '):
        line = line.replace('moves: ', '')
        info = line.split(',')
        statesMoves.append(int(info[0]))
        moves1.append(int(info[1]))
        moves2.append(int(info[2]))
    if line.startswith('helper: '):
        line = line.replace('helper: ', '')
        info = line.split(',')
        statesHelper.append(int(info[0]))
        helper.append(int(info[1]))


pylab.plot(statesMoves, moves1)
pylab.plot(statesMoves, moves2)
pylab.plot(statesHelper, helper)
# pylab.title('Mean Distance from Origin')
# pylab.xlabel('Steps Taken')
# pylab.ylabel('Steps from Origin')
pylab.show()
