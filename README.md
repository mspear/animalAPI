## Animal API
Created used Django REST framework for ease of use

All requests can be made as normal with any appropriate headers

Token auth was not taken into account due to project instructions.

API is as follows

## API
``
/animals/ (GET, POST) 
``

Can either create a new animal or return a list of the ID's, image URLS, and common names

``
/animals/{id} (GET, DELETE)
``

Gets all available information for the specified animal or deletes it