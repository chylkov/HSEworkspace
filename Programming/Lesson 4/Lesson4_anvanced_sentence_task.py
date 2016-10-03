pathname_test = "c:\HSEworkspace\Programming\Lesson 4\/test.txt"

with open(pathname_test, 'r', encoding='utf-8') as inputfile:
    text = inputfile.read()

sentences = []
last_index = 0
for i in range(0, len(text)):
    if text[i] == '.' and text[i+1] == ' ':
        sentences.append(text[last_index: i+2])
        last_index = i + 2
    if text[i] == '.' and text[i+1].isupper():
        sentences.append(text[last_index:i+1])
        last_index = i +1
    if text[i] == '?':
        sentences.append(text[last_index: i+1])
        last_index = i + 1
    if text[i] == '!':
        sentences.append(text[last_index: i+1])
        last_index = i + 1

outputfile = open("c:\HSEworkspace\Programming\Lesson 4\/separated_sentences.txt", 'w', encoding='utf-8')
for s in sentences:
    outputfile.write(s)
    outputfile.write('\n')
outputfile.close()


print(text)
print(len(sentences))

