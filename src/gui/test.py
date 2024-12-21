import tkinter as tk
from tkhtmlview import HTMLLabel, RenderHTML
import tkhtmlview

# # tkhtmlview.html_parser
# # root = tk.Tk() # object
# # # root.geometry('600x700')

# # my_label = HTMLLabel(root, html=RenderHTML('./src/gui/index.html'))
# # my_label.pack(fill='both', expand=True)
# # # my_label.pack(pady=20, padx=200)

# # label = tk.Label(text = "Hellow, Tkinter", fg='white', bg = 'black', width=10)
# # label.pack( expand=True)
# # button = tk.Button(
# #     text="Click me!",
# #     width=25,
# #     height=5,
# #     bg="blue",
# #     fg="yellow",
# # )
# # button.pack()

# # entry = tk.Entry(fg="yellow", bg="blue", width=50)
# # entry.pack()
# # name = entry.get()
# # print(name)

# # root.mainloop()

# # import tkinter as tk

# # # Function to update the label with the text from the entry
# # def update_label():
# #     user_input = entry.get()  # Get the text from the entry box
# #     label.config(text=user_input)  # Update the label with the input text


# # def open_menu():
# #     frame_menu = tk.Frame()
# #     frame_main.b
# #     frame_menu.pack()
# # # Create the main window
# # root = tk.Tk()
# # root.title("Simple GUI Example")  # Title of the window
# # root.geometry("450x800")  # Size of the window

# # frame_main = tk.Frame()

# # # Create a label
# # label = tk.Label(master = frame_main, text="Enter something:", font=("Arial", 14))
# # label.pack(pady=10)  # Add some vertical padding

# # # Create an entry box
# # entry = tk.Entry(master= frame_main, font=("Arial", 14))
# # entry.pack(pady=10)  # Add some vertical padding

# # # Create a button that will call update_label when clicked
# # button = tk.Button(master = frame_main, text="Submit", command=open_menu, font=("Arial", 14))
# # button.pack(pady=10)  # Add some vertical padding

# # # Start the Tkinter event loop
# # root.mainloop()




# # import tkinter as tk
# # from tkinter import messagebox

# # # Function to update the label with the text from the entry
# # def update_label():
# #     user_input = entry.get()  # Get the text from the entry box
# #     label.config(text=user_input)  # Update the label with the input text

# # # Function to show help information
# # def show_help():
# #     messagebox.showinfo("Help", "This is a simple GUI application.\nEnter text and click 'Submit'.")

# # # Create the main window
# # root = tk.Tk()
# # root.title("Simple GUI Example")  # Title of the window
# # root.geometry("300x200")  # Size of the window

# # # Create a menu bar
# # menu_bar = tk.Menu(root)

# # # Create a File menu
# # file_menu = tk.Menu(menu_bar, tearoff=0)
# # file_menu.add_command(label="Exit", command=root.quit)  # Exit option
# # menu_bar.add_cascade(label="File", menu=file_menu)

# # # Create a Help menu
# # help_menu = tk.Menu(menu_bar, tearoff=0)
# # help_menu.add_command(label="Help", command=show_help)  # Help option
# # menu_bar.add_cascade(label="Help", menu=help_menu)

# # # Configure the main window to use the menu bar
# # root.config(menu=menu_bar)

# # # Create a label
# # label = tk.Label(root, text="Enter something:", font=("Arial", 14))
# # label.pack(pady=10)  # Add some vertical padding

# # # Create an entry box
# # entry = tk.Entry(root, font=("Arial", 14))
# # entry.pack(pady=10)  # Add some vertical padding

# # # Create a button that will call update_label when clicked
# # button = tk.Button(root, text="Submit", command=update_label, font=("Arial", 14))
# # button.pack(pady=10)  # Add some vertical padding

# # # Start the Tkinter event loop
# # root.mainloop()





# import tkinter as tk

# class SwipeMenuApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Swipe Menu Example")
#         self.root.geometry("400x300")

#         # Create a frame for the main content
#         self.main_frame = tk.Frame(self.root, bg="lightblue")
#         self.main_frame.pack(fill=tk.BOTH, expand=True)

#         # Create a button to toggle the menu
#         self.toggle_button = tk.Button(self.main_frame, text="Toggle Menu", command=self.toggle_menu)
#         self.toggle_button.pack(pady=10)

#         # Create the side menu
#         self.menu_frame = tk.Frame(self.root, bg="gray", width=200)
#         self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)

#         # Add some items to the menu
#         self.menu_label = tk.Label(self.menu_frame, text="Menu", bg="gray", font=("Arial", 16))
#         self.menu_label.pack(pady=10)

#         # Add example menu items
#         for item in ["Item 1", "Item 2", "Item 3"]:
#             label = tk.Label(self.menu_frame, text=item, bg="gray", font=("Arial", 12))
#             label.pack(pady=5)

#         # Initially hide the menu
#         self.menu_visible = True
#         self.hide_menu()

#     def toggle_menu(self):
#         """Toggle the visibility of the menu."""
#         if self.menu_visible:
#             self.hide_menu()
#         else:
#             self.show_menu()

