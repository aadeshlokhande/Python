
from datetime import datetime
import os
from gtts import gTTS 

while(True):
    now = datetime.now()
    a = now.strftime("%I:%M %p")
    if (a == "07:19 PM"):
        mytext = "be ready" * 3
        print(mytext)
        myobj = gTTS(text=mytext, lang='en', slow=False) 
        myobj.save("audio.mp3")
        for i in range(2): 
            os.system("audio.mp3")         
        break
