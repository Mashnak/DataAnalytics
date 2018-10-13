############################################################
#                                                          #
#             Grundlegende GUI Funktionalität              #
#                                                          #
############################################################

from tkinter import *
from tkinter import filedialog
from DataImport import CSVImport
import webbrowser

window = Tk()
window.title('CSV Analytics')

window.geometry("800x600+%d+%d" % (
    ((window.winfo_screenwidth() / 2.) - (800 / 2.)), ((window.winfo_screenheight() / 2.) - (600 / 2.))))

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
        print(csvfile)
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
        header_label.config(text=headers, background=defaultbg, wraplengt=800)
    except TypeError:
        header_label.config(text='Falsches Dateiformat ausgewählt!', background=errorbg)
    except FileNotFoundError:
        header_label.config(text='Wählen Sie eine passende CSV Datei aus!', background=errorbg)


def getMaxValue():
    if CSVImport.getmaxvalue:
        maxValue_label.config(text=CSVImport.getmaxvalue(csvfile))
    else:
        maxValue_label.config(text="Die Spalte enthält keine nummerischen Werte!", background=errorbg)


def about():
    """

    :return:
    """

    def openlink():
        """

        :return:
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


def donothing():
    x = 0


menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=getfile)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)

header_label = Label(window)
flash_label = Label(window)
maxValue_label = Label(window)
getHeaders_button = Button(window, text='Header anzeigen', command=getheaders)
getMaxValue_button = Button(window, text='Maximalwert', command=getMaxValue)
exit_button = Button(window, text='Beenden', command=window.quit)

flash_label.pack()
getHeaders_button.pack()
header_label.pack()
getMaxValue_button.pack()
maxValue_label.pack()
exit_button.pack()

window.mainloop()
