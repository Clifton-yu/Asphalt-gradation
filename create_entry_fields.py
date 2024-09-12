import tkinter as tk


def create_entry_fields(self):
    label = tk.Label(self, text=self.material + "通过率/\n      筛孔尺寸")
    label.grid(row=1, column=0)
    for i, col in enumerate(self.label_list):
        label = tk.Label(self, text=col)
        label.grid(row=1, column=i + 1)

    for i, row in enumerate(self.size):
        label = tk.Label(self, text=str(row) + "mm")
        label.grid(row=i + 2, column=0)

        row_vars = [tk.DoubleVar(value=100) for j in range(len(self.label_list))]
        self.indices.append(row_vars)

        for j, var in enumerate(row_vars):
            entry = tk.Entry(self, textvariable=var)
            entry.grid(row=i + 2, column=j + 1)