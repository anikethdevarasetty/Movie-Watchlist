import tkinter
import tkinter.messagebox
import pickle
import movieClass

root = tkinter.Tk()
root.title("Movie Watchlist")

#functions

#add
def addToOne():
    movie = entryMov.get()
    if movie != "":
        newMov = movieClass.movieObj(movie) #new movie
        entryMov.delete(0,tkinter.END)
        newMov.setCat(1)
        listboxOne.insert(tkinter.END, newMov.name) #add to listbox one
        movieList.append(newMov) #add to global list
    else:
        tkinter.messagebox.showwarning(title="Error Code 47", message= "You must enter a movie!")

def addToTwo():
    movie = entryMov.get()
    if movie != "":
        newMov = movieClass.movieObj(movie)
        entryMov.delete(0,tkinter.END)
        newMov.setCat(2)
        listboxTwo.insert(tkinter.END, newMov.name)
        movieList.append(newMov)
    else:
        tkinter.messagebox.showwarning(title="Error Code 47", message= "You must enter a movie!")

def addToThree():
    movie = entryMov.get()
    if movie != "":
        newMov = movieClass.movieObj(movie)
        entryMov.delete(0,tkinter.END)
        newMov.setCat(3)
        listboxThree.insert(tkinter.END, newMov.name)
        movieList.append(newMov)
    else:
        tkinter.messagebox.showwarning(title="Error Code 47", message= "You must enter a movie!")

#delete
def delete():
    setUnwatched()
    index = listboxOne.curselection() #find index of selected cell
    if len(index) != 0: #if if listbox 1
        name = listboxOne.get(index[0]) #get name of movie to delete
        movieList.pop(getIndex(name)) #delete from global list
        listboxOne.delete(index[0]) #delete from listbox

    index = listboxTwo.curselection()
    if len(index) != 0: #if in listbox 2
        name = listboxTwo.get(index[0])
        movieList.pop(getIndex(name))
        listboxTwo.delete(index[0])

    index = listboxThree.curselection()
    if len(index) != 0: #if in listbox 3
        name = listboxThree.get(index[0])
        movieList.pop(getIndex(name))
        listboxThree.delete(index[0])

#get index of movie in global list
def getIndex(gname):
    index = 0
    for thisMovie in movieList:
        if gname == thisMovie.name:
            return index
        index += 1

#save
def saveMovies():
    pickle.dump(movieList,open("movieList.dat", "wb"))

#load
def loadMovies():
    tIndex = 0
    hIndex = 0
    eIndex = 0
    for thisMovie in movieList:
        if thisMovie.category == 1:
            listboxOne.insert(tkinter.END, thisMovie.name)
            if thisMovie.status == 1:
                listboxOne.itemconfig(tIndex, {'bg' : 'yellow'})
            tIndex += 1
        if thisMovie.category == 2:
            listboxTwo.insert(tkinter.END, thisMovie.name)
            if thisMovie.status == 1:
                listboxTwo.itemconfig(hIndex, {'bg' : 'yellow'})
            hIndex += 1
        if thisMovie.category == 3:
            listboxThree.insert(tkinter.END, thisMovie.name)
            if thisMovie.status == 1:
                listboxThree.itemconfig(eIndex, {'bg' : 'yellow'})
            eIndex += 1
 
def setWatched():
    index = listboxOne.curselection()
    if len(index) != 0: #if in listbox 1
        listboxOne.itemconfig(index[0], {'bg': 'yellow'}) #set highlight color
        listIndex = getIndex(listboxOne.get(index[0])) # get index in global list 
        movieList[listIndex].setWatch(1) #set status of movie

    index = listboxTwo.curselection()
    if len(index) != 0: #if in listbox 2
        listboxTwo.itemconfig(index[0], {'bg': 'yellow'})
        listIndex = getIndex(listboxTwo.get(index[0]))
        movieList[listIndex].setWatch(1)

    index = listboxThree.curselection()
    if len(index) != 0: #if in listbox 3
        listboxThree.itemconfig(index[0], {'bg': 'yellow'})
        listIndex = getIndex(listboxThree.get(index[0]))
        movieList[listIndex].setWatch(1)
       
def setUnwatched():
    index = listboxOne.curselection()
    if len(index) != 0: #if in listbox 1
        listboxOne.itemconfig(index[0], {'bg': 'white'})
        listIndex = getIndex(listboxOne.get(index[0]))
        movieList[listIndex].setWatch(0)

    index = listboxTwo.curselection()
    if len(index) != 0: #if in listbox 2
        listboxTwo.itemconfig(index[0], {'bg': 'white'})
        listIndex = getIndex(listboxTwo.get(index[0]))
        movieList[listIndex].setWatch(0)

    index = listboxThree.curselection()
    if len(index) != 0: #if in listbox 3
        listboxThree.itemconfig(index[0], {'bg': 'white'})
        listIndex = getIndex(listboxThree.get(index[0]))
        movieList[listIndex].setWatch(0)

