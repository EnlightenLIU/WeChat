# 1.这个可以改进的有登录一次是不是后续不用再扫码登录
# 2.好友比例柱状图显示数值
# 3.好友的省市分布情况
import itchat
from matplotlib import pyplot as plt


def draw(datas):
    for key in datas.keys():
        plt.bar(key, datas[key])

    plt.legend()
    plt.xlabel('sex')
    plt.ylabel('rate')
    plt.title("Gender of Alfred's friends")
    plt.show()

def parse_friedns():
    itchat.login()
    text = dict()
    numbers=itchat.get_friends(update=True)
    print(len(numbers))
    friedns = itchat.get_friends(update=True)[0:]
    print(numbers)
    print(friedns)
    male = "male"
    female = "female"
    other = "other"
    for i in friedns[1:]:
        sex = i['Sex']
        if sex == 1:
            text[male] = text.get(male, 0) + 1
        elif sex == 2:
            text[female] = text.get(female, 0) + 1
        else:
            text[other] = text.get(other, 0) + 1
    total = len(friedns[1:])
    print('男性好友数量：',text[male])
    print('女性好友数量：',text[female])
    print('未知性别好友数量：',text[other])
    print("男性好友比例： %.2f%%" % (float(text[male]) / total * 100) + "\n" +
          "女性好友比例： %.2f%%" % (float(text[female]) / total * 100) + "\n" +

          "不明性别好友比例： %.2f%%" % (float(text[other]) / total * 100))
    draw(text)


if __name__ == '__main__':
    parse_friedns()