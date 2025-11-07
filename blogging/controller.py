from .blog import Blog
from .post import Post  
from datetime import datetime

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


    def create_post(self,title,text): 
        """ creates a new post in current blog """
        if(self.logged_in == False):
            return None
        current_blog = self.get_current_blog()
        if(current_blog is None):
            return None  
        size = len(current_blog.posts) 
        new_post = Post(size+1,title,text)
        current_blog.posts.append(new_post) #add post to list of posts in blog
        return new_post
     
     ### Need to implement search_post() to pass create_post tests
     ### Also need to properly set up __eq__ in post.py, it may need
     ### to have fields for timestamps added, but that comparison of time
     ### could also be done seperately from that eq() to distinguish between
     ### identical posts made at different times


    def search_post(self,code):
        """ search for post by code in current blog """
        if(self.logged_in == False): #cannot search if not logged in
            return None
        current_blog = self.get_current_blog()  # get current blog
        if(current_blog is None):
            return None                         # cannot search post if no blog
        
        for post in current_blog.posts:         # look through posts for matching code
            if (post.code == code):
                return post

        return None
 

    def retrieve_posts(self,text):
        """ search in current blog for post with text inside of the post's title or text """
        if(self.logged_in == False):
            return None
        current_blog = self.get_current_blog()
        if(current_blog is None):
            return None
        retrieved_posts = []
        for post in current_blog.posts:
            if text in post.text or text in post.title:
                retrieved_posts.append(post)

        return retrieved_posts    
 

    def update_post(self, code, title, text):       
        """ update a post's content """
        if(self.logged_in == False):                # if not logged in cannot update
            return False
        
        current_blog = self.get_current_blog()      # if no current blog cannot update
        if current_blog is None:
            return False
        
        update_post = self.search_post(code)        # if no post found with code, cannot update        
        if(update_post is None):    
            return False
        
        update_post.title = title                   # set updated post fields
        update_post.text  = text
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S.%f")
        update_post.update = timestamp                    # there's no test for checking correct
        return update_post                          # updated timestamps, will need to add that

    
    def delete_post(self,code):
        """ delete a post by code within current blog """
        if(self.logged_in == False):                # cannot delete if not logged in
            return False
        current_blog = self.get_current_blog()
        if(current_blog is None):                   # cannot delete if no current blog
            return False
        if(len(current_blog.posts) == 0):           # cannot delete if no posts exists
            return False
        
        index = 0                                   # find correct post to delete
        for post in current_blog.posts:
            if post.code == code:
                removed_post = current_blog.posts.pop(index)
                del removed_post
                return True                         # return when post deleted
            index+=1
 

    def list_posts(self):   
        """ list all posts in order last created to first created """
        if(self.logged_in == False):                # cannot list if not logged in
            return None
        current_blog = self.get_current_blog()
        if(current_blog is None):                   # cannot list posts if no current blog
            return None
        if(len(current_blog.posts) is None):        # cannot list if no posts exist
            return None
        
        post_list = current_blog.posts # get list of posts
        sorted_list = sorted(post_list, key = lambda post: post.creation, reverse = True) #sort them 
        return sorted_list 
    



