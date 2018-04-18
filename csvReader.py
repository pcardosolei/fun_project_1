import csv

# Needs testing
def readCSV(file):
  with open(file,"rb") as filename:
    details = csv.DictReader(filename, delimiter=',')
    data = [r for r in details] #all the data saved as the dictionary



readCSV("/Users/PauloCardoso/desktop/P1.csv")



