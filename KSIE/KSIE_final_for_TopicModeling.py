import csv
import time

flag_keyword_list = []

w = open('KSIE_final_keyword_for_topicmodeling_2.csv', 'w', encoding = 'utf-8')
w.write('Review_Index,Review_Keyword,Term_Freq\n')

f = open('KSIE_final_no_overlap_keyword_6.csv', 'r')
rdr = csv.reader(f)
next(rdr)

for line in rdr:
    flag_keyword = line[0]
    flag_keyword_list.append(flag_keyword)
f.close()
print(len(flag_keyword_list))
time.sleep(3)

count = 0
f = open('KSIE_keyword.csv', 'r', encoding = 'utf-8')
rdr = csv.reader(f)
next(rdr)
for line in rdr:
    keyword = line[1]
    if keyword in flag_keyword_list:
        count += 1
        w.write(line[0] + ',' + line[1] + ',' + line[2] + '\n')
        if count%1000 == 0:
            print(count)
f.close()
w.close()
print(count)