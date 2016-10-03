import pymystem3

pathname_literature = "c:\HSEworkspace\Programming\Lesson 4\/anya.txt"
pathname_literature2 = "c:\HSEworkspace\Programming\Lesson 4\/test.txt"
pathname_stopwords = "c:\HSEworkspace\Programming\Lesson 4\/stopwords.txt"

with open(pathname_stopwords, 'r', encoding='utf-8') as inputfile:
    stopwords_raw = inputfile.read()
stopwords = stopwords_raw.split('\n')

with open(pathname_literature2, 'r', encoding='utf-8') as inputfile:
    all_text = inputfile.readlines()

ignore_list = ['', '\n', '.', ',', ')', '(', '/', ';', ':', '?', '!', '*', '-', '[', ']', '),', '):']
frequency = {}
stemming_object = pymystem3.Mystem()

for line in all_text:
    words = [x.strip() for x in stemming_object.lemmatize(line) if x.strip() not in ignore_list and x.strip() not in stopwords]
    # for words
    for word in words:
        if word not in frequency.keys():
            frequency[word] = 1
        else:
            frequency[word] += 1
    #for bigrams
    for i in range(1, len(words)):
        bigram = words[i-1] + " " + words[i]
        if bigram not in frequency.keys():
            frequency[bigram] = 1
        else:
            frequency[bigram] += 1


outputfile = open("c:\HSEworkspace\Programming\Lesson 4\/answer.txt", 'w', encoding='utf-8')
d = sorted(frequency.items(), key=lambda x: -x[1])
slice_number = 50
for fw in d[:slice_number]:
    print(fw)
    outputfile.write('{0}{1}{2}'.format(fw[0], ':', fw[1]))
    outputfile.write('\n')

outputfile.close()