#bind multiple listboxes to one scrollbar
def yview(*args):
    # scroll multipple listboxes together 
    listboxOne.yview(*args)
    listboxTwo.yview(*args)
    listboxThree.yview(*args)

#binding mousewheel
def OnMouseWheel(event):
    listboxOne.yview("scroll", event.delta,"units")
    listboxTwo.yview("scroll",event.delta,"units")
    listboxThree.yview("scroll",event.delta,"units")
    return "break"

def key_pressed(event):
    if event.keysym == "Delete":
        delete()

    #ctrl + w sets movie to watch
    if event.keysym == 'w':
        try:
            setWatched()
        except:
            pass

    #ctrl + u sest movie to unwatched
    if event.keysym == 'u':
        try:
            setUnwatched()
        except:
            pass

    #ctrl + s saves watchlist
    if event.keysym == 's':
        saveMovies()

    #ctrl + i opens information window of movie
    if event.keysym == 'i':
        try:
            getInfo()
        except:
            pass

def getInfo():
    infoWindow = tkinter.Toplevel(root)
    infoWindow.title("More Info")

    infoCanvas = tkinter.Canvas(infoWindow, height = 300, width = 300)
    infoCanvas.grid(columnspan = 2, rowspan = 10)

    #variables to hold info from GUI widgets
    nameVar = tkinter.StringVar(infoWindow)
    langVar = tkinter.StringVar(infoWindow)
    rateVar = tkinter.IntVar(infoWindow)
    todayStatus = tkinter.IntVar(infoWindow)
    dateVar = tkinter.StringVar(infoWindow)
    status = tkinter.IntVar(infoWindow)
    commVar = tkinter.StringVar(infoWindow)

    #movie name
    nameLab = tkinter.Label(infoWindow, text = "Name:", justify = "left")
    nameLab.grid(column = 0, row = 0)
    nameEntry = tkinter.Entry(infoWindow, textvariable = nameVar)
    nameEntry.grid(column = 1, row = 0)

    #movie language
    langLab = tkinter.Label(infoWindow, text = "Language: ", justify = "left")
    langLab.grid(column = 0, row = 1)
    langEntry = tkinter.Entry(infoWindow, textvariable = langVar)
    langEntry.grid(column = 1, row = 1)

    #movie rating
    rateLab = tkinter.Label(infoWindow, text = "Rating: ", justify = "left")
    rateLab.grid(column = 0, row = 2)
    
    rateEntry = tkinter.Scale(infoWindow, from_ = 1, to = 10, variable = rateVar, orient = "horizontal")
    rateEntry.grid(column = 1, row = 2)

    #movie watch status
    
    watched = tkinter.Checkbutton(infoWindow, text = "Already Watched?", variable = status)
    watched.grid(columnspan = 2, column = 0, row = 3)

    #watch date
    dateLab = tkinter.Label(infoWindow, text = "Watch Date: ", justify = "left")
    dateLab.grid(column = 0, row = 4)
    
    today = tkinter.Checkbutton(infoWindow, text = "Today?", variable = todayStatus)
    today.grid(column = 1, row = 4)

    dateEntry = tkinter.Entry(infoWindow, textvariable = dateVar)
    dateEntry.grid(column = 1, row = 5)

    #movie extra comments
    commLab = tkinter.Label(infoWindow, text = "Comments:", justify = "left")
    commLab.grid(column = 0, row =6)
    
    commEntry = tkinter.Entry(infoWindow, textvariable = commVar)
    commEntry.grid(column = 1, row = 6)

    saveButton = tkinter.Button(infoWindow, text = "Save", width = 16, 
        command = lambda: saveInfo(nameVar.get(),langVar.get(),rateVar.get(),status.get(), todayStatus.get(),
        dateVar.get(),commVar.get()))
    saveButton.grid(row = 8, column = 0)

    closeButton = tkinter.Button(infoWindow, text = "Close", width = 16, command = infoWindow.destroy)
    closeButton.grid(row = 8, column = 1)


    #setting stuff
    index = listboxOne.curselection()
    if len(index) != 0:
        listIndex = getIndex(listboxOne.get(index[0])) #get index

    index = listboxTwo.curselection()
    if len(index) != 0:
        listIndex = getIndex(listboxTwo.get(index[0]))

    index = listboxThree.curselection()
    if len(index) != 0:
        listIndex = getIndex(listboxThree.get(index[0]))

    nameEntry.insert(0, movieList[listIndex].getName()) #name
    lang = movieList[listIndex].getLang()
    langEntry.insert(0,movieList[listIndex].getLang()) #language
    rateEntry.set(movieList[listIndex].getRating()) #rating
    if movieList[listIndex].getWatch() == 1:
        watched.select()
        dateEntry.insert(0, movieList[listIndex].getDate())
    else:
        watched.deselect()
    commEntry.insert(0, movieList[listIndex].getComments())

    infoWindow.mainloop()

