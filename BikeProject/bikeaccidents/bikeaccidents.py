# The usual preamble
import pandas as pd

from enum import Enum

saveLocation = "../data/MTLBikeCollisions2006-2010.csv"


class UnknownTime(Enum):
    include = 1
    exclude = 2
    only = 3


class BikeAccidents:
    def __init__(self):
        self.accidents = pd.read_csv(saveLocation)
        self.accidents['Date'] = pd.to_datetime(self.accidents['Date'])
        self.min_date = min(self.accidents['Date'])
        self.max_date = max(self.accidents['Date'])

    '''
    We are checking between what time and what time the accidents happen, if we are including the unknown
    times, and what date and what date these accidents happen
    '''

    def accident_range(self, start_time="", end_time="", include_unknown_time=UnknownTime.include,
                       start_date="", end_date=""):
        
        my_accidents = self.accidents
        if include_unknown_time.value == UnknownTime.only.value:
            data = my_accidents[my_accidents['Time'].isnull()].copy()  # includes only the unknown times
        elif include_unknown_time.value == UnknownTime.exclude.value:
            data = my_accidents[my_accidents['Time'].notnull()].copy()  # excludes the unknown times
        else:
            data = my_accidents.copy()  # Gets both
        
        # to_datetime is to get the times to a more usable format
        data.loc[:, 'Time'] = pd.to_datetime(data['Time'])
        data.loc[:, 'Date'] = pd.to_datetime(data['Date'])
            
        # We want the string value of our dates, which are the last values depicted
        min_time = "00:00:00" if not start_time else str(start_time)[-8:]
        max_time = "23:59:59" if not start_time else str(end_time)[-8:]
                
        min_date = data["Date"].min() if not start_date else start_date
        max_date = data["Date"].max() if not end_date else end_date

        # We might want to cover a range late at night from 23:00 to 1:00, so we want to have the option to wrap around
        if min_time <= max_time:
            # The more intuitive, is the value between the lower value and the higher value.
            # Checks between the initial time and the end time
            data = data[
                ((data['Time'].isnull()) |
                 (data['Time'] >= pd.to_datetime(min_time)) &
                 (data['Time'] <= pd.to_datetime(max_time)))]
        else:
            # This isn't that complicated, but it can be unintuitive
            # You just need to remember the "min_time" is the higher value
            # This excludes the times between the initial time and the end time
            data = data[
                (data['Time'].isnull() |
                 (data['Time'] >= pd.to_datetime(min_time)) |
                 (data['Time'] <= pd.to_datetime(max_time)))]
        
        # similarly, we might want to include or exclude a range of dates
        if min_date <= max_date:
            data = data[(data['Date'] >= pd.to_datetime(min_date)) &
                        (data['Date'] <= pd.to_datetime(max_date))]
        else:
            data = data[(data['Date'] >= pd.to_datetime(min_date)) |
                        (data['Date'] <= pd.to_datetime(max_date))]

        return data

    def accident_count(self, data_to_map):
        # amalgamates the values that happen at a cerain location
        accident_count_location = data_to_map['Geocoding address'].value_counts()
        return accident_count_location
