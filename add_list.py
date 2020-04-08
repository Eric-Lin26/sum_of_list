# 寫出一個function算出清單中數字的總數
def value():  # 讓使用者輸入值
    aln = []  # 將值存在aln
    while True:     # 使用while迴圈,讓使用者自行需要輸入的值
        user = input("請輸入數字： ")
        if user == "q":
            break
        aln.append(int(user))   # 使用int將值均轉化為整數與字串分開
    return aln   # 回傳輸入的值到value()

def sum_of_list():     # 加總的函式
    return sum(value())  # sum可以為列表進行加總

print(sum_of_list())  # 執行加總函式, 加總函式會告知value函式啟動, 使用者就可以輸入數字
                       # value函式結束後, 就會啟動加總函式, 將加總函式return的結果
                       # 存在sum_of_list()裡面
                       # 就可以print出來了!