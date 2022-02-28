import tkinter as tk
from PIL import Image,ImageTk

#画像の読み込みとサイズを取得
im = Image.open('red.png') #デザイン用画像
w = int(im.width)
h = int(im.height)

#キャンバスオブジェクトの作成
root = tk.Tk()
root.title("pixture")

canvas = tk.Canvas(root,width=w+50, height=h+50)

#キャンバスに画像を表示させる
tk_im = ImageTk.PhotoImage(image=im)
canvas.create_image(0,0, anchor='nw',image=tk_im)

#ボタンの操作、処理
def logo():
    im1 = im.copy()
    im2 = Image.open('logo.png').convert('L') #カリグラフィー用画像画像
    im1.putalpha(im2)
    im1.save('calligraphy.png')

button = tk.Button(text='作成',command=logo)

#ウィジェットの配置
canvas.pack()
button.pack()
canvas.mainloop()

