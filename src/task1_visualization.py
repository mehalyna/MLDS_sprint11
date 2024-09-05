from collections import Counter
from typing import Union, Any

import matplotlib.pyplot as plt
import numpy as np
import collections


def plot_distribution(data):
    """
    Plots the distribution of data using a bar chart.

    Parameters:
    data (array-like): An array of categorical data items.
    """
    counts: Union[Counter[Any], Counter[str]] = collections.Counter(data)

    # Create the bar plot
    plt.bar(counts.keys(), counts.values())
    plt.xlabel('Category')
    plt.ylabel('Frequency')
    plt.title('Data Distribution')
    plt.show()


# Example data
data = np.random.choice(['A', 'B', 'C'], size=100)
plot_distribution(data)
