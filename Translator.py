import goslate

#The next three statments are for file writing purposes only

import sys
reload(sys)
sys.setdefaultencoding('utf8')

word='inner wear'
AllLanguagesFileName='AvaliableLanguages.txt'
RemoveFileName='RemoveList.txt'
translation=[]

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
		print 'Remove List Not Present'
		return []
	else:
		f.close()
		return removelist



removelist=RemoveListFile(RemoveFileName)
gs=goslate.Goslate()
language=gs.get_languages()

for i in removelist:
	if i in language.keys():
		del language[i]

for language_key in language.keys():
	translation.append(gs.translate(word,language_key))

for (j,i) in zip(language.keys(),translation):
	print language[j],i
