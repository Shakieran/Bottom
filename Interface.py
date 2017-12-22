import tkinter

#interface

class GUI:
    def __init__(self):
        #create main window
        self.main_window = tkinter.Tk()

        #create label
        self.label1 = tkinter.Label(self.main_window, text='First Name')

        #create button
        self.button1 = tkinter.Button(self.main_window,
                                      text = 'First Name',
                                      command = self.test)

        #unpacks button
        self.button1.pack()

        #enter the mian loop
        tkinter.mainloop()


    def test(self):
        #display dialog box
        tkinter.messagebox.showinfo('Action Done',
                                    'Your information has been submitted!')
user_inter = GUI()
