############################################################
#                                                          #
#  Funktionalität zur Einbindung von Daten im CSV-Format   #
#                                                          #
############################################################

# Import von pythoninternen CSV Funktionen
import csv

# Globale Variablen Deklaration
csvFilePath = '../Externals/10000 Sales Records.csv'

# Lesen der CSV-Datei
with open(csvFilePath, 'r') as csvFile:
    csvReader = csv.DictReader(csvFile, delimiter=',')
    print(csvReader.fieldnames)
