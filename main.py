from tkinter import *

class MyApplication:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.geometry("300x500")
        self.opening()

    def opening(self):
        self.img1 = PhotoImage(file="images/rsz_opening.png")
        self.label1 = Label(image=self.img1, anchor="nw")
        self.label1.pack(fill="both", expand=True)

        def change_Button1to2(e):
            self.imgx = PhotoImage(file="images/rsz_button2.png")
            self.button1.config(image=self.imgx)
            self.button1.image = self.imgx

        def change_Screen1to2(e):
            self.img1 = PhotoImage(file="images/rsz_screen2.png")
            self.label1.config(image=self.img1)
            self.label1.image = self.img1

        def action_Screen2to3():
            self.label1.destroy()
            self.img_Screen = PhotoImage(file="images/rsz_screen3.png")
            self.label = Label(image=self.img_Screen, anchor="nw")
            self.label.pack(fill="both", expand=True)
            self.label.config(image=self.img_Screen)
            self.label.image = self.img_Screen
            self.button1.destroy()
            action_Screen3to4()

        # Change Screen 1 to 2 with hover
        self.label1.bind("<Enter>", change_Screen1to2)

        # Change Screen 2 to 3 and Button 1 to 2 with hover
        self.imgx = PhotoImage(file="images/white.png")
        self.button1 = Button(image=self.imgx, anchor="nw")
        self.button1 = Button(self.label1, height=57, width=60, image=self.imgx, command=action_Screen2to3,
                              borderwidth=0)
        self.button1.pack(side="bottom", pady=(0, 14))
        self.button1.bind("<Enter>", change_Button1to2)

        def changeScreen(self, screenFileName, funcDestination):
            print(screenFileName)
            print(funcDestination)

            def change_screen():
                self.img_Screen = PhotoImage(file=screenFileName)
                self.label.config(image=self.img_Screen)
                self.label.image = self.img_Screen
                funcDestination()
            return change_screen

        def backTo(self, backDestination, backFunc, buttonToDestroy1, buttonToDestroy2, buttonToDestroy3):
            print(backDestination)
            print(backFunc)
            print(buttonToDestroy1)
            print(buttonToDestroy2)
            print(buttonToDestroy3)
            def change_back():
                self.button_back.destroy()
                buttonToDestroy1.destroy()
                buttonToDestroy2.destroy()
                buttonToDestroy3.destroy()
                self.img_Screen = PhotoImage(file=backDestination)
                self.label.config(image=self.img_Screen)
                self.label.image = self.img_Screen
                backFunc()
            return change_back

        def action_Screen3to4():
            # Make Button "On Quarantine"
            self.img_Button3b = PhotoImage(file="images/rsz_button3b.png")
            self.button3b = Button(self.label, image=self.img_Button3b, anchor="nw")
            self.button3b = Button(self.label, image=self.img_Button3b,
                                   command=changeScreen(self, "images/rsz_screen4b.png", action_Screen4bto5b),
                                   borderwidth=0, highlightthickness=0)
            self.button3b.place(x=20, y=410)

            # Make Button "Going Out"
            self.img_Button3a = PhotoImage(file="images/rsz_button3a.png")
            self.button3a = Button(self.label, image=self.img_Button3a, anchor="nw")
            self.button3a = Button(self.label, image=self.img_Button3a,
                                   command=changeScreen(self, "images/rsz_screen4a.png", action_Screen4ato5a),
                                   borderwidth=0, highlightthickness=0)
            self.button3a.place(x=20, y=310)

            # Make the Back Button
            self.img_Back = PhotoImage(file="images/rsz_white.png")
            self.button_back = Button(self.label, image=self.img_Back, anchor="nw")
            self.button_back = Button(self.label, image=self.img_Back, borderwidth=0, highlightthickness=0)
            self.button_back.place(x=10, y=31)

        def action_Screen4ato5a():
            # Destroy the button
            self.button3a.destroy()
            self.button3b.destroy()

            # Make the Plus Button
            self.img_Button4a = PhotoImage(file="images/rsz_button4a.png")
            self.button4a = Button(self.label, image=self.img_Button4a, anchor="nw")
            self.button4a = Button(self.label, image=self.img_Button4a,
                                   command=changeScreen(self, "images/rsz_screen5a.png", action_afterScreen5a),
                                   borderwidth=0, highlightthickness=0)
            self.button4a.place(x=220, y=408)

            # Make the Back Button
            self.img_Back = PhotoImage(file="images/rsz_backbutton.png")
            self.button_back = Button(self.label, image=self.img_Back, anchor="nw")
            self.button_back = Button(self.label, image=self.img_Back,
                                   command=backTo(self, "images/rsz_screen3.png", action_Screen3to4, self.button4a,
                                                  self.button_back, self.button4a),
                                   borderwidth=0, highlightthickness=0)
            self.button_back.place(x=10, y=31)

        def action_afterScreen5a():
            self.button4a.destroy()

            # Make the Back Button
            self.img_Back = PhotoImage(file="images/rsz_button5a.png")
            self.button_back = Button(self.label, image=self.img_Back, anchor="nw")
            self.button_back = Button(self.label, image=self.img_Back,
                                      command=backTo(self, "images/rsz_screen4a.png", action_Screen4ato5a,
                                                     self.button4a, self.button4a, self.button_back),
                                      borderwidth=0, highlightthickness=0)
            self.button_back.place(x=35, y=410)

        def action_Screen4bto5b():
            # Destroy the button
            self.button3a.destroy()
            self.button3b.destroy()

            # Make the Buy your daily Button
            self.img_Button4b3 = PhotoImage(file="images/rsz_button4b3.png")
            self.button4b3 = Button(self.label, image=self.img_Button4b3, anchor="n")
            self.button4b3 = Button(self.label, image=self.img_Button4b3,
                                    command=changeScreen(self, "images/rsz_screen5b3.png", action_afterScreen5b3),
                                    borderwidth=0, highlightthickness=0)
            self.button4b3.place(x=20, y=300)

            # Make the Medicine Button
            self.img_Button4b1 = PhotoImage(file="images/rsz_button4b1.png")
            self.button4b1 = Button(self.label, image=self.img_Button4b1, anchor ="nw", )
            self.button4b1 = Button(self.label, image=self.img_Button4b1,
                                    command=changeScreen(self, "images/rsz_screen5b1.png", action_afterScreen5b1),
                                    borderwidth=0, highlightthickness=0)
            self.button4b1.place(x=25, y=130)

            # Make the Work Out Button
            self.img_Button4b2 = PhotoImage(file="images/rsz_button4b2.png")
            self.button4b2 = Button(self.label, image=self.img_Button4b2, anchor="nw")
            self.button4b2 = Button(self.label, image=self.img_Button4b2,
                                    command=changeScreen(self, "images/rsz_screen5b2.png", action_afterScreen5b2),
                                    borderwidth=0, highlightthickness=0)
            self.button4b2.place(x=160, y=130)

            # Make the Back Button
            self.img_Back = PhotoImage(file="images/rsz_backbutton.png")
            self.button_back = Button(self.label, image=self.img_Back, anchor="nw")
            self.button_back = Button(self.label, image=self.img_Back,
                                      command=backTo(self, "images/rsz_screen3.png", action_Screen3to4, self.button4b1,
                                                     self.button4b2, self.button4b3),
                                      borderwidth=0, highlightthickness=0)
            self.button_back.place(x=10, y=31)

        def action_afterScreen5b1():
            self.button4b1.destroy()
            self.button4b2.destroy()
            self.button4b3.destroy()

            # Make the Back Button
            self.img_Back = PhotoImage(file="images/rsz_backbutton.png")
            self.button_back = Button(self.label, image=self.img_Back, anchor="nw")
            self.button_back = Button(self.label, image=self.img_Back,
                                      command=backTo(self, "images/rsz_screen4b.png", action_Screen4bto5b, self.button4b1,
                                                     self.button4b3, self.button4b2),
                                      borderwidth=0, highlightthickness=0)
            self.button_back.place(x=10, y=31)

        def action_afterScreen5b2():
            self.button4b1.destroy()
            self.button4b2.destroy()
            self.button4b3.destroy()

            # Make the Back Button
            self.img_Back = PhotoImage(file="images/rsz_backbutton.png")
            self.button_back = Button(self.label, image=self.img_Back, anchor="nw")
            self.button_back = Button(self.label, image=self.img_Back,
                                      command=backTo(self, "images/rsz_screen4b.png", action_Screen4bto5b, self.button3a,
                                                     self.button4b2, self.button3b),
                                      borderwidth=0, highlightthickness=0)
            self.button_back.place(x=10, y=31)

        def action_afterScreen5b3():
            self.button4b1.destroy()
            self.button4b2.destroy()
            self.button4b3.destroy()

            # Make the Back Button
            self.img_Back = PhotoImage(file="images/rsz_backbutton.png")
            self.button_back = Button(self.label, image=self.img_Back, anchor="nw")
            self.button_back = Button(self.label, image=self.img_Back,
                                      command=backTo(self, "images/rsz_screen4b.png", action_Screen4bto5b,self.button3a,
                                                     self.button3b, self.button4b3),
                                      borderwidth=0, highlightthickness=0)
            self.button_back.place(x=10, y=31)

if __name__ == '__main__':
    root = Tk()
    aplikasi = MyApplication(root, "Storona App")
    root.mainloop()