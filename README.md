# Django_Channels
# DJANGO CHANNEL PROJECT - Chatrooms
## develiop an asynchronous chatrooom services using Django and the Channel package
## Concept used :
 Websockets, ASGI , Channels Package

# Project specifications
1. Real live chat(multiple users)
2. User registeration
3.Track conversation and users in chat
4. Record/save conversations
5. Delete/edit messages

## Basic Information .
<details><summary>Synchronous Vs Asynchronous</summary>
<p>

1. Synchronous :- Synchronous communication is limited due to the lapses in application updates that are presented to the user at regular intervals. Even if a synchronous application is designed so that it automatically refreshes information from the application server at regular intervals (for example, every 12 seconds), there will still be consistent periods of delay between data refreshes.
- web synchronous request (HTTP request)
- send request -> stop executing -> wait for reply
- HTTP 200 or HTTP 404  etc

2. Asynchronous :Asynchronous  applications deliver continuously updated application data to users. This is achieved by separating client requests from application updates. Multiple asynchronous communications between client and server may occur simultaneously or in parallel with one another.
- Make request "launch" the request
- forget about it -> carry on executing tasks
- define/create a callback function
</p>
</details>
### Synchronous Vs Asynchronous


<details><summary>Web Sockets</summary>
<p>

### Websockets allows us to create a aynchronous environment
- Bi-directional protocol : server and client message at any time  
> HTTP Protocol is unidirectional
- Full-duplex communication : client and server can talk to each other independently at the same time
- Supported by most browsers
- Secured Websocket's (WSS)  

</p>
</details>



## How do we know who send the message to ?
- We utilize a package called channel
1. Every client has a reply_chaannel
2. Keep track of user in a connected list
3. Chat app -> multiple users (one room)
4. Channel uses Groups : Add user's channel into the group

- image: 



