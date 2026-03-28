"""Pandas introduction - basic operations"""
import pandas as pd
import numpy as np

# Create a simple DataFrame
data = {
    "name": ["Ahmed", "Sara", "Mohamed", "Fatma"],
    "age": [25, 22, 28, 24],
    "city": ["Cairo", "Alex", "Giza", "Cairo"],
    "score": [85, 92, 78, 95]
}
df = pd.DataFrame(data)

# Basic operations
print("Shape:", df.shape)
print("\nDescribe:\n", df.describe())
print("\nMean age:", df["age"].mean())
print("\nFilter Cairo:\n", df[df["city"] == "Cairo"])
