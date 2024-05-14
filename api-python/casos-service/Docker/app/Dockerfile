# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.7-slim

ENV APP_HOME /app

WORKDIR $APP_HOME

# Copy files into the container image.
COPY . .

# Install dependencies.
RUN pip install -r requirements.txt

# Run the web service on container startup.
# EXPOSE 8080

# RUN chmod +x /scripts/*
# RUN apk add --no-cache dos2unix
# RUN dos2unix /scripts/entrypoint.sh

# CMD ["sh", "/scripts/entrypoint.sh"]
