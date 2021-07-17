from tkinter import *
from tkinter import filedialog
from tkinter.font import BOLD
from huffman import HuffmanCoding
import sys

def compressFile():
    filePath = filedialog.askopenfilename()
    useHuffman(filePath)

def decompressFile():
    filePath = filedialog.askopenfilename()
    useHuffmandecom(filePath)

def useHuffman(path):

    # path = "D:/sample.txt"
    h = HuffmanCoding(path)
    output_path = h.compress()
    print("Compressed file path: " + output_path)

def useHuffmandecom(path):
    h = HuffmanCoding(path)
    decom_path = h.decompress(path)
    print("Decompressed file path: " + decom_path)

def on_enter(e):
    e.widget['foreground'] = 'blue'

def on_leave(e):
    e.widget['foreground'] = 'black'

window = Tk()
window.title("Compressor")
window.geometry('400x300')

label2=Label(window,text="")
label2.pack()

label=Label(window,text="File Compressor",font=('Helvetica',20,BOLD))
label.pack()

label2=Label(window,text="",height=2)
label2.pack()

button1 = Button(window,text="Compress",command=compressFile)
button1.pack()

label3=Label(window,text="")
label3.pack()
button2 = Button(window,text="Decompress",command=decompressFile)
button2.pack()

button1.bind("<Enter>", on_enter)
button1.bind("<Leave>", on_leave)
button2.bind("<Enter>", on_enter)
button2.bind("<Leave>", on_leave)

window.mainloop()