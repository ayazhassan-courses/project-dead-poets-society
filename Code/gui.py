import tkinter as gui
from encryption import encryption
from decryption import decryption 

def encrypt_output(text):
    outputbox['text'] = text
def decrypt_output(text):
    outputbox['text'] = text

root = gui.Tk()


canvas = gui.Canvas(root, height = 600, width = 800)
canvas.pack()

frame = gui.Frame(root, bg= '#aed6f1', bd=5)
frame.place( relx = 0.5, rely = 0.1, relwidth= 0.75, relheight = 0.1, anchor='n')

EncryptButton = gui.Button(frame, text= "Encrypt Text", command=lambda:  encrypt_output(encryption(textbox.get(), keybox.get())))
EncryptButton.place(relx = 0.7, relwidth =0.3, relheight= 0.5 )


DecryptButton = gui.Button(frame, text= "Decrypt Text", command=lambda: decrypt_output(decryption(textbox.get(), keybox.get())))
DecryptButton.place(relx = 0.7, rely =0.55 ,relwidth =0.3, relheight= 0.5 )

textbox = gui.Entry(frame)
textbox.place(relx = 0, rely = 0, relwidth= 0.65, relheight = 1)

keyframe= gui.Frame(root, bg='#aed6f1', bd=4)
keyframe.place(relx = 0.5, rely = 0.2 , relwidth = 0.75, relheight = 0.075, anchor='n')

keybox = gui.Entry(keyframe)
keybox.place(relx = 0, rely = 0, relwidth= 0.65, relheight = 1)

result = gui.Frame(root,bg= '#aed6f1', bd=10)
result.place(relx=0.5, rely= 0.25, relwidth =0.75, relheight = 0.6, anchor='n')

outputbox = gui.Label(result, anchor="nw", justify='left', bd=4)
outputbox.place(relwidth=1 ,relheight= 1)

root.mainloop()