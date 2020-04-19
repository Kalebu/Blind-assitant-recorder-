#_________________speech recognition library have ben used______________________

''' 

Fo installations of the library 

you can use pip stall 

---->$ pip install SpeechRecognition 

'''


#__________________importing requied library_______________________

import speech_recognition as sr


class blind_assitant:
    def __init__(self, lang = 'en-US'):
        self.mouth = sr.Recognizer()
        self.b_language = lang
        self.Text = None

#=============method to test if the file is wav=========================
    def wav(self, link):
        link = link.split('.')[-1]
        link = link.lower()
        if link == 'wav':
            return True
        else:
          return False


    def record_audio(self):
        try:
                
           # self.microphone = sr.Microphone()
            
            #_______Recording the sound until the voice is detected_______
            print('recording')
            with sr.Microphone() as source:
                audio = self.mouth.listen(source)
            print('finished recording')
            return audio

        except Exception as ex:
            print(ex)
            print("The above error have occured")
            

#==================================method to load audio=====================
    def load_audio(self, link=None):
        if link:
            try:
                if self.wav(link):
                    
                    #_____________opening the audio file___________
                    try:

                        loaded_audio = sr.AudioFile(link)

                        #__________recording the loaded audio____________

                        with loaded_audio as sound:
                            recorded_audio = self.mouth.record(sound)
                            return recorded_audio

                        #_________returning an loaded audio____________


                    except Exception as ex:

                            print(ex)
                            print("The above error have occured")
                            print('probably the audio does not exist')

                else:
                    #______the audio loaded is not wav_______

                    return False
                

            except Exception as ex:
                print(ex)
                print("The above error have occured")
                pass
        else:
            pass

#================ method to recognize the Audio================
    def speech_to_text(self, sound):
        try:

            #____________Recognizing the Audio using google api________
            self.Text = self.mouth.recognize_google(sound, language=self.b_language)
            return self.Text
        except:
            print("Error occured in understanding audio")
            print("Please check your internet connection ")

#===============  method to save the audio to file =====================     
    def save(self, filename):
        try:
            #_______________writing the informations to file___________
            if self.Text: 
                with open (filename, 'w') as file:
                    file.write(self.Text)
                print("information have been written")
            else:
                print("Please recognize the audio firstly before saving")

        except Exception as ex:
            print(ex)
            print("The above error have occured")

#=================== Deconstructor=================            
    def __del__(self):
        pass