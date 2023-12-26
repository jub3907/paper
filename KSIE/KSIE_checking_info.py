import csv

f = open('KSIE_review_data.csv', 'r', encoding = 'utf-8')
rdr = csv.reader(f)
next(rdr)

brand_list = []
model_list = []

for line in rdr:
    brand = line[1]
    model = line[2]
    if brand not in brand_list:
        brand_list.append(brand)
    if model not in model_list:
        model_list.append(model)
# print(brand_list)
print('--------------------------------------------------------------------------------------')
print(model_list)
f.close()