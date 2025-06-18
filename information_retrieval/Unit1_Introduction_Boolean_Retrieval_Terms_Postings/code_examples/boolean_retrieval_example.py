# Simple Boolean Retrieval Example

# Sample Document Collection
# Each document is a string.
documents = {
    1: "The quick brown fox jumps over the lazy dog.",
    2: "A quick brown dog outruns the lazy fox.",
    3: "The fox is quick, the dog is lazy.",
    4: "No dogs or foxes here, just a quick cat.",
    5: "Another document about a dog and a fox, quick quick!"
}

def preprocess(text):
    """
    Simple preprocessing: lowercase and split into words.
    More advanced preprocessing would include stemming, stop-word removal, etc.
    """
    return text.lower().split()

def create_inverted_index(docs):
    """
    Creates an inverted index from a dictionary of documents.
    The index maps terms to a sorted list of document IDs.
    """
    inverted_idx = {}
    for doc_id, text in docs.items():
        terms = preprocess(text)
        for term in terms:
            if term not in inverted_idx:
                inverted_idx[term] = []
            if doc_id not in inverted_idx[term]: # Add doc_id only once
                inverted_idx[term].append(doc_id)

    # Sort document IDs for efficient merging later
    for term in inverted_idx:
        inverted_idx[term].sort()
    return inverted_idx

# --- Boolean Operations on Postings Lists ---

def intersect_postings(p1, p2):
    """
    Computes the intersection of two sorted postings lists.
    p1, p2: lists of document IDs (sorted)
    Returns a new sorted list of document IDs.
    """
    result = []
    i = 0 # pointer for p1
    j = 0 # pointer for p2
    while i < len(p1) and j < len(p2):
        if p1[i] == p2[j]:
            result.append(p1[i])
            i += 1
            j += 1
        elif p1[i] < p2[j]:
            i += 1
        else:
            j += 1
    return result

def union_postings(p1, p2):
    """
    Computes the union of two sorted postings lists.
    p1, p2: lists of document IDs (sorted)
    Returns a new sorted list of document IDs.
    """
    result = []
    i = 0
    j = 0
    while i < len(p1) or j < len(p2):
        if i < len(p1) and (j == len(p2) or p1[i] < p2[j]):
            if not result or result[-1] != p1[i]: # Avoid duplicates if p1 has them
                result.append(p1[i])
            i += 1
        elif j < len(p2) and (i == len(p1) or p2[j] < p1[i]):
            if not result or result[-1] != p2[j]: # Avoid duplicates if p2 has them
                result.append(p2[j])
            j += 1
        elif i < len(p1) and j < len(p2) and p1[i] == p2[j]: # Both equal
            if not result or result[-1] != p1[i]:
                 result.append(p1[i])
            i += 1
            j += 1
    return result


def not_postings(p, all_doc_ids):
    """
    Computes the complement of a postings list with respect to all document IDs.
    p: a list of document IDs (sorted)
    all_doc_ids: a sorted list of all document IDs in the collection.
    Returns a new sorted list of document IDs.
    """
    result = []
    i = 0 # pointer for p
    j = 0 # pointer for all_doc_ids
    while i < len(p) and j < len(all_doc_ids):
        if all_doc_ids[j] < p[i]:
            result.append(all_doc_ids[j])
            j += 1
        elif all_doc_ids[j] == p[i]:
            i += 1
            j += 1
        else: # p[i] < all_doc_ids[j] - this shouldn't happen if p is a subset of all_doc_ids
            i += 1
    # Add remaining doc_ids from all_doc_ids
    while j < len(all_doc_ids):
        result.append(all_doc_ids[j])
        j += 1
    return result

# --- Main Execution ---
if __name__ == "__main__":
    print("Original Documents:")
    for doc_id, text in documents.items():
        print(f"Doc {doc_id}: {text}")
    print("\n---")

    # 1. Create the Inverted Index
    inverted_index = create_inverted_index(documents)
    print("Inverted Index (Term -> Document IDs):")
    for term, postings in sorted(inverted_index.items()):
        print(f"'{term}': {postings}")
    print("\n---")

    # Get all document IDs for NOT operation context
    all_ids = sorted(list(documents.keys()))
    print(f"All Document IDs: {all_ids}\n---")

    # 2. Process some example Boolean queries

    # Query 1: "quick AND fox"
    print("Query: quick AND fox")
    postings_quick = inverted_index.get("quick", [])
    postings_fox = inverted_index.get("fox", [])
    result_q1 = intersect_postings(postings_quick, postings_fox)
    print(f"Postings for 'quick': {postings_quick}")
    print(f"Postings for 'fox': {postings_fox}")
    print(f"Result (Doc IDs): {result_q1}")
    for doc_id in result_q1:
        print(f"  Doc {doc_id}: {documents[doc_id]}")
    print("\n---")

    # Query 2: "lazy OR cat"
    print("Query: lazy OR cat")
    postings_lazy = inverted_index.get("lazy", [])
    postings_cat = inverted_index.get("cat", [])
    result_q2 = union_postings(postings_lazy, postings_cat)
    print(f"Postings for 'lazy': {postings_lazy}")
    print(f"Postings for 'cat': {postings_cat}")
    print(f"Result (Doc IDs): {result_q2}")
    for doc_id in result_q2:
        print(f"  Doc {doc_id}: {documents[doc_id]}")
    print("\n---")

    # Query 3: "(quick AND fox) AND NOT dog"
    print("Query: (quick AND fox) AND NOT dog")
    # Result from Query 1 is (quick AND fox)
    postings_dog = inverted_index.get("dog", [])
    intermediate_result_q3 = result_q1 # from (quick AND fox)
    not_dog_postings = not_postings(postings_dog, all_ids)

    # To do (A AND NOT B), we can do intersect(postings_A, not_postings_B)
    result_q3 = intersect_postings(intermediate_result_q3, not_dog_postings)

    print(f"Postings for '(quick AND fox)': {intermediate_result_q3}")
    print(f"Postings for 'dog': {postings_dog}")
    print(f"Postings for 'NOT dog': {not_dog_postings}")
    print(f"Result (Doc IDs): {result_q3}")
    for doc_id in result_q3:
        print(f"  Doc {doc_id}: {documents[doc_id]}")
    print("\n---")

    # Query 4: "quick AND (NOT fox OR cat)"
    # This is more complex: requires order of operations.
    # Let's do (NOT fox) first, then ( (NOT fox) OR cat ), then AND with quick.
    print("Query: quick AND (NOT fox OR cat)")
    postings_quick = inverted_index.get("quick", [])
    postings_fox = inverted_index.get("fox", [])
    postings_cat = inverted_index.get("cat", [])

    not_fox = not_postings(postings_fox, all_ids)
    print(f"Postings for 'NOT fox': {not_fox}")

    not_fox_or_cat = union_postings(not_fox, postings_cat)
    print(f"Postings for '(NOT fox) OR cat': {not_fox_or_cat}")

    result_q4 = intersect_postings(postings_quick, not_fox_or_cat)
    print(f"Postings for 'quick': {postings_quick}")
    print(f"Result (Doc IDs): {result_q4}")
    for doc_id in result_q4:
        print(f"  Doc {doc_id}: {documents[doc_id]}")
    print("\n---")

    print("Boolean retrieval example complete.")
