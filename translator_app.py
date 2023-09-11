from tkinter import *
import googletrans , textblob
from tkinter import ttk, messagebox

root = Tk()

root.title('Techy Language translator')
# root.iconbitmap()
root.geometry("880x300")


# Text boxes

def translate():
    translated_text.delete(1.0, END)
    try:
        for key, value in languages.items():
            if value == original_combo.get():
                from_language_key = key

        for key, value in languages.items():
            if value == translated_combo.get():
                to_language_key = key

        words = textblob.TextBlob(original_text.get(1.0, END))

        words = words.translate(from_lang=from_language_key, to=to_language_key)

        translated_text.insert('1.0', words)
        print(words)

    except Exception as e:
        messagebox.showerror("Translator",e)

def clear():
    original_text.delete(1.0, END) #this is what this code is doing
    translated_text.delete(1.0, END) #this is what that code is doing



languages = googletrans.LANGUAGES

language_list = list(languages.values())
print(language_list)

original_text = Text(root, height=10, width=40,  font=('Helvetica', 18))
original_text.grid(row=0, column=0, pady=20, padx=10)

translate_button = Button(root, text="Translate!", font=("Helvetica", 24), command=translate)
translate_button.grid(row=0, column=1, padx=10)

translated_text = Text(root, height=10, width=40, font=('Helvetica', 18))
translated_text.grid(row=0, column=2, pady=20, padx=10)


# comobo box
original_combo = ttk.Combobox(root, width=50, value=language_list)
original_combo.current(21)
original_combo.grid(row=2, column=0)


translated_combo = ttk.Combobox(root, width=50, value=language_list)
translated_combo.current(3)
translated_combo.grid(row=2, column=2)



# clear button
clear_button = Button(root, text="Clear", command=clear)
clear_button.grid(row=2, column=1)

root.mainloop()









































