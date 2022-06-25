from matplotlib.pyplot import grid, title


def make_monthly_prices_plot():
    """
    El archivo debe guardarse en formato PNG en data_lake/business/reports/figures/monthly_prices.png.
    >>> make_monthly_prices_plot()
    """

    import pandas as pd
    import os

    os.chdir("../")

    prices_df = pd.read_csv("src/data_lake/business/precios-mensuales.csv")

    figura = prices_df.plot(
        kind="line",
        x="Fecha",
        y="Precio",
        title="Precio Promedio Histórico Mensual",
        grid=True,
        figsize=(10, 5),
    ).get_figure()

    figura.savefig("src/data_lake/business/reports/figures/monthly_prices.png")


if __name__ == "__main__":
    import doctest

    doctest.testmod()