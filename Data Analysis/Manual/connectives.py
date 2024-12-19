## search through each of the files in TBIBank 
# search each file for the list of connectives in pdtb_connectives.txt
## for each connective in a file add 1 to the count for that file
## output the counts for each file 

import os
import re
from collections import Counter

# read in the list of connectives
connectives = []
with open('pdtb_connectives.txt', 'r') as f:
    for line in f:
        connectives.append(line.strip())


# get all .txt files in a directory
def get_txt_files(directory):
    txt_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                txt_files.append(os.path.join(root, file))
    return txt_files

# specified directories
n_files = get_txt_files('TBIBank/Coelho/N')
tb_files = get_txt_files('TBIBank/Coelho/TB')

all_files = n_files + tb_files

# dictionary to store the counts
counts = {}

# search through each file for the connectives
for file in all_files:
    with open(file, 'r') as f:
        text = f.read()
        counts[file] = Counter()
        for connective in connectives:
            counts[file][connective] += len(re.findall(r'\b' + re.escape(connective) + r'\b', text))

# Output the counts
for file, count in counts.items():
    print(f'Counts for {file}:')
    for connective, cnt in count.items():
        print(f'{connective}: {cnt}')
    print()