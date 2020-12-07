# 关于如何判断文件格式是否正确的方法

1. 在桌面上新建一个文件夹（名字随意取 取一个好打的）将如下文件放到里面，这里以检测hw1q1.py为例:
![](https://i.loli.net/2020/12/08/2FAW9HD3COgESIp.png)
其中，a.txt为一个空的，自己创建的txt文件，随便取一个简单的名字
2. 然后打开 **终端** (MACOS) / **命令提示符** (WIN) , 输入如下指令: ` cd ./desktop/新建文件夹`
![](https://i.loli.net/2020/12/08/jsfXvaKQbrVFnAJ.png)
3. 顺利执行后（若是不顺利，请检查有没有拼写错误，已经前面步骤是否正确进行），输入 `python hw1q1.py <hw1q1in2.txt> a.txt` 若你是是用MACOS系统，请输入 `python3 hw1q1.py <hw1q1in2.txt> a.txt`
![](https://i.loli.net/2020/12/08/QN9aEgI6XYTtL5s.png)
4. 如果顺利进行，此时的a.txt中，应该是你的程序所输出的内容:
![](https://i.loli.net/2020/12/08/deMGbYHOh34ui1R.png)
5. 切回**终端**/**命令提示符**，输入`python cmp_files.py a.txt hw1q1out2.txt` 若你是是用MACOS系统，请输入 `python3 cmp_files.py a.txt hw1q1out2.txt`
![](https://i.loli.net/2020/12/08/4Xk9mdN7ORf3IDK.png)
此步为对比是否和老师给的例子输出的一样 请注意之前使用的是 **hw1q1in2.txt** 这里对应应该是 **hw1q1out2.txt**
6. 若格式正确，则会看到如下输出：
![](https://i.loli.net/2020/12/08/CFUXzPKhoYwcfru.png)
否则，将会提醒在 **line** xxx **column** xxx 有错误
7. 请记得多更换几次老师给的例子，重复上面的步骤～
