# Load Testing with Locust

![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)
![Locust](https://img.shields.io/badge/locust-2.31.0%2B-orange.svg)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Tests](#running-the-tests)

## Overview

This project is designed to perform load testing on APIs using [Locust](https://locust.io/), a scalable load testing tool. It features a modular structure with separate components for API interactions and helper functions, ensuring maintainability and scalability. The project includes comprehensive validation for various HTTP methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) and generates dynamic data for realistic testing scenarios.

## Features

- **Modular Architecture**: Separation of concerns with distinct modules for API interactions and helper utilities.
- **Comprehensive HTTP Method Support**: Handles `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` requests with proper response validations.
- **Dynamic Data Generation**: Utilizes the `Faker` library to generate realistic payloads for testing.
- **Random ID Selection**: Randomly selects resource IDs within a specified range to simulate diverse API interactions.
- **Configuration Management**: Centralized configuration through `locust.conf` for easy adjustments.

### Description of Directories and Files

- **`tests/jsonPlaceholder.py`**: Main Locust script integrating API and helper classes.
- **`utils/api.py`**: Contains the `Api` class with methods for interacting with the API endpoints (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`).
- **`utils/helpers.py`**: Contains the `Helpers` class with methods for generating random IDs and dynamic payloads using the `Faker` library.
- **`locust.conf`**: Configuration file for Locust, specifying settings like the number of users, spawn rate, and host URL.
- **`requirements.txt`**: Lists all Python dependencies required for the project.

## Prerequisites

- **Python 3.11+**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourUsername/yourProject.git
   cd yourProject
   ```

2. **Set Up a Virtual Environment (Recommended)**

   It's best practice to use a virtual environment to manage dependencies.

   ```bash
    python3 -m venv venv
   ```

3. **Activate the Virtual Environment**

- **On Unix/Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```
- **On Windows:**
  ```cmd
  venv\Scripts\activate
  ```

4. **Install Dependencies**

```bash
pip install -r requirements.txt
```

## Configuration

The project uses a `locust.conf` file to manage Locust settings. Here's a breakdown of the configuration options:

```ini
# Save the test report in HTML format with the specified filename
html = jsonPlaceholder.html

# Path to the Locust test file that contains the test scenarios
locustfile = tests/jsonPlaceholder.py

# Run Locust in headless mode (without the web UI)
headless = true

# URL of the host that will be tested
host = https://jsonplaceholder.typicode.com

# Number of virtual users to simulate
users = 5

# Rate at which users are spawned (users per second)
spawn-rate = 1

# Total duration of the test (1 minute in this case)
run-time = 1m

# Automatically start the test without manual intervention
autostart = true

# Time in seconds to automatically quit after the test finishes
autoquit = 10
```

## Running the Tests

Follow these steps to execute the load tests:

1. **Ensure You're in the Project Root Directory**

```bash
cd /path/to/yourProject
```

2. **Activate the Virtual Environment**

- **On Unix/Linux/Mac:**

```bash
source venv/bin/activate
```

- **On Windows:**

```cmd
venv\Scripts\activate
```

3. **Run Locust with Configuration**

```bash
locust
```

4. **Access the Locust Web Interface**

Open your web browser and navigate to http://localhost:8089. Here, you can override configuration settings if needed and start the load test.
