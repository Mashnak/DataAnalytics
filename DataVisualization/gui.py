from tkinter import *
from tkinter import filedialog
from DataImport import CSVImport

window = Tk()
window.title('CSV Analytics')
window.geometry('1280x1024')
NORM_FONT = ("Verdana", 10)

csvfile = None


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
    popup = Tk()
    popup.wm_title("!")
    label = Label(popup, text='File geladen!', font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    b1 = Button(popup, text="Okay", command=popup.destroy)
    b1.pack()


def popupmsgfail(e):
    popup = Tk()
    popup.wm_title("!")
    label = Label(popup, text=e, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    b1 = Button(popup, text="Okay", command=popup.destroy)
    b1.pack()


def getheaders():
    try:
        header_label.config(text=CSVImport.getheader(csvfile))
    except TypeError:
        header_label.config(text='Erst CSV Datei auswählen!')


header_label = Label(window)
showHeaders_button = Button(window, text='Header anzeigen', command=getheaders)
getfile_button = Button(window, text='CSV Datei', command=callback)
exit_button = Button(window, text='Beenden', command=window.quit)

getfile_button.pack()
showHeaders_button.pack()
header_label.pack()
exit_button.pack()

window.mainloop()
