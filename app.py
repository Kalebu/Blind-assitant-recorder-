from tkinter import *
from tkinter import filedialog
import time

#__________importing library for multi-threading______________

from threading import Thread
 
#_________________loading functionality from package___________

from neocortex import Assitant
from neocortex import wave_sound




root = Tk()

class menu:
    def __init__(self, window):
        self.window = window
        self.window.title("Blind reading support")
        self.window.geometry('720x600')
        self.window.configure(bg='#847')
        self.languages = ['English', 'Swahili']
        self.default_language = StringVar()
        self.default_language.set(self.languages[0])

        #______________main menu_____________

      #  self.welcome_label = Label(window, text="Welcome to using our app")
        self.choose_language = Label(window, text="Choose the language", bg='#847', fg='white', font=('verdana', 18,))
        self.language_notification = Label(window, text = "---->", width=10, height=3, bg='#111', fg='white')
        self.language_options = OptionMenu(window, self.default_language, *self.languages, command=self.choose)
        self.language_options.configure(relief='flat', font = ('Arial', 20), bg = 'green', fg='white', width=15)
        

        #___________Audio source menu__________

        self.load_audio_file = Button(window, text = "Load wav audio")
        self.load_audio_file.configure(relief='flat', font = ('Arial', 16), bg = '#342', fg='white', width=15)
        self.record_audio = Button(window, text="Live Record")
        self.record_audio.configure(relief='flat', font = ('Arial', 16), bg = '#242', fg='white', width=15)


        #______________result_menu______________
        #self.result_label = Label(window, )
        #self.result_label.configure(font = ('Arial', 16), bg = '#892', fg='white', width=40, height=12 )
        self.save_file = Button(window, text = "Save to Document")
        self.save_file.configure(relief='flat', font = ('Arial', 16), bg = '#272', fg='white', width=15)

        self.message_session = Text(window, bd=3, relief="flat", font=("consolas", 16, "bold"), undo=True, wrap="word")
        self.message_session.config(width=35, height=15,bg="#AAAAAA", fg="blue")
        self.overscroll = Scrollbar(window, command=self.message_session.yview)
        self.overscroll.config(width=20)
        self.message_session["yscrollcommand"] = self.overscroll.set


    def main_menu(self, state=False):
        if state:
         #   self.welcome_label.place(x=250 , y=10)
            self.choose_language.place(x=250, y = 160)
            self.language_options.place(x = 250, y = 300)
            self.language_notification.place(x = 320, y = 450)
        else:
          #  self.welcome_label.place_forget()
            self.choose_language.place_forget()
            self.language_options.place_forget()
            self.language_notification.place_forget()

    def record_menu(self, state=False):
        if state:
            self.load_audio_file.place(x=50, y=300)
            self.record_audio.place(x=450, y=300)
        else:
            self.load_audio_file.place_forget()
            self.record_audio.place_forget()

    def result_menu(self, state=False):
        if state:
            self.message_session.place(x=150, y=80)
            self.overscroll.place(x=400, y=20)
            self.save_file.place(x=270, y=500)
        else:
            self.overscroll.pack_forget()
            self.message_session.place_forget()
            self.save_file.place_forget()

    def choose(self, event=None):
        language = str(self.default_language.get())
        print(language)
        if language == 'swahili':
            lang = 'sw'
        else:
            lang = 'en-US'
        
        return lang
       # print(self.language_options.get())


