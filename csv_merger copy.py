import csv
import os
import sys
from sys import exit


###########################    ###########################    ###############################

### Simple program to read in csv files and output them in output.csv in the given layout ###

###########################    ###########################    ###############################

# Some global variables
file_headers = []
col_count = 0
file_counter = 0
row_dict = {}
output_layout = ['Provider Name', 'CampaignID', 'Cost Per Ad Click', 'Redirect Link', 'Phone Number', 'Address',
                 'Zipcode']

class csv_merger:

    def has_headers(reader):

        if reader == None:
            return "reader object has null value"

        try:

            for key in reader.fieldnames:
                file_headers.append(key)

            if set(output_layout).issubset(set(file_headers)):
                return True
            else:
                print("required headers don't exist")
                return False

        except AttributeError:
            return "error: File is of invalid format"

    def merge_rows(files):

        if files == "":
            return "error: no files given"

        # reusing global variables
        global col_count
        global file_counter

        if os.path.exists("output.csv"):
            os.remove("output.csv")

        for file in files:

            try:
                # Open the current file as infile, also open outfile
                with open(file, 'r') as infile1, open(
                        "output.csv",
                        'a') as outfile:
                    reader = csv.DictReader(infile1)
                    valid_headers = csv_merger.has_headers(reader)
                    if valid_headers != True:
                        print("skippig file...")
                        break

                    writer = csv.DictWriter(outfile, fieldnames=output_layout, extrasaction="ignore")

                    # create row dictionary for valid headers
                    for field in output_layout:
                        row_dict[field] = field

                    # Keep track of files read.
                    # This will make sure headers are not written twice and can be used further for logistics, example: how many files were read?
                    if file_counter == 0:
                        writer.writerow(row_dict)
                        file_counter = +1

                    write_enable = True

                    for line in reader:
                        for key, value in line.items():
                            if value == "":
                                write_enable = False
                                print("There is an error in this line: ", list(line.values()))
                                break
                            else:
                                if '"' in value:
                                    newValue = line.get(key).replace('"', '')
                                    line[key] = newValue
                                write_enable = True

                        if write_enable is True:
                            writer.writerow(line)

            except OSError as e:
                return "error: File path is invalid"



def main():
    files = ("Homework - Auto Insurance.csv", "Homework - Home Insurance.csv")

    error = csv_merger.merge_rows(files)
    if error != None:
        print("There was an error: ", error)
        sys.exit(1)

    print("Program finished, all valid rows merged successfully")


if __name__ == "__main__":
    main()
