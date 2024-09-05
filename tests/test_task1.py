import numpy as np

from src.task1_visualization import plot_distribution


def test_plot_distribution():
    data = np.array(['A', 'B', 'B', 'C', 'C', 'C'])
    try:
        plot_distribution(data)
        assert True, "Plot generated successfully."
    except Exception as e:
        assert False, f"Plot generation failed with error: {e}"


test_plot_distribution()
