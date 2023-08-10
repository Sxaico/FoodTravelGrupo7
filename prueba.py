import tkinter as tk


root = tk.Tk()
root.title('Prueba de search')
root.geometry('500x300')


def update(data):
    my_list.delete(0, tk.END)
    
    #Agregando a la lista
    for item in data:
        my_list.insert(tk.END, item)

def fillout(e):
    # Limpiamos el listbox
    my_entry.delete(0, tk.END)
    my_entry.insert(0, my_list.get(my_list.curselection()))

def check(e):
    # agarrar todo lo que esta escrito
    typed = my_entry.get()

    if typed == '':
        data = toppings
    else:
        data = []
        for item in toppings:
            if typed.lower() in item.lower():
                data.append(item)
    update(data)

def subir():
    rbtn = var.get()
    print(rbtn)

my_label = tk.Label(root, text='Empieza a escribir', font=('Helvetica',20))
my_label.pack(pady=20)

my_entry = tk.Entry(root, font=('Helvetica', 20))
my_entry.pack(pady=30)

my_list = tk.Listbox(root, width=50)
my_list.pack(pady=30)

toppings = ['Pepperoni', 'Tomate', 'Cheese', 'Mayonesa', 'Ketchup', 'Cebollas']

update(toppings)

my_list.bind('<<ListboxSelect>>', fillout)

my_entry.bind('<KeyRelease>', check)


# RadioButton

# Defino VarString donde se almacenan los str 
var = tk.StringVar(root, '1')

values = {'★☆☆☆☆' : '1',
          '★★☆☆☆' : '2',
          '★★★☆☆' : '3',
          '★★★★☆' : '4',
          '★★★★★' : '5'}

# loop para crear los botones

for text, value in values.items():
    tk.Radiobutton(root, text= text, variable=var,
                   value= value, indicatoron=0,
                   background='light blue', width=10).pack()

btn = tk.Button(root, text='Subir', command=subir)
btn.pack()




root.mainloop()


