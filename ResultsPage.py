import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from BasePage import BasePage
from out_put import click


class ResultsPage(BasePage):
    def __init__(self, parent, controller, before_page, next_page, show_frame):
        super().__init__(parent, controller, before_page, next_page, show_frame)
        self.controller = controller

        def back():
            show_frame(self.before_page)

        label = tk.Label(self, text="新料各档掺配比例为：（%）")
        label.pack(side="top", pady=10)

        self.weight_frame = tk.Frame(self)
        self.weight_frame.pack()

        # Create a canvas to display the plot
        self.plot_canvas = tk.Canvas(self, width=400, height=300)
        self.plot_canvas.pack(pady=10)

        button_frame = tk.Frame(self)
        button_frame.pack(side="bottom", pady=10, expand=True)
        results_button = tk.Button(button_frame, text="计算结果", command=self.click)
        results_button.grid(row=0, column=1, padx=10)
        back_button = tk.Button(button_frame, text="上一页", command=back)
        back_button.grid(row=0, column=0, padx=30)

    def plot_curve(self, size, weighted_indices, lb, ub):
        fig, ax = plt.subplots(figsize=(5, 4), dpi=100)

        # Replace size with an integer vector from 1 to the length of size
        size_int = []
        for _, val in enumerate(size):
            size_int.append(pow(val, 0.45))

        # Plot the curve
        ax.plot(size_int, weighted_indices, 'k--o', markersize=3)
        ax.plot(size_int, lb, 'r')
        ax.plot(size_int, ub, 'b')
        ax.set_xticks(size_int)
        ax.set_xticklabels(size, fontsize=8, rotation=60)

        # Label the points with the corresponding numbers from size
        for i, txt in enumerate(weighted_indices):
            ax.text(size_int[i], weighted_indices[i] + 1, f'{txt:.2f}', ha='right', fontsize=9,rotation=85)
        # 假设 size_int 和 weighted_indices 是已经定义好的列表
        # 设置坐标轴的限制
        ax.set_xlim([min(size_int)-0.3, max(size_int)+0.5])
        ax.set_ylim([min(weighted_indices)-8, max(weighted_indices)+20])

        # 绘制虚线
        for x, y in zip(size_int, weighted_indices):
            ax.vlines(x, ymin=min(weighted_indices)-8, ymax=y, colors=(0, 0, 0), linestyles='dotted', linewidth=0.5)
            ax.hlines(y, xmin=min(size_int)-0.3, xmax=x, colors=(0, 0, 0), linestyles='dotted', linewidth=0.4)

        if self.plot_canvas.winfo_children():
            for child in self.plot_canvas.winfo_children():
                child.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.plot_canvas)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def click(self):
        click(self)
# Copyright (c) 2024 余洪福
# Created on: 2024-04-24
# Author: 余洪福
# Contact: 15391558936
# Description: 沥青级配设计