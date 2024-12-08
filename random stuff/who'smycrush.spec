for x in gals:
    if x["glass"] == "no":
        gals.pop(0)
        gals.pop(1)
    else:
        gals.pop(1)

while True:
    gay = input("is your crush Thai? ")
    if gay == "yes":
        gals = [girls for girls in gals if girls["thai"] != "no"]
        break
    elif gay == "no":
        gals = [girls for girls in gals if girls["thai"] == "no"]
        break
    else:
        
        print("please re-enter yes or no")


sound = gTTS(text, lang="th", slow=False)
sound.save("thai.mp3")
playsound.playsound("thai.mp3")
pyinstaller --onefile --noconsole ttsptest.py
pyinstaller --onefile --hidden-import gtts --hidden-import six --hidden-import requests thai_spelling_1-50.py
