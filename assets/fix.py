import csv

inputfile = 'assets/dms2.csv'
outputfile = 'assets/dms2_fixed.csv'

with open(inputfile, 'r', encoding = 'utf-8') as infile:
    reader = csv.DictReader(infile)
    fieldnames = ['content']
    
    with open(outputfile, mode = 'w', newline = '', encoding = 'utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames = fieldnames)
        writer.writeheader()
        
        for row in reader:
            content = row['content']
            
            if content.strip() == "" or content.lower().startswith('http'):
                continue
            writer.writerow({'content': row['content']})
print('Done')