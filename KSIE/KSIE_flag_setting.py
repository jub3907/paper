import csv
import time

# reject_list = []

# f = open('KSIE_review_data.csv', 'r', encoding = 'utf-8')
# rdr = csv.reader(f)
# next(rdr)

# for line in rdr:
#     brand = line[1].lower()
#     a = brand.split(' ')
#     for i in a:
#         if i in reject_list:
#             pass
#         else:
#             reject_list.append(i)
    
# print(reject_list)
# print(len(reject_list))
# f.close()
# ----------------------------------------------------------
# a = ['nissan', 'chevrolet', 'mercedes', 'benz', 'volkswagen', 'honda', 'hyundai', 'ford', 'kia', 'toyota', 'bmw', 'convertible', 'nismo', 'coupe', 'sedan', 'altima', ' suv ', 'wagon', 'hatchback', 'murano', 'minivan', 'sentra', 'xterra', 'avalanche', 'blazer', 'supercharged', 'corvette', 'stingray', 'cruze', 'equinox', 'impala', 'malibu', 'silverado', 'suburban', 'tahoe', 'trailblazer', 'traverse', 'uplander', 'atlas', 'beetle', 'eurovan', 'jetta', 'passat', 'routan', 'tiguan', 'touareg', 'class', 'sprinter', 'ridgeline', 'crosstour', 'accord', 'civic', 'clarity', 'insight', 'odyssey', 'pilot', 'veracruz', 'veloster', 'sonata', 'tucson', 'genesis', 'tiburon', 'santa', 'accent', 'ioniq', 'azera', 'elantra', 'kona', 'victoria', 'ecoline', 'expedition', 'explorer', 'sportage', 'fiesta', 'telluride', 'focus', 'mustang', 'shelby', 'taurus', 'amanti', 'borrego', 'cadenza', 'forte', 'rondo', 'sedona', 'sorento', 'spectra', 'runner', 'alvalon', 'camry', 'solara', 'corolla', 'cruiser', 'highlander', 'matrix', 'prius', 'sequoia', 'sienna', 'tacoma', 'tundra', 'venza', 'yaris', 'turismo', 'alpina']
# b = []
# for i in a:
#     if len(i) > 4:
#         b.append(i)
# print(b)
# print(len(b))
# ----------------------------------------------------------
f = open('KSIE_row_keyword.csv', 'r', encoding = 'utf-8')
rdr = csv.reader(f)
next(rdr)

w = open('KSIE_row_keyword_1.csv', 'w', encoding = 'utf-8')
w.write('Review_Keyword,DF,TFsum,Flag\n')

reject_list = ['issue', 'till', ' yet ', ' yet', 'yet ', ' would ', ' would', 'would ', ' could ', ' could', 'could ', ' due ', 'due ', ' due', ' may ', 'may ', ' may', ' ever ', ' ever', 'ever ', ' best ', ' best', 'best ', ' like ', ' like', 'like ', ' dont ', ' dont', 'dont ', 'nissan', 'chevrolet', 'mercedes', 'benz', 'volkswagen', 'honda', 'hyundai', 'ford', 'kia', 'toyota', 'bmw', 'convertible', 'nismo', 'coupe', 'sedan', 'altima', ' suv ', 'wagon', 'hatchback', 'murano', 'minivan', 'sentra', 'xterra', 'avalanche', 'blazer', 'supercharged', 'corvette', 'stingray', 'cruze', 'equinox', 'impala', 'malibu', 'silverado', 'suburban', 'tahoe', 'trailblazer', 'traverse', 'uplander', 'atlas', 'beetle', 'eurovan', 'jetta', 'passat', 'routan', 'tiguan', 'touareg', 'class', 'sprinter', 'ridgeline', 'crosstour', 'accord', 'civic', 'clarity', 'insight', 'odyssey', 'pilot', 'veracruz', 'veloster', 'sonata', 'tucson', 'genesis', 'tiburon', 'santa', 'accent', 'ioniq', 'azera', 'elantra', 'kona', 'victoria', 'ecoline', 'expedition', 'explorer', 'sportage', 'fiesta', 'telluride', 'focus', 'mustang', 'shelby', 'taurus', 'amanti', 'borrego', 'cadenza', 'forte', 'rondo', 'sedona', 'sorento', 'spectra', 'runner', 'alvalon', 'camry', 'solara', 'corolla', 'cruiser', 'highlander', 'matrix', 'prius', 'sequoia', 'sienna', 'tacoma', 'tundra', 'venza', 'yaris', 'turismo', 'alpina']

count = 0
rejected_keyword = 0
for line in rdr:
    try:
        if line[1] == '1' or line[1] == '2' or line[1] == '3':
            rejected_keyword += 1
            pass
        else:
            keyword = line[0]
            if keyword[-2:] == 'ed':
                rejected_keyword += 1
                pass
            elif ' ' not in keyword:
                keyword = 'zzzzzzzzzz'
            else:
                for key in reject_list:
                    if key in keyword:
                        keyword = 'zzzzzzzzzz'
                if keyword == 'zzzzzzzzzz':
                    rejected_keyword += 1
                    pass
                else:
                    w.write(line[0] + ',' + line[1] + ',' + line[2] + ',' + '1' + '\n')
                    count += 1
                    if count%10000 == 0:
                        print(count)
    except:
        print('에러: {}번'.format(count))
        pass

print('총 {}개 완료\nrejected_keyword: {}개'.format(count, rejected_keyword))
f.close()
w.close()