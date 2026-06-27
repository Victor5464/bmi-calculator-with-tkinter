import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from logic import bmi_calculator



class BMICalculator:
    def __init__(self, master) -> None:
        #initiating the app 
        self.master= master
        self.master.title('BMI CALCULATOR')
        self.master.resizable(False,False)
        # self.master.geometry('100x50')
       
        
        #frame
        self.entry_frame =ttk.Frame(self.master)
        self.entry_frame.grid(row=0, column=0, padx=10, pady=5)

        #entries
        self.weight_entry =ttk.Entry(master=self.entry_frame, width=10)
        self.weight_entry.grid(row=0, column=1, sticky='e', pady=2 )

        self.height_entry =ttk.Entry(master=self.entry_frame, width=10)
        self.height_entry.grid(row=1, column=1,sticky='e', pady=2)

        #labels
        self.weight_label =ttk.Label(master=self.entry_frame, text='Weight (KG): ')
        self.weight_label.grid(row=0, column=0, sticky='nsew')

        self.height_label =ttk.Label(master=self.entry_frame, text='Height (m): ')
        self.height_label.grid(row=1, column=0, sticky='nsew')

        self.result_label =ttk.Label(master=self.entry_frame)
        self.result_label.grid(row=3, columnspan=2, sticky= 'ew', padx=20)

        #button
        self.convert_button = ttk.Button(master=self.entry_frame, text='Convert', command= self.handle_convert)
        self.convert_button.grid(row=2,columnspan=2, sticky='ew',pady=5)

    def handle_clear(self):
        self.weight_entry.delete(0, 'end')
        self.height_entry.delete(0, 'end')

    def handle_convert(self):
        #collect input
        raw_w = self.weight_entry.get().strip()
        raw_h = self.height_entry.get().strip()

        # clear entry after getting inputs
        # self.handle_clear()

        # iput validation
        if not raw_w or not raw_h:
            messagebox.showwarning('Incomplete Data', 'All fields are required.')
            return
        try:
            w=float(raw_w)
            h=float(raw_h)

            bmi_value, category = bmi_calculator(w,h)
            if bmi_value is None:
                messagebox.showerror('Error', category)
                return
            self.result_label.config(text=f'BMI: {bmi_value:.2f} ({category})')

        except ValueError:
            messagebox.showerror('Invalid Input', 'Please enter valid numbers')
            return
            


def main():
    #instantiating the app
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()

if __name__=='__main__':
    main()