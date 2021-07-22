# Imports
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load data
from sklearn.datasets import load_iris
data = load_iris()

print(data.data)

X = data.data

# Standard Scaler
scaled_data = StandardScaler().fit_transform(X)

# PCA
pca = PCA(n_components=2)
pca.fit(scaled_data)

# Evaluation
# The two components explain approximately 96% of the data variability
print(pca.explained_variance_ratio_)
print(pca.singular_values_)