import os
import webbrowser
import urllib2



#print  '********************************************************************************\n********************************************************************************\n********************************************************************************\n********************************************************************************'
print  '________________________________________________________________________________'
print  '________________________________________________________________________________'
print  '___________________________________KORDY________________________________________'
print  '_______________________________Kyle Schneider___________________________________'
print  '________________________________________________________________________________'
print  '________________________________________________________________________________'


# Opens a web browser with the search results for the song using ultimate-guitar.com/
new=2

title = raw_input("Type in the song name...\nTitle: ")

url="http://ultimate-guitar.com/search.php?search_type=title&value="+ title +"";

webbrowser.open(url,new=new);

# Asks the user to copy the URL from the we browser and paste it in the input field.
# Extrapolates the data printed on the screen and concatinates the string.
# Removes the line breaks.
# Puts brakets around the chords.

print '\n'

userInputedUrl = raw_input("Copy and past the URL here...\nURL: ")

webContents = urllib2.Request(userInputedUrl, headers={'User-Agent' : "Magic Browser"})
response = urllib2.urlopen(webContents)
song = response.read()


indexStart = song.find ("content\":\"")
indexStart = (indexStart + 10)
#print indexStart

indexEnd = song.find ('\",\"revision_id')
#print indexEnd
indexEnd = (indexEnd - 1)

songCut = song[indexStart:indexEnd]

songCut = songCut.replace ('[ch]', '[')
songCut = songCut.replace (r"[\/ch]", "]")
songCut = songCut.replace (r'\n', '\n')
songCut = songCut.replace (r'\r', ' ')

# Extrapolates the song titles and the artist bassed on the URL that was pasted.

# Extrapolates artist name.
titleAndArtist = userInputedUrl[37:len(userInputedUrl)]
print titleAndArtist
Index = titleAndArtist.find ('/')
songArtist = titleAndArtist[0:(Index)]
songArtist = songArtist.replace ('_', ' ')
songArtist = songArtist.title()
print ('Artist: %s' %songArtist)

# Extrapolates the song title.
endOfTitle = titleAndArtist.find ('_chords_')
songTitle = titleAndArtist[(Index+1):(endOfTitle)]
songTitle = songTitle.replace ('_', ' ')
songTitle = songTitle.title()
print ('Title: %s' %songTitle)


# Injects the song title and artist name into the song using chordPro formating.

songCut = ('\173title: %s\175\n\173artist: %s\175\n%s' % (songTitle, songArtist, songCut))



# This will change the "current working directory" to a folder called "Kordy" in the user documents folder.
# If this folder does not. exist, it will be created.

path = os.path.expanduser('~/Documents')

folder = os.path.isdir(path+'/Kordy')
if folder == True:
	print 'folder \'Kordy\' exists in the user documents folder'
else:
	os.makedirs(path+'/Kordy')
	print 'Folder \'Kordy\' has been created in the user documents folder'
os.chdir (path+"/Kordy")

directory = os.getcwd()
print directory

# Creates a document named the title of the song.
# The format of the title will be changed to capitalize the first letter of every word.
# The file will be saved as a ChordPro file, suffix is ".pro".

f = open('%s.pro' % (songTitle), 'w')
f.write(songCut)
f.close






