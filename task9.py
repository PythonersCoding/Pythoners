# Task 9
__Author = "Pythoners"
import pyttsx3

Y = pyttsx3.init()
Y.setProperty('rate', 135)
x = str(input("what word do you want to say ?"))
Y.say(x)
Y.runAndWait()
وده الgui بتاعه

