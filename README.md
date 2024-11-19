# cs361_microserviceA

How to programmatically **REQUEST** data from this microservice:
Using a text file as a pipeline, write the item code/ vending machine button number to the text file.

example call: 
with open('file.txt', 'w') as pipe:
  pipe.write(item_code)


How to programmatically **RECEIVE** data from this microservice:
Using a text file as a pipeline, read the data in the file, and check that it is a digit.  This will provide the animation code.

example call:

UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your teammate (and your grader) will understand.
