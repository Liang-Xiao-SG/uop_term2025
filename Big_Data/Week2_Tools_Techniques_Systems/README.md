# Week 2: Unit 2 - Big Data Tools, Techniques, and Systems

Welcome to Unit 2! This week, we explore the powerful tools, techniques, and systems that make Big Data processing and analysis possible.

## The Hadoop Ecosystem

Apache Hadoop is an open-source framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models. Key components include:

1.  **Hadoop Distributed File System (HDFS):**
    *   A distributed file system designed to run on commodity hardware.
    *   Provides high-throughput access to application data and is suitable for applications that have large data sets.
    *   **Characteristics:** Fault-tolerant, scalable, designed for large files. Data is broken down into blocks and distributed across nodes in a cluster.

2.  **MapReduce:**
    *   A programming model and software framework for processing vast amounts of data in parallel on large clusters.
    *   **Map Phase:** The master node takes the input, divides it into smaller sub-problems, and distributes them to worker nodes. Worker nodes process the smaller problem and pass the answer back to its master node.
    *   **Reduce Phase:** The master node then collects the answers to all the sub-problems and combines them in some way to get the output.

## Apache Spark

Apache Spark is a fast and general-purpose cluster computing system. It provides high-level APIs in Java, Scala, Python, and R, and an optimized engine that supports general execution graphs.

*   **Speed:** Spark can be significantly faster than Hadoop MapReduce for many applications, primarily due to its in-memory processing capabilities.
*   **Ease of Use:** Offers rich APIs and a unified platform for various data processing tasks (SQL, streaming, machine learning, graph processing).
*   **Key Components:**
    *   **Spark Core:** Contains the basic functionality of Spark, including task scheduling, memory management, fault recovery, and interacting with storage systems.
    *   **Spark SQL:** For working with structured data.
    *   **Spark Streaming:** For processing real-time data streams.
    *   **MLlib:** Spark's machine learning library.
    *   **GraphX:** For graph processing.

## NoSQL Databases

NoSQL (Not Only SQL) databases are non-relational databases designed for specific data models and flexible schemas. They are often used in Big Data applications due to their scalability and ability to handle varied data types.

1.  **Key-Value Stores:**
    *   Data is stored in simple key-value pairs.
    *   *Examples:* Redis, Amazon DynamoDB.
    *   *Use Cases:* Caching, session management.

2.  **Document Databases:**
    *   Data is stored in documents (e.g., JSON, BSON, XML). Each document can have a different structure.
    *   *Examples:* MongoDB, Couchbase.
    *   *Use Cases:* Content management, mobile applications.

3.  **Column-Family Stores:**
    *   Data is stored in columns rather than rows. Optimized for queries over large datasets.
    *   *Examples:* Apache Cassandra, HBase.
    *   *Use Cases:* Time-series data, applications requiring high write throughput.

4.  **Graph Databases:**
    *   Designed to store and navigate relationships between entities.
    *   *Examples:* Neo4j, Amazon Neptune.
    *   *Use Cases:* Social networks, recommendation engines, fraud detection.

## Comparing Platforms and Tools

| Feature         | Hadoop MapReduce                     | Apache Spark                          | NoSQL Databases                     |
|-----------------|--------------------------------------|---------------------------------------|-------------------------------------|
| **Processing**  | Batch processing                     | Batch, Interactive, Streaming         | Transactional, Operational          |
| **Speed**       | Slower (disk-based)                  | Faster (in-memory option)             | Varies by type, generally fast for specific operations |
| **Data Model**  | Any (processes data in HDFS)         | RDDs, DataFrames, Datasets            | Key-Value, Document, Column, Graph  |
| **Use Cases**   | Large-scale batch ETL, log analysis  | Complex analytics, ML, streaming      | Web apps, real-time data, flexible schema needs |
| **Fault Tol.**  | High                                 | High                                  | Varies, often high via replication  |

## Python Example: Basic Word Count (Conceptual MapReduce)

While full-fledged MapReduce is typically run on a Hadoop cluster, we can simulate the logic in Python to understand the concept.

```python
# Sample text data
corpus = [
    "hello world",
    "hello big data world",
    "big data is interesting"
]

# --- Map Phase ---
# Goal: Emit (word, 1) for each word in the corpus
mapped_data = []
for sentence in corpus:
    words = sentence.split()
    for word in words:
        mapped_data.append((word, 1))

print("--- Mapped Data ---")
for item in mapped_data:
    print(item)
# Expected output (order might vary):
# ('hello', 1)
# ('world', 1)
# ('hello', 1)
# ('big', 1)
# ('data', 1)
# ('world', 1)
# ('big', 1)
# ('data', 1)
# ('is', 1)
# ('interesting', 1)

# --- Shuffle and Sort Phase (Implicitly handled by MapReduce frameworks) ---
# Goal: Group values by key
shuffled_data = {}
for word, count in mapped_data:
    if word not in shuffled_data:
        shuffled_data[word] = []
    shuffled_data[word].append(count)

print("\n--- Shuffled Data (Grouped by Key) ---")
for word, counts in shuffled_data.items():
    print(f"('{word}', {counts})")
# Expected output (order might vary):
# ('hello', [1, 1])
# ('world', [1, 1])
# ('big', [1, 1])
# ('data', [1, 1])
# ('is', [1])
# ('interesting', [1])


# --- Reduce Phase ---
# Goal: Sum counts for each word
reduced_data = {}
for word, counts in shuffled_data.items():
    reduced_data[word] = sum(counts)

print("\n--- Reduced Data (Word Counts) ---")
for word, total_count in reduced_data.items():
    print(f"('{word}', {total_count})")
# Expected output (order might vary):
# ('hello', 2)
# ('world', 2)
# ('big', 2)
# ('data', 2)
# ('is', 1)
# ('interesting', 1)

def run_word_count_example():
    # Sample text data
    corpus = [
        "hello world",
        "hello big data world",
        "big data is interesting"
    ]

    # --- Map Phase ---
    mapped_data = []
    for sentence in corpus:
        words = sentence.split()
        for word in words:
            mapped_data.append((word, 1))

    print("--- Mapped Data ---")
    for item in mapped_data:
        print(item)

    # --- Shuffle and Sort Phase ---
    shuffled_data = {}
    for word, count in mapped_data:
        if word not in shuffled_data:
            shuffled_data[word] = []
        shuffled_data[word].append(count)

    print("\n--- Shuffled Data (Grouped by Key) ---")
    for word, counts in shuffled_data.items():
        print(f"('{word}', {counts})")

    # --- Reduce Phase ---
    reduced_data = {}
    for word, counts in shuffled_data.items():
        reduced_data[word] = sum(counts)

    print("\n--- Reduced Data (Word Counts) ---")
    for word, total_count in reduced_data.items():
        print(f"('{word}', {total_count})")

# To run the example:
# run_word_count_example()
```

This Python code simulates the core logic of MapReduce for a word count task. In a real Big Data system, these operations would be distributed across many machines to handle massive datasets.

Next week, we'll delve into analytical theories and methods for extracting insights from Big Data.
