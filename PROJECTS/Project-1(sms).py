import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror

def SendSms(num,msg):
    url = "https://www.fast2sms.com/dev/bulkV2"
    params = {

        "authorization" : 'A1vn0i9DgZCYyB2rWIpSfO6etoUHL5VNEXQ8xqMKkm43FcJhjd6GRgeFnjM8bPZKdT5Op9DUfrzv1ayl',
        "sender_id" : 'TXTIND',
        "message":msg,
        "language":'english',
        "route":'v3',
        "numbers":num


    }

    response = requests.get(url,params=params)
    dict = response.json()
    # print(dict)
    return dict.get("return")
# SendSms("8435858587","Hello Surbhi")

def Btn_click():

    num = textNumber.get()
    msg = textMsg.get("1.0",END)
    r = SendSms(num,msg)
    
    if r:
        showinfo('Message Sent',"Successfully Sent")
    
    else:
        showerror('error','Something went wrong...')


# gui
root = Tk()
root.title("Message Sender")
root.geometry("400x550")
font = ("Helvetica", 22, "bold")
textNumber = Entry(root,font=font)
textNumber.pack(fill = X,pady=10)
textMsg = Text(root)
textMsg.pack(fill=X)
sendBtn = Button(root,text="Send SMS",command=Btn_click)
sendBtn.pack(pady=20)


root.mainloop()# always in last to run program