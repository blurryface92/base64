from __init__ import *

app = Tk()
app.title("does things")
app.geometry("150x150")

app.configure(bg="black")

def encrypt(file):
    with open(file,'r') as f:
        data = f.read()
        file_content = b64encode(data.encode('utf-8'))
        with open("encrypted_file.txt",'w+') as f2:
            f2.write(file_content.decode('utf-8'))

def decrypt(file):
    with open(file,'r') as f:
        data = f.read()
        file_content = b64decode(data.encode('utf-8'))
        with open("decrypted_file.txt",'w+') as f2:
            f2.write(file_content.decode('utf-8'))

def generate(file):
    with open(file,'r') as f:
        passwd = f.read()
        with open('hashed.txt','w+') as f:
            f.write(generate_password_hash(passwd,method='sha256'))
    
def check(file):
    with open(file,'r') as f:
        hashed = f.read()
        with open('unhashed.txt','w+') as f:
            f.write(check_password_hash(hashed,'password'))


frame = Frame(app,bg="black")
frame.pack(fill=BOTH,expand=True)

app_title = Label(frame,text="OwO",bg="black",fg="green",font=("Fira Code",12))
app_title.pack(fill=X)

btn_1 = Button(frame,text="B64 Encrypt",command=lambda: encrypt(askopenfilename(filetypes=[("Text Files","*.txt")])))
btn_1.pack(side=BOTTOM,fill=X)

btn_2 = Button(frame,text="B64 Decrypt",command=lambda: decrypt(askopenfilename(filetypes=[("Text Files","*.txt")])))
btn_2.pack(side=BOTTOM,fill=X)

btn_3 = Button(frame,text="SHA256 Encyption",command=lambda: generate(askopenfilename(filetypes=[("Text Files","*.txt")])))
btn_3.pack(side=BOTTOM,fill=X)


app.mainloop()