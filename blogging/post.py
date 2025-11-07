from datetime import datetime
class Post:
    def __init__(self, code, title, text): # initialize post with given fields
        now = datetime.now()  # get current time down to millisecond
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S.%f") # turn the time above into formatted string
        self.code = code 
        self.title = title
        self.text = text
        self.creation = timestamp
        self.update = timestamp
        return 
    
    def __eq__ (self,other): 
        return (self.code == other.code   and 
               self.title == other.title and
               self.text == other.text)

    def __str__(self):
        return f"{self.code}, {self.title}, {self.text}, {self.creation}, {self.update}"
 
    def __repr__(self):
        return f"Post({self.code}, {self.title}, {self.text}, {self.creation}, {self.update})"
