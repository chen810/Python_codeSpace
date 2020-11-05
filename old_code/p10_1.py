# p10_1.py
import easygui as g
import sys
while 1:
    g.msgbox("嗨，欢迎进入第一个界面")
    msg="你想在这￥%……#￥￥#%&￥#？？？"
    title="互动"
    choices=["谈恋爱","编程","其他"]
    choice=g.choicebox(msg,title,choices)
    #note that we convent choice to string,in case
    #the user cancelled the chocice,and we got none
    g.msgbox("你的选择是："+str(choice),"结果")
    msg="你希望重新开始吗？"
    title ="请选择"
    if g.ccbox(msg,title):#show a continue/cancel dialog
        pass # user chose continue
    else:
        sys.exit(0) #user chose cancel
