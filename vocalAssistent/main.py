import sys
import pyttsx3 as tts
from neuralintents import GenericAssistant
import speech_recognition
import audiomath

recognizer = speech_recognition.Recognizer()

speeker = tts.init()
speeker.setProperty('rate', 125)

todo_list = ['Go shopping', 'clean room', 'work']


# descent from AudioSource is required purely to pass an assertion in Recognizer.listen()
class DuckTypedMicrophone(speech_recognition.AudioSource):
    # 1024 samples at 44100 Hz is about 23 ms
    def __init__(self, device=None, chunkSeconds=1024/44100.0):
        self.recorder = None
        self.device = device
        self.chunkSeconds = chunkSeconds

    def __enter__(self):
        self.nSamplesRead = 0
        self.recorder = audiomath.Recorder(audiomath.Sound(
            5, nChannels=1), loop=True, device=self.device)
        # Attributes required by Recognizer.listen():
        self.CHUNK = audiomath.SecondsToSamples(
            self.chunkSeconds, self.recorder.fs, int)
        self.SAMPLE_RATE = int(self.recorder.fs)
        self.SAMPLE_WIDTH = self.recorder.sound.nbytes
        return self

    def __exit__(self, *blx):
        self.recorder.Stop()
        self.recorder = None

    def read(self, nSamples):
        sampleArray = self.recorder.ReadSamples(self.nSamplesRead, nSamples)
        self.nSamplesRead += nSamples
        return self.recorder.sound.dat2str(sampleArray)

    @property
    def stream(self):  # attribute must be present to pass an assertion in Recognizer.listen(), and its value must have a .read() method
        return self if self.recorder else None


def create_note():
    global recognizer

    speeker.say("Cosa vuoi aggiungere alle tue note?")
    speeker.runAndWait()

    done = False

    while not done:
        try:

            with DuckTypedMicrophone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio, language="it-IT")
                note = note.lower()

                speeker.say("Seleziona il nome del file")
                speeker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio, language="it-IT")
                filename = filename.lower()

            with open(filename, 'A') as f:
                f.write(note)
                done = True
                speeker.say("note scritte con successo {filename}")
                speeker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speeker.say("Non ho capito. Ripetere")
            speeker.runAndWait()


def add_todo():
    global recognizer

    speeker.say("cosa vuoi aggiungere alla lista di cose da fare?")

    done = False

    while not done:
        try:
            with DuckTypedMicrophone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                item = recognizer.recognize_google(audio, language="it-IT")
                item = item.lower()

                todo_list.append(item)
                done = True
                speeker.say("{item} aggiunto alla lista di cose da fare")
                speeker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speeker.say("Non ho capito. Ripetere")
            speeker.runAndWait()


def show_todos():
    speeker.say("le cose da fare nella tua lista da fare sono le seguenti")
    for item in todo_list:
        speeker.say(item)
        speeker.runAndWait()


def hello():
    speeker.say(
        "Ciao, sono Dum, l'intelligenza creata dal grandissimo Luca Logallo. Cosa posso fare per te?")
    speeker.runAndWait()


def quit():
    speeker.say("Addio")
    speeker.runAndWait()
    sys.exit(0)


def m():
    speeker.say(
        ",più vengo meno, per non venir più meno, non me lo meno più, o per lo meno, me lo meno di meno")
    speeker.runAndWait()


mappings = {
    "greeting": hello,
    "create_note": create_note,
    "add_todo": add_todo,
    "show_todos": show_todos,
    "exit": quit,
    "p": m
}

#mapping = {'greeting': some_function}
#assistant = GenericAssistant('intends.json', intent_methods=mapping)
assistant = GenericAssistant(
    'D:/t/tra/vocalAssistent/intents.json', intent_methods=mappings)
# assistant.train_model()

# assistant.save_model()
assistant.load_model()
# assistant.request("Hey")

while True:
    # speeker.say("Avvio")
    # speeker.runAndWait()
    try:
        with DuckTypedMicrophone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio, language="it-IT")
            message = message.lower()

        assistant.request(message)
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
