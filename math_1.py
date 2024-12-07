import matplotlib
import matplotlib.pylab
import matplotlib.pyplot
trans = input("What would you like to translate? ")

if trans == "a":
    matplotlib.pyplot.plot([0, 0, 1, 1, 1, 0],[0, 100, 100, 0, 50, 50])

#if trans == "b":
    #matplotlib.pyplot.plot([],[])

matplotlib.pyplot.show()