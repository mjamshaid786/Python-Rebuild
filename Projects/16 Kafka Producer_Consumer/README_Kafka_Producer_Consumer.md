# Kafka Producer / Consumer — Python

A practical Python project demonstrating the fundamentals of **Apache Kafka** by building a simple producer-consumer workflow.

The project publishes structured JSON messages from a Python producer to a Kafka topic and continuously consumes those messages with a Python consumer.

---

## 📌 Project Overview

This project demonstrates the basic event-streaming flow:

```text
Python Producer
      │
      │  JSON Message
      ▼
 Kafka Broker
      │
      ▼
  sales Topic
      │
      ▼
 Consumer Group
      │
      ▼
Python Consumer
      │
      ▼
 Decode & Process Message
```

The goal is to understand how applications can communicate through Kafka using producers, topics, messages, and consumers.

---

## 🎯 Learning Objectives

By completing this project, I practiced:

- Connecting Python applications to Kafka
- Creating and using a Kafka producer
- Creating and configuring a Kafka consumer
- Publishing messages to a Kafka topic
- Subscribing a consumer to a topic
- Using consumer groups
- Polling Kafka for incoming messages
- Serializing Python data to JSON
- Converting JSON data to UTF-8 bytes for transmission
- Decoding Kafka message bytes back into JSON
- Handling continuous message consumption
- Gracefully shutting down the consumer with `Ctrl+C`

---

## 🛠️ Tech Stack

- **Python 3**
- **Apache Kafka**
- **Confluent Kafka Python client**
- **JSON**
- **Docker / Docker Compose** for the local Kafka environment

Python package:

```bash
pip install confluent-kafka
```

---

## 📂 Project Structure

```text
Project/
│
├── producer.py
├── consumer.py
├── docker-compose.yml
└── README.md
```

### `producer.py`

Responsible for:

- Connecting to the Kafka broker
- Sending messages to the `sales` topic
- Creating JSON payloads
- Converting JSON to UTF-8 bytes
- Flushing the producer after publishing

### `consumer.py`

Responsible for:

- Connecting to the Kafka broker
- Joining the `my-simple-group` consumer group
- Subscribing to the `sales` topic
- Polling for new messages
- Decoding JSON messages
- Displaying received messages
- Gracefully closing the consumer

---

## ⚙️ Kafka Configuration

The Python applications connect to:

```text
Broker:
localhost:9092
```

The project uses the following topic:

```text
sales
```

The consumer group is:

```text
my-simple-group
```

The consumer is configured with:

```text
auto.offset.reset = earliest
```

This allows the consumer to start from the earliest available messages when no previous offset exists.

---

## 📤 Producer Flow

The producer accepts user input from the terminal.

Example:

```text
Producer Ready! Message type karein aur Enter dabayein ('exit' to stop):

> Hello Kafka
```

The input is converted into a structured payload:

```json
{
  "sender": "Muhammad Jamshaid",
  "message": "Hello Kafka"
}
```

The payload is then:

```text
Python Dictionary
      ↓
JSON String
      ↓
UTF-8 Bytes
      ↓
Kafka Topic
```

Messages are published to:

```text
sales
```

Typing:

```text
exit
```

stops the producer.

---

## 📥 Consumer Flow

The consumer subscribes to:

```text
sales
```

and continuously polls Kafka for new messages.

The received data is processed as:

```text
Kafka Bytes
    ↓
UTF-8 Decode
    ↓
JSON Decode
    ↓
Python Dictionary
    ↓
Readable Output
```

Example output:

```text
Consumer Listening... (Press Ctrl+C to stop)

Received -> Sender: Muhammad Jamshaid | Message: Hello Kafka
```

Press:

```text
Ctrl + C
```

to stop the consumer gracefully.

---

## ▶️ Running the Project

### 1. Start Kafka

Start the Kafka environment using the included Docker Compose configuration.

### 2. Start the Consumer

Open one terminal and run:

```bash
python consumer.py
```

The consumer will wait for messages.

### 3. Start the Producer

Open a second terminal and run:

```bash
python producer.py
```

Enter messages:

```text
> Hello Kafka
> My first streaming project
> Learning event-driven architecture
```

The consumer should receive them almost immediately.

---

## 🧪 Example

### Producer

```text
Producer Ready! Message type karein aur Enter dabayein ('exit' to stop):

> Hello Kafka
```

### Consumer

```text
Consumer Listening... (Press Ctrl+C to stop)

Received -> Sender: Muhammad Jamshaid | Message: Hello Kafka
```

---

## 🧠 Kafka Concepts Practiced

### Producer

The application that publishes events/messages.

### Consumer

The application that reads and processes messages.

### Broker

The Kafka server responsible for receiving and delivering records.

### Topic

A named stream/channel where records are published.

This project uses:

```text
sales
```

### Message / Record

An individual piece of data published to Kafka.

Example:

```json
{
  "sender": "Muhammad Jamshaid",
  "message": "Hello Kafka"
}
```

### Consumer Group

A logical group of consumers working together.

This project uses:

```text
my-simple-group
```

### Offset

A position associated with records in Kafka partitions. The project uses `auto.offset.reset=earliest` to control where a consumer starts when no prior offset is available.

---

## 🛡️ Error & Shutdown Handling

The consumer includes graceful shutdown handling for:

```text
Ctrl + C
```

and closes the Kafka consumer cleanly.

The project also checks Kafka message errors before processing a received record.

---

## 📈 Project Workflow

```text
User Input
    ↓
Python Producer
    ↓
JSON Serialization
    ↓
Kafka Broker
    ↓
sales Topic
    ↓
Consumer Group
    ↓
Python Consumer
    ↓
JSON Deserialization
    ↓
Message Processing
```

---

## 💡 Key Learning Outcome

The most important concept I learned from this project is the difference between traditional file-based data movement and event streaming.

Instead of:

```text
Application
    ↓
File
    ↓
Another Application
```

Kafka allows the flow to become:

```text
Producer
    ↓
Kafka
    ↓
Consumer
```

This provides the foundation for understanding event-driven and real-time data pipelines.

---

## 🚀 Next Step

This project provides the foundation for the next stage of the learning path:

```text
Kafka Producer
      ↓
Kafka
      ↓
Kafka Consumer
      ↓
PostgreSQL
```

The next project will extend the current Kafka workflow by persisting consumed events into a PostgreSQL database.

---

## 👨‍💻 Author

**Muhammad Jamshaid**

GitHub:  
https://github.com/mjamshaid786

---

## ⭐ Project Status

**Completed ✅**

Core Kafka producer-consumer workflow implemented successfully.
