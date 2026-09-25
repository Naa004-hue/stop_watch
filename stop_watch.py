import tkinter as tk

class stopwatchGUI:

    def __init__(self):

        self.root=tk.Tk()
        self.root.title('Stop Watch')
        self.root.geometry('800x800')
        self.root.config(bg="#FFD1DC")
        self.frame=tk.Frame(bg="#FFD1DC")

        self.timer_frame = tk.Frame(self.frame, bg="#FFD1DC", highlightbackground="#F37482", highlightthickness=3, padx=20, pady=20 )
        self.watch=tk.Label(self.timer_frame , text='00:00:00' ,font=("Consolas", 36, "bold")  ,fg="#F37492" ,bg="#FFD1DC")
        self.watch.grid(row=0 ,column=0 ,columnspan=3 , padx=5, pady=10)
        self.timer_frame.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        self.start_button=tk.Button(self.frame , text='start'  ,bg="#FFD1DC" , command=self.start )
        self.start_button.grid(row=1 ,column=0 ,columnspan=2 , padx=5, pady=10)

        self.lap_button=tk.Button(self.frame , text='lap'  ,bg="#FFD1DC" ,  command=self.lap  )
        self.lap_button.grid(row=2 ,column=0 ,columnspan=2 , padx=5, pady=10)

        self.frame.pack(expand=True)

        self.running=False
        self.reset=False
        self.s = 0
        self.m=0
        self.h=0
        self.laps=[]
        self.laps_widjet=[]


        self.root.mainloop()

    def start(self):
        if not self.reset :
           self.running=True
           self.reset= True
           self.start_button.config(text='reset')
        elif self.reset : 
            self.running=False
            self.reset= False
            self.s = 0
            self.m=0
            self.h=0
            for widjet in self.laps_widjet :
                widjet.destroy()
            self.laps.clear()
            self.laps_widjet.clear()
            self.watch.config(text='00:00:00' )
            self.start_button.config(text='start')
        if self.running:
            self.watch_counter()
        self.laps_widjet=[]
        self.laps=[]

    def lap(self):
            self.laps.append(f'lap: {self.h:02}:{self.m:02}:{self.s:02} ')
            lap_labels=tk.Label(self.frame , text= f' {self.laps[-1]}'  ,bg="#FFD1DC" ,font=("Consolas", 18), fg="#F37492")
            lap_labels.grid(row = 3+ (len(self.laps)-1) ,column=0 ,columnspan=1 , padx=5, pady=10)
            self.laps_widjet.append(lap_labels)
            

    def watch_counter(self):
        if self.running:
            if self.s < 59 :
                self.s += 1
            else :
                self.s = 0
                if self.s == 0 :
                    self.m += 1
                if self.m >= 59 :
                    self.m = 0
                if self.m == 0:
                    self.h += 1
            self.watch.config(text=f'{self.h:02}:{self.m:02}:{self.s:02}')
        self.root.after(1000,self.watch_counter)

    
stopwatchGUI()