from tkinter import *
from DataImport import CSVImport

window = Tk()
window.title('CSV Analytics')
window.geometry('1280x1024')

csvfile = '../Externals/10000 Sales Records.csv'


def getheaders():
    header_label.config(text=CSVImport.getheader(csvfile))


header_label = Label(window)
showHeaders_button = Button(window, text='Header anzeigen', command=getheaders)
exit_button = Button(window, text='Beenden', command=window.quit)

showHeaders_button.pack()
header_label.pack()
exit_button.pack()

window.mainloop()
