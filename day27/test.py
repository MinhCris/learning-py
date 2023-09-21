
import tkinter as tk

# Tạo một cửa sổ
window = tk.Tk()

# Tạo một nút
button = tk.Button(window, text="Click Me")

# Định vị và hiển thị nút bằng pack()
button.pack()

# Tạo một nhãn
label = tk.Label(window, text="Hello, World!")

# Định vị và hiển thị nhãn bằng pack()
label.pack()

# Chạy vòng lặp chính của ứng dụng
window.mainloop()


# *arg ra tuple
# **kw ra dic