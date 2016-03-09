import smopy
#Calls OpenStreetMap
import numpy as np

import pandas as pd
import matplotlib
matplotlib.style.use('ggplot')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from geopy.geocoders import GoogleV3

import geocoder

lat = 45.55
lon = -73.72
offLat = 0.15
offLon = 0.25
#zoomSize = 12
zoomSize = 12
#Montreal latitude/longitude coordinates

fig_height = 12
fig_width = fig_height * 5/3

tlat = np.linspace(lat-offLat, lat+offLat, 7)
tlon = np.linspace(lon-offLon, lon+offLon, 11)
saveLocation = '../Data/montreal.png'
savefigs = '../Data/test.png'

class GetMap:
	def __init__(self):


		#Calls map from OpenStreetMap, sets up coordinates for future use
		self.map = smopy.Map((lat-offLat, lon-offLon, lat+offLat, lon+offLon), z=zoomSize)
		self.map.save_png(saveLocation)#Saves the file to be retrieved later

		self.setupMap()

		#self.fig.set_size_inches(fig_width, fig_height, forward=True)


	def setupMap(self, checkAx = False):

		self.fig = plt.gcf()
		self.fig.clear()#Clears the previous map
		self.ax = self.fig.add_subplot(111)

		self.img=mpimg.imread(saveLocation)
		self.imgplot = plt.imshow(self.img)
		self.imgplot.autoscale()
		self.ax.set_title('Map of Montreal', fontsize=1.5*fig_width, fontweight='bold')

		self.inv = self.ax.transData.inverted()

		plt.axis('off')#We don't want the ticks to be visible
		self.ax.axis('tight')#Makes it fit to the edges


	def getNewMap(self):
		self.map = smopy.Map((lat-offLat, lon-offLon, lat+offLat, lon+offLon), z=zoomSize)

		#grabs map from OpenStreetMaps
		self.map.save_png(saveLocation)#Saves the file to be retrieved later
		#Image(saveLocation)

		self.setupMap()

		return self.img, self.fig, self.ax, self.imgplot

	def getCurrentMap(self):
		return (self.img, self.fig, self.ax, self.imgplot)

	def resetMap(self):
		self.setupMap()

	def drawAccidentsByFrequency(self, datamap, topValues, popup=False):
		self.setupMap()

		geolocator = GoogleV3()#uses google's geolocator api

		lonLatList = []

		#Makes circles to show relative problem areas
		for i in range(0, len(datamap[:topValues])):
			ilat, ilon = geolocator.geocode(datamap.index[i])[1]
			name =  geolocator.geocode(datamap.index[i])[0]

			xloc, yloc= self.map.to_pixels(ilat, ilon)

			lonLatList.append((xloc, yloc),)

			self.ax.plot(xloc,yloc, 'o', ms=5 + 2*datamap[i], mew=2, alpha=0.2, markeredgewidth=2)

		#Creates x markers in exact spots
		for lonLat in lonLatList:
			self.ax.plot(lonLat[0],lonLat[1], 'xk', ms=5, mew=2, alpha=1, markeredgewidth=1)



