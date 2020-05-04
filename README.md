# The_Zebra-_Assignment


CONTENTS OF THIS FILE
------------------------------------
# Introduction
#How to run
#How to Run Unit Test

#Input files:
#Homework - Auto Insurance.csv
#Homework - Home Insurance.csv

#Instructions



Introduction:
This program is written uses Python version 3.7. To run this program, Pycharm or any Python compatiable IDE can be used.
Given multiple csv files, this program checks to see if the required headers are present in each file. If the headers are present, an output csv file is written with the required header field and corresponding values picked from each file. The file names would need to be updated in the main program as needed.


How to Run 
1. Clone git repo: https://github.com/ravimalide/The_Zebra-_Assignment_1-
2. Run Unit_Test.py to make sure all tests pass
3. Run csv_merge.py file
4. output.csv will contain final files with headers

Follow following steps To Run set of files 
1. Update the output_layout to columns as per requirment 
2. Update input file name in files variable
3. update output file name and location as needed
4. Run the csv_merge.py file 
5. Error lines will be shown on the screen 
6. output.csv will contain final rows from each read file with output schema


Output Schema:

1. Provider Name--Type: String, Non Nullable
2. CampaignID --Type: String, Non Nullable
3. Cost Per Ad Click -- Type: Float , Non Nullable
4. Redirect Link --Type: Float , Non Nullable
5. Phone Number --Type: Float , Nullable
6. Address --- Type: Float , Non Nullable
7. Zipcode -- Type: Float , Non Nullable

How to Run Unit Test:
open Unit_Test.py set up the (virtual) environment to use python 3.7
run Unit_Test.py


Future enhancement:
1. The output schema can be prompted to the user as an option to be defined
2. Program can automatically scan csv files in the working directory (recursively) to merge
3. Python Pandas library uses Parquet file format that can be used to convert csv files that have valid headers to parquet. Parquet uses column hashmapping for data arithmetic vs the traditional row by row transactions which consumes more time and memory. This can allow faster merging for output files. More research would be needed to implement this fully