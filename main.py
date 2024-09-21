import tkinter.messagebox
import qrcode
import win32clipboard
import os
import tkinter
from tkinter import *
from tkinter import *
import customtkinter
import io

def generator():
    url_or_text_box = Entry_id4.get()
    check_box_data = Checkbox_id7.get()
    image = qrcode.make(str(url_or_text_box))
   
    if check_box_data == 1:
        image.save(r"images\qr-gen.png")
        os.startfile(r"images\qr-gen.png")
    else:
        io_buffer = io.BytesIO()
        image.save(io_buffer,'BMP')
        data = io_buffer.getvalue()[14:]
        io_buffer.close()
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB,data)
        win32clipboard.CloseClipboard()
        tkinter.messagebox.showinfo("File Copied to your ClipBoard" ,"Successfull")


def show_images():
    os.startfile(r"C:\Users\SHARATH\Documents\CUI\Qrcode -Genetator\images")
def clear_data():
    Entry_id4.delete(0,END)

window = Tk()
window.title("Tkinter")
window.iconbitmap('icon.ico')
window.resizable(FALSE,FALSE)
window.geometry("700x200")
window.title("Qr-code Generator")
window.configure(bg="#ffffff")
canvas_ = tkinter.Canvas(window)

Button_id9 = customtkinter.CTkButton(
    master=window,
    text="Show images",
    font=("undefined", 15),
    text_color="#000000",
    hover=True,
    hover_color="#949494",
    height=30,
    width=95,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#ffffff",
    fg_color="#F0F0F0",
    command=show_images
    )
Button_id9.place(x=370, y=160)
Label_id3 = customtkinter.CTkLabel(
    master=window,
    text="Url or Text",
    font=("Courier New", 20),
    text_color="#000000",
    height=30,
    width=150,
    corner_radius=1,
    bg_color="#ffffff",
    fg_color="#ffffff",
    )
Label_id3.place(x=10, y=80)
Button_id10 = customtkinter.CTkButton(
    master=window,
    text="Clear",
    font=("undefined", 15),
    text_color="#000000",
    hover=True,
    hover_color="#949494",
    height=30,
    width=95,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#ffffff",
    fg_color="#F0F0F0",
    command=clear_data
    )
Button_id10.place(x=490, y=160)
Checkbox_id7 = customtkinter.CTkCheckBox(
    master=window,
    text="Save img",
    text_color="#000000",
    border_color="#000000",
    fg_color="#678dfe",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    )
Checkbox_id7.place(x=190, y=130)
Label_id2 = customtkinter.CTkLabel(
    master=window,
    text="QR Generator",
    font=("Arial", 20),
    text_color="#000000",
    height=30,
    width=140,
    corner_radius=0,
    bg_color="#ffffff",
    fg_color="#ffffff",
    )
Label_id2.place(x=270, y=0)
Entry_id4 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="Enter URL or Text to Make QR",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=40,
    width=500,
    border_width=2,
    corner_radius=10,
    border_color="#000000",
    bg_color="#ffffff",
    fg_color="#F0F0F0",
    )
Entry_id4.place(x=180, y=70)
Button_id8 = customtkinter.CTkButton(
    master=window,
    text="Generate",
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    hover_color="#b3b3b3",
    height=30,
    width=95,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#ffffff",
    fg_color="#F0F0F0",
    command=generator
    )
Button_id8.place(x=250, y=160)



#run the main loop
window.mainloop()