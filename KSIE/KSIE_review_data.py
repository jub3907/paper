import csv

f = open('KSIE_review_data.csv', 'r', encoding = 'utf-8')
rdr = csv.reader(f)
next(rdr)

w1 = open('KSIE_review_1.csv', 'w', encoding = 'utf-8')
w2 = open('KSIE_review_2.csv', 'w', encoding = 'utf-8')
w3 = open('KSIE_review_3.csv', 'w', encoding = 'utf-8')
w4 = open('KSIE_review_4.csv', 'w', encoding = 'utf-8')
w5 = open('KSIE_review_5.csv', 'w', encoding = 'utf-8')
w1.write('index,brand,model,year,month,day,review\n')
w2.write('index,brand,model,year,month,day,review\n')
w3.write('index,brand,model,year,month,day,review\n')
w4.write('index,brand,model,year,month,day,review\n')
w5.write('index,brand,model,year,month,day,review\n')

count = 0
for line in rdr:
    count += 1

    index = line[0]
    brand = line[1]
    model = line[2]
    year = line[3]
    month = line[4]
    day = line[5]
    review = line[6]

    if int(index) <= 20000:
        w1.write(index + ',' + brand + ',' + model + ',' + year + ',' + month + ',' + day + ',' + review + '\n')
    elif int(index) <= 40000:
        w2.write(index + ',' + brand + ',' + model + ',' + year + ',' + month + ',' + day + ',' + review + '\n')    
    elif int(index) <= 60000:
        w3.write(index + ',' + brand + ',' + model + ',' + year + ',' + month + ',' + day + ',' + review + '\n')
    elif int(index) <= 80000:
        w4.write(index + ',' + brand + ',' + model + ',' + year + ',' + month + ',' + day + ',' + review + '\n')
    else:
        w5.write(index + ',' + brand + ',' + model + ',' + year + ',' + month + ',' + day + ',' + review + '\n')
    
    if count%10000 == 0:
        print(count)

print(count)

f.close()
w1.close()
w2.close()
w3.close()
w4.close()
w5.close()
# review 총 갯수 = 96393