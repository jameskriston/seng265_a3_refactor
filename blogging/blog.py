class Blog:
    def __init__(self, blog_id, name, url, email):
        self.blog_id = blog_id
        self.name = name
        self.url = url
        self.email = email
        self.posts = []
        return
    
    def __eq__(self, other):
        return (self.blog_id == other.blog_id and
               self.name == other.name and
               self.url == other.url and 
               self.email == other.email)

    def __repr__(self):
        return f"Blog({self.blog_id}, {self.name}, {self.url}, {self.email}, {self.posts})"

    def __str__(self):
        return f"{self.blog_id}, {self.name}, {self.url}, {self.email}, {self.posts}"
