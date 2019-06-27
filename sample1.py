from googletrans import Translator
import json

translator = Translator()

ho = translator.detect('इंग्लिश में टाइप करे स्पेस दबाये यह हिन्दी में परिवर्तित हो जाएगा ')
print(translator.translate('see you ! ',dest='hi'))
print(ho.lang)
print(ho.confidence)
print(translator.translate('நான் நன்றாக இருக்கிறேன்'))

print(translator.translate('इस पृष्ठ पर इन्टरनेट पर उपलब्ध विभिन्न हिन्दी एवं देवनागरी सम्बंधित साधनों की कड़ियों की सूची है। '))
# print(translator.translate('ਲਿਖੋ ਹਿੰਦੀ ਵਿੱਚ ਪੜੋ ਪੰਜਾਬੀ ਵਿੱਚ',dest='hi'))

hindi_marathi = translator.translate('इस पृष्ठ पर इन्टरनेट पर उपलब्ध विभिन्न हिन्दी एवं देवनागरी सम्बंधित साधनों की कड़ियों की सूची है। ',dest='mr')
print(hindi_marathi.dest ,'\n')
print(hindi_marathi.src,'\n')
# print(type(hindi_marathi.extra_data),'\n')

# with open('output.json','w') as file:
#     json.dump(hindi_marathi.extra_data,file)

print(hindi_marathi.origin,'\n')
print(hindi_marathi.pronunciation,'\n')
print(hindi_marathi.text,'\n')

print(translator.translate('आपला प्रवास सुखाचा होवो!'))

