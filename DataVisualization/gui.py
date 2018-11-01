############################################################
#                                                          #
#             Grundlegende GUI Funktionalität              #
#                                                          #
############################################################

from tkinter import *
from tkinter import filedialog
from DataImport import CSVImport
import webbrowser
from PIL import ImageTk, Image
import PySide2

window = Tk()
window.title('CSV Analytics')
window.state('zoomed')

csvfile = None
defaultbg = window.cget('bg')
errorbg = 'red'
successbg = 'green'


def getfile():
    """

    :return:
    """
    global csvfile
    csvfile = filedialog.askopenfilename(initialdir="../Externals", title="Select file",
                                         filetype=[("csv files", "*.csv")])
    if csvfile != '':
        popupmsgsuccess(csvfile)
        return csvfile
    else:
        popupmsgerror()


def popupmsgsuccess(e):
    """

    :return:
    """
    flash_label.config(text=e + ' geladen!', background=successbg)


def popupmsgerror():
    """

    :return:
    """
    flash_label.config(text='Keine CSV Datei ausgewählt!', background=errorbg)


def getheaders():
    """

    :return:
    """
    try:
        headers = CSVImport.getheader(csvfile)
        headers = ", ".join(headers)
        header_label.config(text=headers, background=defaultbg)
    except TypeError:
        header_label.config(text='Falsches Dateiformat ausgewählt!', background=errorbg)
    except FileNotFoundError:
        header_label.config(text='Wählen Sie eine passende CSV Datei aus!', background=errorbg)


def getMaxValue():
    """

    :return:
    """
    maxtext = CSVImport.getmaxvalue(csvfile, columnname_entry.get())
    if maxtext:
        maxValue_label.config(text=maxtext, background=defaultbg)
    else:
        maxValue_label.config(text="Die Spalte enthält keine nummerischen Werte!", background=errorbg)


def getMinValue():
    """

    :return:
    """
    mintext = CSVImport.getminvalue(csvfile, columnname_entry.get())
    if mintext:
        minValue_label.config(text=mintext, background=defaultbg)
    else:
        minValue_label.config(text="Die Spalte enthält keine nummerischen Werte!", background=errorbg)

def getAvgValue():
    """

    :return:
    """
    avgtext = CSVImport.getavgvalue(csvfile, columnname_entry.get())
    if avgtext:
        avgValue_label.config(text=avgtext, background=defaultbg)
    else:
        avgValue_label.config(text="Die Spalte enthält keine nummerischen Werte!", background=errorbg)


def getDiagramm():
    """
    Calls the CSVIm
    :return:
    """
    CSVImport.getdiagram(csvfile, columnname_entry.get())


def about():
    """
    Window to show the about infos in the menubar
    :return: nothing
    """

    def openlink():
        """
        Function to set the GitHub button on the about window and function to open GitHub link
        :return: nothing
        """
        webbrowser.open(r'https://github.com/Mashnak/DataAnalytics')

    aboutscreen = Tk()
    aboutscreen.title('About')
    aboutscreen.geometry("300x180+%d+%d" % (
        ((window.winfo_screenwidth() / 2.) - (300 / 2.)), ((window.winfo_screenheight() / 2.) - (180 / 2.))))
    about_label = Label(aboutscreen)
    about_label.config(
        text='\n\
************************\n\
Autor: Markus Schmidgall\n\
Date: 12.10.2018\n\
Version: 0.0.1\n\
************************\nGitHub: https://github.com/Mashnak/DataAnalytics\n\n')
    web_button = Button(aboutscreen, text='Öffne GitHub', command=openlink, cursor='hand2')
    about_label.pack()
    web_button.pack()


# Build the menubar
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=getfile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)

#Definition of the gui elements split into Labels and Buttons
header_label = Label(window)
flash_label = Label(window)
maxValue_label = Label(window)
minValue_label = Label(window)
avgValue_label = Label(window)
getHeaders_button = Button(window, text='Header anzeigen', command=getheaders)
getMaxValue_button = Button(window, text='Maximalwert', command=getMaxValue)
getMinValue_button = Button(window, text='Minimalwert', command=getMinValue)
getAvgValue_button = Button(window, text="Durchschnitt", command=getAvgValue)
plotColumn = Button(window, text="Diagramm", command=getDiagramm)
exit_button = Button(window, text='Beenden', command=window.quit)
columnname_entry = Entry(window)

# Packing the gui elements in the gui window element
flash_label.pack()
getHeaders_button.pack()
header_label.pack()
columnname_entry.pack()
getMaxValue_button.pack()
maxValue_label.pack()
getMinValue_button.pack()
minValue_label.pack()
getAvgValue_button.pack()
avgValue_label.pack()
plotColumn.pack()

exit_button.pack()

window.mainloop()
