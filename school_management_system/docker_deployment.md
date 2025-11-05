# Docker Deployment for School Management System

This guide provides instructions for deploying the School Management System using Docker.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your system
- [Docker Compose](https://docs.docker.com/compose/install/) installed on your system

## Deployment Options

### Option 1: Using Docker Compose (Recommended)

Docker Compose allows you to run both the application and a PostgreSQL database with a single command.

1. Navigate to the school_management_system directory:
   ```bash
   cd school_management_system
   ```

2. Start the application and database:
   ```bash
   docker-compose up -d
   ```

3. Access the application:
   - Web Interface: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

4. To stop the application:
   ```bash
   docker-compose down
   ```

### Option 2: Using Docker Only

If you want to run just the application container and connect to an existing database:

1. Build the Docker image:
   ```bash
   cd school_management_system
   docker build -t school-management-system .
   ```

2. Run the container:
   ```bash
   docker run -d -p 8000:8000 \
     -e SECRET_KEY=your-secret-key-here \
     -e USE_SQLITE_MEMORY=false \
     -e DATABASE_URL=postgresql://postgres:postgres@your-db-host:5432/college_management \
     -e FIRST_SUPERUSER=admin@example.com \
     -e FIRST_SUPERUSER_PASSWORD=admin \
     --name school-management-system \
     school-management-system
   ```

   Replace `your-db-host` with the actual hostname or IP address of your PostgreSQL database.

3. Access the application:
   - Web Interface: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

4. To stop the container:
   ```bash
   docker stop school-management-system
   docker rm school-management-system
   ```

## Environment Variables

You can customize the application behavior using the following environment variables:

- `SECRET_KEY`: Secret key for JWT token generation and security
- `USE_SQLITE_MEMORY`: Set to "true" to use SQLite in-memory database, "false" to use PostgreSQL
- `DATABASE_URL`: PostgreSQL connection string (when USE_SQLITE_MEMORY is false)
- `FIRST_SUPERUSER`: Email for the initial admin user
- `FIRST_SUPERUSER_PASSWORD`: Password for the initial admin user

## Initial Login

After deployment, you can log in with the following credentials:

- Email: admin@example.com (or the value of FIRST_SUPERUSER)
- Password: admin (or the value of FIRST_SUPERUSER_PASSWORD)

## Troubleshooting

### Database Connection Issues

If the application cannot connect to the database:

1. Check if the PostgreSQL container is running:
   ```bash
   docker ps
   ```

2. Check the logs for any errors:
   ```bash
   docker-compose logs web
   docker-compose logs db
   ```

### Container Not Starting

If the container fails to start:

1. Check the container logs:
   ```bash
   docker logs school-management-system
   ```

2. Verify that all required environment variables are set correctly.

## Security Considerations

For production deployment:

1. Change the default admin password immediately after first login
2. Generate a secure random string for SECRET_KEY
3. Use a strong password for the PostgreSQL database
4. Consider using Docker secrets or environment files instead of passing sensitive information via command line
