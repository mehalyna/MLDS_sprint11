import pandas as pd

from src.task2_key_principles import create_scatter_plot


def test_create_scatter_plot():
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
    try:
        create_scatter_plot(df)
        assert True, "Scatter plot generated successfully."
    except Exception as e:
        assert False, f"Scatter plot generation failed with error: {e}"


test_create_scatter_plot()
