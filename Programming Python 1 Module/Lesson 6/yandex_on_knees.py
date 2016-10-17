path = 'c:\\HSEWorkspace\\Programming\\Lesson 6\\20ng-test-stemmed.txt'
topics = {}

with open(path, 'r') as inputfile:
    lines = inputfile.readlines()

for line in lines:
    topic_name = line.split('\t')[0]
    if topic_name not in topics:
        topics[topic_name] = []
    topics[topic_name] += line.split('\t')[1].split(' ')

freq_dict = {}
for topic in topics:
    temp = {}
    for word in topics[topic]:
        if word in temp:
            temp[word] += 1
        else:
            temp[word] = 1
    freq_dict[topic] = temp


count_topics = len(topics)
freq_tf_idf = {}

word_idf = {}
for topic_name in topics:
    for word in topics[topic_name]:
        if word in word_idf:
            word_idf[word].add(topic_name)
        else:
            word_idf[word] = set([topic_name])

for topic in freq_dict:
    temp = {}
    for word in freq_dict[topic]:
        temp[word] = freq_dict[topic][word] * count_topics / (1 + len(word_idf[word]))
    freq_tf_idf[topic] = temp

import operator
for topic in freq_tf_idf:
    print(topic)
    s = sorted(freq_tf_idf[topic].items(), key=operator.itemgetter(1), reverse=True)
    print(s[:10])

from scipy import spatial
query = 'armenian people muslim about orbit and vitamin turkish you forsale it and pray for ploygon in jpeg hiv gif imag'
query_list = query.split(' ')
query_vector = [1]*len(query_list)
dictances = {}
data_vector = []
for topic in freq_tf_idf:
    data_vector = []
    for w in query_list:
        if w in freq_tf_idf[topic]:
            data_vector.append(1)
        else:
            data_vector.append(0)
    dictances[topic] = 1 - spatial.distance.cosine(data_vector, query_vector) #грязный хак

print(sorted(dictances.items(), key=operator.itemgetter(1), reverse=True))

#чтобы улучшить поиск, надо убирать стоп-слова
# также можно читать idf-меру в приходящем запросе, тогда вектор будет состоять не из 0 и 1, а из tfidf величин