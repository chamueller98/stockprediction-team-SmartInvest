#defintion for reading csv files - not sure if it works but looks like a good start at the least :)
import csv

def get_file_name():
    # this func gets the name of the file to be renamed
    before_rename = open('C:/Users/my.path/before_rename.txt', 'r')
    to_be_renamed_unf = before_rename.readline()[1:]
    # remove the end CRs & LFs off of the string
    to_be_renamed = to_be_renamed_unf.strip()
    print("File name: " + to_be_renamed)
    return to_be_renamed

def get_fname():
    # get farmer name
    file_name = get_file_name()
    function not defined yet: farmer_name = re.sub('[^A-Z]', ' ', file_name).rstrip().lstrip()
    print(farmer_name)
    return farmer_name

def get_id_from_file():
    # search csv for COOP & Name to find the FID
    csvfile = 'C:/Users/my.path/csv_file_to_read_from.csv'
    # create a dictionary from the csv
    csv_dict = csv.DictReader(open(csvfile))

    fname = get_fname()
    coop_name = 'CALMAN' 
    for row in csv_dict:
        if fname in row:
            if coop_name in row:
                farmer_id = int(row['FID'])
                print(farmer_id)

get_id_from_file()

#now we should be able to have certain values that we need 
# to pass to the table in page2.html --> nested list or dictionary