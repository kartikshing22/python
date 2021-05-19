from translate import Translator  #pip install translate
languages={"spanish":'spanish','english':'english'}
lang1=input("enter the language which you want to translate : ")
lang2=input("enter your language : ")
translation=input(f" enter what you want to translate from {lang1} to {lang2} : ")

translator= Translator(from_lang=languages[lang1], to_lang=languages[lang2])
result=translator.translate(translation)
print(result)
