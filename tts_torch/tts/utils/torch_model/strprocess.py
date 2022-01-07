numdi = {'0': 'zero', '1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six",
         '7': "seven", '8': "eight",'9': "nine"}

num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def num2en(text):
    res_tmp = []
    for i in range(len(text)):
        cha = text[i]
        if cha not in num:
            res_tmp.append(cha)
        else:
            res_tmp.append(numdi[cha])
    res = "".join(i for i in res_tmp)
    return res
