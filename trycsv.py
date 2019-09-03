import csv
def get_info():
   with open('csv_stockfile.csv') as csv_file:
       csv_reader = csv.reader(csv_file, delimiter=',')
       return list(csv_reader)