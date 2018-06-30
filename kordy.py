import webbrowser
import urllib2

new=2

title = raw_input("Type in the song name...\nTitle: ")

url="http://ultimate-guitar.com/search.php?search_type=title&value="+ title +"";

webbrowser.open(url,new=new);

userInputedUrl = raw_input("Copy and past the URL here...\nURL: ")

webContents = urllib2.Request(userInputedUrl, headers={'User-Agent' : "Magic Browser"})
response = urllib2.urlopen(webContents)
song = response.read()


indexStart = song.find ("content\":\"")
indexStart = (indexStart + 10)
print indexStart

indexEnd = song.find ('\",\"revision_id')
print indexEnd
indexEnd = (indexEnd - 1)

songCut = song[indexStart:indexEnd]

songCut = songCut.replace ('[ch]', '[')
songCut = songCut.replace (r"[\/ch]", "]")
songCut = songCut.replace (r'\n', '\n')
songCut = songCut.replace (r'\r', ' ')


f = open('%s.pro' % (title), 'w')
f.write(songCut)
f.close