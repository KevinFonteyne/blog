# mini challenge 1 (class 4)

## blog project

Using what we've learned in classs 1, 2 and 3, let's create and configure a new project

1. The project directory should be `blog`.
2. There should be a configuration folder within it named `config`.
3. Apps for `pages` and `posts` should exist.
4. All apps should be installed.
5. A home page.
6. An about page.
7. Using the model provided below, addd support for:
    7.1. Creating new posts.
    7.2. Listing all posts.
    7.3. Viewing a detail of a post by specifying their ID.
8. Add bootstrap and a navbar.
9. Add static files.

### Note: Your project must be based on a real or ficitonal newspaper.

### Model:

```
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=256)
    subtitle =models.CharField(max_length=256)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self)
        return self.title

    def get_absolute_url(self)
        return reverse('YOUR_DETAIL_URLPATTERN_NAME' args=[self.id])

```  

# Mini challenge 1

### Create two additional ListViews with the following criteria:
1. The first list view should filter so that it returns only "published" posts.
2. The second list view should filter so that it returns only "archived" posts.


## Additionally:
1. Add an anchor tag to the dropdown list so that only logged in users can access these new features.
2. Users should only see their own posts in these views (meaning, they are the author).
