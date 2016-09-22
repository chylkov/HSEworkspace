import pitchfork
import nltk.tokenize

class Album(object): # impove structure - more than one album from artist
    def __init__(self, _artist, _album):
        self.artist = _artist
        self.album = _album

    def add_review(self, r):
        self.review = r

    def add_score(self, s):
        self.score = s


music_library = []
a = Album('justin timberlake', '20/20 experience')
music_library.append(a)
a = Album('justin timberlake', 'futuresex/lovesounds')
music_library.append(a)
a = Album('shamir', 'ratchet')
music_library.append(a)
a = Album('dvsn', 'Sept. 5th')
music_library.append(a)
a = Album('frank ocean', 'blonde / endless')
music_library.append(a)
a = Album('james blake', 'The Colour in Anything')
music_library.append(a)
a = Album('macklemore / ryan lewis', 'This Unruly Mess I\'ve Made')
music_library.append(a)


for music_item in music_library:
    print(music_item.artist, '->', music_item.album, '|  status: ', end='')
    try:
        p = pitchfork.search(music_item.artist, music_item.album)
        music_item.add_review(nltk.tokenize.sent_tokenize(p.editorial()))
        music_item.add_score(p.score())
        print('FINE')
    except:
        print('WRONG')

print()
#p = pitchfork.search('justin timberlake', '20/20 experience')
#print(p.editorial())
#print(p.score())