import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Importing Pillow
global a
global b
import pandas as pd
import cv2
import os
from pathlib import Path

def model(user_color,user_type,user_pattern,user_category):
    df = pd.read_csv('labeled_data.csv')

    # Resetting index if 'Color' is set as index
    df.reset_index(inplace=True)
    #df.info()

    df['color'] = df['color'].str.lower()
    df['Type'] = df['Type'].str.lower()
    df['Pattern'] = df['Pattern'].str.lower()
    df['Category'] = df['Category'].str.lower()
    df['data'] = df['color'] + ' ' + df['Type'] + ' ' + df['Pattern'] + ' ' + df['Category']
    from sklearn.feature_extraction.text import CountVectorizer

    vectorizer = CountVectorizer()
    vectorized = vectorizer.fit_transform(df['data'])

    from sklearn.metrics.pairwise import cosine_similarity

    similarities = cosine_similarity(vectorized)

    # Take user input for preferences
    '''user_color = input("Enter preferred color: ").lower()
    user_type = input("Enter preferred type: ").lower()
    user_pattern = input("Enter preferred pattern: ").lower()
    user_category = input("Enter preferred category: ").lower()'''

    '''user_color= option_menu1.get()
    user_type = option_menu2.get()
    user_pattern= option_menu3.get()
    user_category= option_menu4.get()'''

    # Combine user preferences into one string
    user_data = user_color + ' ' + user_type + ' ' + user_pattern + ' ' + user_category

    # Calculate cosine similarity between user preferences and dataset
    user_vectorized = vectorizer.transform([user_data])
    similarities = cosine_similarity(user_vectorized, vectorized)

    # Get indices of top recommendations
    top_indices = similarities.argsort(axis=1)[:, -5:].flatten()

    # Print recommended items
    print("Top recommendations:")

    for idx in reversed(top_indices):
        print(df.iloc[idx]['S.NO.'])
        image=cv2.imread("C:/Users/anany/OneDrive/Documents/Project sem 4/final dataset/"+str(df.iloc[idx]['S.NO.'])+".png")
        cv2.imshow("recommendation",image)
        cv2.waitKey(0)
    
def validate_login(parent):
    name=["Ananya","ananya3010"]
    print("Login Succesful")
    parent.withdraw()  # Hide the main window
    c = tk.Toplevel(parent)  # Create a new window with parent
    c.geometry("1070x700")
    c.title("FASHION SENSEI - Your virtual fashion mentor")
    c.configure(bg="white smoke")

    # Load the image using Pillow
    image = Image.open(r"C:\Users\anany\OneDrive\Documents\Project sem 4\digital_fashion_0.webp")
    img = ImageTk.PhotoImage(image)

    l = ttk.Label(c, image=img)
    l.image = img  # Keep a reference to avoid garbage collection
    l.place(x=0, y=0)

    # Create style for Labels
    style = ttk.Style()
    l5 = ttk.Label(c, width=500, font=("Lucida Handwriting", 35, "bold"), background='#3E0F24', foreground="#3E0F24")
    l5.place(x=2, y=2)
    l3 = ttk.Label(c, text="Fashion Sensei", width=13, font=("Lucida Handwriting", 25, "bold"), background='#3E0F24', foreground="white")
    l3.place(x=375, y=10)

    l1 = ttk.Label(c, text=" Choose your Preferences:", width=22, font=("Times New Roman", 25, "bold"), background='black', foreground="white")
    l1.place(x=150, y=150)

    # Define options for each dropdown
    options1 = ["red", "pink", "black", "blue", "white", "navy blue", "purple", "brown", "mix", "light blue", "lavender", "cream", "grey", "green", "beige", "Magenta", "Sky blue", "Light pink", "Sea Green", "Yellow", "Grey"]
    options2 = ["ethnic", "western",]
    options3 = ["Plain", "Printed", "Striped", "Butterfly", "Check", "Floral", "Flowers", "Dotted", "embroidery", "Strips"]
    options4 = ["Top", "Jeans", "Shorts", "Shirt", "T-shirt", "Plazo", "Jumpsuit", "saree", "kurti", "suit", "Skirt", "Dress", "Pants", "Leggings", "Jacket", "Kurta"]

    # Create Tkinter variables to store the selected options
    global option1, option2, option3,option4
    option1 = tk.StringVar(value="Colors")
    option2 = tk.StringVar(value="Type")
    option3 = tk.StringVar(value="Pattern")
    option4 = tk.StringVar(value="Category")


    # Create dropdown menus for each option
    option_menu1 = ttk.Combobox(c, textvariable=option1, values=options1, state="readonly",height=40)
    option_menu1.place(x=50,y=250)

    option_menu2 = ttk.Combobox(c, textvariable=option2, values=options2, state="readonly")
    option_menu2.place(x=200,y=250)

    option_menu3 = ttk.Combobox(c, textvariable=option3, values=options3, state="readonly")
    option_menu3.place(x=350,y=250)
    
    option_menu4 = ttk.Combobox(c, textvariable=option4, values=options4, state="readonly")
    option_menu4.place(x=500,y=250)

    # Create a button to get the selected options
    submit_button = ttk.Button(c, text="Submit",command=lambda: model(option_menu1.get(),option_menu2.get(),option_menu3.get(),option_menu4.get()))
    submit_button.place(x=300,y=500)

    # Create a label to display the selected options
    global result_label
    result_label = ttk.Label(c, text="")
    result_label.pack()

    # Create a label to display the selected options

    c.mainloop()



