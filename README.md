# Django Member Management Application

This is a Django web application designed to manage member information. It provides functionalities to add new members, view a list of all members, and see detailed information for each member.

## Features

*   **Member Listing**: View a comprehensive list of all registered members.
*   **Member Details**: Access detailed information for individual members.
*   **Add New Member**: Easily add new members to the system with their first name, last name, phone number, and email. The `joined_date` is automatically set to the current date upon creation.

## Technologies Used

*   **Django**: Web framework for building the application.
*   **PostgreSQL**: Relational database for storing member data.
*   **Docker / Docker Compose**: For containerization and easy deployment of the application and its database.

## Getting Started

### Prerequisites

*   Docker and Docker Compose (recommended for easy setup)
*   Python 3.x (if running locally without Docker)
*   PostgreSQL (if running locally without Docker)

### Running with Docker Compose (Recommended)

1.  **Build and run the containers**:
    ```bash
    docker-compose up --build
    ```
    This command will:
    *   Build the `web` service image based on the `Dockerfile`.
    *   Start the PostgreSQL database service (`db`).
    *   Wait for the database to be ready.
    *   Apply Django database migrations.
    *   Start the Django development server.

2.  **Access the application**:
    Once the services are up and running, open your web browser and navigate to `http://localhost:8000`.

### Running Locally (without Docker)

1.  **Install dependencies**:
    Ensure you have Python 3.x and `uv` installed. Then install the project dependencies:
    ```bash
    uv pip install -r pyproject.toml
    ```

2.  **Set up PostgreSQL**:
    Ensure you have a PostgreSQL server running and create a database named `djangoproject_db` with a user `djangouser` and password `djangopassword`. Alternatively, update the `DATABASES` settings in `my_site/my_site/settings.py` to match your PostgreSQL configuration.

3.  **Apply database migrations**:
    ```bash
    python my_site/manage.py migrate
    ```

4.  **Start the Django development server**:
    ```bash
    python my_site/manage.py runserver 0.0.0.0:8000
    ```

5.  **Access the application**:
    Open your web browser and navigate to `http://localhost:8000`.

## Project Structure

*   `my_site/`: The main Django project directory.
    *   `my_site/settings.py`: Project settings, including database configuration and installed apps.
    *   `my_site/urls.py`: Main URL routing for the project.
*   `my_site/members/`: The Django application for managing members.
    *   `models.py`: Defines the `Member` model.
    *   `views.py`: Contains the logic for handling member-related requests (listing, details, adding).
    *   `urls.py`: URL routing specific to the `members` application.
    *   `forms.py`: Defines the form used for adding members.
    *   `templates/members/`: HTML templates for member-related pages.
*   `docker-compose.yml`: Defines the Docker services (web application and PostgreSQL database).
*   `Dockerfile`: Instructions for building the Docker image for the web application.
*   `run_django.sh`: A script to wait for the database, apply migrations, and start the Django server (used by Docker Compose).
*   `pgdata/`: Directory for PostgreSQL data persistence (used by Docker Compose).