#     def hide_menu(self):
#         """Hide the menu by changing its width to 0."""
#         self.menu_frame.pack_forget()  # Remove from display
#         self.menu_visible = False

#     def show_menu(self):
#         """Show the menu by packing it back."""
#         self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)
#         self.menu_visible = True

# # Create the main window
# root = tk.Tk()
# app = SwipeMenuApp(root)

# # Start the Tkinter event loop
# root.mainloop()


# root = tk.Tk()
# # root.geometry('400x400')
# main = tk.Frame(root, bg='gray')
# main.pack(expand=True, fill= 'both')

# for i, num in zip(['red', 'green', 'blue', 'yellow', 'pink', 'lightblue']*100, range(600)):
#     card = tk.Frame(main, bg=i)
#     card.grid(column=0, row=num)
#     txt = tk.Label(card, text = 'txt', bg=i)
#     txt.pack(fill='both', expand=True)

# root.mainloop()

import tkinter as tk

# class CardApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Card Scrolling Example")
#         self.root.geometry("400x400")

#         # Создаем Canvas для прокрутки
#         self.canvas = tk.Canvas(root)
#         self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
#         self.scrollable_frame = tk.Frame(self.canvas)

#         # Настраиваем scrollable_frame
#         self.scrollable_frame.bind(
#             "<Configure>",
#             lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
#         )

#         # Добавляем scrollable_frame в Canvas
#         self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

#         # Настраиваем scrollbar и canvas
#         self.canvas.configure(yscrollcommand=self.scrollbar.set)

#         # Размещаем canvas и scrollbar
#         self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#         self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#         # Создаем карточки
#         self.create_cards()

#     def create_cards(self):
#         for i in range(60):  # Создаем 20 карточек
#             card = tk.Frame(self.scrollable_frame, bg="lightblue", bd=2, relief="groove")
#             label = tk.Label(card, text=f"Card {i + 1}", bg="lightblue", font=("Arial", 14))
#             label.pack(padx=10, pady=10)
#             card.pack(pady=5, padx=10, fill=tk.X)  # Заполняем по горизонтали

# # Создаем главное окно
# root = tk.Tk()
# app = CardApp(root)

# # Запускаем главный цикл Tkinter
# root.mainloop()
# import tkinter as tk

# class CardApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Card Scrolling Example")
#         self.root.geometry("400x400")

#         # Создаем Canvas для прокрутки
#         self.canvas = tk.Canvas(root)
#         self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
#         self.scrollable_frame = tk.Frame(self.canvas)

#         # Настраиваем scrollable_frame
#         self.scrollable_frame.bind(
#             "<Configure>",
#             lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
#         )

#         # Добавляем scrollable_frame в Canvas
#         self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

#         # Настраиваем scrollbar и canvas
#         self.canvas.configure(yscrollcommand=self.scrollbar.set)

#         # Размещаем canvas и scrollbar
#         self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#         self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#         # Создаем карточки
#         self.create_cards()

#     def create_cards(self):
#         for i in range(20):  # Создаем 20 карточек
#             card = tk.Frame(self.scrollable_frame, bg="lightblue", bd=2, relief="groove")
#             label = tk.Label(card, text=f"Card {i + 1}", bg="lightblue", font=("Arial", 14))
#             label.pack(padx=10, pady=10)
#             card.pack(pady=5, padx=10, fill=tk.X)  # Заполняем по горизонтали

# # Создаем главное окно
# root = tk.Tk()
# app = CardApp(root)

# # Запускаем главный цикл Tkinter
# root.mainloop()




import tkinter as tk

class CardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Card Scrolling Example")
        self.root.geometry("400x400")

        self.main_frame = tk.Frame(self.root, bg='red')
        self.main_frame.pack(fill='both', expand=True)
        # Создаем Canvas для прокрутки
        self.body_frame = tk.Frame(self.main_frame, bg = 'red')
        self.body_frame.pack(fill='both', expand=True)

        self.canvas = tk.Canvas(self.body_frame)
        self.scrollbar = tk.Scrollbar(self.body_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        # Настраиваем scrollable_frame
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        # Добавляем scrollable_frame в Canvas
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Настраиваем scrollbar и canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Размещаем canvas и scrollbar
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Создаем карточки
        self.create_cards()

        # Обработчик событий для прокрутки с помощью тачпада
        self.root.bind_all("<MouseWheel>", self.on_mouse_wheel)

    def create_cards(self):
        for i in range(20):  # Создаем 20 карточек
            card = tk.Frame(self.scrollable_frame, bg="lightblue", bd=2, relief="groove")
            label = tk.Button(card, text=f"Card {i + 1}", bg="lightblue", font=("Arial", 14), command=self.close)
            label.pack(padx=10, pady=10)
            card.pack(pady=5, padx=10, fill=tk.X)  # Заполняем по горизонтали

    def on_mouse_wheel(self, event):
        """Прокрутка с помощью мыши или тачпада."""
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def close(self):
        self.main_frame.pack_forget()

# Создаем главное окно
root = tk.Tk()
app = CardApp(root)

# Запускаем главный цикл Tkinter
root.mainloop()

