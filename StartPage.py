import tkinter as tk
from BasePage import BasePage

class StartPage(BasePage):
    def __init__(self, parent, controller, before_page,next_page,show_frame):
        super().__init__(parent, controller, before_page, next_page, show_frame)
        self.rap = tk.DoubleVar(value=30)
        # label
        label = tk.Label(self, text="请输入RAP的值（%）:")
        label.pack(anchor="center", pady=40)
        # entry
        rap_entry = tk.Entry(self, textvariable=self.rap)
        rap_entry.pack(pady=20)

        # submit
        def on_submit():
            show_frame(self.next_page)

        submit_button = tk.Button(self, text="提交", command=on_submit)
        submit_button.pack(pady=40)

# Copyright (c) 2024 余洪福
# Created on: 2024-04-24
# Author: 余洪福
# Contact: 15391558936
# Description: 沥青级配设计