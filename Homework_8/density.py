import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def make_densityplot(iris):
    
    g = sns.set(style="darkgrid")
    g = sns.jointplot(data = iris, y = "petalWidth", x ="sepalWidth", hue = "species", kind="kde", color="m", marginal_kws=dict(fill=True))
    
    
    return g


if __name__ == "__main__":

    iris = pd.read_csv('data/iris.csv', index_col=0)
    fig = make_densityplot(iris)
    plt.show()