"""Basic matplotlib visualizations"""
import matplotlib.pyplot as plt
import numpy as np

# Simple bar chart
categories = ["Electronics", "Clothing", "Food", "Books", "Sports"]
values = [4500, 3200, 5100, 2800, 1900]

plt.figure(figsize=(10, 6))
plt.bar(categories, values, color=["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7"])
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales (EGP)")
plt.tight_layout()
plt.savefig("sales_chart.png", dpi=100)
print("Chart saved!")
