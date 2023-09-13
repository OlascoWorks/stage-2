## API DOCUMEMTATION 📝

### Detailed guide on how to use API

This is a backend project built on the python framework - [Flask](https://palletsprojects.com/p/flask/) and hosted on [render](https://render.com). It is connected to PostgreSql database that is als hosted remotely on render to allow for manipulation of a Person table by performing CRUD operations on it


> ### Creating a Person
  - **Method** -  POST
  - **Endpoint** -  https://hng-stage2-sam.onrender.com/api
  - **Body** -
    ```
    {
      "name": <string>
    }
    ```
  - **Response** -  If a person with the provided name does not exist and name is valid(a string), a success message like this is received
    ```
    {
      "message": "Successfully created new person",
      "id": 17,
      "name": "Johnson"
    }
    ```


> ### Reading a Person
  - **Method** -  GET
  - **Endpoint** -  https://hng-stage2-sam.onrender.com/api
  - **Body** -
    ```
    {
      "name": <string>
    }
    ```
  - **Response** -  If a person with the provided name exists and name is valid(a string), a success response containing person name and id like this is received
    ```
    {
      "id": 17,
      "name": "Johnson"
    }
    ```


> ### Updating a Person
  - **Method** -  PUT
  - **Endpoint** -  https://hng-stage2-sam.onrender.com/api
  - **Body** -
    ```
    {
      "id": <int>,
      "new_name": <string>
    }
    ```
  - **Response** -  If a person with the provided id exists, the new name is not the same as old name and id is valid(an integer), a success response containing person old name, new name and id like this is received
    ```
    {
      "message": "Successfully updated person",
      "id": "17",
      "new_name": "Johanson",
      "old_name": "Johnson"
    }
    ```


> ### Deleting a Person
  - **Method** -  DELETE
  - **Endpoint** -  https://hng-stage2-sam.onrender.com/api
  - **Body** -
    ```
    {
      "id": <int>
    }
    ```
  - **Response** -  If a person with the provided id exists and id is valid(an integer), a success response like this is received
    ```
    {
      "message": "successfully deleted person with id '17'"
    }
    ```


> ## Request/Response Formats

- **Request Format**: All requests should be in JSON format. The content type of the request should be set to `application/json`.

- **Response Format**: Responses are returned in JSON format and include relevant information or error messages in a case of failure. Most successful responses include a `"message"` field for context.


> ## NOTE‼️

- The API assumes that `"name"` is a unique identifier for persons.
- Validation is performed to ensure that `"name"` is a string value and `"id"` is an integer.


Please refer to the [README](https://github.com/OlascoWorks/stage-2/blob/main/README.md) for instructions on how to set this up on your local machine 
