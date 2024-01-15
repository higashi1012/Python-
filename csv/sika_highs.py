import csv

import matplotlib.pyplot as plt

filename = "data/sitka_weather_07-2018_simple.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row =next(reader)

    # indexと値を確認
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # 最高気温(index番号5を取得)
    highs = [int(row[5]) for row in reader]
    # print(highs)

    # 最高気温のグラフを描画する
    plt.style.use("seaborn")
    fig, ax = plt.subplots()
    ax.plot(highs, c="red")

    # グラフにフォーマットを指定する
    plt.title("Daily high temperatures, july 2018", fontsize=24)
    plt.xlabel("", fontsize=16)
    plt.ylabel("temperature(F)", fontsize=16)
    plt.tick_params(axis="both", which="major", labelsize=16)

    plt.show()