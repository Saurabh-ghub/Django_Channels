# routing.py is same as urls.py 
from channels.auth import AuthMiddlewareStack  # for user authentication and also putting the user name
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

#just like urlpatterns, here we have application 

application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})