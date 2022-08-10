import pyttsx3
from plyer import notification

engine = pyttsx3.init('dummy')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

notification.notify(
    title = "Please drink water",
    message = "you have not drink water since half hour!",
    app_icon = "C:\\Users\\anind\\Downloads\\water_drink_bottle_icon-icons.com_51087.ico",
    timeout = 5
)
speak("Please drink water and stay hydrated")
