#coding: utf-8
import urllib2

print "データをダウンロード中です..."
wagahai = urllib2.urlopen('http://www.aozora.gr.jp/cards/000148/files/789_14547.html')

wagahai2 = wagahai.read()
wagahai3 = unicode(wagahai2, 'shift-jis', errors='ignore')



def wordcount(data, w):
    n = data.count(w)
    print "「{0}」は {1}回でてきました。\n".format(w,n)


while True:
    print "「我が輩は猫である」のなかで探したい言葉を入力してください。"
    print "検索を中止するときは「おわり」と入力してください。"
    word = raw_input()

    if word=="おわり":
        print "ありがとうございました。またのお越しを。"
        quit()
    else:
        wordcount(data=wagahai3, w=word)
