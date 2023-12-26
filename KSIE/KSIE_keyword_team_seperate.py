import csv

f = open('KSIE_flag_keyword_2.csv', 'r', encoding = 'utf-8')
rdr = csv.reader(f)
next(rdr)

w1 = open('KSIE_flag_keyword_2_1.csv', 'w', encoding = 'utf-8')
w2 = open('KSIE_flag_keyword_2_2.csv', 'w', encoding = 'utf-8')
w3 = open('KSIE_flag_keyword_2_3.csv', 'w', encoding = 'utf-8')
w4 = open('KSIE_flag_keyword_2_4.csv', 'w', encoding = 'utf-8')
w1.write('Review_Keyword,DF,TFsum,Flag\n')
w2.write('Review_Keyword,DF,TFsum,Flag\n')
w3.write('Review_Keyword,DF,TFsum,Flag\n')
w4.write('Review_Keyword,DF,TFsum,Flag\n')

count = 0
for line in rdr:
    if count < 4339:
        w1.write(line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + '\n')
    elif count < 8678:
        w2.write(line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + '\n')
    elif count < 13017:
        w3.write(line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + '\n')
    else:
        w4.write(line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + '\n')
    count += 1
f.close()
w1.close()
w2.close()
w3.close()
w4.close()