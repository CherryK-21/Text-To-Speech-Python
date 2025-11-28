from gtts import gTTS
import tkinter as tk
from tkinter import *
from tkinter import ttk, StringVar
import os

# --- settings app ---
app = tk.Tk()
app.geometry("540x340")
app.iconbitmap('text_to_speech.ico')
app.title('SpeechCraft')
app['bg'] = 'orange'
app.resizable(False, False)


# --- config ---
language = 'ru'
activety = tk.BooleanVar(value=False)
output_file = "[SC].mp3"
volume_var = tk.DoubleVar(value=50.0)

# --- functions ---
def lunguages_set(event=None):
    global language
    lang_select = language_var.get()
    if lang_select == 'Russian':
        language = 'ru'
    elif lang_select == 'English':
        language = 'en'
    elif lang_select == 'Deutsch':
        language = 'de'

def start_audio():
    global language
    text = text_entry.get("1.0", "end-1c")
    tts = gTTS(text=text, lang=language, slow=activety.get()) 
    tts.save(output_file)
    os.system(f"start {output_file}")
    
# --- Интерфейс ---
fon = tk.Frame(app, bg='grey', width=533, height=333)
fon.place(x=3, y=3)
frame = Frame(app)
frame.place(x=10, y=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

text_entry = tk.Text(frame, width=35, height=8, font=('Arial', 11), wrap='word', yscrollcommand=scrollbar.set)
text_entry.pack(side=LEFT, fill=BOTH)
text = text_entry.get("1.0", "end-1c")

language_var = tk.StringVar()
languages = ['Russian', 'English', 'Deutsch']
language_comb = ttk.Combobox(app, textvariable=language_var, values=languages, state='readonly', font=('Arial', 12))
language_comb.place(x=320, y=10)
language_comb.set('Russian')
language_comb.bind("<<ComboboxSelected>>", lunguages_set)

scrollbar.config(command=text_entry.yview)

slow_togle = tk.Checkbutton(app, text='Замедление', variable=activety, bg='grey')
slow_togle.place(x=10, y=200)

start_but = tk.Button(app, text='Play', width=13, height=1, command=start_audio)
start_but.place(x=10, y=155)

app.mainloop()
