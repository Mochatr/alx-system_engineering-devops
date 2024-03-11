# 0X1A - Application server

## Project overview

This project enhances our existing web infrastructure by integrating an application server to work alongside Nginx, which is currently serving static web pages. The primary goal is to configure the application server to serve dynamic content for our Airbnb clone project, optimizing our web infrastructure for both static and dynamic content delivery.

## Concepts

For this project, we expect you to look at these concepts:

- Web Server
- Server
- Web stack debugging

## Background Context

Our web infrastructure already uses Nginx to serve web pages. The project aims to incorporate an application server to manage dynamic content effectively, demonstrating a comprehensive web stack configuration.

## Resources

[Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
[How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04) 
[Running Gunicorn](https://docs.gunicorn.org/en/latest/run.html)
[Be careful with the way Flask manages slash in route](https://werkzeug.palletsprojects.com/en/3.0.x/)
[Upstart documentation](https://doc.ubuntu-fr.org/upstart)

# Requirements

## General

- A README.md file at the root is mandatory.
- Utilize python3 for all Python-related tasks.
- All configuration files must include comments.

## Bash Scripts

- Compatible with Ubuntu 16.04 LTS.
- Every file ends with a new line.
- Files must be executable and pass Shellcheck (version 0.3.7-5~ubuntu16.04.1) without errors.
- Include a shebang line #!/usr/bin/env bash and a comment line explaining the script's purpose.

## Setup instructions

- Install Gunicorn: Install Gunicorn globally on your server. Do not use virtualenv.
- Configure Nginx: Update your Nginx configuration to proxy requests to Gunicorn serving the Flask application.
- Deploy Flask Application: Ensure your Flask application is ready for deployment and configured to work with Gunicorn.
- Bash Scripting: Create necessary Bash scripts for deployment and maintenance, following the guidelines provided.
- Testing: Thoroughly test your setup to ensure both static and dynamic content are served correctly.
