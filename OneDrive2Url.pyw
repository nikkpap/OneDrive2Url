from tkinter import *
from tkinter import messagebox
import re

#right click context menu for all Tk Entry and Text widgets
def rClicker(e):


    try:
        def rClick_Copy(e, apnd=0):
            e.widget.event_generate('<Control-c>')

        def rClick_Cut(e):
            e.widget.event_generate('<Control-x>')

        def rClick_Paste(e):
            e.widget.event_generate('<Control-v>')

        e.widget.focus()

        nclst=[
               (' Cut', lambda e=e: rClick_Cut(e)),
               (' Copy', lambda e=e: rClick_Copy(e)),
               (' Paste', lambda e=e: rClick_Paste(e)),
               ]

        rmenu = Menu(None, tearoff=0, takefocus=0)

        for (txt, cmd) in nclst:
            rmenu.add_command(label=txt, command=cmd)

        rmenu.tk_popup(e.x_root+40, e.y_root+10,entry="0")

    except TclError:
        print (' - rClick menu, something wrong')
        pass

    return "break"


def rClickbinder(r):

    try:
        for b in [ 'Text', 'Entry', 'Listbox', 'Label']: #
            r.bind_class(b, sequence='<Button-3>',
                         func=rClicker, add='')
    except TclError:
        print (' - rClickbinder, something wrong')
        pass




def conv_onedrive():
    try:
        strip_html= re.search("src=\"(.*)\" width", textBox1.get() )
        conv_onedrive_html= strip_html[1].replace('embed','download')
        
        textBox2Entry.set(str(conv_onedrive_html))
       
        print(conv_onedrive_html)
        
    except: 
        messagebox.showwarning("Null or Wrong Url...", "Please check your input")
        #print("error")


def about():
    lines = ['OneDrive Direct Download Url Maker v1.0', '                    by nikkpap', 'nikkpap@gmail.com | ALU DEV TEAM']
    messagebox.showinfo("About","\n".join(lines))
    
def close_window0(): 
    window0.destroy()



#<iframe src="https://onedrive.live.com/embed?cid=167101805E8FAB03&resid=167101805E8FAB03%2155904&authkey=ADWla2Q4PDNdRdA" width="98" height="120" frameborder="0" scrolling="no"></iframe>


  
window0= Tk()
window0.title("OneDrive Direct Download Url Maker v1.0")
window0.geometry("800x100")
window0.resizable(False, False)

btnConvOnedrive=Button(window0, height=1, width=10, text="Convert", command= lambda: conv_onedrive())
btnConvOnedrive.place( relx=0.63, rely=0.65, anchor='nw') 
btnAbout=Button(window0, height=1, width=10, text="About", command= lambda: about())
btnAbout.place( relx=0.78, rely=0.65, anchor='nw') 
btnExit=Button(window0, height=1, width=10, text="Exit", command= lambda: close_window0())
btnExit.place( relx=0.89, rely=0.65, anchor='nw') 


textBox1Entry= StringVar()
textBox1= Entry(window0, width=110, textvariable= textBox1Entry)
textBox1.place(relx=0.15, rely=0.2, anchor='w')
textBox1.bind('<Button-3>',rClicker, add='')
lbl1 = Label(window0, text='Oem Ondrive Url: ')
lbl1.place(relx=0.15, rely=0.2, anchor='e')

textBox2Entry= StringVar()
textBox2= Entry(window0, width=110, textvariable= textBox2Entry)
textBox2.place(relx=0.15, rely=0.45, anchor='w')
textBox2.bind('<Button-3>',rClicker, add='')
lbl1 = Label(window0, text='Convert Ondrive Url: ')
lbl1.place(relx=0.15, rely=0.45, anchor='e')
    


mainloop()