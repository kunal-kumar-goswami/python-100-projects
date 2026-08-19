import tkinter

def miles_to_km():
        miles = float(miles_input.get())  
        km = miles * 1.60934              
        kilometer_result_label.config(text=f"{km:.2f}")  
    
window = tkinter.Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = tkinter.Entry()
miles_input.grid(column=1, row=0)

miles_label = tkinter.Label(window, text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = tkinter.Label(window, text="Is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = tkinter.Label(window, text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = tkinter.Label(window, text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = tkinter.Button(window, text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
