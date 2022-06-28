**Face_unlock** is an AI-based face verification engine that includes verifying face using **face_recognition** package and storing the secret details in the database by encrypting using the **cryptography** library.

Unlocks the app using face verification and stores the username and password in the database

![Generic badge](https://img.shields.io/badge/AI-Advance-green.svg) ![Generic badge](https://img.shields.io/badge/Python-3.6|3.7-blue.svg) ![Generic badge](https://img.shields.io/badge/pip-v3-red.svg) ![Generic badge](https://img.shields.io/badge/mongodb-python-latest.svg) ![Generic badge](https://img.shields.io/badge/fastapi-latest-green.svg) ![Generic badge](https://img.shields.io/badge/streamlite-latest-green.svg) ![Generic badge](https://img.shields.io/badge/opencv-python-latest.svg)![Generic badge](https://img.shields.io/badge/cryptography-python-latest.svg)


<h2><img src="https://cdn2.iconfinder.com/data/icons/artificial-intelligence-6/64/ArtificialIntelligence9-512.png" alt="Brain+Machine" height="38" width="38"> Creators </h2>

### Mohan Kumar

### Sandeep Jena

### Md Saquib Quddus

# About the project

## Face_Recognition
Recognize and manipulate faces from Python or from the command line with the world's simplest face recognition library.

Built using dlib's state-of-the-art face recognition built with deep learning. The model has an accuracy of 99.38% on the Labeled Faces in the Wild benchmark.

This also provides a simple face_recognition command line tool that lets you do face recognition on a folder of images from the command line!

## Cryptography
``cryptography`` is a package which provides cryptographic recipes and
primitives to Python developers.  Our goal is for it to be your "cryptographic
standard library". It supports Python 3.6+ and PyPy3 7.2+.

``cryptography`` includes both high level recipes and low level interfaces to
common cryptographic algorithms such as symmetric ciphers, message digests, and
key derivation functions. For example, to encrypt something with


# Setup and Usage

Clone the repository using below command:
```bash
git clone https://github.com/kkkumar2/Face_unlock.git
```
create a conda or virtual env environment using below command:
```bash
conda create -n [env_name] python=3.7 or
virtualenv [env name] --python=python3.7
```

to activate the environment:
```bash
conda activate [env_name] or
source virtualenv/[env_name]/Scripts/activate
```

To install Locally and test the application

```bash
conda install -c conda-forge dlib  
pip install -r STREAMLIT/requirement.txt
pip install -r FASTAPI/requirement.txt
```
To run the ``STREAMLIT`` application open anaconda prompt
```bash
cd STREAMLIT 
streamlit run Streamlit.py
```

To run the ``FASTAPI`` application open anaconda prompt
```bash
cd FASTAPI 
python app.py
```

To test the Application using Docker

command to up the services
```bash
docker-compose up
```

command to down the services
```bash
docker-compose down
```

if making any changes and need to re build the image then you can
```bash
cd [folder name]
docker build -t [image name:tag name] .
```


