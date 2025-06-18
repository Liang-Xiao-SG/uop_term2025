# Lecture 1: Introduction to IR, Boolean Retrieval, Terms and Postings

## 1. What is Information Retrieval (IR)?

*   **Definition:** Information Retrieval is finding material (usually documents) of an unstructured nature (usually text) that satisfies an information need from within large collections (usually stored on computers).
*   **Goal:** To minimize the overhead of a user who is looking for needed information. The user's information need is translated into a query.
*   **Brief History:**
    *   Early ideas: Vannevar Bush's "Memex" (1945).
    *   Pioneering systems in the 1950s-60s (punched cards, batch processing).
    *   Growth of online systems in the 1970s-80s (Dialog, LexisNexis).
    *   The Web explosion in the 1990s changed everything.
*   **Key Challenges:**
    *   **Scale:** Managing and searching vast amounts of data.
    *   **Ambiguity:** Natural language is ambiguous (synonymy, polysemy).
    *   **Relevance:** Understanding user intent and what makes a document relevant.
    *   **User Experience:** Presenting results effectively.
*   **Components of an IR System (Simplified):**
    *   **Text Acquisition:** Selecting and organizing the document collection.
    *   **Indexing:** Creating data structures to enable fast searching (e.g., inverted index).
    *   **Query Processing:** Translating user queries and matching them against the index.
    *   **Ranking:** Scoring documents based on relevance to the query.
    *   **Evaluation:** Measuring the effectiveness and efficiency of the system.
*   **Overview of Retrieval Models:**
    *   **Boolean Model:** Processes queries as Boolean expressions (AND, OR, NOT). Exact match.
    *   **Vector Space Model:** Represents documents and queries as vectors in a high-dimensional space. Ranks documents by similarity. (We'll cover this in Unit 4).
    *   **Probabilistic Models:** Ranks documents by the probability that they are relevant to the query.
    *   **Language Models:** Models the probability of generating a query from a document model.

## 2. Boolean Retrieval

*   **Dealing with Unstructured Data:** Unlike structured databases (with clear schemas), text documents are often unstructured. Boolean retrieval is one of the earliest and simplest models for searching such data.
*   **The Model:**
    *   Documents are sets of terms.
    *   Queries are Boolean expressions of terms, using operators AND, OR, NOT.
    *   Results are a set of documents that satisfy the Boolean expression (exact match).
*   **Example:**
    *   Query: `(Brutus AND Caesar) AND NOT Calpurnia`
    *   This query would retrieve documents that contain both "Brutus" and "Caesar" but do not contain "Calpurnia".
*   **Processing Boolean Queries:**
    *   The core idea is to use an **inverted index**.
    *   **AND:** Intersect the sets of documents containing each term.
    *   **OR:** Union the sets of documents containing each term.
    *   **NOT:** Take the complement of the set of documents containing a term (relative to the entire collection or a prior result set).

## 3. Terms and Postings

*   **Document:** A unit of text in the collection (e.g., a web page, an email, a research paper).
*   **Collection (Corpus):** A set of documents.
*   **Term:** A word or a sequence of words that is indexed. Often, terms are normalized (e.g., stemming, case-folding).
    *   Example: "Retrieval", "retrieving", "retrieved" might all be normalized to "retriev".
*   **Inverted Index:** The fundamental data structure for efficient Boolean retrieval (and many other IR models). It has two main parts:
    1.  **Dictionary (Vocabulary/Lexicon):** A list of all unique terms (the "keys") in the collection. For each term, it usually stores:
        *   The term itself.
        *   The document frequency (DF): the number of documents the term appears in.
        *   A pointer to its postings list.
    2.  **Postings List:** For each term in the dictionary, this is a list of document identifiers (docIDs) that contain the term.
        *   Example Term: `Caesar` -> Postings: `[Doc1, Doc5, Doc10, Doc23]`
        *   Example Term: `Brutus` -> Postings: `[Doc2, Doc5, Doc15, Doc23, Doc30]`
*   **Creating a Simple Inverted Index (Conceptual Steps):**
    1.  **Collect Documents:** Gather all the documents to be indexed.
    2.  **Tokenize Text:** Break down each document into individual words (tokens).
    3.  **Linguistic Preprocessing (Normalization):**
        *   **Case folding:** Convert all tokens to lowercase (e.g., "The" -> "the").
        *   **Stemming/Lemmatization:** Reduce words to their root form (e.g., "running" -> "run", "better" -> "good"). (More on this in Unit 2).
        *   **Stop word removal:** Remove common words like "the", "is", "a" (optional, context-dependent).
    4.  **Indexing:** Create term-document pairs. For each document and each term in it, record that the term occurred in the document.
    5.  **Invert:** Group these pairs by term. For each term, list all documents it appears in. This forms the postings lists.
    6.  **Sort Postings Lists:** Typically, postings lists are sorted by docID for efficient merging (intersection/union).

### Example of Postings Lists Intersection (for AND):

Query: `Caesar AND Brutus`

1.  Retrieve postings for `Caesar`: `[1, 5, 10, 23]`
2.  Retrieve postings for `Brutus`: `[2, 5, 15, 23, 30]`
3.  Intersect these two lists:
    *   Compare 1 (from Caesar) and 2 (from Brutus). Advance Caesar's pointer.
    *   Compare 5 (from Caesar) and 2 (from Brutus). Advance Brutus' pointer.
    *   Compare 5 (from Caesar) and 5 (from Brutus). Match! Add 5 to results. Advance both.
    *   Compare 10 (from Caesar) and 15 (from Brutus). Advance Caesar's pointer.
    *   Compare 23 (from Caesar) and 15 (from Brutus). Advance Brutus' pointer.
    *   Compare 23 (from Caesar) and 23 (from Brutus). Match! Add 23 to results. Advance both.
    *   One list is exhausted.
    *   Result: `[5, 23]`

This process is much more efficient than scanning every document for every query.

---

This lecture provides a foundational understanding. We will delve deeper into dictionary structures, index construction, and more advanced retrieval models in the upcoming units.
