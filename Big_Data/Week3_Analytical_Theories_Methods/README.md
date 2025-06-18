# Week 3: Unit 3 - Analytical Theories and Methods

Welcome to Unit 3! This week, we delve into the analytical theories and methods used to extract meaningful insights from Big Data.

## Types of Analytics

1.  **Descriptive Analytics:** What happened?
    *   Focuses on summarizing past data to understand what has occurred.
    *   Techniques: Dashboards, reporting, data visualization, basic statistical measures (mean, median, mode).
    *   *Example:* A retail company analyzing sales reports from the last quarter to understand which products sold the most.

2.  **Predictive Analytics:** What could happen?
    *   Uses historical data and statistical algorithms to forecast future outcomes.
    *   Techniques: Regression analysis, time series analysis, machine learning models (e.g., decision trees, neural networks).
    *   *Example:* A financial institution using customer data to predict the likelihood of loan defaults.

3.  **Prescriptive Analytics:** What should we do about it?
    *   Goes beyond predicting future outcomes by suggesting actions to take to affect those outcomes or optimize decisions.
    *   Techniques: Optimization algorithms, simulation, decision analysis.
    *   *Example:* An airline using prescriptive analytics to optimize flight scheduling and pricing based on demand forecasts and operational constraints.

## Data Mining Concepts

Data mining is the process of discovering patterns, correlations, anomalies, and other valuable information from large datasets. Key concepts include:

1.  **Classification:**
    *   Assigning items in a collection to target categories or classes. The goal is to accurately predict the target class for each case in the data.
    *   *Algorithms:* Decision Trees, Logistic Regression, Support Vector Machines (SVM), k-Nearest Neighbors (k-NN).
    *   *Example:* Classifying emails as "spam" or "not spam".

2.  **Clustering:**
    *   Grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar to each other than to those in other groups. It's an unsupervised learning technique.
    *   *Algorithms:* K-Means, Hierarchical Clustering, DBSCAN.
    *   *Example:* Segmenting customers into different groups based on their purchasing behavior.

3.  **Association Rule Mining:**
    *   Discovering interesting relationships (associations) between variables in large databases.
    *   *Algorithm:* Apriori.
    *   *Example:* Finding that customers who buy bread and butter together are also likely to buy milk (the "market basket analysis").

4.  **Regression:**
    *   Predicting a continuous value.
    *   *Algorithms:* Linear Regression, Polynomial Regression.
    *   *Example:* Predicting the price of a house based on its features (size, location, number of bedrooms).

5.  **Anomaly Detection (Outlier Detection):**
    *   Identifying data points that deviate significantly from the rest of the dataset.
    *   *Example:* Detecting fraudulent credit card transactions.

## Machine Learning Algorithms for Big Data

Machine learning (ML) is a subset of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Many ML algorithms are used with Big Data:

*   **Supervised Learning:** Uses labeled data (input-output pairs) to train models.
    *   *Examples:* Linear Regression, Logistic Regression, Decision Trees, Random Forests, Gradient Boosting Machines, Support Vector Machines, Neural Networks.
*   **Unsupervised Learning:** Uses unlabeled data to find patterns or structure.
    *   *Examples:* K-Means Clustering, Principal Component Analysis (PCA), Association Rule Mining.
*   **Reinforcement Learning:** Agents learn to make decisions by taking actions in an environment to maximize a cumulative reward.
    *   *Examples:* Q-learning, SARSA.

When dealing with Big Data, these algorithms often need to be adapted or implemented in distributed computing frameworks like Apache Spark (using MLlib) to handle the scale.

## Python Example: Basic K-Means Clustering

Let's illustrate K-Means clustering using Python's `scikit-learn` library. K-Means aims to partition *n* observations into *k* clusters in which each observation belongs to the cluster with the nearest mean.

```python
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample data: (Assume these are two features of some items, e.g., height and weight)
# Let's create some synthetic data that has some inherent grouping.
X = np.array([
    [1, 2], [1.5, 1.8], [1.2, 2.2],  # Cluster 1 around (1,2)
    [5, 8], [5.5, 7.5], [4.8, 8.2],  # Cluster 2 around (5,8)
    [9, 3], [9.5, 2.8], [8.8, 3.2],  # Cluster 3 around (9,3)
    [1.8, 2.5], [5.2, 7.0], [9.2, 3.5] # A few more points
])

# We want to find 3 clusters (k=3)
kmeans = KMeans(n_clusters=3, random_state=42, n_init='auto') # n_init='auto' to suppress warning

# Fit the model to the data
kmeans.fit(X)

# Get the cluster assignments for each data point
labels = kmeans.labels_

# Get the coordinates of the cluster centers
centroids = kmeans.cluster_centers_

print("Data points:\n", X)
print("\nCluster labels for each point:", labels)
print("\nCluster centroids:\n", centroids)

# --- Visualization (Optional, but helpful for understanding) ---
# This part requires matplotlib. If you run this code, make sure it's installed.
# pip install matplotlib

def plot_clusters():
    plt.figure(figsize=(8, 6))

    # Plot data points, colored by their assigned cluster
    scatter = plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', marker='o', label='Data Points')

    # Plot cluster centroids
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=200, label='Centroids')

    plt.title('K-Means Clustering Example')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    plt.grid(True)
    # Instead of plt.show(), we'll save it if this were a script for a real environment.
    # For now, we'll just describe what it would show.
    # plt.savefig("kmeans_clusters.png") # Example of saving
    print("\n--- Plot Description ---")
    print("The plot would show data points colored by their assigned cluster (0, 1, or 2).")
    print("Red 'x' marks would indicate the calculated centers of these clusters.")
    print("This visualization helps to see how K-Means has grouped the data.")

# To run the example and see the plot description:
# plot_clusters()
# If you have matplotlib installed and are running this in an environment that supports plots,
# you can uncomment plt.show() in the function and call it.

# Example of how to use the function (call it if you want to execute the print statements)
# plot_clusters()

# --- How to interpret the output: ---
# 'labels' will show which cluster (0, 1, or 2) each point in X has been assigned to.
# 'centroids' will give the coordinates of the center of each of the 3 clusters.
```

This example demonstrates a fundamental clustering technique. In Big Data scenarios, similar algorithms are applied to much larger datasets using distributed frameworks to identify patterns and segments.

Next, we will explore how to query these vast amounts of data.
