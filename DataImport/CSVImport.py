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


def getmaxvalue(csvfilepath):
    """

    :param csvfilepath:
    :return:
    """
    with open(csvfilepath, 'r') as csvFile:
        csvreader = csv.DictReader(csvFile)
        next(csvreader)
        if checkintorfloat(csvreader):
            maxvalue = max(float(column[0].replace(',', '')) for column in csvreader)
            return maxvalue
        else:
            return False


def checkintorfloat(column):
    """

    :param column:
    :return:
    """
    print(column)
    value = column
    return isinstance(value, int) or isinstance(value, float)
