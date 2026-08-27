# Distributed Healthcare Data Processing Platform

A Java/Spring Boot portfolio project for processing healthcare information through REST APIs, PostgreSQL persistence, validation, exception handling, and container-friendly configuration.

## Tech Stack

Java 17, Spring Boot, REST APIs, PostgreSQL, Maven, Docker-ready configuration, AWS-compatible deployment patterns

## Features

- REST endpoint to create healthcare processing records.
- PostgreSQL persistence through Spring JDBC.
- Input validation for required healthcare fields.
- Centralized HTTP-friendly error handling through Spring Boot defaults.
- Environment-driven database configuration for local or cloud deployment.
- Health-oriented service structure suitable for extension into distributed microservices.

## API

```text
POST /api/records
GET  /api/records
GET  /api/records/{id}
```

### Example Request

```json
{
  "patientReference": "P-10021",
  "recordType": "CLAIM",
  "sourceSystem": "payer-platform",
  "status": "RECEIVED"
}
```

## Run PostgreSQL

Create a database named `healthcare` and configure these environment variables if needed:

```bash
export DB_URL=jdbc:postgresql://localhost:5432/healthcare
export DB_USERNAME=postgres
export DB_PASSWORD=postgres
```

## Run the Application

```bash
mvn spring-boot:run
```

The included `schema.sql` initializes the table automatically when SQL initialization is enabled.

This repository is a portfolio implementation intended to demonstrate the architecture and technologies described in the project section of my resume.
