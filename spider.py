import requests
from lxml import etree
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import tkinter as tk
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
def kaishi():
    def danmu(m):
        try:
            n = re.findall("av.*\d/", m)[0].replace('av', '').replace("/", '').replace("?","")
        except :
            n=re.findall("av.*from",m)[0].replace('av','').replace('?from','')
        url='https://api.bilibili.com/x/player/pagelist?aid={}&jsonp=jsonp'.format(n)
        r=requests .get(url=url,headers=headers)
        urll="https://comment.bilibili.com/{}.xml".format(r.json()['data'][0]['cid'])
        rr=requests .get(url=urll,headers=headers)
        rr.encoding =rr.apparent_encoding
        html=etree.HTML(rr.content )
        dan=html.xpath("//d/text()")
        return dan
    def ciyun():
        text = open("b", "rb").read()
        wordlist = jieba.cut(text, cut_all=True)
        wl = " ".join(wordlist)
        wc = WordCloud(background_color="white",
                       scale=6,
                       max_words=2000,
                       font_path="aa.ttf",#需要下载中文字体库
                       max_font_size=50,
                       random_state=20,
                       )
        myword = wc.generate(wl)
        plt.imshow(myword)
        plt.axis("off")
        plt.show()
    if __name__=='__main__':
        m=link2.get()
        window.destroy()
        list1=danmu(m)
        for i in list1:
            with open('b','a',encoding='utf-8')as fp:
                fp.write(i)
        ciyun()
window=tk.Tk()
window.title('spider-man.bilibili弹幕')
window.geometry ('400x400')
canvas=tk.Canvas(window,bg='blue',height=135,width=190)
l=tk.Label(window,text='输入网站地址',bg='yellow',font=('Calibri',25),width=20,height=2)
l.pack()
link2=tk.Entry(window,width=60)
link2.pack()
b=tk.Button(window,text='生成弹幕词云',bg='orange',font=('Calibri',25),width=20,height=1,command=kaishi)
b.pack()
window .mainloop()
