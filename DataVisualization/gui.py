from tkinter import *
from tkinter import filedialog
from DataImport import CSVImport

window = Tk()
window.title('CSV Analytics')
window.geometry("800x600+%d+%d" % (
    ((window.winfo_screenwidth() / 2.) - (800 / 2.)), ((window.winfo_screenheight() / 2.) - (600 / 2.))))
NORM_FONT = ("Verdana", 10)

csvfile = None
defaultbg = window.cget('bg')


def callback():
    global csvfile
    try:
        name = filedialog.askopenfilename(initialdir="Externals", title="Select file",
                                          filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        popupmsgsuccess()
        csvfile = name
        print(name)
        return name
    except IOError as e:
        popupmsgfail(e)


def popupmsgsuccess():
    flash_label.config(text='CSV Datei geladen!', background='green')


def popupmsgfail(e):
    flash_label.config(text=e, background='red')


def getheaders():
    try:
        headers = CSVImport.getheader(csvfile)
        header_label.config(text=headers, background=defaultbg, wraplengt=200)
    except TypeError:
        header_label.config(text='Erst CSV Datei auswählen!', background='red')

def donothing():
    x=0;


menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

window.config(menu=menubar)

header_label = Label(window)
flash_label = Label(window)
showHeaders_button = Button(window, text='Header anzeigen', command=getheaders)
getfile_button = Button(window, text='CSV Datei', command=callback)
exit_button = Button(window, text='Beenden', command=window.quit)

getfile_button.pack()
flash_label.pack()
showHeaders_button.pack()
header_label.pack()

exit_button.pack()

window.mainloop()
