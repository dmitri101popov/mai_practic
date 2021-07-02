from tkinter import *
from tkinter import ttk

window = Tk()
# опишите свой интерфейс, затем запустите приложение с помощью команды:

window.title("TELEGRAMMMM")
window.geometry('600x450')

# combo = ttk.Combobox(window)
# combo['values'] = 
# combo.current(1)  # установите вариант по умолчанию  
# combo.grid(column=0, row=0)

# label1 = tkinter.Label(window, text='Клиент-приложение мессенджера', font=("Arial Bold", 20))
# label1.grid(column=0, row=1)


tab_control = ttk.Notebook(window)  
tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control)  
tab_control.add(tab1, text='Общий чат')  
tab_control.add(tab2, text='Личные сообщения')  
tab_control.pack(expand=1, fill='both') 




# messege_text = tkinter.Entry(window, width=(50))
# messege_text.grid(column=0, row=2)




window.mainloop()