# <center> Q & A </center>

## Q : Python自带的ILDE实在难受，有没有其他写代码软件？
1.Spyder  [<font color = #F45F3F>**Most recommend!**</font>]  

大二物理实验老师推荐软件，可视化查看数组数据，安装即帮你配置好所有数学分析所需库和环境，缺点是启动好慢，用MAC的同学体验极差，因人而异，量力而行。  

[下载地址](https://www.anaconda.com/products/individual)

2.vscode

轻量的代码编写软件，扩展多十分方便，俺就在用^^。  

[下载地址](https://code.visualstudio.com/)

3.Others: 记事本 命令行 vim 心理素质好word也可以  

## Q : 我没有用Spyder，写代码时用到一些库显示没有怎么办？
matplotlib & numpy & SciPy 是外部库，非python自带安装的，所以如果想要使用需要单独安装（如果是用spyder，它自带了这些库，就不用另外安装，但也只仅限于在spyder中使用。如果想要在所有场合中使用，需要调一下path，或者按下面方法单独安装)  
1.首先检查一下自己的电脑有没有安装pip
打开CMD（命令行 WINDOWS）或者终端（MAC），输入  
`pip --version (WINDOWS) 或 pip3 --version (MAC) `  
如果安装了，可以看到版本号，跳到STEP3 如果没有，接STEP2  
2.一般来说pip会随python一起安装到电脑上，如果没有的话，建议重新安装一遍python，选最新的版本，安装后要重启一下电脑。WINDOWS安装时记得勾选add to all path.[Python官方网站](https://www.python.org/downloads/)  
3.安装完毕一切正常后，输入   
`pip install matplotlib (WINDOWS) & pip3 install matplotlib (MAC)`  
回车等待安装完毕即可。  
Numpy & Scipy 同理 需要注意的是Scipy基于Numpy 所以最好先安装Numpy  
当然 Lecture里面也给出了方法: `python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose `