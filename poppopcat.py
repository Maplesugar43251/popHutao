# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:00:30 2024

@author: user
"""

import tkinter as tk
from PIL import Image, ImageTk

#創建主視窗
w = tk.Tk()
w.title("Popcat pointgame")
w.geometry("400x500")
w.resizable(False, False)


# 載入圖片
closed_mouth_image = ImageTk.PhotoImage(Image.open("closed_mouth.jpg").resize((300,300)))
open_mouth_image = ImageTk.PhotoImage(Image.open("open_mouth.jpg").resize((300,300)))

# 顯示圖片的標籤
cat_label = tk.Label(w, image=closed_mouth_image)
cat_label.pack(pady=20)

# 顯示計數的標籤
count_label = tk.Label(w, text="點擊次數: 0",font=("Arial",18))
count_label.pack(pady=10)

# 初始化計數器
click_count = 0

# 更新點擊次數的函數
def update_count():
    global click_count
    click_count += 1
    count_label.config(text=f"點擊次數: {click_count}")
    
# 切換到張嘴圖片並更新點擊次數
def on_click(event):
    cat_label.config(image=open_mouth_image)
    w.after(200, lambda: cat_label.config(image=closed_mouth_image)) #200毫秒後切回閉嘴圖片
    update_count()

# 綁定點擊事件
cat_label.bind("<Button-1>",on_click)

# 重置計數器
def reset_count():
    global click_count
    click_count = 0
    count_label.config(text="點擊次數: 0")
    
# 重置按鈕
reset_button = tk.Button(w, text="重置", command=reset_count, font=("Arial",14), bg="lightblue")
reset_button.pack(pady=10)

w.mainloop()






