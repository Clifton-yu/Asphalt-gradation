import numpy as np
from entry2np import entry2np
from optimize import optimize
import tkinter as tk
from StartPage import StartPage
from OldMaterialPage import OldMaterialPage
from NewAggregatePage import NewAggregatePage
from RequirementsPage import RequirementsPage
from tkinter import messagebox


def click(self):
    # obtain parameters
    rap = self.controller.frames[StartPage].rap.get()
    weights0 = entry2np(self.controller.frames[OldMaterialPage].weights0)[0]
    indices1 = entry2np(self.controller.frames[OldMaterialPage].indices)
    indices2 = entry2np(self.controller.frames[NewAggregatePage].indices)
    weights1 = entry2np(self.controller.frames[NewAggregatePage].weights1)[0]
    bounds = entry2np(self.controller.frames[RequirementsPage].bounds)
    ub = bounds[0, :]
    lb = bounds[1, :]
    label_list1 = self.label_list1.copy()
    label_list0 = self.label_list0.copy()
    size = self.size.copy()
    j = 0
    for i in range(indices1.shape[1]):
        if int(np.sum(indices1[:, i - j])) == int(100 * indices1.shape[0]):
            indices1 = np.delete(indices1, i - j, axis=1)
            weights0 = np.delete(weights0, i - j)
            del label_list0[i - j]
            j += 1
    weights0 = weights0 / (0.000000001 + np.sum(weights0))
    j = 0
    m = indices2.shape[1]
    for i in range(indices2.shape[1]):
        if int(np.sum(indices2[:, i - j])) == int(100 * indices2.shape[0]):
            indices2 = np.delete(indices2, i - j, axis=1)
            del label_list1[i - j]
            if i >= m - 2:
                weights1 = np.delete(weights1, i - m + weights1.shape[0])
            j += 1
    j = 0
    for i in range(indices2.shape[0]):
        if int(np.sum(indices2[i - j, :])) == int(100 * indices2.shape[1]) and int(np.sum(indices1[i - j, :])) == int(
                100 * indices1.shape[1]):
            indices2 = np.delete(indices2, i - j, axis=0)
            indices1 = np.delete(indices1, i - j, axis=0)
            ub = np.delete(ub, i - j)
            lb = np.delete(lb, i - j)
            del size[i - j]
            j += 1

    grade_texts1 = []
    grade_texts0 = []
    for widget in self.weight_frame.winfo_children():
        widget.destroy()
    for i, str_val in enumerate(label_list1):
        grade_label = tk.Label(self.weight_frame, text=str_val)
        grade_label.grid(row=0 if i <= len(label_list1) - weights1.shape[0] - 1 else 4,
                         column=i + 1 if i <= len(label_list1) - weights1.shape[0] - 1 else int(i - len(label_list1) +
                                                                                                weights1.shape[0] + 1),
                         padx=10)

        grade_text = tk.Text(self.weight_frame, height=1, width=10)
        grade_text.grid(row=1 if i <= len(label_list1) - weights1.shape[0] - 1 else 5,
                        column=i + 1 if i <= len(label_list1) - weights1.shape[0] - 1 else int(i - len(label_list1) +
                                                                                               weights1.shape[0] + 1),
                        padx=10, pady=10)
        grade_texts1.append(grade_text)
    grade_label = tk.Label(self.weight_frame, text=f"新料掺配比({100 - rap - np.sum(weights1)})：")
    grade_label.grid(row=1, column=0, padx=10)

    for i, str_val in enumerate(label_list0):
        grade_label = tk.Label(self.weight_frame, text=str_val)
        grade_label.grid(row=2, column=i + 1, padx=10)

        grade_text = tk.Text(self.weight_frame, height=1, width=10)
        grade_text.grid(row=3, column=i + 1, padx=10, pady=10)
        grade_texts0.append(grade_text)
    grade_label = tk.Label(self.weight_frame, text=f"旧料掺配比({rap})：")
    grade_label.grid(row=3, column=0, padx=10)
    grade_label = tk.Label(self.weight_frame, text="矿粉、水泥绝对掺量：")
    grade_label.grid(row=5, column=0, padx=10)
    # Perform calculation here and update label_results
    weights = optimize(rap, weights0, indices1.T, indices2.T, ub, lb, weights1, 50)
    if weights == 0:
        messagebox.showinfo("请重新输入！", "请在新料界面填入筛分参数！")
    else:
        if not weights.success:
            messagebox.showinfo("优化失败！", "请调整rap或水泥、矿粉掺量！")
        weights = weights.x
        weighted_indices = np.dot(weights[indices2.T.shape[0] - weights1.shape[0]:], indices1.T) + np.dot(
            weights[:indices2.T.shape[0] - weights1.shape[0]], indices2.T[:-weights1.shape[0], :]) + np.dot(
            weights1 / 100, indices2.T[indices2.T.shape[0] - weights1.shape[0]:, :])
        sum_new = np.sum(weights[:len(label_list1) - weights1.shape[0]])
        sum_old = np.sum(weights[len(label_list1) - weights1.shape[0]:])
        print(weights*100)
        for i in range(weights.shape[0]):
            if i < len(label_list1) - weights1.shape[0]:
                weights[i] = weights[i] / sum_new
                grade_texts1[i].delete(1.0, "end")
                grade_texts1[i].insert("end", str(round(weights[i] * 100, 2)))
            else:
                weights[i] = weights[i] / sum_old
                grade_texts0[i - len(label_list1) + weights1.shape[0]].delete(1.0, "end")
                grade_texts0[i - len(label_list1) + weights1.shape[0]].insert("end", str(round(weights[i] * 100, 2)))
        grade_texts1[-1].insert("end", str(round(weights1[-1])))
        grade_texts1[-2].insert("end", str(round(weights1[-2])))
        self.plot_curve(size, weighted_indices, lb, ub)
