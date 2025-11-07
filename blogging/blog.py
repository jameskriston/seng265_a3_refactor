from .post import Post
from datetime import datetime
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
    
    
    def search_post(self,code):
        """ search for post by code in current blog """
        for post in self.posts:         # look through posts for matching code
            if (post.code == code):
                return post
   

    def create_post(self,title,text): 
        """ creates a new post in current blog """
        size = len(self.posts) 
        new_post = Post(size+1,title,text)
        self.posts.append(new_post) #add post to list of posts in blog
        return new_post
            

    def retrieve_posts(self,text):
        """ search in current blog for post with text inside of the post's title or text """
        retrieved_posts = []
        for post in self.posts:
            if text in post.title or text in post.text:
                retrieved_posts.append(post)
        return retrieved_posts   
    

    def update_post(self, code, title, text):       
        """ update a post's content """
        post = self.search_post(code)        # if no post found with code, cannot update
        if(post is None):    
            return False    
        post.title = title
        post.text = text
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S.%f")
        post.update = timestamp      
        return post if post else False


    def delete_post(self,code):
        """ delete a post by code within current blog """
        index = 0                                   # find correct post to delete
        for post in self.posts:
            if post.code == code:
                removed_post = self.posts.pop(index)
                del removed_post
                return True                         # return when post deleted
            index+=1
        return False


    def list_posts(self):   
        """ list all posts in order last created to first created """
        if(len(self.posts) is None):        # cannot list if no posts exist
            return None
        
        post_list = self.posts # get list of posts
        sorted_list = sorted(post_list, key = lambda post: post.creation, reverse = True) #sort them 
        return sorted_list 
