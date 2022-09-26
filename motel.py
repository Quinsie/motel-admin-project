import tkinter
import tkinter.font
import time

# room frame
class room:
    def __init__(self, window, a, b):
        # initialize
        self.pos_x = a
        self.pos_y = b
        self.flag = 0
        self.start_time = -1
        self.type = 0 # 0 = normal, 1 = suite

        self.block = tkinter.Frame(window, relief = "solid")
        self.block.pack()
        self.square = tkinter.Button(self.block, width = 15, height = 8, anchor = "n", bg = "#C4C4C4", activebackground = "#C4C4C4",
                                     relief = "flat", overrelief = "flat", bd = 0, command = self.display_info)
        self.square.pack()
        self.name_font = tkinter.font.Font(family = "Noto Sans KR", size = 10)
        self.name = tkinter.Label(self.block, text = str((a * 100) + b) + "호",  anchor = "n", bg = "#C4C4C4", font = self.name_font)
        self.name.place(x = 36, y = 1)
        
        self.status_box = tkinter.Menubutton(self.block, width = 12, height = 1, background = "#FFFFFF", direction = "right")
        self.status_box.place(x = 8, y = 27)
        self.status_menu = tkinter.Menu(self.status_box, tearoff = 0)
        self.status_menu.add_command(label = "빈  방", command = self.to_void)
        self.status_menu.add_command(label = "대  실", command = self.to_rent)
        self.status_menu.add_command(label = "숙  박", command = self.to_sleep)
        self.status_box["menu"] = self.status_menu
        self.status_font = tkinter.font.Font(family = "Noto Sans KR Black", size = 13)
        self.status_name = tkinter.Label(self.status_box, text = "빈   방", background = "#FFFFFF", font = self.status_font)
        self.status_name.place(x = 21, y = -4)
        
        if b < 4:  self.block.place(x = 215 + (b - 1) * 117, y = 560 - (a - 2) * 133)
        else : self.block.place(x = 215 + (b - 2) * 117, y = 560 - (a - 2) * 133)
    
    def room_config(self):
        # new window base settings
        global new_window
        new_window = tkinter.Toplevel()
        new_window.title("객실 정보 입력")
        new_window.geometry("640x480")
        new_window.configure(background = "white")
        
        room_name = tkinter.Label(new_window, font = ("Noto Sans KR Black", 18, "bold"), bg = "white")
        if self.flag == 1:  room_name.config(text = str(self.pos_x * 100 + self.pos_y) + "호 대실 정보 입력")
        if self.flag == 2:  room_name.config(text = str(self.pos_x * 100 + self.pos_y) + "호 숙박 정보 입력")
        room_name.place(x = 215, y = 5)
        
        
        
    
    def to_void(self):
        self.square.config(bg = "#C4C4C4", activebackground = "#C4C4C4")
        self.name.config(bg = "#C4C4C4")
        self.status_name.config(text = "빈   방")
        
        change_void(self.flag)
        self.flag = 0
        self.start_time = -1
    
    def to_rent(self):
        self.square.config(bg = "#9ECCFF", activebackground = "#9ECCFF")
        self.name.config(bg = "#9ECCFF")
        self.status_name.config(text = "대   실")
        
        change_rent(self.flag)
        self.flag = 1
        
        self.room_config()
    
    def to_sleep(self):
        self.square.config(bg = "#FF9E9E", activebackground = "#FF9E9E")
        self.name.config(bg = "#FF9E9E")
        self.status_name.config(text = "숙   박")
        
        change_sleep(self.flag)
        self.flag = 2
        
        self.room_config()

    def display_info(self):
        display_room_info(self.pos_x, self.pos_y, self.flag)


def clock(): # 현재 시간 표시 / 반복
    live_D = time.strftime("%y-%m-%d")
    live_T = time.strftime("%H:%M:%S") # Real Time
    clock_date.config(text=live_D)
    clock_width.config(text=live_T)
    clock_width.after(200, clock) # .after(지연시간{ms}, 실행함수)
    
def close():
    window.quit()
    window.destroy()

def change_void(flag):
    global void_room, rent_room, sleep_room
    
    if flag == 1:
        void_room += 1
        rent_room -= 1
        room_status_value_void.config(text = str(void_room))
        room_status_value_rent.config(text = str(rent_room))
    elif flag == 2:
        void_room += 1
        sleep_room -= 1
        room_status_value_void.config(text = str(void_room))
        room_status_value_sleep.config(text = str(sleep_room))

