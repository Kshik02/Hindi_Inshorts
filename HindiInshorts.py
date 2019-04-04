from googletrans import Translator
from summarizerAlgo import getrank

f=open("InputText",encoding="utf-8")
hinText=f.read()
f.close()

engText=Translator().translate(hinText,'en')
engSum=getrank(engText.text)

for sentence in engSum:
	hinSent=Translator().translate(sentence,'hi')	
	temp=hinSent.text	
	f=open("SummarizedText",'a', encoding="utf-8")
	f.write(temp)
	f.close()


		
