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
![1](https://user-images.githubusercontent.com/72485869/147384698-b675f058-fca1-4467-99db-98c3af4e5204.jpeg)
![2](https://user-images.githubusercontent.com/72485869/147384700-00a0ca23-15aa-449c-b5c1-971103991dbd.jpeg)
![3](https://user-images.githubusercontent.com/72485869/147384702-36792fc4-88d2-44f4-810e-69264ad0ac31.jpeg)
![4](https://user-images.githubusercontent.com/72485869/147384713-a2bb85e9-e8a2-4620-bc44-630c19de42af.jpeg)

** Workflow in django **

![5](https://user-images.githubusercontent.com/72485869/147384759-a6f84cd7-3799-4f11-8cdb-bf50e6af5020.jpeg)
![6](https://user-images.githubusercontent.com/72485869/147384760-487cf103-26c0-4e8d-adb8-059a3f050293.jpeg)


## How do we know who send the message to ?
- We utilize a package called channel
1. Every client has a reply_chaannel
2. Keep track of user in a connected list
3. Chat app -> multiple users (one room)
4. Channel uses Groups : Add user's channel into the group

- image: 
![7](https://user-images.githubusercontent.com/72485869/147384763-85e80974-e189-41a4-9673-b065c9840553.jpeg)




