from aip import AipFace
import base64
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import *
import PIL

APP_ID = ''#baidu-api
API_KRY = ''#baidu-api
SECRET_KEY = ''#baidu-api
aFace = AipFace(APP_ID,API_KRY,SECRET_KEY)
imageType = "BASE64"

options = {}
options["face_field"] = "age,gender,beauty"

root = Tk()
root.title('颜值打分软件')
root.geometry('1200x500')
decoration = PIL.Image.open('decoration.jpg').resize((1200, 500))
render = ImageTk.PhotoImage(decoration)
img = Label(image=render)
img.image = render
img.place(x=0, y=0)
global path_


def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        content = base64.b64encode(fp.read())
        return content.decode('utf-8')

def FaceScore(filepath) :
    result = aFace.detect(get_file_content(filepath),imageType,options)
    age=result['result']['face_list'][0]['age']
    beauty=result['result']['face_list'][0]['beauty']
    sex=result['result']['face_list'][0]['gender']['type']
    return age,beauty,sex

def show_original_pic():
    global path_
    path_ = askopenfilename(title='选择文件')
    print(path_)
    Img = PIL.Image.open(r'{}'.format(path_))
    Img = Img.resize((270,270),PIL.Image.ANTIALIAS)
    img_png_original = ImageTk.PhotoImage(Img)
    label_Img_original.config(image=img_png_original)
    label_Img_original.image = img_png_original  # keep a reference
    cv_orinial.create_image(5, 5,anchor='nw', image=img_png_original)

def show_openfiles2():
    #path_ = askopenfilename(title='选择文件')
    age,score,sex = FaceScore(path_)
    age = age
    score = score
    sex = sex
    text1.delete(1.0,END)
    text1.insert(END,sex)
    text2.delete(1.0,END)
    text2.insert(END,age)
    text3.delete(1.0,END)
    text3.insert(END,score)

def quit():
    root.destroy()

def show_help():
    print('Are you serious?')


# def StartInterface(self):
Button(root,text="打开文件",command = show_original_pic).place(x=50,y=120)
Button(root,text="运行程序",command = show_openfiles2).place(x=50,y=200)#进行颜值评分
Button(root,text="现实帮助文档",command = show_help).place(x=50,y=280)
Button(root,text="退出软件",command = quit).place(x=900,y=40)

Label(text='原图',font=10).place(x=380,y=120)
label_Img_original = Label(root)
cv_orinial = Canvas(root,bg='white',width=270,height=270)
cv_orinial.create_rectangle(8,8,260,260,width=1,outline='red')
cv_orinial.place(x=260,y=150)
label_Img_original.place(x=260,y=150)

Label(root,text='性别',font=10).place(x=780,y=120)
text1 = Text(root,width=10,height=2,font=('Helvetica',10))
Label(root,text='年龄',font=10).place(x=780,y=220)
text2 = Text(root,width=10,height=2,font=('Helvetica',10))
Label(root,text='评分',font=10).place(x=780,y=320)
text3 = Text(root,width=10,height=2,font=('Helvetica',10))

text1.place(x=760,y=150)
text2.place(x=760,y=250)
text3.place(x=760,y=350)

root.mainloop()



# if __name__ == '__main__':
#     StartInterface()