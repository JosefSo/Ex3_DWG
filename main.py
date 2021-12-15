import csv
import json
from CallForElevator import CallForElevator
from Building import Building

if __name__ == '__main__':

    """ --------- Get csv to calls ------------ """
    rows = []
    calls = []
    with open("Calls_a.csv") as file:
        csvreader =csv.reader(file)
        for row in csvreader:
            o=CallForElevator(name=row[0], time=row[1], src=row[2], dst=row[3], x=0, allc=0)
            calls.append(o)
            rows.append(row)
    print(calls[1].time)
    print(calls)

    """ --------- Get json to building ------------ """



