import csv
import os

# Open the plain text file in append mode ('a')
with open('training_data.txt', mode='a', encoding='utf-8') as txt_file:
    # Iterate through the CSV files you want to process
    csv_files = ['assets/dms1_fixed.csv', 'assets/dms2_fixed.csv', 'assets/gc_fixed.csv']  # Add all CSV filenames here
    
    for csv_filename in csv_files:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                # Assuming the text is in the first column (index 0)
                text = row[0]  # Change this if your text is in a different column
                txt_file.write(text + "\n")  # Append each row as a new line
