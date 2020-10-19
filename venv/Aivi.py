from tkinter import *
from bs4 import BeautifulSoup
import requests


win = Tk()
win.title('Movie Recommendation')
emotionn = StringVar()
img = PhotoImage(file='back.png')
win.geometry('500x500+%d+%d'%(win.winfo_screenwidth()/2-250, win.winfo_screenheight()/2-250))
canvas = Canvas(win, width=500, height=500)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.pack()
listbox = Listbox(canvas)
emotionlist = Listbox(canvas)
emotionlist.config(bg = '#d9d9fd')
emotionlist.insert(END, 'Emotionless', 'Anger', 'Sad', 'Anticipation', 'Surprise', 'Enjoyment', 'Happy', 'Disgust', 'Fear')
emotionlist.place(x=430, y=250, width=70, height=150)
label = Label(canvas, text='Enter your emotion', fg='navy blue')
label.place(x=20, y=20, width=460, height=20)
entry = Entry(canvas, textvariable=emotionn, font=('Segoe Print', 12))
entry.place(x=20, y=50, width=460, height=30)
b = Button(canvas, text='Search Other Emotion', fg='yellow', bg='red')
button = Button(canvas, text='Search', bg='red', fg='yellow')
button.place(x=230, y=470, width=40, height=20)

def newMain():
    emotionn.set('')
    listbox.delete(0,END)
    listbox.place_forget()
    b.place_forget()
    emotionlist.place(x=430, y=250, width=70, height=150)
    label.place(x=20, y=20, width=460, height=20)
    entry.place(x=20, y=50, width=460, height=30)
    button.place(x=230, y=470, width=40, height=20)

b.config(command=newMain)
scrollbar = Scrollbar(canvas, orient=VERTICAL)
def search():
    label.place_forget()
    button.place_forget()
    entry.place_forget()
    emotionlist.place_forget()
    b.place(x=175, y=470, width=150, height=20)
    if emotionn.get() == "Emotionless":

        url = "https://www.imdb.com/chart/top"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        s = soup.find_all(class_='titleColumn')

        for i in s:
            listbox.insert(END, i.find_all('a')[0].text)
        listbox.place(x=40, y=40, width=420, height=420)
        listbox.config(font=('Segoe Print', 10))
        scrollbar.config(command = listbox.yview)
        listbox.config(yscrollcommand=scrollbar.set)


    elif emotionn.get() == "Enjoyment":

        url2 = 'https://www.imdb.com/search/title?sort=num_votes&title_type=tv_series'
        page2 = requests.get(url2)
        soup2 = BeautifulSoup(page2.content, 'html.parser')
        s = soup2.find_all('div', {'class': 'lister-item-content'})

        for i in s:
            listbox.insert(END, i.find_all('a')[0].text)
        listbox.place(x=40, y=40, width=420, height=420)
        listbox.config(font=('Segoe Print', 10))
        scrollbar.config(command = listbox.yview)
        listbox.config(yscrollcommand=scrollbar.set)

    elif emotionn.get() == "Happy":

        url3 = 'https://www.imdb.com/list/ls000183548/'
        page3 = requests.get(url3)
        soup3 = BeautifulSoup(page3.content, 'html.parser')
        s = soup3.find_all('div', {'class': 'lister-item-content'})

        for i in s:
            listbox.insert(END, i.find_all('a')[0].text)
        listbox.place(x=40, y=40, width=420, height=420)
        listbox.config(font=('Segoe Print', 10))
        scrollbar.config(command = listbox.yview)
        listbox.config(yscrollcommand=scrollbar.set)

    elif emotionn.get() == "Sad":

        url = 'https://www.imdb.com/search/title?genres=comedy&title_type=feature&explore=genres'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        s = soup.find_all('div', {'class': 'lister-item-content'})

        for i in s:
            listbox.insert(END, i.find_all('a')[0].text)
        listbox.place(x=40, y=40, width=420, height=420)
        listbox.config(font=('Segoe Print', 10))
        scrollbar.config(command = listbox.yview)
        listbox.config(yscrollcommand=scrollbar.set)


    elif emotionn.get() == "Anger":

        url = 'https://www.imdb.com/search/title?&genres=family&explore=title_type,genres'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        s = soup.find_all('div', {'class': 'lister-item-content'})

        for i in s:
            listbox.insert(END, i.find_all('a')[0].text)
        listbox.place(x=40, y=40, width=420, height=420)
        listbox.config(font=('Segoe Print', 10))
        scrollbar.config(command = listbox.yview)
        listbox.config(yscrollcommand=scrollbar.set)



    elif emotionn.get() == "Fear":

        url = 'https://www.imdb.com/search/title?&genres=musical&explore=title_type,genres'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        s = soup.find_all('div', {'class': 'lister-item-content'})

        for i in s:
            listbox.insert(END, i.find_all('a')[0].text)
        listbox.place(x=40, y=40, width=420, height=420)
        listbox.config(font=('Segoe Print', 10))
        scrollbar.config(command = listbox.yview)
        listbox.config(yscrollcommand=scrollbar.set)


    elif emotionn.get() == "Anticipation":

        url4 = 'https://www.imdb.com/list/ls058238715/'
        page4 = requests.get(url4)
        soup4 = BeautifulSoup(page4.content, 'html.parser')
        s = soup4.find_all('div', {'class': 'lister-item-content'})

        for i in s:
            listbox.insert(END, i.find_all('a')[0].text)
        listbox.place(x=40, y=40, width=420, height=420)
        listbox.config(font=('Segoe Print', 10))
        scrollbar.config(command = listbox.yview)
        listbox.config(yscrollcommand=scrollbar.set)



    elif emotionn.get() == "Disgust":

        url4 = 'https://www.imdb.com/search/title?genres=adventure&title_type=feature&explore=genres'
        page4 = requests.get(url4)
        soup4 = BeautifulSoup(page4.content, 'html.parser')
        s = soup4.find_all('div', {'class': 'lister-item-content'})

        for i in s:
            listbox.insert(END, i.find_all('a')[0].text)
        listbox.place(x=40, y=40, width=420, height=420)
        listbox.config(font=('Segoe Print', 10))
        scrollbar.config(command = listbox.yview)
        listbox.config(yscrollcommand=scrollbar.set)


    elif emotionn.get() == "Surprise":

        url4 = 'https://www.imdb.com/list/ls050514768/'
        page4 = requests.get(url4)
        soup4 = BeautifulSoup(page4.content, 'html.parser')
        s = soup4.find_all('div', {'class': 'lister-item-content'})

        for i in s:
            listbox.insert(END, i.find_all('a')[0].text)
        listbox.place(x=40, y=40, width=420, height=420)
        listbox.config(font=('Segoe Print', 10))
        scrollbar.config(command = listbox.yview)
        listbox.config(yscrollcommand=scrollbar.set)


    else:
        print('Enter Valid Emotion')

button.config(command=search)
win.mainloop()