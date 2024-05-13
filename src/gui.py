import tkinter as tk
import matplotlib.pyplot as plt
import sys
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # used to embed matplotlib graphs in tkinter

class App(tk.Tk):
    def __init__(self, callback=None):
        """
        Initialisation function of the App class with parent class tk.Tk
        and includes displaying the title screen.

        """
        
        super().__init__()
        self.geometry("1920x1080")
        self.title("Photoplethysmografie")
        self.entry_text = tk.StringVar()
        self.path = ""
        self.callback = callback
        self.protocol("WM_DELETE_WINDOW", self.on_close)  # bind the close event to a function
        self.entryVarLC = tk.StringVar(value="0")
        self.entryVarHC = tk.StringVar(value="0")
        self.entryValLC = 0
        self.entryValHC = 0

        self.entryVarLC1 = tk.StringVar(value="0")
        self.entryVarHC1 = tk.StringVar(value="0")
        self.entryValLC1 = 0
        self.entryValHC1 = 0

        self.entryVarLC2 = tk.StringVar(value="0")
        self.entryVarHC2 = tk.StringVar(value="0")
        self.entryValLC2 = 0
        self.entryValHC2 = 0

        self.entryVarLC3 = tk.StringVar(value="0")
        self.entryVarHC3 = tk.StringVar(value="0")
        self.entryValLC3 = 0
        self.entryValHC3 = 0

        self.entryVarLC4 = tk.StringVar(value="0")
        self.entryVarHC4 = tk.StringVar(value="0")
        self.entryValLC4 = 0
        self.entryValHC4 = 0

        self.entryVarLC5 = tk.StringVar(value="0")
        self.entryVarHC5 = tk.StringVar(value="0")
        self.entryValLC5 = 0
        self.entryValHC5 = 0

        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()
        self.center_x = (1920 - window_width) // 2
        self.center_y = (1080 - window_height) // 2

        self.entry_window_text = tk.StringVar()
        self.windows = 0

        self.lstLCHC = []
        self.confirmed = False

        # title screen
        self.stLabel = tk.Label(self, text="Please enter the MP4 file's path:",
                                font=("Helvetica", 20))
        self.stEntry = tk.Entry(self, width=25, font=("Helvetica", 20),
                                  textvariable=self.entry_text)
        self.stBut = tk.Button(self, text="Confirm", font=("Helvetica", 20), 
                                 command=self.stBut_clicked)
        self.stLabel.place(x=self.center_x - 100, y=self.center_y - 30)
        self.stEntry.place(x=self.center_x - 100, y=self.center_y)  
        self.stBut.place(x=self.center_x + 300, y=self.center_y)  

        self.stListbox = tk.Listbox(self)

    def stBut_clicked(self):
        """
        When the confirm button is clicked in the title screen.
        Includes exception handling for when a user doesn't give a 
        path to an .mp4 file

        """
        file_path = self.entry_text.get()

        if not file_path.strip().lower().endswith(".mp4"): # if file doesn't end with ".mp4", display error message
            tk.messagebox.showerror("Error", "Please enter a path to an MP4 file.")
        else:
            self.path = file_path
            self.clear_widgets()
            self.prelaunch()

    def winBut_clicked(self):
        """
        When the confirm button is clicked in the prelaunch app to
        get the amount of windows.

        """
        self.windows = int(self.stListbox.get(tk.ANCHOR))
        self.clear_widgets()
        if self.callback:
            self.callback()

    def continuBut5_clicked(self):
        """
        When the continue button is clicked in the launch app with
        the five windows. Includes exception handling for when an user
        doesn't give a proper numeric value or a zero.

        """
        entry_vars = [self.entryVarLC1, self.entryVarHC1,
                    self.entryVarLC2, self.entryVarHC2,
                    self.entryVarLC3, self.entryVarHC3,
                    self.entryVarLC4, self.entryVarHC4,
                    self.entryVarLC5, self.entryVarHC5]
        try:
            entry_values = [float(entry_var.get()) for entry_var in entry_vars]
            if 0 in entry_values:
                raise ValueError("Zero value detected")
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter valid non-zero numeric values.")
            return  

        self.lstLCHC.append([float(self.entryVarLC1.get()), float(self.entryVarHC1.get())])
        self.lstLCHC.append([float(self.entryVarLC2.get()), float(self.entryVarHC2.get())])
        self.lstLCHC.append([float(self.entryVarLC3.get()), float(self.entryVarHC3.get())])
        self.lstLCHC.append([float(self.entryVarLC4.get()), float(self.entryVarHC4.get())])
        self.lstLCHC.append([float(self.entryVarLC5.get()), float(self.entryVarHC5.get())])

        self.entryValLC1 = 0
        self.entryValHC1 = 0
        self.entryValLC2 = 0
        self.entryValHC2 = 0
        self.entryValLC3 = 0
        self.entryValHC3 = 0    
        self.entryValLC4 = 0
        self.entryValHC4 = 0
        self.entryValLC5 = 0
        self.entryValHC5 = 0

        self.clear_widgets()

        if len(self.lstLCHC) == self.windows:
            self.confirmed = True

    def confBut5_clicked(self, fig):
        """
        When the confirm button is clicked in the launch app with
        the five windows.

        """
        self.clear_widgets()
        labelEnd = tk.Label(self, text="Hearth rate graph",
                                font=("Helvetica", 40))
        fig = FigureCanvasTkAgg(fig, master=self)
        fig.get_tk_widget().place(x=320, y=180, width=1280, height=720)
        labelEnd.place(x=750, y=100)

    def continuBut_clicked(self):
        """
        When the continue button is clicked in the launch app for
        a singular window. Includes exception handling for when an user
        doesn't give a proper numeric value or a zero.

        """
        try:
            self.entryValLC = float(self.entryVarLC.get())
            self.entryValHC = float(self.entryVarHC.get())
            if self.entryValLC == 0.0 or self.entryValHC == 0.0:
                raise ValueError("Zero value detected")
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter valid non-zero numeric values.")
            return  
        
        self.lstLCHC.append([self.entryValLC, self.entryValHC])
        self.entryValLC = 0
        self.entryValHC = 0

        self.clear_widgets()

        if len(self.lstLCHC) == self.windows:
            self.confirmed = True

    def confBut_clicked(self, bpm):
        """
        When the confirm button is clicked in the launch app for
        a singular window.

        :type bpm: int
        """
        self.clear_widgets()
        labelBpm = tk.Label(self, text="The average BPM over the whole video is : " + str(bpm),
                                font=("Helvetica", 28))
        labelBpm.place(x=550, y=400)

    def clear_widgets(self):
        """
        Clear all displayed widgets

        """
        for widget in self.winfo_children():
            widget.destroy()

    def on_close(self):
        """
        When clicking the close button in the top right corner exit Python
        interpreter by raising the 'SystemExit' exception. This way both backend 
        and frontend part of code stop running.

        """
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()
            sys.exit()

    def prelaunch(self): 
        """
        Prelaunch is used to get an input for the amount of windows.

        """
        self.stLabel = tk.Label(self, text="Please select the amount of windows:",
                                font=("Helvetica", 20))
        self.stListbox = tk.Listbox(self, width=25, font=("Helvetica", 20))
        lst_inserts = ["1", "5"] # computationally it is possible for more windows,
                                 # but the GUI is only designed for 1 or 5 graphs, that
                                 # is why no other options are allowed
        for item in lst_inserts:
            self.stListbox.insert(tk.END, item)

        self.stBut = tk.Button(self, text="Continue", font=("Helvetica", 20), 
                                 command=self.winBut_clicked)
        self.stLabel.place(x=self.center_x - 100, y=self.center_y - 30)
        self.stListbox.place(x=self.center_x - 100, y=self.center_y)  
        self.stBut.place(x=self.center_x + 300, y=self.center_y)

    def launch(self, *args):  
        """
        The full app launch

        :type *args: tuple, arbitrary amount of positional arguments
        """
        if args[3] == False: # if it is the first iteration
            labelTitle = tk.Label(self, text = "FIRST ITERATION", font=("Helvetica", 22))  
            labelTitle.place(x=25, y=5)
        else:
            labelTitle = tk.Label(self, text = "SECOND ITERATION", font=("Helvetica", 22))  
            labelTitle.place(x=25, y=5)

        # plotting filter graph, used in both first and second iteration
        figFilt = FigureCanvasTkAgg(args[0], master=self) 
        labelFilt = tk.Label(self, text="Filtered data", font=("Helvetica", 20))
        figFilt.get_tk_widget().place(x=25, y=80, width=500, height=385) 
        labelFilt.place(x=25, y=45)

        if args[5] == 5: # gui placement for 5 figs
            figFTT1 = FigureCanvasTkAgg(args[2][0], master=self)
            figFTT2 = FigureCanvasTkAgg(args[2][1], master=self)
            figFTT3 = FigureCanvasTkAgg(args[2][2], master=self)
            figFTT4 = FigureCanvasTkAgg(args[2][3], master=self)
            figFTT5 = FigureCanvasTkAgg(args[2][4], master=self)

            labelFFT1 = tk.Label(self, text="1st window :", font=("Helvetica", 20))
            labelFFT2 = tk.Label(self, text="2nd window :", font=("Helvetica", 20))
            labelFFT3 = tk.Label(self, text="3rd window :", font=("Helvetica", 20))
            labelFFT4 = tk.Label(self, text="4th window :", font=("Helvetica", 20))
            labelFFT5 = tk.Label(self, text="5th window :", font=("Helvetica", 20))

            figFTT1.get_tk_widget().place(x=650, y=80, width=500, height=385)
            figFTT2.get_tk_widget().place(x=1215, y=80, width=500, height=385)
            figFTT3.get_tk_widget().place(x=25, y=540, width=500, height=385)
            figFTT4.get_tk_widget().place(x=650, y=540, width=500, height=385)
            figFTT5.get_tk_widget().place(x=1215, y=540, width=500, height=385)

            labelFFT1.place(x=650, y=45)
            labelFFT2.place(x=1215, y=45)
            labelFFT3.place(x=25, y=505)
            labelFFT4.place(x=650, y=505)
            labelFFT5.place(x=1215, y=505)

            labelLC1 = tk.Label(self, text="Lowcut", font=("Helvetica", 20))
            labelHC1 = tk.Label(self, text="Highcut", font=("Helvetica", 20))
            entryLC1 = tk.Entry(self, width=10, font=("Helvetica", 20),
                            textvariable=self.entryVarLC1)
            entryHC1 = tk.Entry(self, width=10, font=("Helvetica", 20),
                            textvariable=self.entryVarHC1)
            
            labelLC1.place(x=825, y=10)
            labelHC1.place(x=995, y=10)
            entryLC1.place(x=825, y=45)
            entryHC1.place(x=995, y=45)

            labelLC2 = tk.Label(self, text="Lowcut", font=("Helvetica", 20))
            labelHC2 = tk.Label(self, text="Highcut", font=("Helvetica", 20))
            entryLC2 = tk.Entry(self, width=10, font=("Helvetica", 20),
                            textvariable=self.entryVarLC2)
            entryHC2 = tk.Entry(self, width=10, font=("Helvetica", 20),
                            textvariable=self.entryVarHC2)
            
            labelLC2.place(x=1390, y=10)
            labelHC2.place(x=1560, y=10)
            entryLC2.place(x=1390, y=45)
            entryHC2.place(x=1560, y=45)

            labelLC3 = tk.Label(self, text="Lowcut", font=("Helvetica", 20))
            labelHC3 = tk.Label(self, text="Highcut", font=("Helvetica", 20))
            entryLC3 = tk.Entry(self, width=10, font=("Helvetica", 20),
                            textvariable=self.entryVarLC3)
            entryHC3 = tk.Entry(self, width=10, font=("Helvetica", 20),
                            textvariable=self.entryVarHC3)
            
            labelLC3.place(x=200, y=470)
            labelHC3.place(x=370, y=470)
            entryLC3.place(x=200, y=505)
            entryHC3.place(x=370, y=505)

            labelLC4 = tk.Label(self, text="Lowcut", font=("Helvetica", 20))
            labelHC4 = tk.Label(self, text="Highcut", font=("Helvetica", 20))
            entryLC4 = tk.Entry(self, width=10, font=("Helvetica", 20),
                            textvariable=self.entryVarLC4)
            entryHC4 = tk.Entry(self, width=10, font=("Helvetica", 20),
                            textvariable=self.entryVarHC4)
            
            labelLC4.place(x=1390, y=470)
            labelHC4.place(x=1560, y=470)
            entryLC4.place(x=1390, y=505)
            entryHC4.place(x=1560, y=505)

            labelLC5 = tk.Label(self, text="Lowcut", font=("Helvetica", 20))
            labelHC5 = tk.Label(self, text="Highcut", font=("Helvetica", 20))
            entryLC5 = tk.Entry(self, width=10, font=("Helvetica", 20),
                            textvariable=self.entryVarLC5)
            entryHC5 = tk.Entry(self, width=10, font=("Helvetica", 20),
                            textvariable=self.entryVarHC5)
            
            labelLC5.place(x=825, y=470)
            labelHC5.place(x=995, y=470)
            entryLC5.place(x=825, y=505)
            entryHC5.place(x=995, y=505)

            if args[3] == False: # if we are in the first iteration
                butContinu5 = tk.Button(self, text="Continue", font=("Helvetica", 20), 
                                        command=self.continuBut5_clicked)
                butContinu5.place(x=1760, y=885)
            else:
                butConf5 = tk.Button(self, text="Confirm", font=("Helvetica", 20), 
                                        command=lambda: self.confBut5_clicked(args[4]))
                butConf5.place(x=1760, y=885)

        else: # if we are not using 5 figs, so only 1
            figFTT = FigureCanvasTkAgg(args[1][0], master=self)
            labelFTT = tk.Label(self, text="Fast fourier transformed data", font=("Helvetica", 20))
            figFTT.get_tk_widget().place(x=650, y=80, width=560, height=385) 
            labelFTT.place(x=650, y=45)
            figPSD = FigureCanvasTkAgg(args[2][0], master=self)
            labelPSD = tk.Label(self, text="Power spectral density analysis", font=("Helvetica", 20))
            figPSD.get_tk_widget().place(x=25, y=515, width=1185, height=500) 
            labelPSD.place(x=25, y=480)
            labelLC = tk.Label(self, text="Lowcut", font=("Helvetica", 20))
            labelHC = tk.Label(self, text="Highcut", font=("Helvetica", 20))
            entryLC = tk.Entry(self, width=10, font=("Helvetica", 20),
                            textvariable=self.entryVarLC)
            entryHC = tk.Entry(self, width=10, font=("Helvetica", 20),
                            textvariable=self.entryVarHC)
            labelLC.place(x=1350, y=690)
            labelHC.place(x=1650, y=690)
            entryLC.place(x=1350, y=720)
            entryHC.place(x=1650, y=720)

            if args[3] == False: # if we are in the first iteration
                butContinu5 = tk.Button(self, text="Continue", font=("Helvetica", 20), 
                                        command=self.continuBut_clicked)
                butContinu5.place(x=1760, y=885)
            else:
                butConf5 = tk.Button(self, text="Confirm", font=("Helvetica", 20), 
                                        command=lambda: self.confBut_clicked(args[4]))
                butConf5.place(x=1760, y=885)