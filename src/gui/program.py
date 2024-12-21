import tkinter as tk
from tkhtmlview import HTMLLabel, RenderHTML
import requests
from PIL import ImageTk, Image
from io import BytesIO




# root = tk.Tk()
# root.title('ostrova.65')
# root.geometry('450x700')

# def call_menu():
#     pass
# def hide_menu():
#     pass

# main_frame = tk.Frame(root, bg = '#FFFFFF')
# main_frame.pack(fill='both', expand=True)
# toogle_button = tk.Button(master= main_frame, text = 'menu', command = call_menu)
# toogle_button.pack(padx=10)
# menu_frame = tk.Frame(root, bg = '#FFFFFF')
# menu_frame.pack()

# menu_label = tk.Label(menu_frame, text="menu", bg='white', fg='black')
# menu_label.pack()
# for i in range(1, 4):
#     label = tk.Label(menu_frame, text = f'item {i}', bg = 'gray', font=('Arial', 14))
#     label.pack()

# hide_menu()

# # root.mainloop()



class MainApp:
    def __init__(self, root):
        # Приложение
        self.COLOR_MAIN = 'lightblue'
        self.COLOR_HEAD = 'white'
        self.COLOR_MENU = 'white'
        self.COLOR_BODY = 'lightblue'
        self.COLOR_DETAIL = 'white'
        self.visible_menu = True
        self.root = root
        self.root.title('ostrova.65')
        self.root.geometry('450x700')



                # Создаем Canvas для прокрутки

        # инициализация main fram
        self.main_frame = tk.Frame(root, bg = self.COLOR_MAIN) 
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        # Head frame - дочерний от main frame
        self.head_frame = tk.Frame(self.main_frame, bg = self.COLOR_MAIN)
        self.head_frame.pack(fill = 'both', pady=1)
        self.toogle_button = tk.Button(self.head_frame, text = 'Меню', command=self.call_menu, bg = self.COLOR_HEAD)
        self.toogle_button.pack(side=tk.LEFT, padx=5)

        # menu frame - дочерний объекст от main frame
        self.menu_frame = tk.Frame(self.main_frame, bg=self.COLOR_MENU)
        self.menu_frame.pack(fill = 'both')
        for txt, command in zip(['Избранное ⭐', 'Календарь 📅', 'Карта мероприятий 🌏', 'Уведомления 🔔', 'Мои билеты 🎫', 'История👀'], [self.call_stared, self.check_calendar, self.check_map, self.check_notifications, self.check_tickets, self.check_history]):
            self.label = tk.Button(self.menu_frame, text =txt, bg = self.COLOR_MENU, width= 20, font = ('Roboto', 14), anchor='w', command=command)
            self.label.pack(pady=5, anchor='w', padx=4, expand=False)


        self.find_button = tk.Button(self.head_frame, text='Фильтр',command = self.call_finder, bg = self.COLOR_HEAD)
        self.find_button.pack(side=tk.RIGHT, padx=5)
        self.find_enter = tk.Entry(self.head_frame, bg = self.COLOR_HEAD, justify='left', font=('Arial', 14), fg= 'black', show='')
        self.find_enter.pack(side=tk.RIGHT, padx=5)



        self.body_frame = tk.Frame(self.main_frame, bg=self.COLOR_BODY)
        self.body_frame.pack(fill='both', expand=True)

       #!!!
        # self.card_frame = tk.Frame(self.body_frame, bg=self.COLOR_BODY)
        # self.canvas = tk.Canvas(self.card_frame)
        # self.scrollbar = tk.Scrollbar(self.card_frame, orient="vertical", command=self.canvas.yview)
        # self.scrollable_frame = tk.Frame(self.canvas)
        # self.scrollable_frame.bind(
        #     "<Configure>",
        #     lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        # )
        # self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # # Настраиваем scrollbar и canvas
        # self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # # Размещаем canvas и scrollbar
        # self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # self.root.bind_all("<MouseWheel>", self.on_mouse_wheel)
        self.call_menu()    
    #     self.create_cards()

    # def create_cards(self):
    #     for i in range(20):  # Создаем 20 карточек
    #         card = tk.Frame(self.body_frame, bg="lightblue", bd=2, relief="groove")
    #         label = tk.Label(card, text=f"Card {i + 1}", bg="lightblue", font=("Arial", 14))
    #         label.pack(padx=10, pady=10)
    #         card.pack(pady=5, padx=10, fill=tk.X)

    
    def call_menu(self):
        if self.visible_menu:
            self.menu_frame.pack_forget()
            self.body_frame.pack(fill='both', expand=True)
            self.visible_menu = False
        else:
            self.menu_frame.pack(fill = 'both', expand=True)
            self.body_frame.pack_forget()
            self.visible_menu = True
    
    def call_finder(self):
        pass

    def new_card(self, name:str, cost:str, img_path:str, body_up:str, body_deep:str, tags:str) -> None:
        if len(body_up) > 450:
            body_up = body_up[:440] + '...'
        photo = ImageTk.PhotoImage(file=img_path)

        self.card_frame = tk.Frame(self.body_frame, bg=self.COLOR_BODY)
        self.card_frame.pack(fill='both', expand=True)
        self.name_card = tk.Label(self.card_frame, text = name, font=('Arial', 16), fg = 'black', bg=self.COLOR_BODY)
        self.img_card = tk.Label(self.card_frame, text = 'loading...', image = photo)
        
        self.body_up_card = tk.Label(self.card_frame, text = body_up, font=('Arial', 10), bg = self.COLOR_BODY, anchor='nw', wraplength=400)
        self.detail_button = tk.Button(self.card_frame, text='Подробнее', font = ('Arial', 16), bg = 'white', command=self.open_card)
        self.cost_card = tk.Label(self.card_frame, text = cost + ' руб.', font=('Arial', 16), bg=self.COLOR_BODY)
        self.new_card_button = tk.Button(self.card_frame, text = 'Следющая', font=('Arial', 16), bg='white', command=self.next_card)
        self.name_card.pack(pady=10)
        # c.pack(anchor='center', pady=10)
        self.img_card.pack(pady=20)
        self.body_up_card.pack(anchor='nw', padx=10, pady=10)
        self.cost_card.pack(side='left', anchor='sw', pady=10, padx=10)
        self.detail_button.pack(side='left', anchor='s', pady=10, padx=10)
        self.new_card_button.pack(side='right', anchor='se', pady=10, padx=10)

    def open_card(self):
        self.detail_card_frame = tk.Frame(self.body_frame, bg = self.COLOR_DETAIL)
        self.detail_card_frame.pack(fill='both', expand=True)
        self.back_button = tk.Button(self.detail_card_frame, text = 'Назад', command=self.back_to_park, bg=self.COLOR_DETAIL, font=('Arial', 14))
        self.back_button.pack(side='bottom', anchor='center', pady=10)
        self.card_frame.pack_forget()

    def back_to_park(self):
        self.detail_card_frame.pack_forget()
        self.card_frame.pack(fill='both', expand=True)

    def next_card(self):
        pass



    def call_stared(self):
        pass
    
    def check_calendar(self):
        pass

    def check_map(self):
        pass
    
    def check_notifications(self):
        pass

    def check_history(self):
        pass

    def check_tickets(self):
        pass

    def on_mouse_wheel(self, event):
        """Прокрутка с помощью мыши или тачпада."""
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")


class AppGUI(MainApp):
    def __init__(self):
        super().__init__


if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(root)
    # input()

    
    app.new_card(name=f'Test name of Card - 1', cost= '500', img_path ='./pyt.png', body_up = 'Описание'*400, body_deep='Подробности', tags = '')
    root.mainloop()

    # card = AppGUI()

