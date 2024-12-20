import tkinter as tk
from tkhtmlview import HTMLLabel, RenderHTML





root = tk.Tk()
root.title('ostrova.65')
root.geometry('450x700')

def call_menu():
    pass

main_frame = tk.Frame(root, bg = '#d68ae6')
main_frame.pack(fill='both', expand=True)
toogle_button = tk.Button(master= main_frame, text = 'menu', command = call_menu)
menu_frame = tk.Frame(root), bg = '#87e6cc'



