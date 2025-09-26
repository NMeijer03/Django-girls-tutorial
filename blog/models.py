from django.conf import settings
from django.db import models
from django.utils import timezone

# Defines the object. Inherits from django's models class giving all the functionality we need
class Post(models.Model):

    # A foreign key is a explicit reference to another object within our data
    # In this example we have a explicit reference to the writer of the post
    # Because of this reference we can trace back messages and moderate them if necessary.
    # Explicit references like this cannot be nothing. A post must have a author and therefore if the author deleted their account and the reference seizes to exist we need a strategy for deletion
    # Cascade means that once a reference is deleted any object containing that reference is also deleted
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Models contain attributes
    # Below we see 2 texts fields (title and text) for a post. Now everyone can add a title and text to their posts.
    # We also see a created_date field which automatically gets filled with the current time.
    # And a published that can be empty.
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # This function sets the published date of a object. The moment this function is called the published_date field of the object is updated with the current time.
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Dunder str.
    # The __str__ function is the string representation of a object. In this case we specify that it is just the title.
    # If we put self.text here instead we see the actual post content.
    def __str__(self):
        return self.title