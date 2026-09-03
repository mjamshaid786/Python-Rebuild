# 🚀 End-to-End Data Engineering Capstone Pipeline

A production-inspired **end-to-end Data Engineering pipeline** built with Python that collects user data from a REST API, validates and transforms the records, streams them through Apache Kafka, and stores the processed data in PostgreSQL for analysis.

The project demonstrates practical Data Engineering concepts including **API ingestion, data validation, transformation, event streaming, Kafka consumers/producers, PostgreSQL storage, duplicate handling, error handling, logging, and SQL analytics**.

---

## 📌 Project Overview

This project simulates a real-world data pipeline in which data is continuously moved through multiple stages:

```text
REST API
   ↓
Data Ingestion
   ↓
Validation
   ↓
Transformation
   ↓
Kafka Producer
   ↓
Apache Kafka
   ↓
Kafka Consumer
   ↓
PostgreSQL
   ↓
SQL Analysis
```

The source data is collected from the **DummyJSON Users API** and transformed into a clean structure before being published to a Kafka topic named `users`.

A Kafka consumer receives the events and inserts them into a PostgreSQL database while handling malformed messages, database errors, and duplicate records.

---

## 🎯 Project Objectives

The main objectives of this project are to:

* Consume data from a REST API using Python
* Safely handle API failures and network errors
* Validate incoming user records
* Extract only the required fields
* Transform nested API data into a clean structure
* Serialize records into JSON
* Publish user events to Apache Kafka
* Consume Kafka messages using a consumer group
* Decode and process JSON messages
* Store processed records in PostgreSQL
* Handle duplicate records safely
* Maintain centralized application logging
* Perform SQL-based analysis on the stored data

---

## 🛠️ Tech Stack

| Technology          | Purpose                                    |
| ------------------- | ------------------------------------------ |
| **Python**          | Main programming language                  |
| **Requests**        | REST API communication                     |
| **Apache Kafka**    | Event streaming / message broker           |
| **Confluent Kafka** | Python Kafka client                        |
| **PostgreSQL**      | Persistent data storage                    |
| **psycopg2**        | PostgreSQL connectivity                    |
| **python-dotenv**   | Environment variable management            |
| **JSON**            | Data serialization                         |
| **Logging**         | Application monitoring and error reporting |
| **SQL**             | Data analysis                              |

---

## 📂 Project Structure

```text
capstone_pipeline/
│
├── api_client.py
├── validator.py
├── transformer.py
├── producer.py
├── consumer.py
├── database.py
├── logger_config.py
├── main.py
├── sql_analysis.py
├── .env
├── requirements.txt
└── README.md
```

> The exact filenames may vary slightly depending on the latest version of the project, but the modules follow the same separation of responsibilities.

---

## 🔄 Pipeline Workflow

### 1. API Data Ingestion

The pipeline starts by requesting user data from:

```text
https://dummyjson.com/users
```

Python's `requests` library is used to perform the API request.

The API layer handles common failures such as:

* Connection errors
* Timeout errors
* HTTP errors
* Request exceptions

A request timeout is also configured to prevent the application from waiting indefinitely.

---

### 2. Data Validation

Incoming records are validated before entering the streaming pipeline.

Important fields include:

```text
id
firstName
lastName
email
age
city
company
```

Invalid records are rejected instead of being blindly sent to Kafka.

This prevents bad data from propagating through the downstream pipeline.

---

### 3. Data Transformation

The raw API response contains nested structures such as:

```text
address.city
company.name
```

The pipeline extracts the required attributes and converts the records into a normalized structure.

Example:

```json
{
  "id": 1,
  "full_name": "Emily Johnson",
  "email": "emily.johnson@example.com",
  "age": 28,
  "city": "Phoenix",
  "company": "Example Company"
}
```

This creates a clean event format suitable for Kafka and PostgreSQL.

---

## 📡 Kafka Streaming

After validation and transformation, the processed records are published to the Kafka topic:

```text
users
```

### Producer Responsibilities

The producer:

1. Receives transformed user records
2. Creates a JSON payload
3. Serializes the payload
4. Encodes it as UTF-8 bytes
5. Publishes it to Kafka
6. Flushes pending messages

Example event:

