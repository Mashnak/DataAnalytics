############################################################
#                                                          #
#  Funktionalität zur Einbindung von Daten im CSV-Format   #
#                                                          #
############################################################

# Import von pythoninternen CSV Funktionen
import csv


# Lesen der CSV-Datei
def getheader(csvfilepath):
    """

    :param csvfilepath:
    :return:
    """
    with open(csvfilepath, 'r') as csvFile:
        csvreader = csv.DictReader(csvFile, delimiter=',')
        returnstring = ', '.join(csvreader.fieldnames)
        return returnstring


def getmaxvalue(csvfilepath, columnname):
    """

    :param csvfilepath:
    :param columnname:
    :return:
    """
    if columnname is '':
        return False
    with open(csvfilepath, 'r') as csvFile:
        csvreader = csv.DictReader(csvFile)
        next(csvreader)
        try:
            answer = max(csvreader, key=lambda column: int(column[columnname].replace(',', '')))
            return answer
        except ValueError:
            return False


def getavgvalue(csvfilepath, columnname):
    """

    :param csvfilepath:
    :param columnname:
    :return:
    """
    if columnname is '':
        return False
    with open(csvfilepath, 'r') as csvFile:
        csvreader = csv.DictReader(csvFile)
        next(csvreader)
        try:
            answer = 0

            return answer
        except ValueError:
            return False
