import tkinter as tk

def submit():
    name=entry_name.get()
    age=entry_age.get()
    course=entry_course.get()
    address=entry_address.get()

    result_label.config(text=f"Name:{name}\nAge: {age}\nCourse: {course}\nAddress: {address}")


root = tk.Tk()
root.title("User Details Form")
root.geometry("300x400")

tk.Label(root,text ='Name:').grid(row=0, column=0, padx=10,pady=5, sticky='w')
entry_name = tk.Entry(root,width=30)
entry_name.grid(row=0,column=1)

tk.Label(root,text ='Age:').grid(row=1, column=0, padx=10,pady=5, sticky='w')
entry_age = tk.Entry(root,width=30)
entry_age.grid(row=1,column=1)

tk.Label(root,text ='Course:').grid(row=2, column=0, padx=10,pady=5, sticky='w')
entry_course = tk.Entry(root,width=30)
entry_course.grid(row=2,column=1)

tk.Label(root,text ='Address:').grid(row=3, column=0, padx=10,pady=5, sticky='w')
entry_address = tk.Entry(root,width=30)
entry_address.grid(row=3,column=1)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=7, column=0, columnspan=3, pady=10)

result_label=tk.Label(root,text="", justify="left",anchor="w")
result_label.grid(row=7,column=0, columnspan=2, padx=10, pady=5,sticky="w")


root.mainloop()