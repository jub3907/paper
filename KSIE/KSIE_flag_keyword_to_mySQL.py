import csv
# import pymysql

# keyword_list = []
# f = open('KSIE_flag_keyword_10.csv', 'r')
# rdr = csv.reader(f)
# next(rdr)

# w = open('KSIE_flag_keyword_11.csv', 'w', encoding = 'utf-8')
# w.write('Review_Keyword,DF,TFsum,Flag\n')

# reject_list = ['traction control', 'nav system', 'blind spots', 'spare tire', 'apple carplay', 'heated steering wheel', 'door handle', 'little car', 'big car', 'entertainment system', 'adaptive cruise control', 'long run', 'perfect vehicle', 'put gas', 'service center', 'quality control', 'comfortable inside', 'regular gas', 'electric range', 'full charge', 'company car', 'tire rotations', 'door handles', 'michelin tires', 'infotainment system', 'timing chain', 'negative reviews', 'many options', 'german engineering', 'extremely quiet', ]
# # reject_2 = 'space'
# not_reject_1 = ['power memory seats', 'power seat', 'seat heaters', 'auto seats', 'electric seats', 'electric seat adjustment', 'power adjustable seats']
# not_reject_2 = ['interior design', 'exterior design', 'led interior lights', 'interior size', 'interior noises']

# count1 = 0
# count2 = 0
# for line in rdr:
#     keyword = line[0]
#     if line[3] != '1':
#         count1 += 1
#         continue
#     else:
#         if keyword in keyword_list:
#             count1 += 1
#             continue
#         else:
#             keyword_list.append(keyword)
#             count2 += 1
#             w.write(line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + '\n')
# f.close()
# w.close()
# print(count1, count2)

# --------------------------------------------------------------

flag_keyword_list = []

w = open('KSIE_final_keyword_for_topicmodeling_1.csv', 'w', encoding = 'utf-8')
w.write('Review_Index,Review_Keyword,Term_Freq\n')

f = open('KSIE_final_no_overlap_keyword_5.csv', 'r')
rdr = csv.reader(f)
next(rdr)

for line in rdr:
    flag_keyword = line[0]
    flag_keyword_list.append(flag_keyword)
f.close()
print(len(flag_keyword_list))

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

# --------------------------------------

# db = pymysql.connect(host = "127.0.0.1", user = "root", password = "6836", db = "ksie", charset = "utf8mb4")
# cursor = db.cursor()
# count = 0
# f = open('KSIE_flag_keyword_4.csv', 'r', encoding = 'utf-8')
# rdr = csv.reader(f)
# next(rdr)
# for line in rdr:
#     if line[3] == '1':
#         try:
#             cursor.execute("INSERT INTO ksie_flag_keyword values (%s, %s, %s, %s);", (line[0],line[1],line[2],line[3]))
#             db.commit()
#             count += 1
#             if count%100 == 0:
#                 print(count)
#         except:
#             pass
# f.close()
# print(count)

