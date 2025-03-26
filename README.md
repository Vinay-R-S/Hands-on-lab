# **Hands-on Lab: PyUnit, PyLint, Git, GitHub, Docker, Docker Hub, and GitHub Actions**


# **📌PyUnit**
## 1️⃣ **Writing and Running Unit Tests with PyUnit**

### **Step 1** - Install Required Packages
Python's built-in `unittest` module will be used.
~~~
pip install pytest
~~~
<span style="color:cyan">Optional, if you prefer pytest for running unittests</span>

### **Step 2** - Create a Sample Python Script `(app.py)`
~~~
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
~~~

### **Step 3** - Write Unit Tests `(test_app.py)`
~~~
import unittest
from app import add, subtract

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

if __name__ == "__main__":
    unittest.main()
~~~

### **Step 4** - Run Unit Tests
~~~
python -m unittest discover
~~~
Or, using `pytest`
~~~
pytest test_app.py
~~~


# **📌PyLint**
## 2️⃣ **Analyzing and Improving Code Quality with PyLint**

### **Step 1** - Install PyLint
~~~
pip install pylint
~~~

### **Step 2** - Run PyLint on `app.py`
~~~
pylint app.py
~~~

### **Step 3** - Fix Issues Based on PyLint Suggestions
Modify `app.py` based on PyLint feedback to improve code quality.


# **📌Git & GitHub**
## 3️⃣ **Managing Code Versions and Collaborating with Git & GitHub**

### **Step 1** - Initialize a Git Repository
~~~
git init
~~~

### **Step 2** - Add and Commit Files
~~~
git add .
git commit -m "Initial commit"
~~~

### **Step 3** - Create a GitHub Repository and Push Code
~~~
git remote add origin https://github.com/your-username/your-repo.git
git branch -M main
git push -u origin main
~~~

# **📌Docker**
## 3️⃣ **Managing Code Versions and Collaborating with Git & GitHub**

### **Step 1** - Install Docker
Follow the [Docker installation guide](https://docs.docker.com/desktop/setup/install/windows-install/)


### **Step 2** - Create a `Dockerfile`
~~~
# Use an official Python runtime as base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install pytest pylint

# Command to run the unit tests
CMD ["python", "-m", "unittest", "discover"]
~~~

### **Step 3** - Build and Run the Docker Container
~~~
docker build -t myapp .
docker run myapp
~~~

### **Step 4** - Push Image to Docker Hub
~~~
docker tag myapp your-dockerhub-username/myapp
docker login
docker push your-dockerhub-username/myapp
~~~

# **📌CI/CD**
## 3️⃣ **Automating Workflows with GitHub Actions for CI/CD**

### **Step 1** - Create a GitHub Actions Workflow
Create a `.github/workflows/ci.yml` file in your repository.
~~~
name: CI Pipeline

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.9
      
      - name: Install dependencies
        run: |
          pip install pytest pylint
      
      - name: Run PyLint
        run: pylint app.py || true  # Avoid failure due to linting errors
      
      - name: Run Unit Tests
        run: pytest test_app.py

  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Log in to Docker Hub
        run: echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin
      
      - name: Build Docker Image
        run: docker build -t your-dockerhub-username/myapp .
      
      - name: Push Docker Image
        run: docker push your-dockerhub-username/myapp
~~~

### **Step 2** - Configure GitHub Secrets for Docker Hub
1. Go to your GitHub repository.
2. Navigate to `Settings > Secrets > Actions`.
3. Add `DOCKER_USERNAME` and `DOCKER_PASSWORD` secrets.
~~~
docker build -t myapp .
docker run myapp
~~~

### **Step 4** - Push Changes to Trigger GitHub Actions
~~~
git add .
git commit -m "Added GitHub Actions CI/CD"
git push origin main
~~~