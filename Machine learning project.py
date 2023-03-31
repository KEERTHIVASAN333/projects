#lap top recomendation
import tkinter as Tk
from tkinter import messagebox, simpledialog
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix


root = Tk.Tk()
root.geometry("1366x768")
root.title("LOG IN")
root.config(bg="#2D283E")

s1 = Tk.Frame(root, height="200", width="400", bg="#2D283E")
s1.place(x=450, y=250)

Tk.Label(root, text="LAPTOP RECOMMENDER", fg="#802BB1", bg="#2D283E",
         font=("times new roman", 35, "bold")).place(x=380, y=10)


def lap():
    my_f = simpledialog.askinteger("input", "Enter Your Budget", parent=s1)
    my_g = simpledialog.askfloat("input", "Enter Rating ", parent=s1)
    dataset = pd.read_csv("D:\\keerthi_ml_project\\products - Copy 3 .csv") # change the path if needed
    x = dataset.iloc[:, [2, 3]].values
    y = dataset.iloc[:, -4].values
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25,
                                                        random_state=0)
    classifier = GaussianNB()
    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test)
    classifier.score(x_train, y_train)
    cm = confusion_matrix(y_test, y_pred)

    if my_f < 5000:
        messagebox.showinfo("Message", "Oops! Your budgeted laptop is not currently available")
        messagebox.showinfo("Message", "Can we show best laptop under RS:11999 ")
    else:
        labelen = LabelEncoder()
        yy = labelen.fit_transform(y)
        model = classifier.predict([[my_g, my_f]])

        Tk.Label(root, text="This is the best laptop for your budget:", fg="white", bg="#659DBD",
                 font=("times new roman", 17, "bold")).place(x=100, y=100)
        Tk.Label(root, text=model, fg="white", bg="#F64C72",
                 font=("times new roman", 17, "bold")).place(x=100, y=150)


pre = Tk.Button(root, relief=Tk.FLAT, text="start", command=lap, bg="#F64C72", fg="black",
                font=("times new roman", 20, "bold"))
pre.place(x=600, y=540)

root.mainloop()
