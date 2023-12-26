import csv
from nltk.stem import WordNetLemmatizer

count = 0

f = open('KSIE_beforestemming_1.csv', 'r', encoding = 'UTF-8')
rdr = csv.reader(f)
next(rdr)

w = open('KSIE_afterLemmatizing_1.csv', 'w', encoding = 'UTF-8') 
w.write('index,keyword,term_freq\n')

for line in rdr:
   try:
      count += 1
      lematizer = WordNetLemmatizer()
      lemmas = [lematizer.lemmatize(token) for token in line]
      w.write(str(lemmas[0]) + ',' + str(lemmas[1]) + ',' + str(lemmas[2]) + "\n")
      if count%1000 == 0:
         print(count)
   except:
      pass

f.close()
w.close()
#---------------------------------------------------------------------------------
f = open('KSIE_beforestemming_2.csv', 'r', encoding = 'UTF-8')
rdr = csv.reader(f)
next(rdr)

w = open('KSIE_afterLemmatizing_2.csv', 'w', encoding = 'UTF-8') 
w.write('index,keyword,term_freq\n')

for line in rdr:
   try:
      count += 1
      lematizer = WordNetLemmatizer()
      lemmas = [lematizer.lemmatize(token) for token in line]
      w.write(str(lemmas[0]) + ',' + str(lemmas[1]) + ',' + str(lemmas[2]) + "\n")
      if count%1000 == 0:
         print(count)
   except:
      pass

f.close()
w.close()
#---------------------------------------------------------------------------------
f = open('KSIE_beforestemming_3.csv', 'r', encoding = 'UTF-8')
rdr = csv.reader(f)
next(rdr)

w = open('KSIE_afterLemmatizing_3.csv', 'w', encoding = 'UTF-8') 
w.write('index,keyword,term_freq\n')

for line in rdr:
   try:
      count += 1
      lematizer = WordNetLemmatizer()
      lemmas = [lematizer.lemmatize(token) for token in line]
      w.write(str(lemmas[0]) + ',' + str(lemmas[1]) + ',' + str(lemmas[2]) + "\n")
      if count%1000 == 0:
         print(count)
   except:
      pass

f.close()
w.close()
#---------------------------------------------------------------------------------
f = open('KSIE_beforestemming_4.csv', 'r', encoding = 'UTF-8')
rdr = csv.reader(f)
next(rdr)

w = open('KSIE_afterLemmatizing_4.csv', 'w', encoding = 'UTF-8') 
w.write('index,keyword,term_freq\n')

for line in rdr:
   try:
      count += 1
      lematizer = WordNetLemmatizer()
      lemmas = [lematizer.lemmatize(token) for token in line]
      w.write(str(lemmas[0]) + ',' + str(lemmas[1]) + ',' + str(lemmas[2]) + "\n")
      if count%1000 == 0:
         print(count)
   except:
      pass
f.close()
w.close()
#---------------------------------------------------------------------------------
f = open('KSIE_beforestemming_5.csv', 'r', encoding = 'UTF-8')
rdr = csv.reader(f)
next(rdr)

w = open('KSIE_afterLemmatizing_5.csv', 'w', encoding = 'UTF-8') 
w.write('index,keyword,term_freq\n')

for line in rdr:
   try:
      count += 1
      lematizer = WordNetLemmatizer()
      lemmas = [lematizer.lemmatize(token) for token in line]
      w.write(str(lemmas[0]) + ',' + str(lemmas[1]) + ',' + str(lemmas[2]) + "\n")
      if count%1000 == 0:
         print(count)
   except:
      pass

f.close()
w.close()

print(count)
# keywork 총 갯수 = 1288595