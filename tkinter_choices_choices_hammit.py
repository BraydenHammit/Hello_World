import tkinter as tk

root = tk.Tk()
root.title('Choices, Choices')                  #screen / ui
root.geometry('700x500')

traits = []         #traits empty to add later

def runQ2():

    q2.pack(pady=10)

    yes2.pack(pady=0)

    no2.pack(pady=5)

    maybe2.pack(pady=10)

def runQ3():

    q3.pack(pady=10)                                                        #run next question (2,3,4)

    yes3.pack(pady=0)

    no3.pack(pady=5)

    maybe3.pack(pady=5)

def runQ4():

    q4.pack(pady=10)

    rain4.pack(pady=0)

    sun4.pack(pady=5)

def runQ5():

    q5.pack(pady=10)

    yes5.pack(pady=0)

    no5.pack(pady=5)







def hideButtonsN1():

    yes1.pack_forget()

    q1.pack_forget()

    no1.pack_forget()

    gamer = False

    traits.append(' person')

    runQ2()

def hideButtonsY1():                                        #question1

    yes1.pack_forget()

    q1.pack_forget()

    no1.pack_forget()

    traits.append(' gamer')

    runQ2()





def hideButtonsN2():

    yes2.pack_forget()

    q2.pack_forget()

    no2.pack_forget()

    maybe2.pack_forget()

    traits.append('n extroverted')

    runQ3()

def hideButtonsM2():

    yes2.pack_forget()

    q2.pack_forget()

    no2.pack_forget()
#                                                                            question 2
    maybe2.pack_forget()

    traits.append(' sometimes social')

    runQ3()

def hideButtonsY2():

    yes2.pack_forget()

    q2.pack_forget()

    no2.pack_forget()

    traits.append('n introverted')

    maybe2.pack_forget()

    runQ3()





def hideButtonsY3():

    yes3.pack_forget()

    q3.pack_forget()

    no3.pack_forget()

    traits.append('indoors')

    maybe3.pack_forget()

    runQ4()

def hideButtonsN3():

    yes3.pack_forget()

    q3.pack_forget()

    no3.pack_forget()                                       #question 3

    traits.append('outdoors')

    maybe3.pack_forget()

    runQ4()

def hideButtonsM3():

    yes3.pack_forget()

    q3.pack_forget()

    no3.pack_forget()

    traits.append('indoors and outdoors')

    maybe3.pack_forget()

    runQ4()




def hideButtonsS4():

    sun4.pack_forget()

    q4.pack_forget()

    rain4.pack_forget()

    if traits[2] == 'indoors':

        traits.append('staying inside on sunny days')

    elif traits[2] == 'outdoors':

        traits.append('being outside in the sun')

    else:

        traits.append('sunny days')

    runQ5()

def hideButtonsR4():                                                                        #question 4

    sun4.pack_forget()

    q4.pack_forget()

    rain4.pack_forget()

    if traits[2] == 'indoors':

        traits.append('being inside and hearing and/or watching the rain')

    elif traits[2] == 'outdoors':

        traits.append('being outside on rainy days')

    else:

        traits.append('the peace and quiet of rain')

    runQ5()









def hideButtonsY5():

    yes5.pack_forget()

    q5.pack_forget()

    no5.pack_forget()

    if traits[0] == ' gamer':

        traits[0] = ', book enjoying gamer'

    else:

        traits[0] = ' reader'

    ending()

def hideButtonsN5():                                                                        #question 5

    yes5.pack_forget()

    q5.pack_forget()

    no5.pack_forget()

    ending()










def hide_intro():

    intro.pack_forget()

    hideIntro.pack_forget()

    q1.pack(pady=20)

    yes1.pack(pady=0)                                                               #hide introduction label and start question 1

    no1.pack(pady=10)

def ending():

    endText = tk.Label(root,text = 'You are a'+traits[1]+', '+traits[2]+' enjoying'+traits[0]+' who enjoys '+traits[3]+'.')                  # final output

    endText.pack(pady=20)



no1 = tk.Button(root, text = 'No',command=hideButtonsN1)
yes1 = tk.Button(root, text = 'Yes',command=hideButtonsY1)                  #question 1
q1 = tk.Label(root, text = 'Do you like gaming?')



no2 = tk.Button(root, text = 'No',command=hideButtonsN2)
yes2 = tk.Button(root, text = 'Yes',command=hideButtonsY2)                              #questopn 2
maybe2 = tk.Button(root, text = 'Maybe',command=hideButtonsM2)
q2 = tk.Label(root, text = 'Do you like socializing?')



no3 = tk.Button(root, text = 'No',command=hideButtonsN3)
yes3 = tk.Button(root, text = 'Yes',command=hideButtonsY3)                                  #question 3
maybe3 = tk.Button(root, text = 'Maybe',command=hideButtonsM3)
q3 = tk.Label(root, text = 'Do you like staying inside?')



rain4 = tk.Button(root, text = 'Rain',command=hideButtonsR4)
sun4 = tk.Button(root, text = 'Sun',command=hideButtonsS4)                                  # question 4
q4 = tk.Label(root, text = 'Do you like the sun or the rain?')



yes5 = tk.Button(root, text = 'Yes',command=hideButtonsY5)
no5 = tk.Button(root, text = 'No',command=hideButtonsN5)                                  # question 5
q5 = tk.Label(root, text = 'Do you like to read?')




intro = tk.Label(root, text='''Hello! This is a personality tester. 
Answer these five questions and it will 
tell you what it thinks about you!''') #intro
intro.pack(pady=20)                                                                     #introduction 
hideIntro = tk.Button(root, text='Begin!', command = hide_intro)
hideIntro.pack(pady=0)



root.mainloop()             #start the code