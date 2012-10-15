from django.conf.urls.defaults import *
from guestbook.api import EntryResource

entry_resource = EntryResource()
urlpatterns = patterns('guestbook.views',
    (r'^$', 'list_greetings'),
    (r'^api/', include(entry_resource.urls)),
    (r'^sign$', 'create_greeting')
)