```json
{
  "id": 1,
  "full_name": "Emily Johnson",
  "email": "emily.johnson@example.com",
  "age": 28,
  "city": "Phoenix",
  "company": "Example Company"
}
```

---

## 📥 Kafka Consumer

The consumer subscribes to the:

```text
users
```

topic using a Kafka consumer group.

The consumer:

1. Polls Kafka for messages
2. Detects Kafka message errors
3. Decodes UTF-8 payloads
4. Parses JSON
5. Processes the user record
6. Inserts the record into PostgreSQL
7. Commits the Kafka offset after successful database processing

Automatic Kafka offset commits are disabled so that offsets can be controlled explicitly.

---

## 🗄️ PostgreSQL Database

The project stores processed records in:

```text
Database: capstone_pipeline
Table: users
```

### Table Schema

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    full_name VARCHAR NOT NULL,
    email VARCHAR,
    age INT,
    city VARCHAR,
    company VARCHAR,
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Column Description

| Column        | Type      | Description                |
| ------------- | --------- | -------------------------- |
| `id`          | INT       | Unique user identifier     |
| `full_name`   | VARCHAR   | User's complete name       |
| `email`       | VARCHAR   | User email                 |
| `age`         | INT       | User age                   |
| `city`        | VARCHAR   | User city                  |
| `company`     | VARCHAR   | Company name               |
| `ingested_at` | TIMESTAMP | Record ingestion timestamp |

---

## ♻️ Duplicate Handling

The pipeline handles duplicate user IDs using PostgreSQL conflict handling:

```sql
ON CONFLICT (id) DO NOTHING
```

This prevents the same user from being inserted multiple times.

For example:

```text
User ID 101 → INSERTED ✅

User ID 101 → DUPLICATE → IGNORED ✅
```

This provides safer, more idempotent behavior when messages are replayed or processed more than once.

---

## 🔐 Environment Configuration

Sensitive database information is stored in environment variables instead of being hard-coded into the application.

Example `.env`:

```env
host=localhost
user=postgres
password=YOUR_PASSWORD
port=5432
dbname=capstone_pipeline
```

### Important

Do **not** commit `.env` to GitHub.

Add it to `.gitignore`:

```gitignore
.env
```

---

## 📝 Logging

The project uses Python's built-in `logging` module with centralized logger configuration.

Different log levels are used to represent different events:

```text
INFO
WARNING
ERROR
```

Example pipeline events include:

```text
INFO    → API request started
INFO    → Data received
INFO    → Transformation completed
INFO    → Kafka producer ready
INFO    → Data received by consumer
INFO    → Record saved to PostgreSQL

WARNING → Invalid record rejected

ERROR   → API unavailable
ERROR   → Kafka failure
ERROR   → Database insertion failure
ERROR   → Malformed JSON
```

Centralized logging makes debugging and monitoring easier.

---

## ⚠️ Error Handling

The pipeline is designed to handle failures at multiple stages.

### API Layer

Handles:

```text
ConnectionError
Timeout
HTTPError
RequestException
```

### Kafka Layer

Handles:

```text
Kafka message errors
Producer/consumer failures
```

### JSON Processing

Malformed JSON payloads are handled using:

```python
json.JSONDecodeError
```

The consumer can log the problem without terminating the entire processing loop.

### PostgreSQL

Database failures are handled with rollback logic to prevent incomplete transactions.

---

## 🧪 Testing Scenarios

The project can be tested against multiple real-world failure scenarios.

### API Failure

Stop network access or make the API unavailable.

**Expected result:**

```text
API error is logged
Pipeline handles the failure gracefully
```

### Invalid Record

Introduce an invalid user record.

**Expected result:**

```text
Record is rejected
Validation warning is logged
Invalid data does not continue to Kafka
```

### Duplicate Record

Publish the same user ID more than once.

**Expected result:**

```text
First record → inserted
Duplicate record → ignored
```

### Kafka Unavailable

Stop Kafka before running the producer.

**Expected result:**

```text
Kafka failure is detected and logged
```

### PostgreSQL Unavailable

Stop PostgreSQL while the consumer is running.

**Expected result:**

```text
Database error is logged
Transaction is rolled back
Message is not falsely treated as successfully processed
```

### Malformed JSON

Send an invalid JSON payload.

