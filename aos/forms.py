from django import forms
from aos.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user',)

    def save(self, user, commit = True):
        post = super(PostForm, self).save(commit = False)
        post.user = user

        if commit:
            post.save()

        return post
