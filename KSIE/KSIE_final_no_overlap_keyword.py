import csv

f = open('KSIE_final_no_overlap_keyword_5.csv', 'r', encoding = 'utf-8')
rdr = csv.reader(f)
next(rdr)

# delete_list_1 = ['problems', 'car', 'vehicle', 'miss', 'point', 'cars', 'rogue', 'camry', 'gti', 'bit', 'lot', 'jetta', 'crv', 'end', 'equinox', 'lots', 'bed', 'pilot', 'home', 'cr v', 'week', 'rust', 'hood', 'kids', 'passat', 'people', 'rav', 'maxima', 'volt', 'junk', 'experience', 'month', 'nice car', 'jeep', 'piece', 'city', 'dealers', 'soul', 'lemon', 'superior', 'dealership', 'sun', 'forte', 'old', 'age', 'right', 'lots', 'wagon', 'trans', 'great vehicle', 'rabbit', 'rev', 'noticed', 'hit', 'glk', 'golf', 'honda accord', 'leaf', 'needs', 'another one', 'superb', 'aware', 'lincoln', 'great value', 'luxury car', 'month', 'smile', 'people', 'fact', 'new truck', 'suburban', 'first car', 'onstar', 'happen', 'good vehicle', 'bit', 'touareg', 'accent', 'tdi', 'winner', 'tons', 'rio', 'red', 'reach', 'one problem', 'couple', 'noticed', 'cube', 'excellent car', 'best car', 'best vehicle', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
delete_list_2 = ['van', 'need', 'great car', 'comfort', 'time', 'way', 'truck', 'better', 'warranty', 'quality', 'accord', 'snow', 'leather', 'trucks', 'suv', 'reliable', 'vehicles', 'park', 'winter', 'drives', '']

w = open('KSIE_final_no_overlap_keyword_6.csv', 'w', encoding = 'utf-8')
w.write('Review_Keyword,TFsum,DF,Flag\n')

count = 0
for line in rdr:
    keyword = line[0]
    if keyword in delete_list_1:
        continue
    else:
        count += 1
        w.write(line[0] + ',' + line[1] + ',' + line[2] + ',' + '1' + '\n')
f.close()
w.close()
print(count)