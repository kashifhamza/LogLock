import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from imblearn.over_sampling import RandomOverSampler

# Load the dataset
df = pd.read_csv("keyloggingdata.csv")

# Check the initial shape and distribution
print("Initial shape:", df.shape)
print("Initial label distribution:")
print(df['label'].value_counts())

# Check current label distribution
label_counts = df['label'].value_counts()
m_0 = label_counts[0]
m_1 = label_counts[1]

# Use RandomOverSampler to balance and expand the dataset
ros = RandomOverSampler(sampling_strategy={0: 500, 1: 500}, random_state=42)
X_resampled, y_resampled = ros.fit_resample(df.drop(columns=['label']), df['label'])

# Create the new DataFrame
df_resampled = pd.DataFrame(X_resampled, columns=df.columns[:-1])
df_resampled['label'] = y_resampled

# Check the final label distribution and shape
print("Resampled shape:", df_resampled.shape)
print("Resampled label distribution:")
print(df_resampled['label'].value_counts())

# Display the head of the resampled DataFrame
print(df_resampled.head())
