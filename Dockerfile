# Use official Python image
FROM python:3.12

# Set working directory inside the container
WORKDIR /app

# Copy all files from the repository into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run tests when the container starts
CMD ["pytest", "test_app.py"]
