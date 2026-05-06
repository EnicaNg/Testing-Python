import tkinter as tk
from tkinter import messagebox

def calculate_total():
    try:
        # 讀取輸入框的值
        price = float(entry_price.get())
        tax = float(entry_tax.get())
        # 套用公式 Total = Price * Tax
        total = price * tax
        # 顯示結果
        messagebox.showinfo("計算結果", f"Total = {total}")
    except ValueError:
        messagebox.showerror("錯誤", "請輸入正確的數字！")

root = tk.Tk()
root.title("輸入資料計算 Total")

# Label 在第 0 行第 0 欄
tk.Label(root, text="價格 Price:").grid(row=0, column=0)
# Entry 在第 0 行第 1 欄
entry_price = tk.Entry(root)
entry_price.grid(row=0, column=1)

# Label 在第 1 行第 0 欄
tk.Label(root, text="稅率 Tax:").grid(row=1, column=0)
# Entry 在第 1 行第 1 欄
entry_tax = tk.Entry(root)
entry_tax.grid(row=1, column=1)

# 計算按鈕在第 2 行
tk.Button(root, text="計算 Total", command=calculate_total).grid(row=2, column=0, columnspan=2)

root.mainloop()
