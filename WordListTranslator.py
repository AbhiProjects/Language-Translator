import goslate

#The next three statments are for file writing purposes only

import sys
reload(sys)
sys.setdefaultencoding('utf8')

AllLanguagesFileName='AvaliableLanguages.txt'
RemoveFileName='RemoveList.txt'
tempFileName='WordList.txt'
TranslationList=[]

"""
FileName : Name Of The File Where All Languages Will Be Stored 
Stores All The Avaliable Languages In The File
"""
def AvaliableLanguages(FileName):

	gs=goslate.Goslate()
	language=gs.get_languages()

	f = open(FileName,'w')
	for language_key in language.keys():
		t=language_key+' '+language[language_key]+'\n'
		f.write(t)
	f.close()

"""
FileName: Name of The File From Where Language Keys Of The Different Languages Will Be Exported To be Removed
Returns A List of Language Keys Which Will Be Removed From The Language Dictionary  
"""	
def RemoveListFile(FileName):
	
	removelist=[]

	try:
		f = open(FileName,'r')
		for line in f.read().split('\n'):
    			removelist.append(line)
	except:
		print FileName,' Not Present'
		return []
	else:
		f.close()
		return removelist


wordlist=RemoveListFile(tempFileName)
wordlist.remove('')
removelist=RemoveListFile(RemoveFileName)
gs=goslate.Goslate()
language=gs.get_languages()

for i in removelist:
	if i in language.keys():
		del language[i]

for word in wordlist:

	print 'Translating ',word,'......'
	translation=[]
	
	for language_key in language.keys():
		translation.append(gs.translate(word,language_key))
	TranslationList.append(translation)


for (w,translation) in zip(wordlist,TranslationList):
	
	print w
	
	for (j,i) in zip(language.keys(),translation):
		print language[j],
		print i
	print

