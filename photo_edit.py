'coded by hosein-khanalizadeh'

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo , askyesno
import tkinter.filedialog as filedialog
from PIL import Image, ImageTk , ImageOps , ImageFilter , ImageEnhance , ImageDraw



class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.openimage = None

        self.title('Photo Editor')
        self.attributes('-fullscreen', True)
        self.configure(bg='#ffffff')

        self.menubar = tk.Menu(self)
        self.file = tk.Menu(self.menubar, tearoff=0 , bg='#f0f0f0' , selectcolor='#303030')
        self.menubar.add_cascade(label='فایل', menu=self.file)
        self.file.add_command(label='باز کردن...', command=self.open_picture)
        self.file.add_command(label='ذخیره', command=self.save_picture)
        self.file.add_separator()
        self.file.add_command(label='خروج', command=self.exit)
        self.config(menu=self.menubar)

        self.themes = tk.Menu(self.menubar, tearoff=0 , bg='#f0f0f0' , selectcolor='#303030')
        self.menubar.add_cascade(label='تم ها', menu=self.themes)
        self.themes.add_command(label='تاریک', command=self.dark_theme)
        self.themes.add_command(label='روشن', command=self.light_theme)
        self.themes.add_command(label='مخصوص', command=self.special_theme)
        self.themes.add_command(label='رنگین کمان', command=self.rainbow_theme)

        self.menu_lable = tk.Label(self, bg='#ebe8e8' , fg='#000000' , width=394 , height=800)
        self.menu_lable.place(x = 1500 , y = 0)

        self.firstimage_button = tk.Button(self, text='عکس اولیه 🏠' , width=50 , height=3 , bg='#bfbfbf' , fg='#171414' , activebackground='#13ba00' , command=self.first_image)
        self.firstimage_button.place(x = 1530 , y = 50)

        self.gray_button = tk.Button(self, text='سیاه سفید 🔲' , width=20 , height=3 , bg='#bfbfbf' , fg='#171414' , activebackground='#13ba00' , command=self.gray)
        self.gray_button.place(x = 1740 , y = 125)

        self.enhance_edges_button = tk.Button(self, text='تقویت لبه ها' , width=20 , height=3 , bg='#bfbfbf' , fg='#171414' , activebackground='#13ba00' , command=self.enhance_edges)
        self.enhance_edges_button.place(x = 1530 , y = 125)

        self.edges_button = tk.Button(self, text='لبه ها' , width=20 , height=3 , bg='#bfbfbf' , fg='#171414' , activebackground='#13ba00' , command=self.find_edges)
        self.edges_button.place(x = 1740 , y = 200)

        self.enhance_emboss_button = tk.Button(self, text='برجسته' , width=20 , height=3 , bg='#bfbfbf' , fg='#171414' , activebackground='#13ba00' , command=self.enhance_emboss)
        self.enhance_emboss_button.place(x = 1530 , y = 200)

        self.flip_button = tk.Button(self, text='آیینه 🪞' , width=20 , height=3 , bg='#bfbfbf' , fg='#171414' , activebackground='#13ba00' , command=self.flip)
        self.flip_button.place(x = 1740 , y = 275)

        self.up_and_down_button = tk.Button(self, text='زیر و رو' , width=20 , height=3 , bg='#bfbfbf' , fg='#171414' , activebackground='#13ba00' , command=self.up_and_down)
        self.up_and_down_button.place(x = 1530 , y = 275)

        self.blur_lable = tk.Label(self , text='بلور 💧' , width=10 , height=2 , bg='#ebe8e8' , fg='#000000')
        self.blur_lable.place(x = 1830 , y = 562)
        self.blur_scale = ttk.Scale(self, from_=0, to=14, orient=tk.HORIZONTAL ,variable=tk.DoubleVar() ,length=200 , command=self.blur)
        self.blur_scale.place(x = 1600 , y = 570)
        self.blur_scale.set(0)
        self.change_blur_button = tk.Button(self, text='تایید' , width=6 , height=2 , bg='#bfbfbf' , fg='#171414' , activebackground='#13ba00' , command=self.confirm_blur)
        self.change_blur_button.place(x = 1520 , y = 562)

        self.color_lable = tk.Label(self , text='رنگ' , width=10 , height=2 , bg='#ebe8e8' , fg='#000000')
        self.color_lable.place(x = 1830 , y = 617)
        self.color_scale = ttk.Scale(self, from_=-7, to=7, orient=tk.HORIZONTAL ,variable=tk.DoubleVar() ,length=200 , command=self.color)
        self.color_scale.place(x = 1600 , y = 625)
        self.color_scale.set(0)
        self.change_color_button = tk.Button(self, text='تایید' , width=6 , height=2 , bg='#bfbfbf' , fg='#171414' , activebackground='#13ba00' , command=self.confirm_color)
        self.change_color_button.place(x = 1520 , y = 617)

        self.brightness_lable = tk.Label(self , text='روشنایی' , width=10 , height=2 , bg='#ebe8e8' , fg='#000000')
        self.brightness_lable.place(x = 1830 , y = 672)
        self.brightness_scale = ttk.Scale(self, from_=-7, to=7, orient=tk.HORIZONTAL ,variable=tk.DoubleVar() ,length=200 , command=self.brightness)
        self.brightness_scale.place(x = 1600 , y = 680)
        self.brightness_scale.set(0)
        self.change_brightness_button = tk.Button(self, text='تایید' , width=6 , height=2 , bg='#bfbfbf' , fg='#171414' , activebackground='#13ba00' , command=self.confirm_brightness)
        self.change_brightness_button.place(x = 1520 , y = 672)

        self.contrast_lable = tk.Label(self , text='کنتراست' , width=10 , height=2 , bg='#ebe8e8' , fg='#000000')
        self.contrast_lable.place(x = 1830 , y = 727)
        self.contrast_scale = ttk.Scale(self, from_=-7, to=7, orient=tk.HORIZONTAL ,variable=tk.DoubleVar() ,length=200 , command=self.contrast)
        self.contrast_scale.place(x = 1600 , y = 735)
        self.contrast_scale.set(0)
        self.change_contrast_button = tk.Button(self, text='تایید' , width=6 , height=2 , bg='#bfbfbf' , fg='#171414' , activebackground='#13ba00' , command=self.confirm_contrast)
        self.change_contrast_button.place(x = 1520 , y = 727)

        self.rotate_lable = tk.Label(self , text='چرخش' , width=10 , height=2 , bg='#ebe8e8' , fg='#000000')
        self.rotate_lable.place(x = 1830 , y = 785)
        self.rotate_degree = ttk.Entry(width=8)
        self.rotate_degree.place(x = 1760 , y = 792)
        self.right_rotate_button = tk.Button(self, text='↩' , width=3 , height=1 , bg='#bfbfbf' , fg='#171414' , activebackground='#13ba00' , command=self.rotate_right)
        self.left_rotate_button = tk.Button(self, text='↪' , width=3 , height=1 , bg='#bfbfbf' , fg='#171414' , activebackground='#13ba00' , command=self.rotate_left)
        self.right_rotate_button.place(x=1700, y=790)
        self.left_rotate_button.place(x = 1650 , y = 790)

        self.crop_lable = tk.Label(self , text='برش' , width=10 , height=2 , bg='#ebe8e8' , fg='#000000' , font=(5))
        self.crop_lable.place(x = 1660 , y = 830)
        self.x_start_lable = tk.Label(self , text='چپ' , bg='#ebe8e8' , fg='#000000' , width=8 , height=1)
        self.y_start_lable = tk.Label(self , text='بالا' , bg='#ebe8e8' , fg='#000000' , width=8 , height=1)
        self.x_finish_lable = tk.Label(self , text='راست' , bg='#ebe8e8' , fg='#000000' , width=8 , height=1)
        self.y_finish_lable = tk.Label(self , text='پایین' , bg='#ebe8e8' , fg='#000000' , width=8 , height=1)
        self.x_start_lable.place(x = 1530 , y = 880)
        self.y_start_lable.place(x = 1730 , y = 880)
        self.x_finish_lable.place(x = 1530 , y = 905)
        self.y_finish_lable.place(x = 1730, y = 905)
        self.x_start_input = ttk.Entry(width=8)
        self.y_start_input = ttk.Entry(width=8)
        self.x_finish_input = ttk.Entry(width=8)
        self.y_finish_input = ttk.Entry(width=8)
        self.x_start_input.place(x = 1630 , y = 880)
        self.y_start_input.place(x = 1830 , y = 880)
        self.x_finish_input.place(x = 1630 , y = 905)
        self.y_finish_input.place(x = 1830 , y = 905)
        self.crop_button = tk.Button(self, text='تایید' , width=6 , height=2 , bg='#bfbfbf' , fg='#171414' , activebackground='#13ba00' , command=self.crop)
        self.crop_button.place(x = 1686 , y = 940)

        self.change_size_lable = tk.Label(self , text='تغییر سایز' , width=10 , height=2 , bg='#ebe8e8' , fg='#000000')
        self.change_size_lable.place(x = 1760 , y = 1015)
        self.decrease_size_button = tk.Button(self, text='-' , width=3 , height=1 , bg='#bfbfbf' , fg='#171414' , activebackground='#13ba00' , command=self.decrease_size)
        self.increase_size_button = tk.Button(self, text='+' , width=3 , height=1 , bg='#bfbfbf' , fg='#171414' , activebackground='#13ba00' , command=self.increase_size)
        self.decrease_size_button.place(x=1700, y=1021)
        self.increase_size_button.place(x = 1650 , y = 1021)

    def create_image_lable(self , image):
        self.x_image_lable = 1050
        self.y_image_lable = 1050
        self.image_label = tk.Label(self, image=self.image, width=self.x_image_lable, height=self.y_image_lable , bg='#ffffff')
        self.image_label.place(x=(1496 - self.x_image_lable)/2, y=(1054 - self.y_image_lable)/2)

    def open_picture(self):
        self.path = filedialog.askopenfilename()
        try:
            self.x_image = 800
            self.y_image = 800
            self.openimage = Image.open(self.path, 'r').resize((self.x_image, self.y_image))
            self.firstimage = self.openimage
            self.beforeimage = self.openimage
            self.before_contrast = self.openimage
            self.image = ImageTk.PhotoImage(self.openimage)
            self.create_image_lable(self.image)
        except:
            pass

    def save_picture(self):
        try:
            self.openimage.save(self.path+'_edited.png')
        except:
            showinfo('ارور' , 'عکسی باز نشده است !')

    def exit(self):
        self.response = askyesno('تایید خروج' , 'برای خروج مطمئن هستید ؟')
        if self.response:
            self.destroy()

    def dark_theme(self):
        self.configure(bg='#1f1f1f')
        self.file.configure(bg='#2d2d2d' , fg='#a2a2a2')
        self.themes.configure(bg='#2d2d2d' , fg='#a2a2a2')
        self.menu_lable.configure(bg='#0d0d0d' , fg='#dedede')
        self.firstimage_button.configure(bg='#171414' , fg='#bdbdbd')
        self.gray_button.configure(bg='#171414' , fg='#bdbdbd')
        self.enhance_edges_button.configure(bg='#171414' , fg='#bdbdbd')
        self.edges_button.configure(bg='#171414' , fg='#bdbdbd')
        self.enhance_emboss_button.configure(bg='#171414' , fg='#bdbdbd')
        self.flip_button.configure(bg='#171414' , fg='#bdbdbd')
        self.up_and_down_button.configure(bg='#171414' , fg='#bdbdbd')
        self.blur_lable.configure(bg='#0d0d0d' , fg='#dedede')
        self.change_blur_button.configure(bg='#171414' , fg='#bdbdbd')
        self.color_lable.configure(bg='#0d0d0d' , fg='#dedede')
        self.change_color_button.configure(bg='#171414' , fg='#bdbdbd')
        self.brightness_lable.configure(bg='#0d0d0d' , fg='#dedede')
        self.change_brightness_button.configure(bg='#171414' , fg='#bdbdbd')
        self.contrast_lable.configure(bg='#0d0d0d' , fg='#dedede')
        self.change_contrast_button.configure(bg='#171414' , fg='#bdbdbd')
        self.rotate_lable.configure(bg='#0d0d0d' , fg='#dedede')
        self.right_rotate_button.configure(bg='#171414' , fg='#bdbdbd')
        self.left_rotate_button.configure(bg='#171414' , fg='#bdbdbd')
        self.crop_lable.configure(bg='#0d0d0d', fg='#dedede')
        self.x_start_lable.configure(bg='#0d0d0d' , fg='#ededed')
        self.y_start_lable.configure(bg='#0d0d0d' , fg='#ededed')
        self.x_finish_lable.configure(bg='#0d0d0d' , fg='#ededed')
        self.y_finish_lable.configure(bg='#0d0d0d' , fg='#ededed')
        self.crop_button.configure(bg='#171414' , fg='#bdbdbd')
        self.change_size_lable.configure(bg='#0d0d0d' , fg='#dedede')
        self.decrease_size_button.configure(bg='#171414' , fg='#bdbdbd')
        self.increase_size_button.configure(bg='#171414' , fg='#bdbdbd')

    def light_theme(self):
        self.configure(bg='#ffffff')
        self.file.configure(bg='#f0f0f0', fg='#303030')
        self.themes.configure(bg='#f0f0f0', fg='#303030')
        self.menu_lable.configure(bg='#ebe8e8', fg='#000000')
        self.firstimage_button.configure(bg='#bfbfbf', fg='#171414')
        self.gray_button.configure(bg='#bfbfbf', fg='#171414')
        self.enhance_edges_button.configure(bg='#bfbfbf', fg='#171414')
        self.edges_button.configure(bg='#bfbfbf', fg='#171414')
        self.enhance_emboss_button.configure(bg='#bfbfbf', fg='#171414')
        self.flip_button.configure(bg='#bfbfbf', fg='#171414')
        self.up_and_down_button.configure(bg='#bfbfbf', fg='#171414')
        self.blur_lable.configure(bg='#ebe8e8', fg='#000000')
        self.change_blur_button.configure(bg='#bfbfbf', fg='#171414')
        self.color_lable.configure(bg='#ebe8e8', fg='#000000')
        self.change_color_button.configure(bg='#bfbfbf', fg='#171414')
        self.brightness_lable.configure(bg='#ebe8e8', fg='#000000')
        self.change_brightness_button.configure(bg='#bfbfbf', fg='#171414')
        self.contrast_lable.configure(bg='#ebe8e8', fg='#000000')
        self.change_contrast_button.configure(bg='#bfbfbf', fg='#171414')
        self.rotate_lable.configure(bg='#ebe8e8', fg='#000000')
        self.right_rotate_button.configure(bg='#bfbfbf', fg='#171414')
        self.left_rotate_button.configure(bg='#bfbfbf', fg='#171414')
        self.crop_lable.configure(bg='#ebe8e8', fg='#000000')
        self.x_start_lable.configure(bg='#ebe8e8', fg='#000000')
        self.y_start_lable.configure(bg='#ebe8e8', fg='#000000')
        self.x_finish_lable.configure(bg='#ebe8e8', fg='#000000')
        self.y_finish_lable.configure(bg='#ebe8e8', fg='#000000')
        self.crop_button.configure(bg='#bfbfbf', fg='#171414')
        self.change_size_lable.configure(bg='#ebe8e8', fg='#000000')
        self.decrease_size_button.configure(bg='#bfbfbf', fg='#171414')
        self.increase_size_button.configure(bg='#bfbfbf', fg='#171414')

    def special_theme(self):
        self.configure(bg='#307a9c')
        self.file.configure(bg='#0bba91', fg='#fffb08')
        self.themes.configure(bg='#0bba91', fg='#fffb08')
        self.menu_lable.configure(bg='#001a38', fg='#7dba0b')
        self.firstimage_button.configure(bg='#108d8f', fg='#ed0000')
        self.gray_button.configure(bg='#108d8f', fg='#ed0000')
        self.enhance_edges_button.configure(bg='#108d8f', fg='#ed0000')
        self.edges_button.configure(bg='#108d8f', fg='#ed0000')
        self.enhance_emboss_button.configure(bg='#108d8f', fg='#ed0000')
        self.flip_button.configure(bg='#108d8f', fg='#ed0000')
        self.up_and_down_button.configure(bg='#108d8f', fg='#ed0000')
        self.blur_lable.configure(bg='#001a38', fg='#7dba0b')
        self.change_blur_button.configure(bg='#108d8f', fg='#ed0000')
        self.color_lable.configure(bg='#001a38', fg='#7dba0b')
        self.change_color_button.configure(bg='#108d8f', fg='#ed0000')
        self.brightness_lable.configure(bg='#001a38', fg='#7dba0b')
        self.change_brightness_button.configure(bg='#108d8f', fg='#ed0000')
        self.contrast_lable.configure(bg='#001a38', fg='#7dba0b')
        self.change_contrast_button.configure(bg='#108d8f', fg='#ed0000')
        self.rotate_lable.configure(bg='#001a38', fg='#7dba0b')
        self.right_rotate_button.configure(bg='#108d8f', fg='#ed0000')
        self.left_rotate_button.configure(bg='#108d8f', fg='#ed0000')
        self.crop_lable.configure(bg='#001a38', fg='#7dba0b')
        self.x_start_lable.configure(bg='#001a38', fg='#7dba0b')
        self.y_start_lable.configure(bg='#001a38', fg='#7dba0b')
        self.x_finish_lable.configure(bg='#001a38', fg='#7dba0b')
        self.y_finish_lable.configure(bg='#001a38', fg='#7dba0b')
        self.crop_button.configure(bg='#108d8f', fg='#ed0000')
        self.change_size_lable.configure(bg='#001a38', fg='#7dba0b')
        self.decrease_size_button.configure(bg='#108d8f', fg='#ed0000')
        self.increase_size_button.configure(bg='#108d8f', fg='#ed0000')

    def rainbow_theme(self):
        self.configure(bg='#eb4034')
        self.file.configure(bg='#400a10', fg='#b94fc9')
        self.themes.configure(bg='#400a10', fg='#b94fc9')
        self.menu_lable.configure(bg='#f2ef22', fg='#100b40')
        self.firstimage_button.configure(bg='#1ee6aa', fg='#2e0b0a')
        self.gray_button.configure(bg='#1ee6aa', fg='#2e0b0a')
        self.enhance_edges_button.configure(bg='#1ee6aa', fg='#2e0b0a')
        self.edges_button.configure(bg='#1ee6aa', fg='#2e0b0a')
        self.enhance_emboss_button.configure(bg='#1ee6aa', fg='#2e0b0a')
        self.flip_button.configure(bg='#1ee6aa', fg='#2e0b0a')
        self.up_and_down_button.configure(bg='#1ee6aa', fg='#2e0b0a')
        self.blur_lable.configure(bg='#f2ef22', fg='#100b40')
        self.change_blur_button.configure(bg='#62de31', fg='#510373')
        self.color_lable.configure(bg='#f2ef22', fg='#100b40')
        self.change_color_button.configure(bg='#62de31', fg='#510373')
        self.brightness_lable.configure(bg='#f2ef22', fg='#100b40')
        self.change_brightness_button.configure(bg='#62de31', fg='#510373')
        self.contrast_lable.configure(bg='#f2ef22', fg='#100b40')
        self.change_contrast_button.configure(bg='#62de31', fg='#510373')
        self.rotate_lable.configure(bg='#f2ef22', fg='#100b40')
        self.right_rotate_button.configure(bg='#1d2cdb', fg='#f280ca')
        self.left_rotate_button.configure(bg='#1d2cdb', fg='#f280ca')
        self.crop_lable.configure(bg='#f2ef22', fg='#100b40')
        self.x_start_lable.configure(bg='#f2ef22', fg='#100b40')
        self.y_start_lable.configure(bg='#f2ef22', fg='#100b40')
        self.x_finish_lable.configure(bg='#f2ef22', fg='#100b40')
        self.y_finish_lable.configure(bg='#f2ef22', fg='#100b40')
        self.crop_button.configure(bg='#c90e62', fg='#ebe302')
        self.change_size_lable.configure(bg='#f2ef22', fg='#100b40')
        self.decrease_size_button.configure(bg='#ebc18f', fg='#b30600')
        self.increase_size_button.configure(bg='#ebc18f', fg='#b30600')

    def first_image(self):
        try:
            self.openimage = self.firstimage
            self.beforeimage = self.openimage
            self.image = ImageTk.PhotoImage(self.openimage)
            self.create_image_lable(self.image)
        except:
            showinfo('ارور' , 'عکسی باز نشده است !')

    def gray(self):
        try:
            self.openimage = ImageOps.grayscale(self.openimage)
            self.beforeimage = self.openimage
            self.image = ImageTk.PhotoImage(self.openimage)
            self.create_image_lable(self.image)
        except:
            showinfo('ارور' , 'عکسی باز نشده است !')

    def enhance_edges(self):
        try:
            self.openimage = self.openimage.filter(ImageFilter.EDGE_ENHANCE)
            self.beforeimage = self.openimage
            self.image = ImageTk.PhotoImage(self.openimage)
            self.create_image_lable(self.image)
        except:
            showinfo('ارور', 'عکسی باز نشده است !')

    def find_edges(self):
        try:
            self.openimage = self.openimage.filter(ImageFilter.FIND_EDGES)
            self.beforeimage = self.openimage
            self.image = ImageTk.PhotoImage(self.openimage)
            self.create_image_lable(self.image)
        except:
            showinfo('ارور', 'عکسی باز نشده است !')

    def enhance_emboss(self):
        try:
            self.openimage = self.openimage.filter(ImageFilter.EMBOSS)
            self.beforeimage = self.openimage
            self.image = ImageTk.PhotoImage(self.openimage)
            self.create_image_lable(self.image)
        except:
            showinfo('ارور', 'عکسی باز نشده است !')

    def flip(self):
        try:
            self.openimage = self.openimage.transpose(Image.FLIP_LEFT_RIGHT)
            self.beforeimage = self.openimage
            self.image = ImageTk.PhotoImage(self.openimage)
            self.create_image_lable(self.image)
        except:
            showinfo('ارور', 'عکسی باز نشده است !')

    def up_and_down(self):
        try:
            self.openimage = self.openimage.transpose(Image.FLIP_TOP_BOTTOM)
            self.beforeimage = self.openimage
            self.image = ImageTk.PhotoImage(self.openimage)
            self.create_image_lable(self.image)
        except:
            showinfo('ارور', 'عکسی باز نشده است !')

    def rotate_right(self):
        try:
            try:
                self.degree = self.rotate_degree.get()
                if int(self.degree) >= 180:
                    showinfo('ارور', 'درجه باید زیر 180 باشد !')
                else:
                    self.openimage = self.openimage.rotate(-int(self.degree))
                    self.beforeimage = self.openimage
                    self.image = ImageTk.PhotoImage(self.openimage)
                    self.create_image_lable(self.image)
            except ValueError:
                showinfo('ارور', 'لطفا عدد وارد کنید !')
        except:
            showinfo('ارور' , 'عکسی باز نشده است !')

    def rotate_left(self):
        try:
            try:
                self.degree = self.rotate_degree.get()
                if int(self.degree) >= 180:
                    showinfo('ارور', 'درجه باید زیر 180 باشد !')
                else:
                    self.openimage = self.openimage.rotate(int(self.degree))
                    self.beforeimage = self.openimage
                    self.image = ImageTk.PhotoImage(self.openimage)
                    self.create_image_lable(self.image)
            except ValueError:
                showinfo('ارور', 'لطفا عدد وارد کنید !')
        except:
            showinfo('ارور' , 'عکسی باز نشده است !')

    def blur(self , blur_value):
        if self.openimage != None:
            try:
                self.blur_value = float(blur_value)
                if self.blur_value == 0:
                    self.openimage = self.beforeimage.filter(ImageFilter.GaussianBlur(self.blur_value))
                elif self.blur_value > 0:
                    self.openimage = self.beforeimage.filter(ImageFilter.GaussianBlur(self.blur_value + 1))
                self.image = ImageTk.PhotoImage(self.openimage)
                self.create_image_lable(self.image)
            except:
                showinfo('ارور', 'عکسی باز نشده است !')
        else:
            pass

    def confirm_blur(self):
        try:
            self.blur_value = self.blur_scale.get()
            if self.blur_value == 0:
                self.openimage = self.beforeimage.filter(ImageFilter.GaussianBlur(self.blur_value))
            elif self.blur_value > 0:
                self.openimage = self.beforeimage.filter(ImageFilter.GaussianBlur(self.blur_value + 1))
            self.image = ImageTk.PhotoImage(self.openimage)
            self.create_image_lable(self.image)
            self.beforeimage = self.openimage
        except:
            showinfo('ارور', 'عکسی باز نشده است !')
        self.blur_scale.set(0)

    def color(self , color_value):
        if self.openimage != None:
            try:
                self.color_value = float(color_value)
                self.openimage = ImageEnhance.Color(self.beforeimage)
                if self.color_value == 0:
                    self.openimage = self.openimage.enhance(1)
                elif self.color_value > 0:
                    self.openimage = self.openimage.enhance(self.color_value + 1)
                elif self.color_value < 0:
                    self.openimage = self.openimage.enhance(abs(1/(self.color_value - 1)))
                self.image = ImageTk.PhotoImage(self.openimage)
                self.create_image_lable(self.image)
            except:
                showinfo('ارور', 'عکسی باز نشده است !')
        else:
            pass

    def confirm_color(self):
        try:
            self.color_value = self.color_scale.get()
            self.openimage = ImageEnhance.Color(self.beforeimage)
            if self.color_value == 0:
                self.openimage = self.openimage.enhance(1)
            elif self.color_value > 0:
                self.openimage = self.openimage.enhance(self.color_value + 1)
            elif self.color_value < 0:
                self.openimage = self.openimage.enhance(abs(1 / (self.color_value - 1)))
            self.image = ImageTk.PhotoImage(self.openimage)
            self.create_image_lable(self.image)
            self.beforeimage = self.openimage
        except:
            showinfo('ارور', 'عکسی باز نشده است !')
        self.color_scale.set(0)

    def brightness(self , brightness_value):
        if self.openimage != None:
            try:
                self.brightness_value = float(brightness_value)
                self.openimage = ImageEnhance.Brightness(self.beforeimage)
                if self.brightness_value == 0:
                    self.openimage = self.openimage.enhance(1)
                elif self.brightness_value > 0:
                    self.openimage = self.openimage.enhance(self.brightness_value + 1)
                elif self.brightness_value < 0:
                    self.openimage = self.openimage.enhance(abs(1/(self.brightness_value - 1)))
                self.image = ImageTk.PhotoImage(self.openimage)
                self.create_image_lable(self.image)
            except:
                showinfo('ارور', 'عکسی باز نشده است !')
        else:
            pass

    def confirm_brightness(self):
        try:
            self.brightness_value = self.brightness_scale.get()
            self.openimage = ImageEnhance.Brightness(self.beforeimage)
            if self.brightness_value == 0:
                self.openimage = self.openimage.enhance(1)
            elif self.brightness_value > 0:
                self.openimage = self.openimage.enhance(self.brightness_value + 1)
            elif self.brightness_value < 0:
                self.openimage = self.openimage.enhance(abs(1 / (self.brightness_value - 1)))
            self.image = ImageTk.PhotoImage(self.openimage)
            self.create_image_lable(self.image)
            self.beforeimage = self.openimage
        except:
            showinfo('ارور', 'عکسی باز نشده است !')
        self.brightness_scale.set(0)

    def contrast(self , contrast_value):
        if self.openimage != None:
            try:
                self.contrast_value = float(contrast_value)
                self.openimage = ImageEnhance.Contrast(self.beforeimage)
                if self.contrast_value == 0:
                    self.openimage = self.openimage.enhance(1)
                elif self.contrast_value > 0:
                    self.openimage = self.openimage.enhance(self.contrast_value + 1)
                elif self.contrast_value < 0:
                    self.openimage = self.openimage.enhance(abs(1 / (self.contrast_value - 1)))
                self.image = ImageTk.PhotoImage(self.openimage)
                self.create_image_lable(self.image)
            except:
                showinfo('ارور', 'عکسی باز نشده است !')
        else:
            pass

    def confirm_contrast(self):
        try:
            self.contrast_value = self.contrast_scale.get()
            self.openimage = ImageEnhance.Contrast(self.beforeimage)
            if self.contrast_value == 0:
                self.openimage = self.openimage.enhance(1)
            elif self.contrast_value > 0:
                self.openimage = self.openimage.enhance(self.contrast_value + 1)
            elif self.contrast_value < 0:
                self.openimage = self.openimage.enhance(abs(1 / (self.contrast_value - 1)))
            self.image = ImageTk.PhotoImage(self.openimage)
            self.create_image_lable(self.image)
            self.beforeimage = self.openimage
        except:
            showinfo('ارور', 'عکسی باز نشده است !')
        self.contrast_scale.set(0)

    def crop(self):
        try:
            self.x_start = self.x_start_input.get()
            self.y_start = self.y_start_input.get()
            self.x_finish = self.x_finish_input.get()
            self.y_finish = self.y_finish_input.get()
            try:
                self.openimage = self.openimage.crop((int(self.x_start) , int(self.y_start) , int(self.x_finish) , int(self.y_finish)))
                self.image = ImageTk.PhotoImage(self.openimage)
                self.create_image_lable(self.image)
            except ValueError:
                showinfo('ارور', 'لطفا عدد وارد کنید !')
        except:
            showinfo('ارور' , 'عکسی باز نشده است !')

    def decrease_size(self):
        try:
            if self.x_image > self.x_image_lable/5 and self.y_image > self.x_image_lable/5:
                self.x_image -= 50
                self.y_image -= 50
                self.openimage = self.openimage.resize((self.x_image , self.y_image))
                self.beforeimage = self.openimage
                self.image = ImageTk.PhotoImage(self.openimage)
                self.create_image_lable(self.image)
            else:
                pass
        except:
            showinfo('ارور', 'عکسی باز نشده است !')

    def increase_size(self):
        try:
            if self.x_image < self.x_image_lable and self.y_image < self.y_image_lable:
                self.x_image += 50
                self.y_image += 50
                self.openimage = self.openimage.resize((self.x_image , self.y_image))
                self.beforeimage = self.openimage
                self.image = ImageTk.PhotoImage(self.openimage)
                self.create_image_lable(self.image)
            else:
                pass
        except:
            showinfo('ارور', 'عکسی باز نشده است !')

if __name__ == "__main__":
    app = App()
    app.mainloop()
