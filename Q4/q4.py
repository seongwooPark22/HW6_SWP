import csv
import matplotlib.pyplot as plt

def sort_dict(dict) :
    ret_list = []

    for item in list(dict.items()) :
        if len(ret_list) == 0 :
            ret_list.append(item)
        else :
            temp_l = ret_list[::]
            for i, l_item in enumerate(temp_l) :
                if item[1] >= l_item[1]:
                    if i == len(temp_l)-1 :
                        ret_list.append(item)
                    continue;
                else :
                    ret_list.insert(i, item)
                    break;
    return ret_list

def main() :
    station_geton_dict = {}
    station_quit_dict = {}
    station_total_dict = {}

    f = open("q4.csv", encoding="UTF-8")
    datas = csv.reader(f, delimiter=',')
    next(datas)
    next(datas)

    for row in datas :
        if row[3] == "" or row[4] == "" or row[5] == "" or row[6] == "" or  row[7] == "" :
            continue;
        else :
            row[4] = int(row[4])
            row[5] = int(row[5])
            row[6] = int(row[6])
            row[7] = int(row[7])

            if not row[3] in station_geton_dict.keys() :
                station_geton_dict[row[3]] = 0
                station_quit_dict[row[3]] = 0
                station_total_dict[row[3]] = 0
            station_geton_dict[row[3]] += row[4] + row[6]
            station_quit_dict[row[3]] += row[5] + row[7]
            station_total_dict[row[3]] += station_geton_dict[row[3]] + station_quit_dict[row[3]]
    f.close()

    sorted_dicts = [
        sort_dict(station_geton_dict)[-30:],
        sort_dict(station_quit_dict)[-30:],
        sort_dict(station_total_dict)[-30:]
    ]
    plt.rc('font', family="Malgun Gothic")
    plt.rcParams['axes.unicode_minus'] = False
    fig, axe = plt.subplots(1, 3)
    fig.set_tight_layout(True)

    axe[0].set_title("Top 30 Aboarding Passangers Number")
    axe[1].set_title("Top 30 Quitting Passangers Number")
    axe[2].set_title("Top 30 (Total) Passangers Number")
    for i, sorted_item in enumerate(sorted_dicts) :
        xdata = [item[0] for item in sorted_item]
        ydata = [item[1] for item in sorted_item]

        axe[i].bar(xdata, ydata)
        axe[i].set_xlabel("Station", size=8)
        axe[i].set_ylabel("Passangers")
        axe[i].set_yticks(list(range(0,max(ydata)+200000,50000)),minor=True)
        axe[i].set_ylim(0,max(ydata)+200000)
        axe[i].set_xticklabels(
            axe[i].get_xticklabels(),
            rotation=50,horizontalalignment='right',
            fontweight='light',
            fontsize='x-small'
        )
        axe[i].set_yticklabels(["{0:.0f}".format(x) for x in axe[i].get_yticks()])
    plt.show()
    
    geton_n = [item[0] for item in sorted_dicts[0]]
    quit_n = [item[0] for item in sorted_dicts[1]]
    total_n = [item[0] for item in sorted_dicts[2]]

    geton_v = [item[1] for item in sorted_dicts[0]]
    quit_v = [item[1] for item in sorted_dicts[1]]
    total_v = [item[1] for item in sorted_dicts[2]]

    print("승/하차가 가장 많은 역들은 다음과 같다")
    print("승차가 가장 많은 역:",geton_n[-1])
    print("-승차한 인구 :",geton_v[-1])
    print("하차가 가장 많은 역:",quit_n[-1])
    print("-하차한 인구 :",quit_v[-1])
    print("승하차가 가장 많은 역:",total_n[-1])
    print("-승하차한 인구 :",total_v[-1])

if __name__ == "__main__" :
    main()
