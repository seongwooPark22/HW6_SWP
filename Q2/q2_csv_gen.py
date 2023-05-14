import random

def main() :
    n_list = []
    dice_list = []
    for x in range(2,6) :
        n_list.append(10**x)
    for n in n_list:
        dice_list.append([random.randint(1,6) for i in range(0,n)])
    f = open("q2.csv", 'w', encoding="UTF-8")
    for i, result in enumerate(dice_list) :
        f.write(str(n_list[i])+","+",".join(list(map(str,result)))+'\n')
    f.close()

if __name__ == "__main__" :
    main()