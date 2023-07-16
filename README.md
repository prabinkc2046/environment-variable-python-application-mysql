# Project Name

This project demonstrates the usage of environment variables in a Python application with a MySQL database.

## Overview

The project involves the following steps:

1. Creation of a virtual environment named "venv" in the "environment" folder on Ubuntu for Python.
2. Installation of the `mysql-connector-python` package within the virtual environment using pip.
3. Development of two Python scripts: `app_hardcoded.py` and `app.py`.
4. In `app_hardcoded.py`, MySQL server configurations were hardcoded to establish a connection to the MySQL server.
5. In `app.py`, the script was updated to retrieve the MySQL server configurations from environment variables.
6. Successful execution of both scripts within the virtual environment, enabling successful connection to the MySQL server.
7. Creation of a Dockerfile to containerize the application.
8. Building of a Docker image named "env" based on the Dockerfile, followed by running a container from it.
9. The container, utilizing the "env" image, connected to the MySQL server and performed the required database operations.

