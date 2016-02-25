__author__ = 'MegaPete'

'''
Special thanks to http://opentechschool.github.io/python-data-intro/

This program takes data about airports (provided by http://www.openflights.org/data.html) and plots them on a map.
It takes the longitude and latitude of an airport and places them on a map. In the RGB values, which start as [1,1,1], the R values decreases as the
absolute value of the longitude increases, the G values decreases as you go south, and the B values decreases as you go north.
Original Map from http://en.wikipedia.org/wiki/Equirectangular_projection, converted to png.
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import csv
import math as m

size = 30



LONGITUDE = 180
LATITUDE = 90
LONGITUDE_TICK = 30
LATITUDE_TICK = 30
latitudes = {}
longitudes = {}

fig = None
ax = None
imgplot = None

# Setup the map plot
fig = plt.gcf()
ax = fig.add_subplot(111)
fig.set_size_inches(size, size/2)
fig.savefig("../AllData/test2png.png", dpi=100)

img=mpimg.imread('../AllData/Equirectangular_projection_SW.png')
imgplot = plt.imshow(img, extent=[-180, 180, -90, 90])
imgplot.autoscale()
plt.axis([-180, 180, -90, 90])

ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
imgplot.autoscale()

major_ticksX = np.arange(-LONGITUDE, LONGITUDE+1, LONGITUDE_TICK)
major_ticksY = np.arange(-LATITUDE, LATITUDE+1, LATITUDE_TICK)

ax.set_xticks(major_ticksX)
ax.set_yticks(major_ticksY)
#plt.plot(0, 0, 'ro', markersize=10)

f = open("../AllData/airports.dat", encoding="utf8")
toDeleteCount = 0

for row in csv.reader(f):
    #grabs the value from airports.dat, creates dictionaries with the values for later use
    airportID = row[0]
    latitudes[airportID] = float(row[6])
    longitudes[airportID] = float(row[7])

    #Makes the colours different

    if latitudes[airportID] >=0:
        colour = [1-abs(longitudes[airportID])/LONGITUDE, 1-latitudes[airportID]/LATITUDE, 1]
    else:
        colour = [1-abs(longitudes[airportID])/LONGITUDE, 1,  1+latitudes[airportID]/LATITUDE]


    plt.plot(longitudes[airportID], latitudes[airportID], color=colour, marker = 'o', markersize=4)

    '''
    #this is just test coding, in case I want to run through the values quickly
    if toDeleteCount > 1000:
        break
    toDeleteCount += 1
    if toDeleteCount % 1000 == 0:
        print("Work in progress: " + str(toDeleteCount/1000))

    '''
plt.show()