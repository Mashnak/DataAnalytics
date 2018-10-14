############################################################
#                                                          #
#  Funktionalität zur Einbindung von Daten im CSV-Format   #
#                                                          #
############################################################

# Import von pythoninternen CSV Funktionen
import pandas as pd

# Lesen der CSV-Datei
def getheader(csvfilepath):
    """

    :param csvfilepath:
    :return:
    """
    data = pd.read_csv(csvfilepath)
    return list(data)


def getmaxvalue(csvfilepath, columnname):
    """

    :param csvfilepath:
    :param columnname:
    :return:
    """
    if columnname is '':
        return False
    data = pd.read_csv(csvfilepath)
    try:
        return data[columnname].max()
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
    data = pd.read_csv(csvfilepath)
    try:
        return data[columnname].mean()
    except ValueError:
        return False