def change_rent(flag):
    global void_room, rent_room, sleep_room
    
    if flag == 0:
        rent_room += 1
        void_room -= 1
        room_status_value_void.config(text = str(void_room))
        room_status_value_rent.config(text = str(rent_room))
    elif flag == 2:
        rent_room += 1
        sleep_room -= 1
        room_status_value_rent.config(text = str(rent_room))
        room_status_value_sleep.config(text = str(sleep_room))

def change_sleep(flag):
    global void_room, rent_room, sleep_room
    
    if flag == 0:
        sleep_room += 1
        void_room -= 1
        room_status_value_void.config(text = str(void_room))
        room_status_value_sleep.config(text = str(sleep_room))
    elif flag == 1:
        sleep_room += 1
        rent_room -= 1
        room_status_value_void.config(text = str(void_room))
        room_status_value_rent.config(text = str(rent_room))

def display_room_info(a, b, flag):
    displayer_now_room.config(text = str(a * 100 + b) + " 호")

    if flag == 0: displayer_status.config(text = "빈   방", fg = "black")
    elif flag == 1: displayer_status.config(text = "대   실", fg = "blue")
    else: displayer_status.config(text = "숙   박", fg = "red")
    
        
if __name__ == "__main__":
    # initialize
    total_room = 45
    void_room = 45
    rent_room = 0
    sleep_room = 0

    rent_price = 20000
    sleep_price = 50000
    
    
    # basic window
    window = tkinter.Tk()
    window.title("객실 관리")
    window.geometry("1280x720+100+100")
    window.configure(background = "#E5F0FF")
    window.resizable(False, False)

    
    # live clock
    clock_frame = tkinter.Frame(window)
    clock_frame.pack()
    clock_background = tkinter.Label(clock_frame, bg = "#BCDAFF", width = 23, height = 5)
    clock_background.pack()
    clock_frame.place(x = 25, y = 28)

    clock_width = tkinter.Label(clock_background, font = ("Times", 24, "bold"), bg = "#BCDAFF", bd = 8)
    clock_width.place(x = 15, y = 23)
    clock_date = tkinter.Label(clock_background, font = ("Times", 12, "bold"), bg = "#BCDAFF", bd = 8)
    clock_date.place(x = 15, y = 3)

    # time_txt_font = tkinter.font.Font(family = "Noto Sans KR", size = 9)
    # time_txt_width = tkinter.Label(clock_background, text = "현재 시간", bg = "#E5F0FF", font = time_txt_font)
    # time_txt_width.place(x = 55, y = -1)
    
    clock()
    

    # room status
    room_status_font = tkinter.font.Font(family = "Noto Sans KR", size = 10)
    room_status_txt_frame = tkinter.Frame(window)
    room_status_txt_frame.pack()
    room_status_txt_window = tkinter.Label(room_status_txt_frame, background = "#BCDAFF", width = 23, height = 8)
    room_status_txt_window.pack()
    room_status_txt_frame.place(x = 25, y = 120)
    
    room_status_txt_total = tkinter.Label(room_status_txt_window, background = "#BCDAFF", text = "총  객실   : ", font = room_status_font)
    room_status_txt_total.place(x = 25, y = 5)
    room_status_value_total = tkinter.Label(room_status_txt_window, background = "#BCDAFF", text = str(total_room), font = room_status_font)
    room_status_value_total.place(x = 100, y = 5)
    
    room_status_txt_void = tkinter.Label(room_status_txt_window, background = "#BCDAFF", text = "빈     방   : ", fg = "green", font = room_status_font)
    room_status_txt_void.place(x = 25, y = 33)
    room_status_value_void = tkinter.Label(room_status_txt_window, background = "#BCDAFF", text = str(void_room), fg = "green", font = room_status_font)
    room_status_value_void.place(x = 100, y = 33)
    
    room_status_txt_rent = tkinter.Label(room_status_txt_window, background = "#BCDAFF", text = "대     실   : ", fg = "blue", font = room_status_font)
    room_status_txt_rent.place(x = 25, y = 61)
    room_status_value_rent = tkinter.Label(room_status_txt_window, background = "#BCDAFF", text = str(rent_room), fg = "blue", font = room_status_font)
    room_status_value_rent.place(x = 100, y = 61)
    
    room_status_txt_sleep = tkinter.Label(room_status_txt_window, background = "#BCDAFF", text = "숙     박   : ", fg = "red", font = room_status_font)
    room_status_txt_sleep.place(x = 25, y = 89)
    room_status_value_sleep = tkinter.Label(room_status_txt_window, background = "#BCDAFF", text = str(sleep_room), fg = "red", font = room_status_font)
    room_status_value_sleep.place(x = 100, y = 89)

    
    # top menu (dummy)
    menubar = tkinter.Menu(window, bg = "#BAD7FF", relief = "flat")

    menu_1 = tkinter.Menu(menubar, tearoff = 0)
    menu_1.add_command(label = "   열기  ", state = "disable")
    menu_1.add_command(label = "   저장  ", state = "disable")
    menu_1.add_separator()
    menu_1.add_command(label = "   종료  ", command = close)
    menubar.add_cascade(label = "   파일   ", menu = menu_1)

    menu_2 = tkinter.Menu(menubar, tearoff = 0)
    menu_2.add_command(label = "   실행 취소  ", state = "disable")
    menu_2.add_command(label = "   찾기  ", state = "disable")
    menu_2.add_command(label = "   바꾸기  ", state = "disable")
    menubar.add_cascade(label = "   편집   ", menu = menu_2)

    menu_3 = tkinter.Menu(menubar, tearoff = 0)
    menu_3.add_checkbutton(label = "   확장  ", state = "disable")
    menu_3.add_checkbutton(label = "   전체 화면  ", state = "disable")
    menubar.add_cascade(label = "   보기   ", menu = menu_3)

    menu_4 = tkinter.Menu(menubar, tearoff=0)
    menu_4.add_command(label = "   시작하기  ", state = "disable")
    menu_4.add_command(label = "   설명서  ", state = "disable")
    menu_4.add_separator()
    menu_4.add_command(label = "   릴리스 정보  ", state = "disable")
    menubar.add_cascade(label = "   도움말   ", menu = menu_4)

    window.config(menu = menubar)
    

    # price adjust button (left mid)
    price_adjust = tkinter.Frame(window)
    price_adjust.pack()
    price_adjust_window = tkinter.Label(price_adjust, background = "#BCDAFF", width = 23, height = 6)
    price_adjust_window.pack()
    price_adjust.place(x = 25, y = 257)
    price_adjust_title = tkinter.Label(price_adjust_window, background = "#BCDAFF", text = "요금 조정", font = ("Noto Sans KR", 10))
    price_adjust_title.place(x = 53, y = 0)

    normal_rent_button = tkinter.Button(price_adjust_window, width = 9, height = 1, text = "일반 대실", font = ("Noto Sans KR", 8, "bold"))
    normal_rent_button.place(x = 6, y = 29)
    normal_sleep_button = tkinter.Button(price_adjust_window, width = 9, height = 1, text = "일반 숙박", font = ("Noto Sans KR", 8, "bold"))
    normal_sleep_button.place(x = 6, y = 60)
    suite_rent_button = tkinter.Button(price_adjust_window, width = 9, height = 1, text = "특실 대실", font = ("Noto Sans KR", 8, "bold"))
    suite_rent_button.place(x = 85, y = 29)
    suite_sleep_button = tkinter.Button(price_adjust_window, width = 9, height = 1, text = "특실 숙박", font = ("Noto Sans KR", 8, "bold"))
    suite_sleep_button.place(x = 85, y = 60)

    # display room info (left below)
    displayer = tkinter.Frame(window)
    displayer.pack()
    displayer_window = tkinter.Label(displayer, background = "#BCDAFF", width = 23, height = 21)
    displayer_window.pack()
    displayer_inside_window = tkinter.Label(displayer_window, background = "white", width = 20, height = 18)
    displayer_inside_window.place(x = 8, y = 30)
    displayer.place(x = 25, y = 365)
    displayer_title = tkinter.Label(displayer_window, background = "#BCDAFF", text = "객실 정보", font = ("Noto Sans KR", 10))
    displayer_title.place(x = 53, y = 2)

    displayer_room_name_font = tkinter.font.Font(family = "Noto Sans KR Black", size = 12)
    displayer_default_font = tkinter.font.Font(family = "Noto Sans KR", size = 10)

    displayer_now_room = tkinter.Label(displayer_inside_window, bg = "white", text = "000 호", font = displayer_room_name_font)
    displayer_now_room.place(x = 43, y = 3)
    displayer_status_title = tkinter.Label(displayer_inside_window, bg = "white", text = "상태 : ", font = displayer_default_font)
    displayer_status_title.place(x = 15, y = 35)
    displayer_status = tkinter.Label(displayer_inside_window, bg = "white", text = "빈   방", font = displayer_default_font)
    displayer_status.place(x = 75, y = 35)
    

    # room initialize
    building = []
    for i in range(2, 7):
        building.append([])
        for j in range(1, 11):
            if j == 4: continue
            building[i - 2].append(room(window, i, j))
    
    
    window.mainloop()
