# Unit 1: Assignment - Boolean Retrieval and Index Concepts

This assignment aims to solidify your understanding of the fundamental concepts covered in Unit 1: Introduction to Information Retrieval, the Boolean Retrieval model, and the basics of terms and postings lists.

## Part 1: Conceptual Questions (60 points)

Please answer the following questions clearly and concisely. Refer to the lecture notes and textbook readings.

1.  **Information Retrieval (15 points):**
    *   In your own words, define Information Retrieval.
    *   Describe two key challenges in IR and explain why they are challenging.
    *   What is the primary purpose of an inverted index in an IR system?

2.  **Boolean Retrieval (25 points):**
    *   Given the following document collection:
        *   Doc1: "The quick brown fox jumps over the lazy dog."
        *   Doc2: "A quick brown dog outruns the lazy fox."
        *   Doc3: "The fox is quick, the dog is lazy."
        *   Doc4: "No dogs or foxes here, just a quick cat."
    *   Construct a simple inverted index (term -> list of DocIDs) for this collection. Assume basic tokenization (split by space) and case-folding to lowercase. Do not perform stemming or stop-word removal for this question.
    *   Show the step-by-step process for how a Boolean retrieval system would find the documents matching the query: `(quick AND fox) AND NOT dog` using your inverted index. List the documents returned.

3.  **Terms and Postings (20 points):**
    *   Explain the difference between a term's document frequency (DF) and its term frequency (TF) within a specific document. Which one is typically stored in the dictionary part of an inverted index?
    *   Why are postings lists for terms usually sorted by document ID?

## Part 2: Practical Exercise - Simple Boolean Search (40 points)

Imagine you have the following postings lists for a larger collection:

*   `stars`: [3, 8, 12, 15, 22, 28, 35, 40, 45, 50]
*   `moon`: [1, 8, 15, 20, 28, 33, 40, 48, 50]
*   `sun`: [5, 12, 20, 28, 35, 42, 50]
*   `planets`: [3, 10, 15, 22, 30, 40, 47]

Manually trace the execution of the following Boolean queries. Show which postings lists are accessed and how they are processed (e.g., merged, intersected). List the document IDs in the final result set for each query.

1.  `stars AND moon`
2.  `sun OR planets`
3.  `(stars AND planets) AND NOT moon`
4.  `(sun OR moon) AND (stars OR planets)`

*(For this part, you don't need to write code, but describe the algorithm/logic you'd use to process the postings lists, similar to the intersection example in the lecture notes.)*

## Submission Guidelines:

*   Submit your answers in a single document (e.g., PDF or Markdown file).
*   For Part 1, ensure your answers are well-explained.
*   For Part 2, clearly show the intermediate steps of processing the postings lists.
*   **Due Date:** [Specify Due Date Here]

Good luck! This assignment will help you build a strong foundation for the more advanced topics we'll cover later in the course.
