# stage-2
This is a simple API that performs basic CRUD (Create, Read, Update, Delete) operations on a "person" resource.


### Table Of Contents
- Getting Started
  - Prerequisites
  - Setup
  - Installation
- Running
- Documentation


## Getting Started
# Prerequisites
To utilize this API, you need to have the following installed on your machine:
- Python 3.x
- [Postman](https://www.postman.com/downloads/) (for testing purposes) [Optional]

# Setup
1. Create a new folder to house your API
2. Set your environment variables ny running the following in the command line:
   Windows and Mac
   ```
   set DATABASE_URI=<A valid Postgresql URL>
   set SECRET_KEY=<A secret key in string format>
   ```
   Linux:
   ```
   export DATABASE_URI=<A valid Postgresql URL>
   export SECRET_KEY=<A secret key in string format>
   ```
3. Clone the this repository:
   ```
   git clone https://github.com/OlascoWorks/stage-2.git
   ```

# Installation
1. To install all the required dependencies, run:
   ```
   pip install -r requirements.txt
   ```

# Running
To run this, run the following command in your terminal
```
python app.py
```
If successful, you should see a message in your terminal `serving flask app "app.py"`

# Documentation
Please refer to the [Documentation]() of this API to read details
