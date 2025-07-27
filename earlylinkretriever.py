from tkinter import *


root = Tk()

root.title('ELR')


#dropdown menu
Label(root, text = "Sites").grid(row=0)

def show():
    myLabel = Label(root,text=clicked.get())
    return myLabel

def availabilitycheck():
  r = requests.get()

  products = json.loads((r.text))['products']

  for product in products:
      print(product['title'])
      productname = product['title']

options = ["yeezysupply",
           "kith",
           "bodega"]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked,*options).grid(row=0, column=1)

but = Button(root, text="find products", command=show).grid(row=0, column=3)

root.mainloop()
