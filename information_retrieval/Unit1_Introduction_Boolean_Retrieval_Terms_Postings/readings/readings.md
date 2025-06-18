# Unit 1: Readings - Introduction to IR, Boolean Retrieval, Terms and Postings

## Primary Textbook:

For this course, we will primarily refer to:

*   **"Introduction to Information Retrieval" by Christopher D. Manning, Prabhakar Raghavan and Hinrich Schütze.** (Cambridge University Press, 2008).
    *   You can find it online: [https://nlp.stanford.edu/IR-book/](https://nlp.stanford.edu/IR-book/)

## Unit 1 Readings:

This week's topics—Introduction to Information Retrieval, Boolean Retrieval, and the concepts of Terms and Postings—are covered extensively in the following chapters of the textbook:

*   **Chapter 1: Boolean retrieval**
    *   This chapter introduces the problem of information retrieval and the first model of retrieval, Boolean retrieval. It covers:
        *   An example information retrieval problem.
        *   A first take at building an inverted index.
        *   Processing Boolean queries.
        *   The extended Boolean model versus ranked retrieval (briefly).

*   **Chapter 2: The term vocabulary and postings lists**
    *   This chapter delves deeper into the fundamental data structures used in IR systems. It covers:
        *   Document delineation and character sequence decoding.
        *   Determining the vocabulary of terms: tokenization, normalization (including case-folding, stemming, lemmatization), and stop words.
        *   Postings lists: faster postings list intersection via skip pointers, and positional postings for phrase queries.

## Recommendations for Reading:

*   **Start with Chapter 1:** Get a solid understanding of what IR is and how the basic Boolean model works. Pay attention to the logic of processing Boolean queries.
*   **Proceed to Chapter 2:** Focus on how documents are processed to extract terms and how these terms and their postings lists are structured. The concepts of tokenization and normalization are crucial.
*   **Take Notes:** As you read, jot down key definitions, concepts, and any questions you might have.
*   **Relate to Lectures:** Try to connect the material in the textbook with the topics discussed in the `lecture1.md` file. The textbook provides more depth and formal definitions.

These chapters will provide a strong foundation for understanding the core mechanics of information retrieval systems, which we will build upon throughout the course.
