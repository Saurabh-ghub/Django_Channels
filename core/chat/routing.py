from django.urls import re_path # to utilize more path utilites so we use relative paths. We need this because sometimes redular path doesn't meet our requirement
from . import consumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$',consumer.ChatRoomConsumer.as_asgi()),

]
# in the above ` \w+ ` means whatever se type after / it is going to store in the room name
# ` w ` basically means word that can be uppercase or lowercase letter a or digits 0-9 or other character too 