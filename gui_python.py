#importing
import tkinter as tk 
from script import magic_date_find

#Window and window configuration
window = tk.Tk()
window.title(" Magic Date_of_Birth Finder",)
window.configure(bg = "#58aad6")

# Code to add widgets will go below

#Top Lable with instructions
title = tk.Label(text = "First take the number of the month in which you were born (For Example, if you were born on Feb 15, take 2 ).\nDouble this number(2*2) \nAdd 5 to this number(4+5) \nMultiply this by 5(9*5)\nPut a zero after this answer(450) \n Add your date of birth.(So,450 + 15 )" , font = ("Times New Roman" , 12),bg = "#58aad6")
title.pack()

#Label for button 
title = tk.Label(text = "Enter Your Final Result" , font = ("Times New Roman" , 14), bg = "#60baeb")
title.pack()

#User input - Entry widget
entry1 = tk.Entry(master = window)
entry1.pack()

#Output display window
display_window = tk.Text(master = window , width = 40 ,  height = 5 , font = ("Times New Roman" , 17) , bg = "#58aad6")
display_window.config(state='disabled')
display_window.pack()

#Button code 
def button_code():
    #Variable that prints 100 new lines
    clear_screen = "\n"*100
    #Display Window - Normal
    display_window.config(state = "normal")
    display_window.insert(0.0 , clear_screen)
    #Gets user input
    user_number = entry1.get()
    #Runs the functionh
    Result = magic_date_find(user_number)
    #Result is displayed
    display_window.insert( 0.0 , Result )
    #Display Windoe - Disabled
    display_window.config(state = "disabled")
    
#Button widget
button = tk.Button(text = "Click Me !" , bg = "#e62020" , font = ("Times New Roman" , 20) , command = button_code )
button.pack()

#keeps the window displayed
window.mainloop()