def saveInfo(nameVar,langVar,rateVar,status,todayStatus, dateVar,commVar):
    listIndex = getIndex(nameVar)
    movieList[listIndex].setName(nameVar)
    movieList[listIndex].setLang(langVar)
    movieList[listIndex].setRating(rateVar)
    if status == 1:
        setWatched()
        movieList[listIndex].setWatch(1)
        movieList[listIndex].setDate(dateVar)
        if todayStatus == 1:
            movieList[listIndex].setToday()
    else:
        setUnwatched()
        movieList[listIndex].setWatch(0)
    movieList[listIndex].setComments(commVar)
    
#GUI ##################################################################################
frame_movies = tkinter.Frame(root)
frame_movies.pack()

listboxOne = tkinter.Listbox(frame_movies, height = 10, width = 20)
listboxOne.pack(side=tkinter.LEFT)

listboxTwo = tkinter.Listbox(frame_movies, height = 10, width = 20)
listboxTwo.pack(side=tkinter.LEFT)

listboxThree = tkinter.Listbox(frame_movies, height = 10, width = 20)
listboxThree.pack(side=tkinter.LEFT)

scrollbar = tkinter.Scrollbar(frame_movies, command = yview)
scrollbar.pack(side = tkinter.RIGHT, fill=tkinter.Y)

listboxOne.config(yscrollcommand = scrollbar.set)
listboxTwo.config(yscrollcommand = scrollbar.set)
listboxThree.config(yscrollcommand = scrollbar.set)

listboxOne.bind("<MouseWheel>", OnMouseWheel)
listboxTwo.bind("<MouseWheel>", OnMouseWheel)
listboxThree.bind("<MouseWheel>", OnMouseWheel)

listboxClick = tkinter.Listbox(root,height = 1, width = 60)
listboxClick.pack()
listboxClick.insert(0,"Freespace Click")

entryMov = tkinter.Entry(root, width = 50)
entryMov.pack()

#menubar style
menubar = tkinter.Menu(root)

addmenu = tkinter.Menu(menubar, tearoff = 0)
addmenu.add_command(label = "Add to One", command = addToOne)
addmenu.add_command(label = "Add to Two", command = addToTwo)
addmenu.add_command(label = "Add to Three", command = addToThree)
addmenu.add_separator()
addmenu.add_command(label = "Delete", command = delete)
menubar.add_cascade(label = "Add/Delete", menu = addmenu)

othermenu = tkinter.Menu(menubar, tearoff = 0)
othermenu.add_command(label = "Set Watched", command = setWatched)
othermenu.add_command(label = "Set Unwatched", command = setUnwatched)
othermenu.add_separator()
othermenu.add_command(label = "Save", command = saveMovies)
menubar.add_cascade(label = "Set/Save", menu = othermenu)

#button style
frame_addbuttons = tkinter.Frame(root)
frame_addbuttons.pack()

button_addTel = tkinter.Button(frame_addbuttons, text = "Add to One", width = 16, command = addToOne)
button_addTel.pack(side = tkinter.LEFT)

button_addHin = tkinter.Button(frame_addbuttons, text = "Add to Two", width = 16, command = addToTwo)
button_addHin.pack(side = tkinter.LEFT)

button_addEng = tkinter.Button(frame_addbuttons, text = "Add to Three", width = 16, command = addToThree)
button_addEng.pack(side = tkinter.RIGHT)

button_getInfo = tkinter.Button(root, text = "Get Movie Infomation", width = 48, command = getInfo)
button_getInfo.pack()

# button_delete = tkinter.Button(root, text = "Delete", width = 48, command=delete)
# button_delete.pack()

# button_saveMovs = tkinter.Button(root, text ="Save Watchlist", width = 48, command = saveMovies)
# button_saveMovs.pack()

# button_setWatched = tkinter.Button(root, text = "Set Watched", width = 25, command = setWatched)
# button_setWatched.pack(side=tkinter.LEFT)

# button_setUnwatched = tkinter.Button(root, text= "Set Unwatched", width = 25, command = setUnwatched)
# button_setUnwatched.pack(side =tkinter.RIGHT)

#loading movie list file
try: 
    movieList = pickle.load(open("movieList.dat", "rb")) 
except: 
    movieList = [] 
loadMovies() #populate GUI window
root.config(menu=menubar)
root.bind("<Control-s>", key_pressed)
root.bind("<Control-w>", key_pressed)
root.bind("<Control-u>", key_pressed)
root.bind("<Control-i>", key_pressed)
root.bind("<Delete>", key_pressed)
root.mainloop()