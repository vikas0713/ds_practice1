import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def read():
    return pd.read_csv('iris.csv')


def pair_plot():
    iris = read()
    sns.set_style("whitegrid")
    sns.pairplot(iris, hue="variety", size=3)
    plt.show()

def main():
    iris = read()
    # iris.plot(x="sepal.length",y="sepal.width" , kind="scatter")
    # plt.show()
    sns.set_style("whitegrid")
    sns.FacetGrid(iris, hue="variety", size=3).map(plt.scatter, "sepal.length", "sepal.width").add_legend()
    plt.show()



if __name__ == "__main__":
    pair_plot()

