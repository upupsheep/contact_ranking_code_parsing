import re
import csv
"""
- Total 13 column: 
['?色', '文本名', '代?', '重量', '部分', '作者', '?建日期', '批注',	'文本?', '?域',	'覆?率 %', '起?', '??\n']

- Encoding by: big5hkscs
"""
### Read Input File ###
filename = "contact_ranking.txt"
in_file = open(filename, "r", encoding="big5hkscs")
line = in_file.readline()
# print(line)

### Read by Line into a list ###
code_dict = {}
buffer = []
while line:
    str_split = re.split(r'\t+', line)  # Split by tab

    ### length > 1 means there's a code. ###
    ### But the first line must be excluded. ###
    if len(str_split) > 1 and str_split[0] != '?色':
        if str_split[0] == '●':
            buffer = str_split
        else:  # accedently cutted, so append it to the last list
            buffer.extend(str_split)

        print(buffer)
        print(len(buffer))
        code_name = buffer[2]
        content = buffer[4]
        ### Put the buffer into the dictionary ###
        if content not in code_dict:
            code_dict[content] = list()
        code_dict[content].append([code_name])
        # print(code_dict)

    line = in_file.readline()  # read next line

### Write the dictionary into a csv file ###
w = csv.writer(open("output1.csv", "w", encoding="big5hkscs"))
for key, val in code_dict.items():
    w.writerow([key, val])

in_file.close()