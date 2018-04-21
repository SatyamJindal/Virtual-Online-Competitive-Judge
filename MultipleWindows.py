import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive):
            

            frame = F(container, self)

            self.frames[F]= frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

def qf(param):
    print(param)


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="See Problem 1",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="See Problem 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        button3 = ttk.Button(self, text="See Problem 3",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()
        button4 = ttk.Button(self, text="See Problem 4",
                            command=lambda: controller.show_frame(PageFour))
        button4.pack()
        button5 = ttk.Button(self, text="VSee Problem 5",
                            command=lambda: controller.show_frame(PageFive))
        button5.pack()

class PageOne(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Page 1", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="See Problem 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        button3 = ttk.Button(self, text="See Problem 3",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()
        button4 = ttk.Button(self, text="See Problem 4",
                            command=lambda: controller.show_frame(PageFour))
        button4.pack()
        button5 = ttk.Button(self, text="VSee Problem 5",
                            command=lambda: controller.show_frame(PageFive))
        button5.pack()

class PageTwo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="See Problem 1",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        button3 = ttk.Button(self, text="See Problem 3",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()
        button4 = ttk.Button(self, text="See Problem 4",
                            command=lambda: controller.show_frame(PageFour))
        button4.pack()
        button5 = ttk.Button(self, text="See Problem 5",
                            command=lambda: controller.show_frame(PageFive))
        button5.pack()

class PageThree(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page three!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="See Problem 1",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()

        button3 = ttk.Button(self, text="See Problem 2",
                            command=lambda: controller.show_frame(PageTwo))
        button3.pack()
        button4 = ttk.Button(self, text="See Problem 4",
                            command=lambda: controller.show_frame(PageFour))
        button4.pack()
        button5 = ttk.Button(self, text="VSee Problem 5",
                            command=lambda: controller.show_frame(PageFive))
        button5.pack()

class PageFour(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page four!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="See Problem 1",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()

        button3 = ttk.Button(self, text="See Problem 2",
                            command=lambda: controller.show_frame(PageTwo))
        button3.pack()
        button4 = ttk.Button(self, text="See Problem 3",
                            command=lambda: controller.show_frame(PageThree))
        button4.pack()
        button5 = ttk.Button(self, text="VSee Problem 5",
                            command=lambda: controller.show_frame(PageFive))
        button5.pack()

class PageFive(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page five!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="See Problem 1",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()

        button3 = ttk.Button(self, text="See Problem 2",
                            command=lambda: controller.show_frame(PageTwo))
        button3.pack()
        button4 = ttk.Button(self, text="See Problem 3",
                            command=lambda: controller.show_frame(PageThree))
        button4.pack()
        button5 = ttk.Button(self, text="See Problem 4",
                            command=lambda: controller.show_frame(PageFour))
        button5.pack()

app = SeaofBTCapp()
app.mainloop()