def login1(parent):
    parent.withdraw()  # Hide the main window
    b = tk.Toplevel(parent)  # Create a new window with parent
    b.geometry("1070x700")
    b.title("FASHION SENSEI - Your virtual fashion mentor")
    b.configure(bg="white smoke")
    name=["Ananya","ananya3010"]


    # Load the image using Pillow
    image = Image.open(r"C:\Users\anany\OneDrive\Documents\Project sem 4\digital_fashion_0.webp")
    img = ImageTk.PhotoImage(image)

    l = ttk.Label(b, image=img)
    l.image = img  # Keep a reference to avoid garbage collection
    l.place(x=0, y=0)

    # Create style for Labels
    style = ttk.Style()
    l5 = ttk.Label(b, width=500,font=("Lucida Handwriting", 35, "bold"),background='#3E0F24',foreground="#3E0F24")
    l5.place(x=2, y=2)
    l3 = ttk.Label(b, text="Fashion Sensei", width=13, font=("Lucida Handwriting", 25, "bold"), background='#3E0F24',foreground="white")
    l3.place(x=375, y=10)

    
    l1 = ttk.Label(b, text="Username", width=9, font=("Times New Roman", 25, "bold"), background='black',foreground="white")
    l1.place(x=150, y=250)

    l2 = ttk.Label(b, text="Password", width=9, font=("Times New Roman", 25, "bold"), background='black',foreground="white")
    l2.place(x=150, y=350)
    text1=ttk.Entry(b,width=25)
    text1.place(x=350,y=250,height=35)
    text2=ttk.Entry(b,width=25)
    text2.place(x=350,y=350,height=35)
    
    Uname=text1.get()
    Pswd=text2.get()

    # Create style for Buttons
    style.configure('TButton', font=("Times", 15, "bold"), padding=5, background='white smoke')
    B1 = ttk.Button(b, text="Login",command=lambda: validate_login(b))
    B1.place(x=250, y=500)
    b.mainloop()

    

def main():
    a = tk.Tk()
    a.geometry("1070x700")
    a.title("FASHION SENSEI - Your virtual fashion mentor")
    a.configure(bg="white smoke")

    # Load the image using Pillow
    image = Image.open(r"C:\Users\anany\OneDrive\Documents\Project sem 4\digital_fashion_0.webp")
    img = ImageTk.PhotoImage(image)

    l = ttk.Label(a, image=img)
    l.image = img  # Keep a reference to avoid garbage collection
    l.place(x=0, y=0)

    # Create style for Labels
    style = ttk.Style()
    l1 = ttk.Label(a, text="FASHION", width=8, font=("Lucida Handwriting", 55, "bold"), background='#3E0F24',
                   foreground="white")
    l1.place(x=150, y=105)

    l3 = ttk.Label(a, text="''Your virtual fashion mentor''", width=25,
                   font=("Lucida Handwriting", 20, "bold"), background='#3E0F24', foreground="white")
    l3.place(x=100, y=400)

    l2 = ttk.Label(a, text="SENSEI", width=6, font=("Lucida Handwriting", 55, "bold"), background='#3E0F24',
                   foreground="white")
    l2.place(x=200, y=220)

    # Create style for Buttons
    style.configure('TButton', font=("Times", 15, "bold"), padding=5, background='white smoke')

    B1 = ttk.Button(a, text="Signup")
    B1.place(x=200, y=600)

    B2 = ttk.Button(a, text="Login", command=lambda: login1(a))
    B2.place(x=350, y=600)

    a.mainloop()

main()





    
                    
                    
