
import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import os

class CustomDesktop(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Custom OS Desktop")
        self.geometry("800x600")
        
        # Загрузка фона рабочего стола
        self.desktop_image_path = "system/wallpaper/img0.jpg"
        self.load_background()

        # Создание иконок
        self.create_icon("system/icons/img1.png", self.run_fn_x, x=50, y=100)
        self.create_icon("system/icons/img2.png", self.run_browser, x=50, y=200)
        self.create_icon("system/icons/img3.png", self.run_notepad, x=50, y=300)

    def load_background(self):
        # Загрузка изображения обоев
        background_image = Image.open(self.desktop_image_path)
        background_image = background_image.resize((800, 600), Image.ANTIALIAS)  # Настройка размерности
        self.background_photo = ImageTk.PhotoImage(background_image)
        
        # Label для фона
        background_label = tk.Label(self, image=self.background_photo)
        background_label.place(relwidth=1, relheight=1)

    def create_icon(self, icon_path, command, x, y):
        # Загрузка иконки
        icon_image = Image.open(icon_path)
        icon_image = icon_image.resize((50, 50), Image.ANTIALIAS)  # Настройка размерности
        icon_photo = ImageTk.PhotoImage(icon_image)

        # Button для иконки
        icon_button = tk.Button(self, image=icon_photo, command=command, borderwidth=0, bg='white')
        icon_button.image = icon_photo  # Сохранение ссылки на изображение
        icon_button.place(x=x, y=y)

    def run_fn_x(self):
        subprocess.Popen(["python", "folder_with_scripts/FN-X.py"])

    def run_browser(self):
        subprocess.Popen(["python", "folder_with_scripts/BrowserBeta.py"])

    def run_notepad(self):
        subprocess.Popen(["python", "folder_with_scripts/notepad.py"])

if __name__ == "__main__":
    app = CustomDesktop()
    app.mainloop()
