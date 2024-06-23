
Set up
----
- To create a virtual environment: `pip install virtualenv` and then `virtualenv env` (**`env`** is just a name, it can be something else)

(Virtualenv: a tool to create isolated Python environments)

- Activiate the environment
	- for windows: `env\Scripts\activate`
	- for mac: `source env/bin/activate`

(After this step is done, in terminal there will be **`(env)`** surfix in front of the command line pointer, like **`(base)`** in anaconda)

- Install the required packages for this project:
	- pip install flask
	- pip install flask_sqlalchemy

	**or:**
	- pip install flask flask_sqlalchemy

Note
---
- in app.py, there is a db defined, to actually create this table, go to terminal and open python Interactive Mode with `python`:
```
from app import db
db.create_all()
exit()
```


After this step, there should be db created directly in the file structure with the name defined in **'sqlite:///mydb.db'**. In this case, the database name is *mydb*, then a file named *mydb.db* appears 
