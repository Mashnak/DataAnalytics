############################################################
#                                                          #
#  Funktionalität zur Einbindung von Daten im CSV-Format   #
#                                                          #
############################################################

# Import von pythoninternen CSV Funktionen
import pandas as pd
import matplotlib.pyplot as plt


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
        maxvalue = data[columnname].max()
        # Fixing the if statement to see if maxvalue is a string or not
        if maxvalue is int:
            return maxvalue
        else:
            return False
    except ValueError:
        return False

def getminvalue(csvfilepath, columnname):
    """

    :param csvfilepath:
    :param columnname:
    :return:
    """
    if columnname is '':
        return False
    data = pd.read_csv(csvfilepath)
    try:
        minvalue = data[columnname].min()
        # Fixing the if statement to see if minvalue is a string or not
        if minvalue is int:
            return minvalue
        else:
            return False
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
        meanvalue = data[columnname].mean()
        if meanvalue is int:
            return meanvalue
        else:
            return False
    except TypeError:
        return False


def getdiagram(csvfilepatch, columnname):
    """

    :param csvfilepatch:
    :param columnname:
    :return:
    """
    if columnname is '':
        return False
    data = pd.read_csv(csvfilepatch)
    try:
        x = data[columnname]
        y = data.index.values
        plt.plot(y, x)
        plt.show()
    except ValueError:
        print('False')
        return False
