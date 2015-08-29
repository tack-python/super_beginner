#coding: utf-8
print "いらっしゃいませ。お金を入れてください。"

money = raw_input()
money = int(money)

#投入金額が商品の最低金額の場合、返金してプログラムを終了する。
if money <100:
    print "最低100円は入れてください。"
    print "{0}円お返しします。".format(money)
    quit()

#投入時の金額を money_start に保存しておく。
money_start = money

while money >= 100:

    #残金が投入時の金額より少ないときに残金を表示する。
    if money < money_start:
        print "\n残金は{0}円です".format(money)

    print "どの商品になさいますか？"
    print "1. 　お水　　", "100円"
    print "2. ジュース　", "150円"
    print "3. 高級玉露　", "180円"
    print "4. 買わない"
    print "-"*50
    print "商品番号を入力してください"
    print "-"*50

    drink = raw_input()

    #買わない場合、while ループを終了する。
    if drink=="4":
        break
    elif drink=="1" and money>=100:
        money = money - 100
        print "{0} ですね。{1}円になります！".format("お水",100)
    elif drink=="2" and money>=150:
        money = money - 150
        print "{0} ですね。{1}円になります！".format("ジュース",150)
    elif drink=="3" and money>=180:
        money = money - 180
        print "{0} ですね。{1}円になります！".format(money,180)
    #金額が不足している場合、ふたたび商品選択に戻る。
    else:
        print "金額が足りません\n"

#おつりが 0円の場合、おつりがないことを説明して、終了する。
if money==0:
    print "おつりはありません。ありがとうございました！"
else:
    print "\nおつりは" + str(money) + "円です。ありがとうございました！"
