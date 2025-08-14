# Project Overview
____
A web application featuring a login form developed with Streamlit for the user interface. The backend is managed using FastAPI and an SQLite database.

### Set up and run
**All necessary libraries are in requirements.txt** <br/>
To quickly install: <br/>
``` pip install -r requirements.txt ```

### In order to run the app you should do <br/>
> 1. Open two terminals in your IDE <br />
> 2. Start the FastAPI with uvicorn <br />
``` uvicorn main:app --reload ``` <br />
> 3. Start **streamlit** FrontEnd <br />
 ```streamlit run ./utilities/ui.py```<br />
## Note </br>
Even though the Streamlit sessions can be rerun, the database remains static due to the use of SQL and SQLite, meaning registered user data persists between sessions. <br/>

### You can access the application at: <br/>

__FastAPI__: http://127.0.0.1:8000/api/people <br/>
__Streamlit__: http://localhost:8501 <br/> 
