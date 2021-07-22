# Principal Component Analysis (PCA)

PCA is an unsupervised learning algorithm that groups variable information into main components.

Requirements: variables must be numeric and data standardized.

The transformation is applied in such a way that linearly correlated variables get transformed into uncorrelated variables. Correlation tells us that there is redundancy of information, and if that redundancy can be reduced, the information can be compressed.

In this case, I used sklearn's Iris Dataset to do the dimensionality reduction.