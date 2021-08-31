## Intro

Python application written using FastAPI framework and WorldTimeAPI showing current Moscow time.

## Getting Started

Local installation
Before running the application, please install its prerequisites:
Python 3.6+, pip

To run from the master branch, follow the instructions below:

1. Clone web application repository locally.

```
git clone https://github.com/Danielatonge/devops
cd devops/app_python/
```

2. Create virtual environment.

```
python3 -m venv venv
source venv/bin/activate
```

3. Install packages.

```
pip install -r requirements.txt
```

4. Run the application. Web app will open at http://localhost:3000/.

```
uvicorn Current_Moscow_Time.main:app --reload
```

## Docker installation

Before running the application, please install its prerequisites:
Docker 20.10.7+

To run from the master branch, follow the instructions below:

1. Clone web application repository locally.

```
git clone https://github.com/Danielatonge/devops
cd devops/app_python/
```

2. [Optional] Build the image.

```
docker build -t danielatonge/current_moscow_time .
```

3. Run the container. Web app will open at http://localhost:3000/.

```
docker run -p 3000:3000 danielatonge/current_moscow_time
```

## Unit Tests

To run from the master branch, follow the instructions below:

1. Clone web application repository locally.

```
git clone https://github.com/Danielatonge/devops
cd devops/app_python/Current_Moscow_Time
```

2. Create virtual environment.

```
python3 -m venv venv
source venv/bin/activate
```

3. Install packages.

```
pip install -r requirements.txt
```

4. Run pytest. The console will take some time to run all the test and verify the results

```
pytest
```
