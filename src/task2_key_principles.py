import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


def create_scatter_plot(data):
    """
    Creates a scatter plot using Seaborn.

    Parameters:
    data (DataFrame): A DataFrame containing 'x' and 'y' columns.
    """
    fig, _ = plt.subplots()
    sns.scatterplot(x='x', y='y', data=data)
    plt.title('Scatter Plot of X vs Y')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()
    return fig



# Example data
data = pd.DataFrame({
    'x': np.random.rand(50),
    'y': np.random.rand(50)
})
create_scatter_plot(data)
