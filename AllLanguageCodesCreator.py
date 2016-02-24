import goslate

FileName='AvaliableLanguages.txt'

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

if __name__ == '__main__':
	AvaliableLanguages(FileName)
