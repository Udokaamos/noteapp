from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .models import Post


# a signal to delete an image and audio, if a post is deleted
@receiver(post_delete, sender=Post) # the signal is triggered after a delete() function in the Post model
def submission_delete(sender, instance, **kwargs): # taking the model and the specific post (instance) as parameters
    instance.text.delete(save=False)


# a signal to delete an image, if a post is updated with another image or the image is removed
@receiver(pre_save, sender=Post) # the signal is triggered before a save() function in the Post model
def updating_text_delete(sender, instance, **kwargs): # taking the model and the specific post (instance) as parameters
    if instance.pk:
        # running this code first
        try:
            old_text = Post.objects.get(pk=instance.pk).text
        # if the post doesn't exist, then return False
        except Post.DoesNotExist:
            return False
        # if there wasn't that exception
        else:
            new_text = instance.text
            if new_text:
                if old_text and old_text.url != new_text.url:
                    old_text.delete(save=False)
            else:
                old_text.delete(save=False)
    if not instance.pk:
        return False


