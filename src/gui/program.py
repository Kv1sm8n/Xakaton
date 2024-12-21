import tkinter as tk
from tkhtmlview import HTMLLabel, RenderHTML
import requests
from PIL import ImageTk, Image
from io import BytesIO


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
        self.cards = []



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


        self.find_button = tk.Button(self.head_frame, text='Фильтр',command = self.search_cards, bg = self.COLOR_HEAD)
        self.find_button.pack(side=tk.RIGHT, padx=5)
        self.find_enter = tk.Entry(self.head_frame, bg = self.COLOR_HEAD, justify='left', font=('Arial', 14), fg= 'black', show='')
        self.find_enter.pack(side=tk.RIGHT, padx=5)



        self.body_frame = tk.Frame(self.main_frame, bg=self.COLOR_BODY)
        self.body_frame.pack(fill='both', expand=True)

       #!!!
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
        # self.create_cards()

        # Обработчик событий для прокрутки с помощью тачпада
        self.root.bind_all("<MouseWheel>", self.on_mouse_wheel)
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
        #!!!!!!!!!!!!!!!!!!!!!
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


    def search_cards(self):
        query = self.find_enter.get().lower()  # Получаем текст из поля ввода и приводим к нижнему регистру
        for card_name, card_text, tags, card in self.cards:
            if query in card_text.lower() or query in card_name.lower() or query in tags.lower():  # Проверяем наличие текста в карточке
                card.pack(pady=5, padx=10, fill=tk.X)  # Показываем карточку
            else:
                card.pack_forget()  # Скрываем карточку

    def new_card(self, name:str, cost:str, img_path:str, body:str, tags:str) -> None:
        if len(body) > 450:
            body = body[:440] + '...'
        photo = ImageTk.PhotoImage(file=img_path)

        card_frame = tk.Frame(self.scrollable_frame, bg=self.COLOR_BODY)
        card_frame.pack(fill='both', expand=True)
        name_card = tk.Label(card_frame, text = name, font=('Arial', 16), fg = 'black', bg=self.COLOR_BODY)
        img_card = tk.Label(card_frame, text = 'loading...', image = photo)
        
        body_card = tk.Label(card_frame, text = body, font=('Arial', 10), bg = self.COLOR_BODY, anchor='nw', wraplength=400)
        detail_button = tk.Button(card_frame, text='Подробнее', font = ('Arial', 16), bg = 'white', command=self.open_card)
        cost_card = tk.Label(card_frame, text = cost + ' руб.', font=('Arial', 16), bg=self.COLOR_BODY)
        # self.new_card_button = tk.Button(self.card_frame, text = 'Следющая', font=('Arial', 16), bg='white', command=self.next_card)
        name_card.pack(pady=10)
        # c.pack(anchor='center', pady=10)
        img_card.pack(pady=20)
        body_card.pack(anchor='nw', padx=10, pady=10)
        cost_card.pack(side='left', anchor='sw', pady=10, padx=10)
        detail_button.pack(side='left', anchor='s', pady=10, padx=10)
        # self.new_card_button.pack(side='right', anchor='se', pady=10, padx=10)
        self.cards.append((name, body, tags, card_frame))



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

    for i in range(25):
        app.new_card(name=f'Test name of Card - {i}', cost= '500', img_path ='./pyt.png', body = 'Описание'*400, tags = '')
    root.mainloop()

    # card = AppGUI()

