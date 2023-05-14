import csv
import matplotlib.pyplot as plt

def main() :
    file_names = ["q3_jeju_{0}.csv".format(str(1992+i)) for i in range(0,31,10)]
    totals = []
    for fi in file_names :
        f = open(fi, 'r', encoding="UTF-8")
        data = csv.reader(f, delimiter=',')
        for i in range(0,5) :
            next(data)
        total = next(data)
        if total[6] == "" or total[7] == "" :
            continue
        else : 
            total[6] = total[6].strip()
            total[7] = total[7].strip()
            total[6] = int(total[6])
            total[7] = int(total[7])
        totals.append((total[6], total[7]))
    f.close()

    years = [1992, 2002, 2012, 2022]
    male_data = [i[0] for i in totals]
    female_data = [i[1] for i in totals]
    gender_ratio = [i[0]/i[1] for i in totals] #male / female

    fig, axe = plt.subplots(1,3)
    fig.suptitle("Does Jeju have more Female than Male?")
    fig.set_tight_layout(True)

    axe[0].set_title("Male and Female Population")
    axe[0].plot(years, male_data,'.-', color='blue',label='Male')
    axe[0].plot(years, female_data,'.-', color='hotpink',label='Female')
    axe[0].set_xlabel("Year")
    axe[0].set_ylabel("Population")
    axe[0].set_xticks(years)
    axe[0].legend()

    pie_color = ['powderblue', 'skyblue','royalblue','cornflowerblue','hotpink','darkmagenta','pink','deeppink']
    pie_data = male_data[::]
    pie_data.extend(female_data[::])
    axe[1].set_title("Male and Female\nCumulative\nPopulation Pie Graph")
    axe[1].pie(pie_data,autopct="%.1f%%", labels=years+years, colors=pie_color)
    axe[1].set_xlabel("Population by Year\n(blue-ish: male, red-ish: female)")

    axe[2].set_title("Male/Female Ratio")
    axe[2].plot(years, gender_ratio, '.-.' , color='black', label="Ratio")
    axe[2].axhline(1.0, 0.0, 3000.0, color='red', linestyle='--', linewidth=2)
    axe[2].set_xlabel("Year")
    axe[2].set_ylabel("Ratio(Male/Female)")
    axe[2].set_xticks(years)
    axe[2].legend()

    plt.show()

    print("나타난 그래프를 봤을 때, 제주도의 '제주도에는 여자가 더 많다' 라는 속설은 최소한 1990년대 이후로는 거짓이라고 볼 수 있다.")
    print("초반에는 분명히 여성인구수가 더 많았다. 하지만 최근에 들어 남성인구에 근소하게나마 뒤쳐지고 있다.")
    print("세번째 그래프와 전국의 성비를 비교해보았는데 내국민만 고려했을 때 2022년 12월 기준 여성 100명당 남성의 수가 99.4명이다.")
    print("그렇기 때문에 최근에는 오히려 전국과 반대로 남초를 띄고 있다.")

if __name__ == "__main__" :
    main()

