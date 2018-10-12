############################################################
#                                                          #
#  Funktionalität zur Einbindung von Daten im CSV-Format   #
#                                                          #
############################################################

# Import von pythoninternen CSV Funktionen
import csv


# Globale Variablen Deklaration


# Lesen der CSV-Datei
def getheader(csvfilepath):
    with open(csvfilepath, 'r') as csvFile:
        csvreader = csv.DictReader(csvFile, delimiter='{')
        return csvreader.fieldnames
