import tkinter as tk


class BasePage(tk.Frame):
    def __init__(self, parent, controller, before_page, next_page, show_frame):
        tk.Frame.__init__(self, parent)
        self.before_page = before_page
        self.next_page = next_page
        self.controller = controller
        self.show_frame = show_frame
        self.label_list1 = ["1#", "2#", "3#", "4#", "矿粉", "水泥"]
        self.label_list0 = ["1#", "2#", "3#"]
        self.size = [26.5, 19, 16, 13.2, 9.5, 4.75, 2.36, 1.18, 0.6, 0.3, 0.15, 0.075]
