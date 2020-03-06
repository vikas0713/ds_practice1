import pandas as pd
import matplotlib.pyplot as plt


def get_dataframe():
    data_frame = pd.read_csv('company_sales_data.csv')
    return data_frame


def show_profit_month():
    # Exercise 1: Read Total profit of all months and show it using a line plot
    dframe = get_dataframe()
    month_list = dframe.month_number.tolist()
    profit_list = dframe.total_profit.tolist()
    plt.plot(month_list, profit_list, label="Profit by month")
    plt.title("Total Profit of all months")
    plt.show()


def exercise2():
    """
    Exercise Question 2: Get Total profit of all months and show line plot with the following Style properties
    Generated line plot must include following Style properties: –

    Line Style dotted and Line-color should be red
    Show legend at the lower right location.
    X label name = Month Number
    Y label name = Sold units number
    Add a circle marker.
    Line marker color as read
    Line width should be 3

    """
    dframe = get_dataframe()
    month_list = dframe.month_number.tolist()
    profit_list = dframe.total_profit.tolist()
    plt.plot(month_list, profit_list, label="Profit by month", color="r", marker="o", linestyle="--")
    plt.show()


def exercise3():
    """
    Display the number of units sold per month for each product using multiline plots.
    i.e., Separate Plotline for each product.
    """
    dframe = get_dataframe()
    month_list = dframe.month_number.tolist()
    face_cream_list = dframe.facecream.tolist()
    face_wash_list = dframe.facewash.tolist()
    toothpaste_list = dframe.toothpaste.tolist()
    moisturizer_list = dframe.moisturizer.tolist()
    bathingsoap_list = dframe.bathingsoap.tolist()
    shampoo_list = dframe.shampoo.tolist()
    plt.plot(month_list, face_cream_list, linestyle="--", label="Face Cream")
    plt.plot(month_list, face_wash_list, linestyle="--", label="Face Wash")
    plt.plot(month_list, toothpaste_list, linestyle="--", label="Toothpaste")
    plt.plot(month_list, moisturizer_list, linestyle="--", label="Moisturizer")
    plt.plot(month_list, bathingsoap_list, linestyle="--", label="Bathing Soap")
    plt.plot(month_list, shampoo_list, linestyle="--", label="Shampoo")
    plt.legend()
    plt.title("Sales of per unit by month data")
    plt.show()


def exercise4():
    """
    Read toothpaste sales data of each month and show it using a scatter plot
    """
    dframe = get_dataframe()
    month_list = dframe.month_number.tolist()
    toothpaste_list = dframe.toothpaste.tolist()
    plt.scatter(month_list, toothpaste_list, label="Toothpaste month data")
    plt.xlabel("Month number")
    plt.ylabel("Toothpaste units sold")
    plt.legend()
    plt.grid()
    plt.show()


def exercise5():
    """
    Read face cream and facewash product sales data and show it using the bar chart
    """
    dframe = get_dataframe()
    month_list = dframe.month_number.tolist()
    face_cream_list = dframe.facecream.tolist()
    face_wash_list = dframe.facewash.tolist()
    plt.bar(month_list, face_cream_list, label="Face Cream", width=0.250, align="edge")
    plt.bar(month_list, face_wash_list, label="Face Wash", width=-0.250, align="edge")
    plt.legend()
    plt.show()


def exercise6():
    """
    Read sales data of bathing soap of all months and show it using a bar chart. Save this plot to your hard disk
    """
    dframe = get_dataframe()
    month_list = dframe.month_number.tolist()
    bathingsoap_list = dframe.bathingsoap.tolist()
    plt.bar(month_list, bathingsoap_list, label="Bathing Soap")
    plt.legend()
    plt.savefig("graphs/exercise6.png")
    plt.show()


def exercise7():
    """
    Calculate total sale data for last year for each product and show it using a Pie chart
    """
    labels = ["Facewash", "Facecream", "Toothpaste", "Bathing Soap", "Shampoo", "Moisturizer"]
    dframe = get_dataframe()
    total_sum = [
        dframe["facewash"].sum(), dframe["facecream"].sum(), dframe["toothpaste"].sum(),
        dframe["bathingsoap"].sum(), dframe["shampoo"].sum(), dframe["moisturizer"].sum()
    ]
    plt.pie(total_sum, labels=labels, autopct="%1.1f%%")        # autopct basically shows percentage on chart
    plt.legend()
    plt.savefig("graphs/exercise7.png")
    plt.show()


if __name__ == "__main__":
    exercise7()