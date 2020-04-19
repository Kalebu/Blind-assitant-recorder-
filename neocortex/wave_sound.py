''' 
This app require the installation of gtts python library

To install the library just do 

---->pip install gtts


'''


#__________________importing required library_________________

import platform

from gtts import gTTS

from pygame import mixer

import os

import threading


class Universe:
    def __init__(self):
        self.default_platform  = platform.system()
        self.current_dir = os.getcwd()
        self.language = 'en'    
        self.mixer = mixer
        self.mixer.init()

    
    def choose_lang(self, new_choice):
        self.language = new_choice

    def speak(self, mp3 = None):
        try:
            if mp3:
                
                if self.default_platform == 'Linux':
                    music_start = 'mpg123 '+mp3
                    os.system(music_start)
                elif self.default_platform == 'Windows': 
                    self.mixer.music.load(mp3)
                    self.mixer.music.play(0)      
                   # music_start = 'start '+mp3
                    #os.system('start {}'.format(music_start))
                else:
                    print("This module can operate only on windows and linux")
            else:
                print("Please specify the text or mp3")
        except Exception as ex:
            print(ex)
            print("The above error have occured please check it out")

    def text_to_speech(self, raw_text):
        try:
            speech = gTTS(raw_text, lang=self.language)
            filename = 'audio_command.mp3'
            speech.save(filename)
            print('music saved')
            return filename
        except Exception as ex:
            print(ex)
            print("The above error have occured please check it out")

    def say(self, text_signal):
        music_filename = self.text_to_speech(text_signal)
        music_thread = threading.Thread(target=self.speak, args=(music_filename,))
        music_thread.daemon=True
        music_thread.start()

            

    def __del__(self):
        pass

