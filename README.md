# PyQt5各种demo
## 其它几个都是简易demo，Weather demo比较完整，放一下截图
![界面效果](pic/001.png)

## 安装：
- pip install PyQt5
- pip install PyQt5-tools
#### 国内加速：
- pip install PyQt5 -i https://pypi.douban.com/simple
- pip install PyQt5-tools -i https://pypi.douban.com/simple


## 编译：
#### 不带调试窗口：
- C:\Python36\Scripts\pyinstaller.exe  -F -w -i  logo.ico Tools.py -n weather
#### 带调试窗口：
- C:\Python36\Scripts\pyinstaller.exe  -F -i  logo.ico Tools.py -n weather
#### 参考文档：
- https://blog.csdn.net/weixin_42296333/article/details/81178915

## 其他：
1. 因为要打成exe包，代码中加载的静态资源最好都是绝对位置，因为py和exe执行是不一样的
项目中现在使用os.path.split(os.path.realpath(sys.argv[0]))[0]获取绝对位置

2. Weather demo中还带了一个有个sql sever使用demo，用的是pymssql库

3. 使用QtSql连接mysql数据库时，可能会有连不上的情况
需要把文件C:\Program Files\MySQL\MySQL Server 5.7\lib\libmysql.dll
复制到C:\Python36\Lib\site-packages\PyQt5\Qt\bin目录下

4. 报错提示Pyqt5.sip找不到
原因是版本不匹配，重新安装pyqt5，pyqt5-tool库

5. 使用icon时，需要用工具把png转换到icon，不能直接改后缀名

6. 图片打包后不生效，需要再在res.qrc中添加png文件名，然后使用pyqcc外部工具编译res.qrc文件，生成res_rc.py

7. 如果其它电脑无法使用，把这个路径下的3个文件放一起，当前项目放在了dist\platforms目录下
C:\Python36\Lib\site-packages\PyQt5\plugins\platforms
qminimal.dll
qoffscreen.dll
qwindows.dll


## 三个外部工具的配置(待补充)