class app(menu):
    def __init__(self, window):
        super().__init__(window)

              #____________Binding the labels_______
        self.language_notification.bind('<Button-1>', self.second_window)
        self.load_audio_file.bind('<Button-1>', self.third_window_2)
        self.record_audio.bind('<Button-1>', self.third_window)
        self.save_file.bind('<Button-1>', self.saving_file)
        self.information = 'jomba'

    def first_window(self):
        self.message_session.delete(1.0, END)
        self.main_menu(True)
        self.result_menu()

    def second_window(self, event=None):
    #_________functional code______________
        lang = self.choose()
        self.peterpan = Assitant.blind_assitant(lang=lang)
        self.main_menu()
        self.record_menu(True)
    
    def third_window(self, event=None):
        self.record_menu()
        #self.sound_studio()
        sound = self.peterpan.record_audio()
        print(sound)
        self.information = self.peterpan.speech_to_text(sound)
        self.message_session.insert(END, self.information)
        self.result_menu(True)


    def third_window_2(self, event):
        self.record_menu()
        audio = filedialog.askopenfilename()
        sound = self.peterpan.load_audio(audio)
        print(sound)
        self.information = self.peterpan.speech_to_text(sound)
        self.message_session.insert(END, self.information)
        self.result_menu(True)


    def saving_file(self, event):
        #________saving the information to file_____
        try:
            information_file = filedialog.asksaveasfile(mode="w", defaultextension='.doc')
            information_file.write(self.information)
            information_file.close()
            print('file has been writted')
        except:
            print("There is error in saving the document")

        finally:
            self.first_window()

    def local_save(self, document, filename):
        with open(filename, 'w') as file:
            file.write(document)
        print('file has been saved')

    def get_text(self, lang = 'sw', insert=None):
        self.peterpan = Assitant.blind_assitant(lang=lang)
        sound = self.peterpan.record_audio()
        print(sound)
        self.information = self.peterpan.speech_to_text(sound)
        if insert:
            self.message_session.insert(END, self.information)
            self.result_menu(True)
            self.record_menu()
        return self.information

    def body(self):
        #__________loading audio functionality from wave sound ______________
        self.first_window()
        self.assitant_voice = wave_sound.Universe()
        self.assitant_voice.choose_lang('sw')
        #assitant_voice.say('Hello your welcome using our application')
        self.assitant_voice.speak("./voice_commands/welcome.mp3")
        time.sleep(2)
        self.assitant_voice.speak("./voice_commands/option.mp3")
        time.sleep(0.3)
        answer = self.get_text()
        state = True
        #______________checking the option_____________
        while state:
            if 'swahili' or 'ngereza' in answer:
                state = False
                if 'swahili' in answer:
                    answer = 'sw'
                    self.assitant_voice.speak('./voice_commands/kiswahili.mp3')
                else:
                    answer = 'en'
                    self.assitant_voice.choose_lang('en')
                    self.peterpan = Assitant.blind_assitant()
                    self.assitant_voice.speak('./voice_commands/kiingereza.mp3')
            else:
                self.assitant_voice.speak('./voice_commands/sijaelewa.mp3')
                answer = self.get_text()
        self.second_window()
        self.assitant_voice.speak('./voice_commands/anza.mp3')
        content = self.get_text(insert=True)
        self.assitant_voice.speak('./voice_commands/nimemaliza.mp3')
        if answer=='sw':
            message = 'umesema '+content
        else:
            message = 'You said ' +content
        self.assitant_voice.say(message)
        time.sleep(4)
        self.assitant_voice.speak('./voice_commands/hifadhi.mp3')
        state = True
        while state:
            answer = self.get_text()
            answer = answer.lower()
            if 'apana' in answer or 'io' in answer:
                state = False
                if 'apana' in answer:
                    pass
                else:
                    self.assitant_voice.speak('./voice_commands/jina.mp3')
                    time.sleep(1)
                    name = self.get_text()
                    self.local_save(content, name)
            else:
                self.assitant_voice.speak('./voice_commands/sijaelewa.mp3')
                



        print(content)
        #print('Umechangua {}'.format(answer))'''

        #_________configuring language_____________
        #time.sleep(1.5)
       # print('hello')
       # self.second_window()
       # assitant_voice.say('Anza kurekodi ujumbe')
       # self.third_window()
       
    def weird(self):
        test = Thread(target=self.body)
        test.daemon=True
        test.start()
        print('Finished')
    
    def get_language(self):
        pass
    def __del__(self):
        pass

Application = app(root)
Application.first_window()
Application.weird()
root.mainloop()
print('giss')


