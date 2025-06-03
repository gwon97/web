FROM python:3.10-slim

# Install sudo and other useful tools
RUN apt-get update && apt-get install -y sudo

# Create a user (optional)
RUN useradd -ms /bin/bash myuser && echo 'myuser ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Set up working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Switch to user (optional)
USER myuser

# Run the app
CMD ["python", "app.py"]
