# Creates "Metadata point - Column name" dictionary

file1 = open('ExoplanetDataset/Columns.txt', "r")
content = file1.readlines()
# print(content)
file1.close()

columns = {}
for col in content:
    sample = col.split()[1][:-1]
    columns[sample] = col.split()[2:]
    s = ''
    for i in range(len(columns[col.split()[1][:-1]])):
        s += columns[sample][i] + " "
    columns[sample] = s.strip()
print(columns)

# Clears the existing file.
with open("ExoplanetDataset/Exo_Rows.txt", "w") as file2:
    file2.write('')
file2.close()

with open("ExoplanetDataset/Exo_Cut.txt", "w") as file4:
    file4.write('')
file4.close()

# Separates the exoplanet data from column name metadata and forms a list with all rows as lists.
import csv
x=0
exo_row = []
with open('ExoplanetDataset/Rows.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if x == 0:
            column_metadata = row
        else:
            with open("ExoplanetDataset/Exo_Rows.txt", "a") as file2:
                file2.write(', '.join(row) + "\n")
                exo_row.append(row)
        x+=1
file2.close()
print(column_metadata)

# Chooses all characteristics needed for the final dataset.

chosen_char_num = [6, 10, 14, 18]
chosen_char = [[], [], [], []]


for i in range(len(chosen_char_num)):
    for j in range(3):
        chosen_char[i].append(column_metadata[j+chosen_char_num[i]])
print(chosen_char)

# Creates a function for better data .

def v3_to_v2_max(y, y_upper, y_lower):
    """Transforms three-value range format into two-value range format. Returns true upper value of the range. 
    
    Keyword arguments:
    y -- Middle value of the range.
    y_upper -- Distance from the middle value to the upper value of the range.
    y_lower -- Distance from the middle value to the lower value of the range.
    """
    if y == '' or y_upper == '' or y_lower == '':
        return -1
    else:
        y_max = float(y)+float(y_upper)
        return y_max

def v3_to_v2_min(y, y_upper, y_lower):
    """Transforms three-value range format into two-value range format. Returns true lower value of the range. 
    
    Keyword arguments:
    y -- Middle value of the range.
    y_upper -- Distance from the middle value to the upper value of the range.
    y_lower -- Distance from the middle value to the lower value of the range.
    """
    if y == '' or y_upper == '' or y_lower == '':
        return -1
    else:
        y_min = float(y)+float(y_lower)
        return y_min

# Forms a dataset from chosen characteristics.

exo_row_cut = []

for rownum in range(len(exo_row)):
    value = [exo_row[rownum][0]]
    for char in chosen_char_num:
        true_val_max = v3_to_v2_max(exo_row[rownum][char], exo_row[rownum][char+1], exo_row[rownum][char+2])
        true_val_min = v3_to_v2_min(exo_row[rownum][char], exo_row[rownum][char+1], exo_row[rownum][char+2])
        value.append(true_val_max)
        value.append(true_val_min)
    exo_row_cut.append(value)

    
for i in range(len(exo_row_cut)):
    s = ''
    for j in range(len(exo_row_cut[i])): 
        s += str(exo_row_cut[i][j]) + ", "   
    with open("ExoplanetDataset/Exo_Cut.txt", "a") as file4:
        file4.write(s.strip(", ")+"\n")    
file4.close()