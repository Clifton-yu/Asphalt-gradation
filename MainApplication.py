import tkinter as tk
from tkinter import messagebox
import sys
from StartPage import StartPage
from OldMaterialPage import OldMaterialPage
from NewAggregatePage import NewAggregatePage
from RequirementsPage import RequirementsPage
from ResultsPage import ResultsPage


class MainApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("大比例再生沥青混合料新-旧集料级配设计优化系统")
        container = tk.Frame(self)
        container.pack(padx=30, pady=30, expand=True)
        self.frames = {}

        for F in (StartPage, OldMaterialPage, NewAggregatePage, RequirementsPage, ResultsPage):
            frame = F(container, self, None, None, show_frame=self.show_frame)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        pages = [StartPage, OldMaterialPage, NewAggregatePage, RequirementsPage, ResultsPage]
        for arg, F in enumerate(pages):
            if F == StartPage:
                self.frames[F].before_page = None
                self.frames[F].next_page = pages[arg + 1]
            elif F == ResultsPage:
                self.frames[F].before_page = pages[arg - 1]
                self.frames[F].next_page = None
            else:
                self.frames[F].before_page = pages[arg - 1]
                self.frames[F].next_page = pages[arg + 1]
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == "__main__":
    app = MainApplication()



    def on_closing():
        if messagebox.askokcancel("Quit", "Please verify to quit!"):
            app.destroy()
            sys.exit(0)


    app.protocol('WM_DELETE_WINDOW', on_closing)
    app.mainloop()


# pyinstaller -F -n 大比例再生沥青混合料新-旧集料级配设计优化 -w MainApplication.py -i jp1.ico
# datas=['test.xlsx','test_旧料','test_新料','test_级配要求'],
# Copyright (c) 2024 余洪福
# Created on: 2024-04-24
# Author: 余洪福
# Contact: 15391558936
# Description: 沥青级配设计
