# General description of the project

This is our project of the alphabot.  
It use sockets (TCP) to connect the server (raspberry on the Alphabot) with the client (on our computers).  
  
Our Alphabt can also make complex moves. Furthermore we can see if our battery are charged or not with the command "battery".  

We also use threads to manage client on our server.

# What we implemented
  
To make complex moves we use a DataBase readed with the library "sqlite3" who contain a table (Movimenti) with the name of the move and the sequence of basic movements (forward, backward, left, right, stop) to make them.  
We use also the library subrocess to control our battery.  

By Masia Matteo & Fenoglio Cristian
