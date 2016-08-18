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

try:
    from getmap.getmap import GetMap
except:
    from getmap.getmap import GetMap
try:
    
    from bikeaccidents.bikeaccidents import BikeAccidents
except:
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
from enum import Enum


class UnknownTime(Enum):
    include = 1
    exclude = 2
    only = 3


# Need to add this, otherwise doesn't work
class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.setupVars()
        
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(850, 858)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacer_item = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacer_item, 4, 1, 1, 1)
        spacer_item1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacer_item1, 4, 3, 1, 3)
        self.labelTime = QtGui.QLabel(self.centralwidget)
        self.labelTime.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.labelTime.setWordWrap(True)
        self.labelTime.setObjectName(_fromUtf8("labelTime"))
        self.gridLayout.addWidget(self.labelTime, 1, 0, 1, 6)
        self.check_box_date_end = QtGui.QCheckBox(self.centralwidget)
        self.check_box_date_end.setChecked(False)
        self.check_box_date_end.setObjectName(_fromUtf8("check_box_date_end"))
        self.gridLayout.addWidget(self.check_box_date_end, 15, 2, 1, 1)
        self.check_box_day_start = QtGui.QCheckBox(self.centralwidget)
        self.check_box_day_start.setChecked(False)
        self.check_box_day_start.setObjectName(_fromUtf8("check_box_day_start"))
        self.gridLayout.addWidget(self.check_box_day_start, 5, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 7, 0, 1, 1)
        self.labelDate = QtGui.QLabel(self.centralwidget)
        self.labelDate.setWordWrap(True)
        self.labelDate.setObjectName(_fromUtf8("labelDate"))
        self.gridLayout.addWidget(self.labelDate, 8, 0, 1, 6)
        self.labelUnknownTimes = QtGui.QLabel(self.centralwidget)
        self.labelUnknownTimes.setObjectName(_fromUtf8("labelUnknownTimes"))
        self.gridLayout.addWidget(self.labelUnknownTimes, 6, 1, 1, 2)
        self.timeEditPrimary = QtGui.QTimeEdit(self.centralwidget)
        self.timeEditPrimary.setEnabled(True)
        self.timeEditPrimary.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.timeEditPrimary.setAutoFillBackground(False)
        self.timeEditPrimary.setWrapping(True)
        self.timeEditPrimary.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.timeEditPrimary.setCalendarPopup(False)
        self.timeEditPrimary.setObjectName(_fromUtf8("timeEditPrimary"))
        self.gridLayout.addWidget(self.timeEditPrimary, 4, 0, 1, 1)
        self.labelPrimaryTime = QtGui.QLabel(self.centralwidget)
        self.labelPrimaryTime.setObjectName(_fromUtf8("labelPrimaryTime"))
        self.gridLayout.addWidget(self.labelPrimaryTime, 3, 0, 1, 1)
        self.labelSecondaryTime = QtGui.QLabel(self.centralwidget)
        self.labelSecondaryTime.setObjectName(_fromUtf8("labelSecondaryTime"))
        self.gridLayout.addWidget(self.labelSecondaryTime, 3, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 6, 1, 1)
        self.datePrimary = QtGui.QDateEdit(self.centralwidget)
        self.datePrimary.setWrapping(True)
        # Setting the min/max times at start
        self.datePrimary.setDateTime(
            QtCore.QDateTime(QtCore.QDate(self.earliest_date.year, self.earliest_date.month, self.earliest_date.day),
                             QtCore.QTime(0, 0, 0)))
        self.datePrimary.setMaximumDateTime(
            QtCore.QDateTime(QtCore.QDate(self.latest_date.year, self.latest_date.month, self.latest_date.day),
                             QtCore.QTime(23, 59, 59)))
        self.datePrimary.setMinimumDateTime(
            QtCore.QDateTime(QtCore.QDate(self.earliest_date.year, self.earliest_date.month, self.earliest_date.day),
                             QtCore.QTime(0, 0, 0)))
        self.datePrimary.setCalendarPopup(False)
        self.datePrimary.setObjectName(_fromUtf8("datePrimary"))
        self.gridLayout.addWidget(self.datePrimary, 14, 0, 1, 1)
        self.check_box_day_end = QtGui.QCheckBox(self.centralwidget)
        self.check_box_day_end.setChecked(False)
        self.check_box_day_end.setObjectName(_fromUtf8("check_box_day_end"))
        self.gridLayout.addWidget(self.check_box_day_end, 5, 2, 1, 1)
        self.labelSecondaryDate = QtGui.QLabel(self.centralwidget)
        self.labelSecondaryDate.setObjectName(_fromUtf8("labelSecondaryDate"))
        self.gridLayout.addWidget(self.labelSecondaryDate, 12, 2, 1, 1)
        self.time_edit_secondary = QtGui.QTimeEdit(self.centralwidget)
        self.time_edit_secondary.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time_edit_secondary.setAutoFillBackground(False)
        self.time_edit_secondary.setWrapping(True)
        self.time_edit_secondary.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(23, 59, 0)))
        self.time_edit_secondary.setCalendarPopup(False)
        self.time_edit_secondary.setObjectName(_fromUtf8("time_edit_secondary"))
        self.gridLayout.addWidget(self.time_edit_secondary, 4, 2, 1, 1)
        self.checkBoxDateStart = QtGui.QCheckBox(self.centralwidget)
        self.checkBoxDateStart.setChecked(False)
        self.checkBoxDateStart.setObjectName(_fromUtf8("checkBoxDateStart"))
        self.gridLayout.addWidget(self.checkBoxDateStart, 15, 0, 1, 1)
        self.matplotlibMap = MatplotlibWidget(self.centralwidget)
        self.matplotlibMap.setObjectName(_fromUtf8("matplotlibMap"))
        self.gridLayout.addWidget(self.matplotlibMap, 16, 0, 1, 7)
        self.label_primary_date = QtGui.QLabel(self.centralwidget)
        self.label_primary_date.setObjectName(_fromUtf8("label_primary_date"))
        self.gridLayout.addWidget(self.label_primary_date, 12, 0, 1, 1)
        self.dateSecondary = QtGui.QDateEdit(self.centralwidget)
        self.dateSecondary.setWrapping(True)
        # Setting the min/max times at start
        self.dateSecondary.setDate(QtCore.QDate(self.latest_date.year, self.latest_date.month, self.latest_date.day))
        self.dateSecondary.setMaximumDateTime(
            QtCore.QDateTime(QtCore.QDate(self.latest_date.year, self.latest_date.month, self.latest_date.day),
                             QtCore.QTime(23, 59, 59)))
        self.dateSecondary.setMinimumDateTime(
            QtCore.QDateTime(QtCore.QDate(self.earliest_date.year, self.earliest_date.month, self.earliest_date.day),
                             QtCore.QTime(0, 0, 0)))
        self.dateSecondary.setCalendarPopup(False)
        self.dateSecondary.setObjectName(_fromUtf8("dateSecondary"))
        self.gridLayout.addWidget(self.dateSecondary, 14, 2, 1, 1)
        self.btnStart = QtGui.QPushButton(self.centralwidget)
        self.btnStart.setObjectName(_fromUtf8("btnStart"))
        self.gridLayout.addWidget(self.btnStart, 15, 6, 1, 1)
        self.comboBoxUnknownTimes = QtGui.QComboBox(self.centralwidget)
        self.comboBoxUnknownTimes.setObjectName(_fromUtf8("comboBoxUnknownTimes"))
        self.comboBoxUnknownTimes.addItem(_fromUtf8(""))
        self.comboBoxUnknownTimes.addItem(_fromUtf8(""))
        self.comboBoxUnknownTimes.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBoxUnknownTimes, 6, 0, 1, 1)
        self.spinBoxLimit = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxLimit.setMinimum(1)
        self.spinBoxLimit.setMaximum(20)
        self.spinBoxLimit.setProperty("value", 10)
        self.spinBoxLimit.setObjectName(_fromUtf8("spinBoxLimit"))
        self.gridLayout.addWidget(self.spinBoxLimit, 15, 5, 1, 1)
        self.label_spinner = QtGui.QLabel(self.centralwidget)
        self.label_spinner.setWordWrap(True)
        self.label_spinner.setObjectName(_fromUtf8("label_spinner"))
        self.gridLayout.addWidget(self.label_spinner, 14, 4, 1, 3)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.labelinfoUpdate = QtGui.QLabel(self.centralwidget)
        self.labelinfoUpdate.setWordWrap(True)
        self.labelinfoUpdate.setObjectName(_fromUtf8("labelinfoUpdate"))
        self.gridLayout.addWidget(self.labelinfoUpdate, 17, 0, 1, 5)
        self.btnResetMap = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnResetMap.setFont(font)
        self.btnResetMap.setObjectName(_fromUtf8("btnResetMap"))
        self.gridLayout.addWidget(self.btnResetMap, 17, 6, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.labelTime.setText(_translate("MainWindow",
                                          "Enter a time range. The range will include the hours and minutes between the primary time and the secondary time, unless the primary time is higher than the secondary time, where it will instead exclude the time between them.",
                                          None))
        self.check_box_date_end.setText(_translate("MainWindow", "End at the latest date", None))
        self.check_box_day_start.setText(_translate("MainWindow", "Start from the beginning of the day", None))
        self.labelDate.setText(_translate("MainWindow",
                                          "Enter a date range. The range will include the dates between the primary date and the secondary date, unless the primary date is higher than the secondary date, where it will instead exclude the dates between them.",
                                          None))
        self.labelUnknownTimes.setText(_translate("MainWindow", "include unknown times", None))
        self.timeEditPrimary.setDisplayFormat(_translate("MainWindow", "hh:mm", None))
        self.labelPrimaryTime.setText(_translate("MainWindow", "Enter the primary time", None))
        self.labelSecondaryTime.setText(_translate("MainWindow", "Enter the secondary time", None))
        self.check_box_day_end.setText(_translate("MainWindow", "Finish at the end of the day", None))
        self.labelSecondaryDate.setText(_translate("MainWindow", "Enter the secondary date", None))
        self.time_edit_secondary.setDisplayFormat(_translate("MainWindow", "hh:mm", None))
        self.checkBoxDateStart.setText(_translate("MainWindow", "Start from the earliest date", None))
        self.label_primary_date.setText(_translate("MainWindow", "Enter the primary date", None))
        self.btnStart.setText(_translate("MainWindow", "Calculate", None))
        self.comboBoxUnknownTimes.setItemText(0, _translate("MainWindow", "Do", None))
        self.comboBoxUnknownTimes.setItemText(1, _translate("MainWindow", "Do not", None))
        self.comboBoxUnknownTimes.setItemText(2, _translate("MainWindow", "Only", None))
        self.label_spinner.setText(_translate("MainWindow",
                                             "Enter a value. It will pick the top most accident prone locations given your parameters. API limits prevent too many from being displayed.",
                                             None))
        self.label.setText(_translate("MainWindow",
                                      "This program calculates and displays the most hazardous locations in Montreal for a cyclist  between certain hours of the day over a period of time.\n"
                                      "Please have a stable internet connection.", None))
        self.labelinfoUpdate.setText(_translate("MainWindow",
                                                "You are getting the locations of accidents at the times between 0:00 and 23:59, between the dates of 2006-01-01 and 2010-12-31, including the accidents without specific times",
                                                None))
        self.matplotlibMap.setAutoFillBackground(True)
        self.btnResetMap.setText(_translate("MainWindow", "Reset Map", None))
        
        self.btnStart.clicked.connect(self.calculateDataMap)
        self.btnResetMap.clicked.connect(self.getMap)
        self.btnResetMap.clicked.connect(self.change_data_parameters)
        
        self.comboBoxUnknownTimes.currentIndexChanged.connect(self.change_data_parameters)
        self.check_box_date_end.stateChanged.connect(self.change_data_parameters)
        self.checkBoxDateStart.stateChanged.connect(self.change_data_parameters)
        self.check_box_day_end.stateChanged.connect(self.change_data_parameters)
        self.check_box_day_start.stateChanged.connect(self.change_data_parameters)
        
        self.datePrimary.dateChanged.connect(self.change_data_parameters)
        self.dateSecondary.dateChanged.connect(self.change_data_parameters)
        self.timeEditPrimary.timeChanged.connect(self.change_data_parameters)
        self.time_edit_secondary.timeChanged.connect(self.change_data_parameters)
        self.spinBoxLimit.valueChanged.connect(self.change_data_parameters)
        self.btnResetMap.clicked.connect(self.resetMap)
        
        # We want to call it so the text is correct at the beginning
        self.change_data_parameters()
        
        self.getMap()
    
    def setupVars(self):
        # Sets up variables for use in program
        self.gm = GetMap()
        self.img, self.fig, self.ax, self.imgplot = self.gm.get_current_map()
        
        self.bikeAccidents = BikeAccidents()
        self.earliest_date = pd.to_datetime(self.bikeAccidents.min_date)
        self.latest_date = pd.to_datetime(self.bikeAccidents.max_date)
        self.gettingLooking = "looking for"
    
    def calculateDataMap(self):
        self.gettingLooking = "getting"
        self.change_data_parameters()
        
        # Filters out the data
        data = self.bikeAccidents.accident_range(start_time=self.timeEditPrimary.time().toString(),
                                                 end_time=self.time_edit_secondary.time().toString(),
                                                 include_unknown_time=self.includeUnknown,
                                                 start_date=self.pdate.strftime("%Y-%m-%d"),
                                                 end_date=self.sdate.strftime("%Y-%m-%d"),
                                                 )
        
        dataAccidentLocation = self.bikeAccidents.accident_count(data)  # Groups the data according to location
        self.gm.draw_accidents_by_frequency(dataAccidentLocation, self.topAccidents)
        
        self.matplotlibMap.draw()
    
    def resetMap(self):
        self.gm.resetMap()
        self.matplotlibMap.figure = self.fig
        self.matplotlibMap.draw()
    
    def getMap(self):
        self.matplotlibMap.figure = self.fig
        self.matplotlibMap.draw()
    
    def change_data_parameters(self):
        
        self.topAccidents = self.spinBoxLimit.value()
        
        # Checks if our check boxes are checked, to see if we want to use the extreme dates or not
        if (self.checkBoxDateStart.isChecked()):
            # Set up so is time date
            self.pdate = self.earliest_date
        else:
            self.pdate = pd.to_datetime(self.datePrimary.date().toString())
        
        if (self.check_box_date_end.isChecked()):
            # Set up so is time date
            self.sdate = self.latest_date
        else:
            self.sdate = pd.to_datetime(self.dateSecondary.date().toString())
        
        pdateY, pDateM, pDateD = self.pdate.year, self.pdate.month, self.pdate.day
        sdateY, sDateM, sDateD = self.sdate.year, self.sdate.month, self.sdate.day
        
        if (self.check_box_day_start.isChecked()):
            self.ptime = pd.to_datetime("0:00", format='%H:%M')
        else:
            self.ptime = pd.to_datetime(self.timeEditPrimary.time().toString())
        
        ptimeH, ptimeM = self.ptime.hour, self.ptime.minute
        if (self.check_box_day_end.isChecked()):
            self.stime = pd.to_datetime("23:59", format='%H:%M')
        else:
            self.stime = pd.to_datetime(self.time_edit_secondary.time().toString())
        
        stimeH, stimeM = self.stime.hour, self.stime.minute
        
        # We want to either get the dates between certain dates, or dates not between certain dates
        if (self.sdate >= self.pdate):
            dateBetweenText = "between"
            midDateTimeFrame = "{}-{:02d}-{:02d} and {}-{:02d}-{:02d}".format(pdateY, pDateM, pDateD, sdateY, sDateM,
                                                                              sDateD)
        else:
            dateBetweenText = "between " + self.earliest_date.strftime(
                "%Y-%m-%d") + " and " + self.latest_date.strftime("%Y-%m-%d") + ", excluding the dates between"
            midDateTimeFrame = "{}-{:02d}-{:02d} and {}-{:02d}-{:02d}".format(sdateY, sDateM, sDateD, pdateY, pDateM,
                                                                              pDateD)
        
        endText = "the accidents without specific times."
        
        if (self.comboBoxUnknownTimes.currentText() == "Only"):
            timeBetweenText = ""
            unknown_time_text = "only using"
            self.includeUnknown = UnknownTime.only
        else:
            if (self.stime >= self.ptime):
                timeBetweenText = "at the times between "
                timeBetweenText += "{}:{:02d} and {}:{:02d},".format(ptimeH, ptimeM, stimeH, stimeM)
            
            else:
                timeBetweenText = "excluding the times between "
                timeBetweenText += "{}:{:02d} and {}:{:02d},".format(stimeH, stimeM, ptimeH, ptimeM)
            
            if (self.comboBoxUnknownTimes.currentText() == "Do"):
                unknown_time_text = "including"
                self.includeUnknown = UnknownTime.include
            
            elif (self.comboBoxUnknownTimes.currentText() == "Do not"):
                unknown_time_text = "not including"
                self.includeUnknown = UnknownTime.exclude
        
        if (self.topAccidents == 1):
            self.locationText = "location"
            self.accidentText = ""
        else:
            self.locationText = "locations"
            self.accidentText = str(self.topAccidents) + " "
        
        text = "You are {gettingLooking} the top {accidentText}accident {locationText} {timeBetweenText} {dateBetweenText} {timeFrame}, {unknown_time_text} {endText}".format(
            gettingLooking=self.gettingLooking, accidentText=self.accidentText, locationText=self.locationText,
            timeBetweenText=timeBetweenText, dateBetweenText=dateBetweenText, timeFrame=midDateTimeFrame,
            unknown_time_text=unknown_time_text, endText=endText)
        
        self.labelinfoUpdate.setText(text)
        
        # Changes "Getting" to "Looking For" after clicking since
        self.gettingLooking = "looking for"


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = MyForm()
    GUI.show()
    sys.exit(app.exec_())


run()
