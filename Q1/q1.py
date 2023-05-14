import csv
import matplotlib.pyplot as plt

def main() :
    region_file = {
        "whole" : "q1_whole.csv",
        "seoul" : "q1_seoul.csv",
        "busan" : "q1_busan.csv",
        "daejeon" : "q1_daejeon.csv",
        "jeju" : "q1_jeju.csv"
    }
    region_data = {
        "whole" : [],
        "seoul" : [],
        "busan" : [],
        "daejeon" : [],
        "jeju" : []
    }

    for region in region_file.keys() :
        f = open(region_file[region], 'r', encoding="cp949")
        datas = csv.reader(f, delimiter=',')
        next(datas)
        for row in datas :
            if row[-1] == "" or row[-2] == "" or row[-3] == "" :
                continue
            else :
                row[-1] = float(row[-1])
                row[-2] = float(row[-2])
                row[-3] = float(row[-3])
            region_data[region].append(row)
        f.close()

    plt.title("2022 Monthly Average Temperature Comparision by Region in South Korea")
    plt.xlabel("Month")
    plt.ylabel("Average Temperature(Celsius)")

    w = 1/len(region_data)
    month = [1,2,3,4,5,6,7,8,9,10,11,12]

    for i, region in enumerate(region_data.keys()) :
        average = []
        for data in region_data[region] :
            average.append(data[2])
        plt.plot(month, average, '^:', label=region)
    plt.xticks(month)
    plt.legend()

    plt.show()
    
    print("전국 평균보다 서울, 부산, 대전, 제주의 월평균 기온이 더 낮은 경우는 잘 없음.")
    print("전국 평균에 비해 더 더운 지역은 역시 제주라고 할 수 있고")
    print("겨울에 그나마 서울과 대전이 더 낮아지지만, 사실상 더 추운 지역은 제시된 지역중에서는 없다고 봐도 무방함.")

if __name__ == "__main__" :
    main()