Example:

```text
this-is-not-json
```

**Expected result:**

```text
JSON decoding error is logged
Consumer continues running
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd capstone_pipeline
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure PostgreSQL

Make sure PostgreSQL is running.

Create or configure the required credentials in:

```text
.env
```

---

### 5. Start Kafka

Make sure your Kafka broker is running on:

```text
localhost:9092
```

The pipeline uses the Kafka topic:

```text
users
```

---

### 6. Initialize the database

Run the project's database initialization logic so that the following are available:

```text
Database: capstone_pipeline
Table: users
```

---

### 7. Start the consumer

Run the consumer first so it is ready to receive Kafka events.

```bash
python consumer.py
```

Expected output:

```text
Consumer Listening...
```

---

### 8. Start the producer / pipeline

In another terminal:

```bash
python main.py
```

or run the producer according to the project's current orchestration.

The pipeline will:

```text
API
 ↓
Validation
 ↓
Transformation
 ↓
Kafka
 ↓
Consumer
 ↓
PostgreSQL
```

---

## 📊 SQL Analysis

After data has been stored in PostgreSQL, SQL queries can be used to analyze the pipeline output.

Examples of analysis include:

### Total Users

```sql
SELECT COUNT(*)
FROM users;
```

### Average Age

```sql
SELECT AVG(age)
FROM users;
```

### Users by City

```sql
SELECT city, COUNT(*)
FROM users
GROUP BY city
ORDER BY COUNT(*) DESC;
```

### Users by Company

```sql
SELECT company, COUNT(*)
FROM users
GROUP BY company
ORDER BY COUNT(*) DESC;
```

### Latest Ingested Records

```sql
SELECT *
FROM users
ORDER BY ingested_at DESC;
```

These queries demonstrate the final **storage → analysis** stage of the pipeline.

---

## 🧠 Data Engineering Concepts Demonstrated

This project provides practical experience with:

* REST API ingestion
* Data validation
* Data transformation
* JSON processing
* Event-driven architecture
* Apache Kafka
* Kafka producers
* Kafka consumers
* Consumer groups
* Manual offset management
* Message processing
* PostgreSQL
* SQL
* Transactions
* Rollbacks
* Duplicate handling
* Idempotent processing
* Environment variables
* Logging
* Exception handling
* Modular Python architecture
* End-to-end data pipelines

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │    DummyJSON API    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    API Client       │
                    │   api_client.py     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Validator       │
                    │    validator.py     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Transformer      │
                    │    transformer.py   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Kafka Producer    │
                    │    producer.py     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Kafka Topic      │
                    │       users         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Kafka Consumer    │
                    │    consumer.py     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     PostgreSQL      │
                    │ capstone_pipeline   │
                    │       users         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    SQL Analysis     │
                    └─────────────────────┘
```

---

## 🚀 Future Improvements

Possible next steps for this project include:

* Dockerize Kafka and PostgreSQL
* Add Kafka delivery callbacks
* Add retry mechanisms
* Introduce dead-letter queues for invalid messages
* Add batch processing
* Add automated tests with `pytest`
* Add Airflow orchestration
* Add monitoring and metrics
* Deploy the pipeline to AWS
* Replace the REST API with a production data source
* Introduce Apache Spark/PySpark for large-scale processing

---

## 📚 Learning Outcome

This project represents the transition from individual Python scripts to a **complete distributed data pipeline**.

It combines the major concepts learned throughout the previous projects:

```text
Python
  +
APIs
  +
JSON
  +
Data Transformation
  +
Kafka
  +
PostgreSQL
  +
SQL
  +
Logging
  +
Error Handling
```

The result is an end-to-end pipeline capable of taking external data, processing it, streaming it through Kafka, and persisting it into a relational database for analysis.

---

## 👨‍💻 Author

**Muhammad Jamshaid**

Computer Science Student | Aspiring Data Engineer

Focused on:

```text
Python
Data Engineering
SQL
Kafka
PostgreSQL
ETL / ELT
Cloud Data Engineering
AI & Data
```

---

## ⭐ Project Status

**Status:** Completed / Capstone Project

**Pipeline:** API → Kafka → PostgreSQL

**Primary Goal:** Practical implementation of an end-to-end Data Engineering workflow.
