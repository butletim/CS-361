# CS-361 - Microservice
Microservice for Student Roster


**A.** How to REQUEST data
  
  To request data I implemented useing ZeroMQ for Python. A JSON file is to be expected, so sending one is simple.
  
  To correctly call for the request would be something like this:
  
  ```
  socket.send_json(file_1_contents)
  ```

**B.** How to RECIEVE data

  To recieve data, it is very similar to requesting. This time, the code will recieve a string, indicating the file location of the PDF.
  
  A call will be something like this:
  
  ```
  socket.recv_string()
  ```
  
  
**C.** UML Sequence Diagram

<img width="641" alt="Screen Shot 2022-10-31 at 9 11 12 PM" src="https://user-images.githubusercontent.com/91582032/199150607-777f4800-693d-4a04-af33-2c4e16620ea1.png">

