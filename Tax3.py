import tkinter as tk

root = tk.Tk()

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

root.mainloop()
