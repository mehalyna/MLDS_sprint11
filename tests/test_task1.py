import numpy as np
from matplotlib import pyplot as plt

from src.task1_visualization import plot_distribution


def test_plot_distribution():
    data = np.array(['A', 'B', 'B', 'C', 'C', 'C'])
    try:
        plot_distribution(data)
        print("Bar plot generated successfully.")
    except Exception as e:
        assert False, f"Plot generation failed with error: {e}"


test_plot_distribution()
