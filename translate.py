from googletrans import Translator
translater = Translator()
out = translater.translate("welcome",dest='ta')

print(out.text)