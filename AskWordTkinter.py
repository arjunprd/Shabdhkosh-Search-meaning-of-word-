from enum import unique
from tkinter import *
from tkinter import messagebox
from tkinter import font
import requests
from bs4 import BeautifulSoup
import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_c
olor_theme("green")

root = customtkinter.CTk()

root.resizable(False,False)

# setting dimensions of tk window
root.geometry("500x500")

# using title() to display message at the top
root.title("ShabdhKosh with Python")

# search word string 
search_word = StringVar()

#entry box to write word
search_word_Entry = customtkinter.CTkEntry(root, width=180, height = 40,fg_color="black", textvariable=search_word).place(x=160, y=100)



def submit():


    # #website used for finding meaning
    search_website = 'https://www.dictionary.com/browse/'
    
    word = str(search_word.get())

    url = str(search_website) + str(word)

    resp = requests.get(url)

    soup = BeautifulSoup(resp.text,'html.parser')    
   
    # # l is the list which contains all the meaning 
    
    # ESah86zaufmd2_YPdZtq
    l = soup.find("div",{"class":"ESah86zaufmd2_YPdZtq"})
    
    
    # #now we want to print only the text part of the anchor.
    # #find all the elements of a, i.e anchor tag
    
    material = ""

# updated scraped class below 
##<div class="_bzA3f8_vqmJSIKsgOar"><ol start="1"><li><div class="ESah86zaufmd2_YPdZtq" data-type="word-definition-content"><p>a hard, brittle, noncrystalline, more or less transparent substance produced by fusion, usually consisting of mutually dissolved silica and silicates that also contain soda and lime, as in the ordinary variety used for windows and bottles.</p></div><aside class="jeTO7vsIKonI6Z05WfmT ehTSU7DreSCZJDrYAQxS" data-type="ad-vertical"><div class="fHACXxic9xvQeSNITiwH" id="dcomMobileSERPDisplayTopAd-300x250"></div></aside></li><li><div class="ESah86zaufmd2_YPdZtq" data-type="word-definition-content"><p>any artificial or natural noncrystalline and transparent hard substance, such as fused borax, obsidian, or the like.</p></div></li></ol></div>
    
    
    if l is not None:
        for i in l:
             material = material + i.text

    material_length = len(material)

    clean_material = ""
    for i in range(1,material_length-1):
        clean_material = clean_material + material[i]

    print(material_length)
    print(clean_material)


    # #show meaning in messagebox
    if l is None:
        clean_material = "Sorry, couldn't find your word😥😓"

    messagebox.showinfo("meaning of " + word , clean_material)
    
    print(word)


button = customtkinter.CTkButton(master = root , text = 'Search!' , command = submit).place(x = 180 , y = 200)
root.mainloop()
