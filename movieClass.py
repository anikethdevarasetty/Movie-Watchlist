from datetime import date
#movie class properties
class movieObj:
    name = "" 
    lang = ""
    category = 0
    rating = 0
    wdate = ""
    comments = ""
    status = 0

    def __init__(self, gname):
        self.name = gname

    def setName(self, gname):
        self.name = gname
        
    def getName(self):
        return self.name

    def setLang(self, glang):
        self.lang = glang

    def getLang(self):
        return self.lang

    def setCat(self, num):
        self.category = num

    def getCat(self):
        return self.category

    def setWatch(self, num):
        self.status = num

    def getWatch(self):
        return self.status

    def setRating(self, rev):
        self.rating = rev

    def getRating(self):
        return self.rating

    def setComments(self, comms):
        self.comments = comms

    def getComments(self):
        return self.comments

    def setDate(self, gdate):
        self.wdate = gdate

    def setToday(self):
        today = date.today()
        self.wdate = today.strftime("%m/%d/%y")

    def getDate(self):
        return self.wdate