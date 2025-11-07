from .blog import Blog  
class Controller:
    def __init__(self):
        self.logged_in = False 
        self.blogs     = [] 
        self.current_blog = None 
        
    
    def login(self,username,password):
        """ login using hardcoded username and password, if not logged in already """
        if(self.logged_in == False and username == "user" and password == "blogging2025"):
            self.logged_in = True 
            return True 
        else:
            return False


    def logout(self):
        """ logout, if currently logged in """
        if(self.logged_in == False):
            return False
        else:
            self.logged_in = False
            return True


    def create_blog(self,blog_id, name, url, email):
        """ create a new blog, takes blog id, name, url, and email as parameters """
        if(self.logged_in == False): #if nobody logged in, can't create blog
            return None 

        if any(blog.blog_id == blog_id for blog in self.blogs): #if blog with same ID already exits, cannot create that blog   
            return None
        
        new_blog = Blog(blog_id, name, url, email) # create new blog
        self.blogs.append(new_blog) #append new blog to blogs[]
        return new_blog #return blog
    

    def search_blog(self, blog_id): 
        """ search for blog from given ID """
        if(self.logged_in == False):
            return None #if not logged in, cannot search
        for blog in self.blogs: #check all blogs for equal blog ID, return blog if ID is matched
            if blog.blog_id == blog_id:
                return blog
        return None    #if no ID match found return none


    def retrieve_blogs(self, name): 
        """ retrieve all blogs with search "search query" within a blog's name """
        if(self.logged_in == False):
            return None #check login status
        matching_blogs = [] # to store any blogs matched
        for blog in self.blogs: 
            if name in blog.name: #if "name" is identical or a substring of a blog's name, append blog
                matching_blogs.append(blog) 
        return matching_blogs 


    def update_blog(self, blog_id, new_id, new_name, new_url, new_email):
        """ update a blog by given id """
        if(self.logged_in == False) or (blog_id != new_id and self.search_blog(new_id)): #if not logged in, or new blog id already exists, cannot update
            return False
    
        current = self.get_current_blog()
        if(current is not None and current.blog_id == blog_id): #check if trying to update current blog
            return False
        
        blog = self.search_blog(blog_id) #if blog exists, find it and update it
        if blog:
            blog.blog_id = new_id
            blog.name = new_name
            blog.url = new_url
            blog.email = new_email
            return True
        else:
            return False


    def delete_blog(self, blog_id):
        """ delete a blog by given id """
        if self.logged_in == False or not self.search_blog(blog_id):
            return False
        
        current = self.get_current_blog() #check to not delete current blog
        if(current is not None and current.blog_id == blog_id):
            return False
        
        index=0
        for blog in self.blogs:
            if blog.blog_id == blog_id:
                removed_blog = self.blogs.pop(index)
                del removed_blog
                return True
            index+=1


    def list_blogs(self): 
        """ lists all blogs """
        if(self.logged_in == False):
            return None
        return self.blogs


    def set_current_blog(self, blog_id): 
        """ set current blog (as long as logged in and blog exists) """
        if(self.logged_in == False or not self.search_blog(blog_id)):
            return None
        self.current_blog = self.search_blog(blog_id)

    def get_current_blog(self): # get current blog if logged in
        if(self.logged_in == False):
            return None 
        return self.current_blog


    def unset_current_blog(self): 
        """ set current blog to none """
        if(self.logged_in == False):
            return None
        self.current_blog = None      


    def create_post(self,code,title,text):
        if(self.logged_in is False):
            return False
        blog = self.get_current_blog()
        return blog.update_post(code,title,text)
    
    def search_post(self,code):
        if(self.logged_in is False):
            return False
        blog = self.get_current_blog()
        return blog.search_post(code)
    def retrieve_posts(self,text):
        if(self.logged_in is False):
                return False
        blog = self.get_current_blog()
        return blog.retrieve_posts(text)
    
    
    def update_post(self,code,title,text):
        if(self.logged_in is False):
            return False
        blog = self.get_current_blog()
        return blog.update_post(code,title,text)


    def delete_post(self,code):
        if(self.logged_in is False):
                return False
        blog = self.get_current_blog()
        return blog.delete_post(code)
        

    def list_post(self):
        if(self.logged_in is False):
                return False
        blog = self.get_current_blog()
        return blog.list_posts()