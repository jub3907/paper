import csv

f = open('KSIE_keyword_for_topicmodeling_8.csv', 'r', encoding = 'utf-8')
rdr = csv.reader(f)
next(rdr)

w = open('KSIE_keyword_for_topicmodeling_9.csv', 'w', encoding = 'utf-8')
w.write('Review_Index,Review_Keyword,Term_Freq\n')

# reject_keyword = ['leather seats', 'little car', 'big car', 'adaptive cruise control', 'apple carplay']
count = 0
for line in rdr:
    count += 1
    keyword = line[1]
    if keyword == 'little car':
        pass
    else:
        w.write(line[0] + ',' + line[1] + ',' + line[2] + '\n')
    if count%100 == 0:
        print(count)
f.close()
w.close()