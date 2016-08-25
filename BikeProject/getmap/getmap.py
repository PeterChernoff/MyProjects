from geopy.geocoders import GoogleV3
import smopy # Calls OpenStreetMap
import numpy as np
import json
import matplotlib
matplotlib.style.use('ggplot')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# import pandas as pd
# import geocoder

lat = 45.55
lon = -73.72
offLat = 0.15
offLon = 0.25
# zoomSize = 12
zoomSize = 12
# Montreal latitude/longitude coordinates

fig_height = 12
fig_width = fig_height * 5 / 3

tlat = np.linspace(lat - offLat, lat + offLat, 7)
tlon = np.linspace(lon - offLon, lon + offLon, 11)
save_location = 'Data/montreal.png'
savefigs = 'Data/test.pdf'
locationFile = 'Data/locations.json'


class GetMap:
    def __init__(self):
        
        # Calls map from OpenStreetMap, sets up coordinates for future use
        
        self.map = smopy.Map((lat - offLat, lon - offLon, lat + offLat, lon + offLon), z=zoomSize)
        try:
            self.map
        except:
            self.map.save_png(save_location)  # Saves the file to be retrieved later
        self.dict_location = self.load_dictionary
    
        # we have several variables that we will want to set up multiple times,
        # so it's easier to set their variables in a method.
        
        self.fig = None
        self.ax = None
        self.img = None
        self.imgplot = None
        self.inv = None
        
        self.setup_map()
    
    # self.fig.set_size_inches(fig_width, fig_height, forward=True)
    
    @property
    def load_dictionary(self):
        # We don't want to have to call the API over and over again, so we load the pre-existing dictionary
        try:
            json_file = open(locationFile)
            json_str = json_file.read()
            dict_location = json.loads(json_str)
            # if the file is empty the ValueError will be thrown
            # self.save_dictionary()#the file kep
            json_file.close()
        except OSError:
            # reset the dictionary and create its file if it does not exist
            dict_location = {}
            self.reset_dictionary()
        
        return dict_location
    
    def save_dictionary(self):
        
        # We don't want to have to call the API every time, we only have a limit,
        # so we save the locations in a json file
        
        with open(locationFile, 'w') as f:
            json.dump(self.dict_location, f)
        f.close()
    
    def reset_dictionary(self):
        # Sometimes, we may need to recalibrate the dictionary
        open(locationFile, 'w').close()
        self.dict_location = {}
    
    # def setup_map(self, check_ax=False):
    def setup_map(self):
        
        self.fig = plt.gcf()
        self.fig.clear()  # Clears the previous map
        self.ax = self.fig.add_subplot(111)
        
        self.img = mpimg.imread(save_location)
        self.imgplot = plt.imshow(self.img)
        self.imgplot.autoscale()
        self.ax.set_title('Map of Montreal', fontsize=1.5 * fig_width, fontweight='bold')
        
        self.inv = self.ax.transData.inverted()
        
        plt.axis('off')  # We don't want the ticks to be visible
        self.ax.axis('tight')  # Makes it fit to the edges
    
    def get_new_map(self):
        self.map = smopy.Map((lat - offLat, lon - offLon, lat + offLat, lon + offLon), z=zoomSize)
        # grabs map from OpenStreetMaps
        
        self.map.save_png(save_location)  # Saves the file to be retrieved later
        # Image(save_location)
                
        self.setup_map()
        
        return self.img, self.fig, self.ax, self.imgplot
    
    def get_current_map(self):
        return self.img, self.fig, self.ax, self.imgplot
    
    def reset_map(self):
        self.reset_dictionary()  # resets the dictionary too, since it might be edited
        self.setup_map()
    
    # def draw_accidents_by_frequency(self, datamap, top_values, popup=False):
    def draw_accidents_by_frequency(self, datamap, top_values):
        self.setup_map()
        
        geolocator = GoogleV3()  # uses google's geolocator api
        
        lon_lat_list = []
        
        # Makes circles to show relative problem areas
        for i in range(0, len(datamap[:top_values])):
            location_string = str(datamap.index[i])
            
            if location_string not in self.dict_location:
                location = geolocator.geocode(datamap.index[i])
            # Call the API if there's nothing in the API
            else:
                location = self.dict_location[location_string]
            # Call the dictionary
            
            ilat, ilon = location[1]
            
            xloc, yloc = self.map.to_pixels(ilat, ilon)
            
            lon_lat_list.append((xloc, yloc), )
            
            self.ax.plot(xloc, yloc, 'o', ms=5 + 2 * datamap[i], mew=2, alpha=0.2, markeredgewidth=2)
            
            if location_string not in self.dict_location:
                self.dict_location[location_string] = [[], [ilat, ilon]]
        
        self.save_dictionary()
        
        # Creates x markers in exact spots
        for lonLat in lon_lat_list:
            self.ax.plot(lonLat[0], lonLat[1], 'xk', ms=5, mew=2, alpha=1, markeredgewidth=1)
