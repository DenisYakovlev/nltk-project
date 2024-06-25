# Simple nltk project

REST api with implementation of basic nltk functionality 

## Technologies used

Python, NLTK, Docker;

## Installation and local setup
Before you begin, ensure than you have the following installed:  

* **Git**
* **Python** version >= 3.10.12
* **Pip**

### Setting Up the Application  
Clone the Repository  

```
git clone https://github.com/DenisYakovlev/nltk-project.git
```

### Enviroment variables
Create a .env file in root directory of project. You can check **.env.sample** file for example.

You need to insert values:
* DEBUG - debug mode of application, you can use 1 or 0
* PORT - port of application, default is 8000
* NLTK_DATA_PATH - the path for installation of nltk datasets

### Virtual Environment
To create venv, download dependencies and run your environment you need to run this from root directory of project:

**For Unix/MacOS**
```
python3 -m venv venv
pip install -r requirements.txt
source venv/bin/activate
```

**For Windows**
```
python -m venv venv
pip install -r requirements.txt
.\venv\Scripts\activate
```

### Launching
You can run app running this commands while using your venv:

**For Unix/MacOS**
```
cd ./src
python3 main.py
```

**For Windows**
```
cd ./src
python main.py
```

### Launching with Docker
Ensure, that you have **Docker** installed on your machine

You can build app image and run it with this commands:

```
docker build -t nltk_app .
docker run -p 8000:8000 nltk_app:latest
```
