import tkinter
from menu import Menu
  
class Application:
    def __init__(self):
        window = tkinter.Tk()
        window.minsize(1024, 1024)
        mb = Menu(window)
        window.title('Sistema Instituição de ensino')
        window.geometry('{}x{}+0+0'.format(*window.maxsize()))
        window.configure(background='#7FFFD4')
        window.mainloop()
 
if __name__ == '__main__': 
    Application()
