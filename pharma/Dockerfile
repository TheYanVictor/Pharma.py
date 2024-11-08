# Use the official MySQL image as a base
FROM mysql:latest
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# # Install dependencies
# RUN pip install -r requirements.txt

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Set the default user for the MySQL image
USER mysql

# Set environment variables for the new user
ENV MYSQL_USER=mysql_user
ENV MYSQL_PASSWORD=mysql_user_password
ENV MYSQL_DATABASE=pharmacy

# Run the following commands to create the new user and grant them the necessary permissions
COPY init.sql /docker-entrypoint-initdb.d/


# Expose port 3306 to allow connections to the database
EXPOSE 3306

# Start the MySQL server when the container is run
CMD ["mysqld"]


