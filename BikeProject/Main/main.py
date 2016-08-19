# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MapGet.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys

import pandas as pd
from PyQt4 import QtCore, QtGui
from matplotlibwidget import MatplotlibWidget

from enum import Enum

try:
    from getmap.getmap import GetMap
except Exception:
    from getmap.getmap import GetMap
try:
    from bikeaccidents.bikeaccidents import BikeAccidents
except Exception:
    from bikeaccidents.bikeaccidents import BikeAccidents

import matplotlib

matplotlib.style.use('ggplot')


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    
    
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class UnknownTime(Enum):
    include = 1
    exclude = 2
    only = 3


# Need to add this, otherwise doesn't work
class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = UIMainWindow(self)
        # self.ui.setup_ui(self)


class UIMainWindow(object):
    def __init__(self, main_window):
        self.setup_vars()
        
        main_window.setObjectName(_fromUtf8("main_window"))
        main_window.resize(850, 858)
        self.centralwidget = QtGui.QWidget(main_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.grid_layout = QtGui.QGridLayout(self.centralwidget)
        self.grid_layout.setObjectName(_fromUtf8("grid_layout"))
        spacer_item = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer_item, 4, 1, 1, 1)
        spacer_item1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer_item1, 4, 3, 1, 3)
        self.labelTime = QtGui.QLabel(self.centralwidget)
        self.labelTime.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.labelTime.setWordWrap(True)
        self.labelTime.setObjectName(_fromUtf8("labelTime"))
        self.grid_layout.addWidget(self.labelTime, 1, 0, 1, 6)
        self.check_box_date_end = QtGui.QCheckBox(self.centralwidget)
        self.check_box_date_end.setChecked(False)
        self.check_box_date_end.setObjectName(_fromUtf8("check_box_date_end"))
        self.grid_layout.addWidget(self.check_box_date_end, 15, 2, 1, 1)
        self.check_box_day_start = QtGui.QCheckBox(self.centralwidget)
        self.check_box_day_start.setChecked(False)
        self.check_box_day_start.setObjectName(_fromUtf8("check_box_day_start"))
        self.grid_layout.addWidget(self.check_box_day_start, 5, 0, 1, 1)
        spacer_item2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer_item2, 7, 0, 1, 1)
        self.labelDate = QtGui.QLabel(self.centralwidget)
        self.labelDate.setWordWrap(True)
        self.labelDate.setObjectName(_fromUtf8("labelDate"))
        self.grid_layout.addWidget(self.labelDate, 8, 0, 1, 6)
        self.label_unknown_times = QtGui.QLabel(self.centralwidget)
        self.label_unknown_times.setObjectName(_fromUtf8("label_unknown_times"))
        self.grid_layout.addWidget(self.label_unknown_times, 6, 1, 1, 2)
        self.time_edit_primary = QtGui.QTimeEdit(self.centralwidget)
        self.time_edit_primary.setEnabled(True)
        self.time_edit_primary.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time_edit_primary.setAutoFillBackground(False)
        self.time_edit_primary.setWrapping(True)
        self.time_edit_primary.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.time_edit_primary.setCalendarPopup(False)
        self.time_edit_primary.setObjectName(_fromUtf8("time_edit_primary"))
        self.grid_layout.addWidget(self.time_edit_primary, 4, 0, 1, 1)
        self.label_primary_time = QtGui.QLabel(self.centralwidget)
        self.label_primary_time.setObjectName(_fromUtf8("label_primary_time"))
        self.grid_layout.addWidget(self.label_primary_time, 3, 0, 1, 1)
        self.label_secondary_time = QtGui.QLabel(self.centralwidget)
        self.label_secondary_time.setObjectName(_fromUtf8("label_secondary_time"))
        self.grid_layout.addWidget(self.label_secondary_time, 3, 2, 1, 1)
        spacer_item3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.grid_layout.addItem(spacer_item3, 4, 6, 1, 1)
        self.date_primary = QtGui.QDateEdit(self.centralwidget)
        self.date_primary.setWrapping(True)
        # Setting the min/max times at start
        self.date_primary.setDateTime(
            QtCore.QDateTime(QtCore.QDate(self.earliest_date.year, self.earliest_date.month, self.earliest_date.day),
                             QtCore.QTime(0, 0, 0)))
        self.date_primary.setMaximumDateTime(
            QtCore.QDateTime(QtCore.QDate(self.latest_date.year, self.latest_date.month, self.latest_date.day),
                             QtCore.QTime(23, 59, 59)))
        self.date_primary.setMinimumDateTime(
            QtCore.QDateTime(QtCore.QDate(self.earliest_date.year, self.earliest_date.month, self.earliest_date.day),
                             QtCore.QTime(0, 0, 0)))
        self.date_primary.setCalendarPopup(False)
        self.date_primary.setObjectName(_fromUtf8("date_primary"))
        self.grid_layout.addWidget(self.date_primary, 14, 0, 1, 1)
        self.check_box_day_end = QtGui.QCheckBox(self.centralwidget)
        self.check_box_day_end.setChecked(False)
        self.check_box_day_end.setObjectName(_fromUtf8("check_box_day_end"))
        self.grid_layout.addWidget(self.check_box_day_end, 5, 2, 1, 1)
        self.label_secondary_date = QtGui.QLabel(self.centralwidget)
        self.label_secondary_date.setObjectName(_fromUtf8("label_secondary_date"))
        self.grid_layout.addWidget(self.label_secondary_date, 12, 2, 1, 1)
        self.time_edit_secondary = QtGui.QTimeEdit(self.centralwidget)
        self.time_edit_secondary.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time_edit_secondary.setAutoFillBackground(False)
        self.time_edit_secondary.setWrapping(True)
        self.time_edit_secondary.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(23, 59, 0)))
        self.time_edit_secondary.setCalendarPopup(False)
        self.time_edit_secondary.setObjectName(_fromUtf8("time_edit_secondary"))
        self.grid_layout.addWidget(self.time_edit_secondary, 4, 2, 1, 1)
        self.check_box_date_start = QtGui.QCheckBox(self.centralwidget)
        self.check_box_date_start.setChecked(False)
        self.check_box_date_start.setObjectName(_fromUtf8("check_box_date_start"))
        self.grid_layout.addWidget(self.check_box_date_start, 15, 0, 1, 1)
        self.matplotlib_map = MatplotlibWidget(self.centralwidget)
        self.matplotlib_map.setObjectName(_fromUtf8("matplotlib_map"))
        self.grid_layout.addWidget(self.matplotlib_map, 16, 0, 1, 7)
        self.label_primary_date = QtGui.QLabel(self.centralwidget)
        self.label_primary_date.setObjectName(_fromUtf8("label_primary_date"))
        self.grid_layout.addWidget(self.label_primary_date, 12, 0, 1, 1)
        self.date_secondary = QtGui.QDateEdit(self.centralwidget)
        self.date_secondary.setWrapping(True)
        # Setting the min/max times at start
        self.date_secondary.setDate(QtCore.QDate(self.latest_date.year, self.latest_date.month, self.latest_date.day))
        self.date_secondary.setMaximumDateTime(
            QtCore.QDateTime(QtCore.QDate(self.latest_date.year, self.latest_date.month, self.latest_date.day),
                             QtCore.QTime(23, 59, 59)))
        self.date_secondary.setMinimumDateTime(
            QtCore.QDateTime(QtCore.QDate(self.earliest_date.year, self.earliest_date.month, self.earliest_date.day),
                             QtCore.QTime(0, 0, 0)))
        self.date_secondary.setCalendarPopup(False)
        self.date_secondary.setObjectName(_fromUtf8("date_secondary"))
        self.grid_layout.addWidget(self.date_secondary, 14, 2, 1, 1)
        self.btnStart = QtGui.QPushButton(self.centralwidget)
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.grid_layout.addWidget(self.btnStart, 15, 6, 1, 1)
        self.combo_box_unknown_times = QtGui.QComboBox(self.centralwidget)
        self.combo_box_unknown_times.setObjectName(_fromUtf8("combo_box_unknown_times"))
        self.combo_box_unknown_times.addItem(_fromUtf8(""))
        self.combo_box_unknown_times.addItem(_fromUtf8(""))
        self.combo_box_unknown_times.addItem(_fromUtf8(""))
        self.grid_layout.addWidget(self.combo_box_unknown_times, 6, 0, 1, 1)
        self.spin_box_limit = QtGui.QSpinBox(self.centralwidget)
        self.spin_box_limit.setMinimum(1)
        self.spin_box_limit.setMaximum(20)
        self.spin_box_limit.setProperty("value", 10)
        self.spin_box_limit.setObjectName(_fromUtf8("spin_box_limit"))
        self.grid_layout.addWidget(self.spin_box_limit, 15, 5, 1, 1)
        self.label_spinner = QtGui.QLabel(self.centralwidget)
        self.label_spinner.setWordWrap(True)
        self.label_spinner.setObjectName(_fromUtf8("label_spinner"))
        self.grid_layout.addWidget(self.label_spinner, 14, 4, 1, 3)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.grid_layout.addWidget(self.label, 0, 0, 1, 3)
        self.labelinfo_update = QtGui.QLabel(self.centralwidget)
        self.labelinfo_update.setWordWrap(True)
        self.labelinfo_update.setObjectName(_fromUtf8("labelinfo_update"))
        self.grid_layout.addWidget(self.labelinfo_update, 17, 0, 1, 5)
        self.btn_reset_map = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_reset_map.setFont(font)
        self.btn_reset_map.setObjectName(_fromUtf8("btn_reset_map"))
        self.grid_layout.addWidget(self.btn_reset_map, 17, 6, 1, 1)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(main_window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        main_window.setStatusBar(self.statusbar)
        
        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)
    
    def retranslate_ui(self, main_window):
        main_window.setWindowTitle(_translate("main_window", "main_window", None))
        self.labelTime.setText(_translate("main_window",
                                          "Enter a time range. The range will include the hours and minutes "
                                          "between the primary time and the secondary time, unless the "
                                          "primary time is higher than the secondary time, where it will "
                                          "instead exclude the time between them.",
                                          None))
        self.check_box_date_end.setText(_translate("main_window", "End at the latest date", None))
        self.check_box_day_start.setText(_translate("main_window", "Start from the beginning of the day", None))
        self.labelDate.setText(_translate("main_window",
                                          "Enter a date range. The range will include the dates between the "
                                          "primary date and the secondary date, unless the primary date is "
                                          "higher than the secondary date, where it will instead exclude "
                                          "the dates between them.",
                                          None))
        self.label_unknown_times.setText(_translate("main_window", "include unknown times", None))
        self.time_edit_primary.setDisplayFormat(_translate("main_window", "hh:mm", None))
        self.label_primary_time.setText(_translate("main_window", "Enter the primary time", None))
        self.label_secondary_time.setText(_translate("main_window", "Enter the secondary time", None))
        self.check_box_day_end.setText(_translate("main_window", "Finish at the end of the day", None))
        self.label_secondary_date.setText(_translate("main_window", "Enter the secondary date", None))
        self.time_edit_secondary.setDisplayFormat(_translate("main_window", "hh:mm", None))
        self.check_box_date_start.setText(_translate("main_window", "Start from the earliest date", None))
        self.label_primary_date.setText(_translate("main_window", "Enter the primary date", None))
        self.btnStart.setText(_translate("main_window", "Calculate", None))
        self.combo_box_unknown_times.setItemText(0, _translate("main_window", "Do", None))
        self.combo_box_unknown_times.setItemText(1, _translate("main_window", "Do not", None))
        self.combo_box_unknown_times.setItemText(2, _translate("main_window", "Only", None))
        self.label_spinner.setText(_translate("main_window",
                                              "Enter a value. It will pick the top most accident prone "
                                              "locations given your parameters. API limits prevent too many "
                                              "from being displayed.", None))
        self.label.setText(_translate("main_window",
                                      "This program calculates and displays the most hazardous locations in "
                                      "Montreal for a cyclist  between certain hours of the day over a "
                                      "period of time.\n"
                                      "Please have a stable internet connection.", None))
        self.labelinfo_update.setText(_translate("main_window",
                                                 "You are getting the locations of accidents at the times "
                                                 "between 0:00 and 23:59, between the dates of 2006-01-01 "
                                                 "and 2010-12-31, including the accidents without specific "
                                                 "times", None))
        self.matplotlib_map.setAutoFillBackground(True)
        self.btn_reset_map.setText(_translate("main_window", "Reset Map", None))

        QtCore.QObject.connect(self.btnStart, QtCore.SIGNAL('clicked()'), self.calculate_data_map)
        
        self.btnStart.clicked.connect(self.calculate_data_map)
        self.btn_reset_map.clicked.connect(self.get_map)
        self.btn_reset_map.clicked.connect(self.change_data_parameters)
        
        self.combo_box_unknown_times.currentIndexChanged.connect(self.change_data_parameters)
        self.check_box_date_end.stateChanged.connect(self.change_data_parameters)
        self.check_box_date_start.stateChanged.connect(self.change_data_parameters)
        self.check_box_day_end.stateChanged.connect(self.change_data_parameters)
        self.check_box_day_start.stateChanged.connect(self.change_data_parameters)
        
        self.date_primary.dateChanged.connect(self.change_data_parameters)
        self.date_secondary.dateChanged.connect(self.change_data_parameters)
        self.time_edit_primary.timeChanged.connect(self.change_data_parameters)
        self.time_edit_secondary.timeChanged.connect(self.change_data_parameters)
        self.spin_box_limit.valueChanged.connect(self.change_data_parameters)
        self.btn_reset_map.clicked.connect(self.reset_map)
        
        # We want to call it so the text is correct at the beginning
        self.change_data_parameters()
        
        self.get_map()
    
    def setup_vars(self):
        # Sets up variables for use in program
        self.gm = GetMap()
        self.img, self.fig, self.ax, self.imgplot = self.gm.get_current_map()
        
        self.bike_accidents = BikeAccidents()
        self.earliest_date = pd.to_datetime(self.bike_accidents.min_date)
        self.latest_date = pd.to_datetime(self.bike_accidents.max_date)
        self.getting_looking = "looking for"
    
    def calculate_data_map(self):
        self.getting_looking = "getting"
        self.change_data_parameters()
        
        # Filters out the data
        data = self.bike_accidents.accident_range(start_time=self.ptime,
                                                  end_time=self.stime,
                                                  include_unknown_time=self.include_unknown,
                                                  start_date=self.pdate.strftime("%Y-%m-%d"),
                                                  end_date=self.sdate.strftime("%Y-%m-%d"),
                                                  )
        
        data_accident_location = self.bike_accidents.accident_count(data)  # Groups the data according to location
        self.gm.draw_accidents_by_frequency(data_accident_location, self.top_accidents)
        
        self.matplotlib_map.draw()
    
    def reset_map(self):
        self.gm.reset_map()
        self.matplotlib_map.figure = self.fig
        self.matplotlib_map.draw()
    
    def get_map(self):
        self.matplotlib_map.figure = self.fig
        self.matplotlib_map.draw()
    
    def change_data_parameters(self):
        
        self.top_accidents = self.spin_box_limit.value()
        
        # Checks if our check boxes are checked, to see if we want to use the extreme dates or not
        if self.check_box_date_start.isChecked():
            # Set up so is time date
            self.pdate = self.earliest_date
        else:
            self.pdate = pd.to_datetime(self.date_primary.date().toString())
        
        if self.check_box_date_end.isChecked():
            # Set up so is time date
            self.sdate = self.latest_date
        else:
            self.sdate = pd.to_datetime(self.date_secondary.date().toString())
        
        pdate_y, p_date_m, p_date_d = self.pdate.year, self.pdate.month, self.pdate.day
        sdate_y, sdate_m, sdate_d = self.sdate.year, self.sdate.month, self.sdate.day
        
        # using pandas Timestamps for formatting
        if self.check_box_day_start.isChecked():
            self.ptime = pd.to_datetime("00:00:00")
        else:
            self.ptime = pd.to_datetime(self.time_edit_primary.time().toString(), format='%H:%M:%S')
        
        ptime_h, ptime_m = self.ptime.hour, self.ptime.minute
        if self.check_box_day_end.isChecked():
            self.stime = pd.to_datetime("23:59:59")
        else:
            self.stime = pd.to_datetime(self.time_edit_secondary.time().toString())
            
        stime_h, stime_m = self.stime.hour, self.stime.minute
        
        # We want to either get the dates between certain dates, or dates not between certain dates
        if self.sdate >= self.pdate:
            date_between_text = "between"
            mid_date_time_frame = "{}-{:02d}-{:02d} and {}-{:02d}-{:02d}".format(pdate_y, p_date_m, p_date_d, sdate_y,
                                                                                 sdate_m, sdate_d)
        else:
            date_between_text = "between " + self.earliest_date.strftime(
                "%Y-%m-%d") + " and " + self.latest_date.strftime("%Y-%m-%d") + ", excluding the dates between"
            mid_date_time_frame = "{}-{:02d}-{:02d} and {}-{:02d}-{:02d}".format(sdate_y, sdate_m, sdate_d,
                                                                                 pdate_y, p_date_m, p_date_d)
        
        end_text = "the accidents without specific times."
        unknown_time_text = ""
        if self.combo_box_unknown_times.currentText() == "Only":
            time_between_text = ""
            unknown_time_text = "only using"
            self.include_unknown = UnknownTime.only
        else:
            if self.stime >= self.ptime:
                time_between_text = "at the times between "
                time_between_text += "{}:{:02d} and {}:{:02d},".format(ptime_h, ptime_m, stime_h, stime_m)
            
            else:
                time_between_text = "excluding the times between "
                time_between_text += "{}:{:02d} and {}:{:02d},".format(stime_h, stime_m, ptime_h, ptime_m)
            
            if self.combo_box_unknown_times.currentText() == "Do":
                unknown_time_text = "including"
                self.include_unknown = UnknownTime.include
            
            elif self.combo_box_unknown_times.currentText() == "Do not":
                unknown_time_text = "not including"
                self.include_unknown = UnknownTime.exclude
        
        if self.top_accidents == 1:
            self.location_text = "location"
            self.accident_text = ""
        else:
            self.location_text = "locations"
            self.accident_text = str(self.top_accidents) + " "
        
        text = 'You are {getting_looking} the top {accident_text}accident {location_text} ' \
               '{time_between_text} {date_between_text} {time_frame}, ' \
               '{unknown_time_text} {end_text}'.format(
            getting_looking=self.getting_looking, accident_text=self.accident_text,
            location_text=self.location_text,
            time_between_text=time_between_text, date_between_text=date_between_text,
            unknown_time_text=unknown_time_text,
            time_frame=mid_date_time_frame,
            end_text=end_text)
        
        self.labelinfo_update.setText(text)
        
        # Changes "Getting" to "Looking For" after clicking since
        self.getting_looking = "looking for"


def run():
    app = QtGui.QApplication(sys.argv)
    gui = MyForm()
    gui.show()
    sys.exit(app.exec_())


run()
