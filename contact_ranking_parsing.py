import re
import csv
"""
Total 13 column: 
['?色', '文本名', '代?', '重量', '部分', '作者', '?建日期', '批注',	'文本?', '?域',	'覆?率 %', '起?', '??\n']

Encoding by: big5hkscs
"""
filename = "contact_ranking.txt"
in_file = open(filename, "r", encoding="big5hkscs")

line = in_file.readline()
# print(line)

code_dict = {}
buffer = []
while line:
    str_split = re.split(r'\t+', line)
    # print(str_split)
    if len(str_split) > 1 and str_split[0] != '?色':
        # print(str_split[0])
        if str_split[0] == '●':
            # print('yes!!!')
            buffer = str_split
        else:
            buffer.extend(str_split)

        print(buffer)
        print(len(buffer))
        code_name = buffer[2]
        content = buffer[4]

        if code_name not in code_dict:
            code_dict[code_name] = list()
        code_dict[code_name].append([content])
        # print(code_dict)

        # out_file.write("\n".join(buffer))
    line = in_file.readline()

w = csv.writer(open("output.csv", "w", encoding="big5hkscs"))
for key, val in code_dict.items():
    w.writerow([key, val])
'''
dictlist = []
for key, value in code_dict.items():
    temp = [key, value]
    dictlist.append(temp)
print(dictlist)
'''
'''
with open("output.csv", "w", encoding="big5hkscs") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(code_dict.keys())
    writer.writerows(zip(*code_dict.values()))
'''
in_file.close()