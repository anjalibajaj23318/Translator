from translate import Translator
translator= Translator(to_lang="ko")
try:
    with open("myfile.txt","r") as my_file:
        text=my_file.read()
        translation = translator.translate(text)
        with open("text-korean.txt" , "w" , encoding="utf-8") as file:
            file.write(translation)
except FileNotFoundError:
    print("check your file path!!!!!")
