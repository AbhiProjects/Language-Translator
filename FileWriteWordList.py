import goslate

#The next three statments are for file writing purposes only

import sys
reload(sys)
sys.setdefaultencoding('utf8')

WORD=''
AllLanguagesFileName='AvaliableLanguages.txt'
RemoveFileName='RemoveList.txt'
WordListFileName='WordList.txt'

"""
removelist: List of all language codes whose translation is not done 
Returns A list of all the avalibale language codes in which translation will be done 
"""
def AvaliableLanguages(removelist):

	gs=goslate.Goslate()
	language=gs.get_languages()

	for i in removelist:
		if i in language.keys():
			del language[i]

	return language

"""
FileName: Name of The File From Where Language Keys Of The Different Languages Will Be Exported To be Removed
Returns A List of Language Keys Which Will Be Removed From The Language Dictionary  
"""	
def FileReader(FileName):
	
	temp=[]

	try:
		f = open(FileName,'r')
		for line in f.read().split('\n'):
    			temp.append(line)
	except:
		print FileName,' Not Present'
		return []
	else:
		f.close()
		return temp

"""
wordlist: The list of words to be translated
language: The list of language codes in which translation will take place
Returns A list of all the translation
"""
def TranslationProcess(wordlist,language):
	
	gs=goslate.Goslate()
	TranslationList=[]
	
	for word in wordlist:

		print 'Translating ',word,'......'
		translation=[]
	
		for language_key in language.keys():
			translation.append(gs.translate(word,language_key))
		
		TranslationList.append(translation)

	return TranslationList


"""
wordlist: The list of words to be translated
TranslationList: The list of translations to be written to file
Creates a file named temp.txt where all translations are stored
"""
def FileWrite(wordlist,TranslationList):
	
	f=open('temp.txt','a+')
	
	for (w,translation) in zip(wordlist,TranslationList):
	
		f.write(w)
		f.write('\n')
	
		for i in translation:		
			f.write(i)
			f.write('\n')

		f.write('\n')
	
	f.close()

"""
wordlist: The list of words to be translated
TranslationList: The list of translations to be written to file
Prints all the translations in the terminal window
"""
def PrintInTerminal(wordlist,TranslationList):

	for (w,translation) in zip(wordlist,TranslationList):
		print w
	
		for i in translation:		
			print i

		print

if __name__ == '__main__':
	
	wordlist=FileReader(WordListFileName)

	removelist=FileReader(RemoveFileName)
	language=AvaliableLanguages(removelist)
	
	TranslationList=TranslationProcess(wordlist,language)

	FileWrite(wordlist,TranslationList)
	PrintInTerminal(wordlist,TranslationList)


