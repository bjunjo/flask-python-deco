# Let's make a user class
class User():
    def __init__(self, name):
        self.name = name
        self.is_loggedin = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_loggedin == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_a_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

user = User("ByoungJun")
user.is_loggedin = True
create_a_blog_post(user)