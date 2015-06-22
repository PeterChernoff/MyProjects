from tkinter import *
# import tkMessageBox
from tkinter import ttk
import sqlite3

import matplotlib

matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
#---# <-Refers to bookmarked areas that need to be changed if I am modifying this with alternate data
class BuildGUI(Frame):
    # we are making some values that we might want to be able to change at a later date.
    # these values let us change the range which is being represented
    # The plots I am using go from 1960 to 2014, and relevent numerical information start at index 1.
    SIZE = 15
    DEFAULT_TEXT_COMBO_BOX = "No Region/Demographic Selected"
    MIN_YEAR = 1960
    MAX_YEAR = 2013
    DEFAULT_YEAR_START = 1980
    DEFAULT_YEAR_RANGE = 20
    MIN_WIDTH = 6

    #---#
    MAX_Y_TICK = 60 #Information for the highest expected values

    def __init__(self, root=None, sqlLocations=None):
        Frame.__init__(self)
        self.startYear = self.DEFAULT_YEAR_START
        self.rangeIndex = self.DEFAULT_YEAR_RANGE
        self.indexStartYear = self.startYear - (self.MIN_YEAR - 1)
        self.indexEndYear = self.MAX_YEAR - (self.MIN_YEAR - 1)

        self.sqlCDB = sqlLocations
        self.root = root
        self.cursor = self.sqlCDB.cursor() #Set up the DB.

        ####################################################
        #Sets up the variables we are going to use for the window
        self.spinVarStart = StringVar()  # spinner variable for the beginning year
        self.spinVarRange = StringVar()  # spinner value for the range of years
        self.bdVar = StringVar() #determines whether we are using birth or death
        self.errorVar = StringVar()  ##This variable is for displaying a message regarding certain range errors
        self.countryVar = StringVar() #determines what country we are using
        ####################################################

        self.root.protocol("WM_DELETE_WINDOW", self.closeWork)#Cleans things up upon completion

        self.init_window()

    def init_window(self):
        # Sets up the windows to stretch as intended
        self.root.columnconfigure(1, weight=0, pad=40)
        self.root.columnconfigure(2, weight=0, pad=40)
        self.root.columnconfigure(3, weight=1)
        self.root.rowconfigure(0, weight=0)
        self.root.rowconfigure(1, weight=0)
        self.root.rowconfigure(2, weight=0)
        self.root.rowconfigure(3, weight=0)
        self.root.rowconfigure(4, weight=0)
        self.root.rowconfigure(5, weight=0)
        self.root.rowconfigure(6, weight=0)
        self.root.rowconfigure(7, weight=0)

        ####################################################
        #Puts a little padding around the frame
        self.framePadTop = Label(self.root, height=2).grid(row=0, column=0, sticky=N)
        self.framePadLeft = Label(self.root, width=3).grid(row=0, column=0, sticky=W)
        self.framePadRight = Label(self.root, width=3).grid(row=0, column=4, sticky=E)
        self.framePadBottom = Label(self.root, height=2) #We don't insert this one just yet...
        ####################################################

        #Sets instructions
        labelInstructions = "To begin, select an option from the combobox, \npress 'Click To Start', or select a radio button."
        self.labelInstructions = Label(self.root, text=labelInstructions,
                                  justify=LEFT).grid(row=1, column=1, sticky=W+S)
        ####################################################

        #Sets the variables that will be used by the spinbox
        self.spinVarStart.set(
            str(self.DEFAULT_YEAR_START))  # sets the spinner value to the default year start (2015-06-18 sets it as 1984)
        self.spinVarRange.set(
            str(self.DEFAULT_YEAR_RANGE))  # sets the spinner value to the default year range (2015-06-18 sets it as 20)
        stringRange = "Select year and range."
        self.stringRangeLabel = Label(self.root, text=stringRange, bd='3',
                                      justify=LEFT).grid(row=3, column=2, sticky=W) #Instructions label
        ####################################################
        #sets a spinbox for the beginning year
        self.spinboxSelectStart = Spinbox(self.root, from_=self.MIN_YEAR, to=self.MAX_YEAR,
                                          textvariable=self.spinVarStart, width=4,
                                          justify=LEFT) #Creates a spinbox for the start year
        self.spinboxSelectStart.grid(row=4, column=2, sticky=W)
        ####################################################
        #creates a spinbox for a range of years to use
        self.spinboxSelectRange = Spinbox(self.root, from_=1, to=self.MAX_YEAR - self.MIN_YEAR,
                                          textvariable=self.spinVarRange, width=4,
                                          justify=LEFT)
        self.spinboxSelectRange.grid(row=5, column=2, sticky=W)
        ####################################################
        #Sets the labels for the start year and the range
        textYearRanges = "Start Year (select between %s and %s."%(self.MIN_YEAR, self.MAX_YEAR)
        self.spinLabelStart = Label(self.root, text=textYearRanges ).grid(row=4, column=2, sticky=W, padx=40)
        self.spinLabelRange = Label(self.root, text="Range.").grid(row=5, column=2, sticky=W, padx=40)
        ####################################################
        #Creates a button to activate in case you switch up the
        self.selectButton = Button(self.root, text="Click To Start", padx=2,
                                   command = self.selectStuff)
        self.selectButton.grid(row=6, column=2, sticky=W)
        ####################################################
        #Sets up an error message section, in case your year is too high, too low, or the year range
        # would cause it to go out of range
        self.errorVar.set("No Errors.")
        self.errorLabel = Label(self.root, textvariable=self.errorVar, justify=LEFT,
                                height=2, padx=2)
        self.errorLabel.grid(row=7, column=2, sticky=N+W)
        ####################################################
        #Sets instructions
        #---#
        labelText = "Select a region/demographic:"
        self.labelCountry = Label(self.root, text=labelText,
                                  justify=LEFT).grid(row=1, column=2, sticky=N+W)
        self.labelBDText = Label(self.root, text="Select birth/death")
        self.labelBDText.grid(row=2, column=1, sticky=W)
        ####################################################
        #Creates the radio buttons. I designed it to be modular so I can swap out data easily.
        self.dataInsert = []
        #---#
        self.listRB = [["Birth", "birth"], ["Death", "death"]]

        #cycles through the data provided to create the buttons
        for idxCreate, valueCreate in enumerate(self.listRB):
            radioInsert =  Radiobutton(self.root, text=valueCreate[0], variable=self.bdVar,
                                        value=valueCreate[1], command=self.selectStuff)
            radioInsert.grid(row=idxCreate+3, column=1, sticky=W)
            self.dataInsert.append(radioInsert)
        #If we don't have anything to cycle through, we still may want to go forward. In case there is only a single
        #choice, a radio button is not useful.
        try:
            idxCreate
        except NameError:
            print("Possible missing data.")
            idxCreate = 0
        self.rowCanvasLast = idxCreate + 5

        self.labelRadio = Label(self.root, height='2', width='45', anchor='w',
                                justify=LEFT)
        self.labelRadio.grid(row=idxCreate+4, column=1, sticky=W)

        #Sets the last row, the canvas row to be weight 2, so it expands while the others don't.
        if self.rowCanvasLast > 7:
            for i in range(7, self.rowCanvasLast):
                self.root.rowconfigure(i, weight=0)
            self.root.rowconfigure(i+1, weight=2)
        else:
            self.rowCanvasLast = 8
            self.root.rowconfigure(self.rowCanvasLast, weight=2)

        ####################################################
        #We can now place framePadBottom now that we know the number of rows involved
        self.root.rowconfigure(self.rowCanvasLast+1, weight=0)
        self.framePadBottom.grid(row=self.rowCanvasLast+1, column=0, sticky=S)

        ####################################################
        #Creates a combobox that calls the location when selected.
        self.comboBx = ttk.Combobox(self.root, textvariable=self.countryVar)
        self.comboBx.grid(row=2, column=2, sticky=W)
        ####################################################
        #Creates the range of regions/demographics
        #---#
        sql1 = "SELECT Country FROM birth_rate ORDER BY Country ASC"
        insertList = [self.DEFAULT_TEXT_COMBO_BOX]
        maxLength = 0
        results = []
        try:
            '''
            calls an SQL function, then arranges them alphabetically. For some strange reason
            they had curly braces, so I remove them.
            We take the value of the longest string and make it the width, so every option
            can be shown.
            '''
            self.cursor.execute(sql1)
            results = self.cursor.fetchall()
            for row in results:
                valueRow = row[0].strip('{}')
                if len(valueRow) > maxLength:
                    maxLength = len(valueRow)
                insertList.append(valueRow)
        except:
            print("Error: unable to retrieve data.")
        self.comboBx['width'] = maxLength
        self.comboBx['values'] = insertList
        # The entries are only going to be what's on the list.
        self.comboBx.state(['readonly'])
        # Select a combobox option to activate. This should be the first one.
        self.comboBx.bind('<<ComboboxSelected>>', self.selectComboBox)
        self.comboBx.current(0)


        #If the list is not empty
        if self.dataInsert:
            self.dataInsert[0].invoke()
            self.dataInsert[0].select()



    def selectComboBox(self, entry):
        #Activating the combobox
        self.selectStuff()

    def selectStuff(self):
        #What to do when an activation event has been triggered.
        self.checkRange()
        # sets the birth/death and region/demographic for our program
        selectionBD = ''

        #Sees if you have selected a region/demographic or not.
        if str(self.countryVar.get()) != self.DEFAULT_TEXT_COMBO_BOX:
            #---#
            selectionBD = "%s %ss \nper 1000 people." % (str(self.countryVar.get()), str(self.bdVar.get()))
        else:
            #---#
            selectionBD = '''Please select a region/demographic for \n%ss per 1000 people.''' % (str(self.bdVar.get()))
        self.labelRadio['text']=selectionBD
        #selectionRegion = str(self.countryVar.get())
        self.callGraph()

    def resetValues(self, checkYears, checkRanges):
        #If there is an error with the values, like someone entered a string or a decimal value, we reset them
        self.spinVarStart.set(str(checkYears))
        self.spinVarRange.set(str(checkRanges))
        self.spinboxSelectStart.config(textvariable=self.spinVarStart)
        self.spinboxSelectRange.config(textvariable=self.spinVarRange)

    def endSQL(self):
        self.sqlCDB.close()

    def checkRange(self):
        # makes sure that the values actually work
        # spinVarStart
        # spinVarRange
        checkYear = 0
        checkRange = 0
        errorString = 'No Errors'
        try:
            #Makes sure the value is properly inputted, no non-integers
            checkYear = int(self.spinVarStart.get())  # Is the data provided an integer?
            checkRange = int(self.spinVarRange.get())
        except:
            #If not, reset to default year and range
            checkYear = self.DEFAULT_YEAR_START
            checkRange = self.DEFAULT_YEAR_RANGE
            errorString = "Error: Improper Input, Resetting values."
            self.resetValues(checkYear, checkRange)  # Tells the UI to reset.
            self.errorVar.set(errorString)

        noProbsSF = True  # No Problems So Far, just for error reporting.

        if checkYear > self.MAX_YEAR:
            checkYear = self.MAX_YEAR
            errorString = "Error: Initial year too high. Resetting."
            #self.errorVar.set(errorString)
            noProbs = False
            self.resetValues(checkYear, checkRange)
        elif checkYear < self.MIN_YEAR:
            checkYear = self.MIN_YEAR
            errorString = "Error: Initial year too low. Resetting."
            #self.errorVar.set(errorString)
            noProbsSF = False
            self.resetValues(checkYear, checkRange)
        if checkYear + checkRange > self.MAX_YEAR + 1 or checkRange < 1:
            checkRange = self.MAX_YEAR + 1 - checkYear
            if noProbsSF:  # In case there is more than one problem
                errorString = "Error: Out of range. Resetting."
            else:
                errorString = errorString + "\nError: Out of range. Resetting."

        self.errorVar.set(errorString)
        self.resetValues(checkYear, checkRange)

        self.startYear = checkYear
        #Creates an index value to cycle through
        self.indexStartYear = self.startYear - (self.MIN_YEAR - 1)

        self.rangeIndex = checkRange


    def callGraph(self):
        # This calls the graph function

        graphYRate = [] #The ages that are called
        graphXYear = [] #The range of years we will use
        #graph0Values = [0] #This was meant for a possible situation where the values are empty, but currently
        #the way it's set up, the empty values default to 0 when being entered.
        #########################
        #---#
        sqlGraph = 'SELECT * FROM %s_rate WHERE Country="%s"' % (str(self.bdVar.get()), str(self.countryVar.get()))
        countryName = ''
        if str(self.countryVar.get()) != self.DEFAULT_TEXT_COMBO_BOX:
            try:
                '''
                calls an SQL function to retrieve data for graphing.
                '''
                self.cursor.execute(sqlGraph)
                resultsSQL = self.cursor.fetchall()
                convertedSQL = list(resultsSQL[0]) # converts from tuple to list.
                countryName = convertedSQL[0] #Grabs the country name

                for idx, rowSQL in enumerate(convertedSQL[self.indexStartYear:self.indexStartYear + self.rangeIndex]):
                    #
                    graphXYear.append(str(self.startYear + idx))
                    graphYRate.append(rowSQL)
            except:
                print("Error: unable to retrieve data.")
            # Working on getting the stuff to display
        #Sets up the information behind the scenes for the canvas to display the bars
        plt.clf()
        self.fig = plt.gcf()
        self.canvas = FigureCanvasTkAgg(self.fig, self.root) #Allows the Canvas to interface with the GUI
        ax = self.fig.add_subplot(111) #Allows the graph information
        #---#Sets the y axis to be between 0 and 100, marking every 5 points
        major_ticksY = np.arange(-0, self.MAX_Y_TICK, 5)
        ax.set_yticks(major_ticksY)
        #Sets the x and y axis labels.
        ax.set_xlabel('Year')
        #---#
        ax.set_ylabel("Rate (Per 1000).")


        #If there is a region/demographic selected
        if str(self.countryVar.get()) != self.DEFAULT_TEXT_COMBO_BOX:
            #sets up the range of years to be used.
            x = np.arange(len(graphXYear))
            #Sets up the bars to be used, x is the order of the bars, graphYRate is the height
            plt.bar(x, graphYRate, color='aqua', width=.8, align='center')
            plt.xticks(x, graphXYear, rotation=90) #Sets up the ticks to be used
            minWidthCheck = len(graphXYear) * .4 #Sets up a minimum width
            plt.axis([-0, self.rangeIndex, 0, self.MAX_Y_TICK]) #-#Sets up the axis limits, this case,
            plt.grid(True)
            #---#
            infoTitle = "%s \n%ss Per 1000 People \nOver A %s Year Period." % (
                countryName, str(self.rangeIndex), str(self.bdVar.get().capitalize()))
            plt.title(infoTitle)

            #---#
            #Not necessary, but it adds the exact values alongside the graph bars, stating "No data available" if there is a 0
            for idx, check0 in enumerate(graphYRate):
                if check0 == 0:
                    insertText = "No data available."
                else:
                    insertText = check0
                plt.text(idx, 5, insertText, verticalalignment='bottom',
                         horizontalalignment='center', rotation=90, fontsize=8)
            #sets the minimum value of width for the canvas
            if (minWidthCheck) < self.MIN_WIDTH: #--#If the size is less than 6
                minWidthCheck = self.MIN_WIDTH

            if len(graphXYear)!=0: #Puts a little space around bars from the x-axis
                plt.xlim([min(x) - 1, max(x) + 1])
            else:
                print("Possible data issue")
        else:
            #If there is no region/demographic selected
            minWidthCheck = self.MIN_WIDTH
            plt.xticks([ 0 ], ['No Data Selected']) #Creates no xticks
            infoTitle = "Please Select A Region/Demographic."
            plt.title(infoTitle)
            plt.axis([-0, 1, 0, self.MAX_Y_TICK])


        self.fig.set_size_inches(minWidthCheck, self.SIZE * .5) #Sets the size
        self.canvas = FigureCanvasTkAgg(self.fig, self.root) #connects the canvas to the GUI
        self.canvas.show() #Calls the information
        #Places the information on the widget
        self.canvas.get_tk_widget().grid(row=self.rowCanvasLast, column=1,sticky=W+E+N+S, columnspan=3)


    def closeWork(self): #Upon exiting, clean things up
        self.quit()
        self.destroy()

if __name__ == "__main__":
    rootB = Tk()


    rootB.title("Births/Deaths Per 1000 People Various Regions/Demographics.")
    sqlLocations = '../../AllData/SQL_BirthDeath_Rate.sqlite'
    sqlDB = sqlite3.connect(sqlLocations)

    guiBuild = BuildGUI(rootB, sqlDB)

    rootB.mainloop()
    sqlDB.close()
