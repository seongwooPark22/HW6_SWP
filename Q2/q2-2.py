import csv
import matplotlib.pyplot as plt

def main() :
    dice_datas = []
    
    f = open("q2.csv", 'r', encoding="UTF-8")
    
    data = csv.reader(f, delimiter=',')
    for row in data :
        dice_datas.append(row)

    f.close()

    fig, axs = plt.subplots(1,len(dice_datas))
    fig.set_tight_layout(True)
    for i in range(len(dice_datas)) :
        dice_data = list(map(int, dice_datas[i]))
        sample_num = dice_data[0]
        axs[i].set_title("{0}th roll".format(sample_num))
        axs[i].set_xlabel("Dice Side")
        axs[i].set_ylabel("Count")
        axs[i].set_xticks([1,2,3,4,5,6])
        axs[i].hist(dice_data[1:], bins=6)

    fig.suptitle("6Side Dice Roll Simulate")
    plt.show()

    for i in range(len(dice_datas)) :
        dice_data = list(map(int, dice_datas[i]))
        print("Roll Dice {0}th:".format(dice_data[0]), end=" ")
        nums = [0,0,0,0,0,0]
        for Count in dice_data[1:] :
            nums[Count-1] += 1
        prob = [i/dice_data[0] for i in nums]
        print(nums)
        print("-Probability: ", prob)

    print("N번 시행했다고 했을 때, (프로그램에서 특정 숫자를 직접 뽑아서 나온 횟수/전체 시행 횟수 N)이")
    print("N이 커질 수록 히스토그램이 균일해지며 각 횟수로 구한 확률이 수학적인 확률인 1/6(1.666...)에 점점 수렴함을 볼 수 있다.")

if __name__ == "__main__" :
    main()
