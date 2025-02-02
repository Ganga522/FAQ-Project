# Use the official Python image as the base image
FROM python:3.13

# Set the working directory inside the container
WORKDIR /app

# Copy the entire project into the container
COPY . /app

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Use Gunicorn to serve the app (replace faq_project with your project name)
CMD ["gunicorn", "faq_project.wsgi:application", "--bind", "0.0.0.0:8000"]
