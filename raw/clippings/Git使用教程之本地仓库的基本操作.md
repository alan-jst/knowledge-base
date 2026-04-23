## 1、Git是什么？

一个分布式版本控制系统，和 [SVN](https://zhida.zhihu.com/search?content_id=230579925&content_type=Article&match_order=1&q=SVN&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzcxMDgxODQsInEiOiJTVk4iLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMzA1Nzk5MjUsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.FRj7PijD1CmWL4_ZYIoZXkkbDg4dvhCFZ1yhxLNOyqM&zhida_source=entity) 类似，但远比SVN强大的一个版本控制系统。

①Git可以方便的在本地进行版本管理，如同你本地有一个版本管理服务器一样我们可以选择在合适的时间将本地版本推送到统一的版本管理服务器

②Git每次会提取整个代码仓库的完整镜像，相当于对整个代码仓库都进行了一次备份，这样计时版本服务器除了问题，我们可以直接采用本地仓库恢复！结合本地版本管理功能，远程版本管理服务器出问题了，我们依然能继续写自己的代码，当他恢复的时候我们再提交我们的本地版本！

Git研发初期是为了更好的管理 [Linux内核](https://zhida.zhihu.com/search?content_id=230579925&content_type=Article&match_order=1&q=Linux%E5%86%85%E6%A0%B8&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzcxMDgxODQsInEiOiJMaW51eOWGheaguCIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjIzMDU3OTkyNSwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.fADzdZ7FRempcZFQf9InBEyAHu_rSOOVZxbyyN0SUp0&zhida_source=entity) ，不过现在已经广泛应用于各种项目中！

## 2、安装Git

如果你的系统是Linux的话，直接打开shell输入:

```
sudo apt-get install git
```

当然，大部分的系统估计都是Windows，这就需要我们到网上下载一个Git For Window了，可到下述网站下载： [git-for-windows.github.io](https://link.zhihu.com/?target=https%3A//git-for-windows.github.io/)

点击 Download，跳转到 Github ，下载对应安装包即可！

![](https://pic2.zhimg.com/v2-1acd192885e414e71632ff0fbe4ec3cb_1440w.jpg)

点击后进入页面，下载如下文件即可

![](https://pic1.zhimg.com/v2-9efb28818af974918168ffaf164e9f28_1440w.jpg)

或者直接下载目前最新版2.7.0： [v2.7.0.windows.1](https://link.zhihu.com/?target=https%3A//github.com/git-for-windows/git/releases/tag/v2.7.0.windows.1) 接着傻瓜式的下一步就可以了~接下来你可以找到 [Git Gui](https://zhida.zhihu.com/search?content_id=230579925&content_type=Article&match_order=1&q=Git+Gui&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzcxMDgxODQsInEiOiJHaXQgR3VpIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MjMwNTc5OTI1LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.NZvo2SrBhfiVXBCZfAc5aT6YE08jkWFg34wpad9Jppo&zhida_source=entity) 然后开始玩Git，不过如果以后换到其他平台上，没有图形化界面你就寸步难行了！

So，如果你有兴趣的话，我们来玩命令行，以后换了系统也能正常的玩Git！

## 3、玩转Git命令行

当然Git肯定是搭配着 [GitHub](https://zhida.zhihu.com/search?content_id=230579925&content_type=Article&match_order=1&q=GitHub&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzcxMDgxODQsInEiOiJHaXRIdWIiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoyMzA1Nzk5MjUsImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.2FolT2qjh-A_6R_VKLK1lRNLW6FRYv95uTAIEXviozk&zhida_source=entity) 玩才够味的，不过先来学习一些本地的指令先把！当你安装完Git后我们可以在任意位置右键，点击 [Git bash](https://zhida.zhihu.com/search?content_id=230579925&content_type=Article&match_order=1&q=Git+bash&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzcxMDgxODQsInEiOiJHaXQgYmFzaCIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjIzMDU3OTkyNSwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.d2GeYKmHN3HUAkyycIR6EfoxYsFrvJcqgVI1A0uMu6o&zhida_source=entity) 打开我们的Git命令行！你可以可以点击Git Init Here直接在当前目录下创建一个代码仓库，又或者点击Git Gui打开Gui的图形操作页面！

![](https://pic4.zhimg.com/v2-430e3bfcc2559a028c3ad6a7fe0a6e03_1440w.jpg)

### 3.1、创建代码仓库

Step 1：先配置下我们的身份吧，这样在提交代码的时候Git就可以知道是谁提交的，命令如下：

```
git config --global user.name "coder-pig"
git config --global user.email "779878443@qq.com"
```

配置完成后，我们可以再次输入，不包括名称，可以看到我们已经配置成功了

![](https://pic4.zhimg.com/v2-940a70656f18c43a9bddc22b4afdf27b_1440w.jpg)

Step 2：找个地方创建我们的代码仓库，然后我创建了一个新的项目：TestForGit，来到工程的目录下，右键，打开我们的Git Bash，键入下述指令完成代码仓库的建立！另外这个代码仓库其实是用来保存版本管理所需的一些信息，我们本地提交的代码都会提交到代码仓库中，于是乎我们可以选择还原到某个版本，当然，如果需要的话，我们还可以将保存在代码仓库中的代码推送那个到远程仓库中！比如GitHub!

```
git init
```

一个简单的代码，代码仓库就创建完毕了！继续输入：ls - al可以看到下目录下有个.git的文件夹就是他了！

![](https://pic4.zhimg.com/v2-ad684b7c7a35bb61a8481aecfefc4e03_1440w.jpg)

也可以打开工程目录，同样看也看到.git文件夹；如果我们想删除代码仓库只需把这个文件夹删掉即可！

![](https://pica.zhimg.com/v2-23a920e5ba5e1f70fcc3f407cae051d0_1440w.jpg)

### 3.2、提交本地代码

创建完代码仓库，接下来说下如何提交代码，我们是先用add命令把要提交的内容都加进来，然后commit才是真的去执行提交操作！命令例子如下，你可以一次次慢慢添加，当然也可以全部提交，直接 [git add](https://zhida.zhihu.com/search?content_id=230579925&content_type=Article&match_order=1&q=git+add&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzcxMDgxODQsInEiOiJnaXQgYWRkIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MjMwNTc5OTI1LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.3_XEVQMMYUhYejl-7g953_u4byWL1R5RvgyPE5T6Z7w&zhida_source=entity).即可完成！我们现在工程目录下创建一个readme.txt的文件试试，随便写点东西，然后依次输入下述指令：

```
git add readme.txt
 git commit -m "Wrote a readme file"
```

输入命令试试：

![](https://pic1.zhimg.com/v2-a8e3a7ff6b97f73329b79152388a9368_1440w.jpg)

当然如果你可以add多个文件后再一次性commit，不过如果我们改动的文件很多的话，我们可以git add.一次添加全部，但有一些是几百年都不变一次的又或者自动生成的，比如lib，gen，bin文件夹等等，我们可以在代码仓库的根目录下创建一个名为.gitignore的文件，然后编辑里面的内容，把不需提交的文件忽略掉！

![](https://pic2.zhimg.com/v2-329d04468f9a9dafd3973d7acbcbb13b_1440w.jpg)

接着输入要提交时忽略的文件内容即可！

![](https://pic2.zhimg.com/v2-1938f67f9bfe8687754722b891f95917_1440w.jpg)

那么我们git add.的时候，这里的文件就不会add，另外可能你会觉的commit后面写-m "xxx"很麻烦，想偷懒，但还是写上吧！输入的是本次提交的一些声明，比如自己修改了些什么！就好像写代码的时候，你偷懒不写注释，过几天你连自己写的什么鬼都不知道...

### 3.3、查看修改内容

好吧，前面我们用git add提交了整个项目到本地仓库，接下来我们改点东西，然后使用 [git status](https://zhida.zhihu.com/search?content_id=230579925&content_type=Article&match_order=1&q=git+status&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzcxMDgxODQsInEiOiJnaXQgc3RhdHVzIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MjMwNTc5OTI1LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.2E6tZ7xMzJE4z2r5kp7zLlQ3jnuHq0sNkJhxh_orlAs&zhida_source=entity) 可以查看修改的部分，比如，我们删掉MainActivity.java里的菜单的代码以及多余的菜单相关的包！

![](https://pic4.zhimg.com/v2-7b02a3049d31574bce1da76993e5efa1_1440w.jpg)

他就会提示我们哪些文件发生了改变，但是还没有提交，如果我们想看下具体更改了什么，我们可以用到 [git diff](https://zhida.zhihu.com/search?content_id=230579925&content_type=Article&match_order=1&q=git+diff&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzcxMDgxODQsInEiOiJnaXQgZGlmZiIsInpoaWRhX3NvdXJjZSI6ImVudGl0eSIsImNvbnRlbnRfaWQiOjIzMDU3OTkyNSwiY29udGVudF90eXBlIjoiQXJ0aWNsZSIsIm1hdGNoX29yZGVyIjoxLCJ6ZF90b2tlbiI6bnVsbH0.k_uvyDUP6aJ0pn5K-VaFj8hnolG1s1luumeYWJ8mUZg&zhida_source=entity) 命令，另外，按Q可以退回命令行输入！

![](https://pic3.zhimg.com/v2-df7233b005239966173ef56b8eba4dda_1440w.jpg)

### 3.4、查看提交记录

当然随着我们项目的深入，Commit的次数也会越来越多，可能你早已忘记每次提交都修改了什么内容，没事，Git帮你记着呢，使用git log即可查看历史提交信息！键入

```
git log
```

回车：

![](https://pic4.zhimg.com/v2-f7fcc499235deb47a8f76ad0a1db8a19_1440w.jpg)

我们取其中一小部分来分析：

```
commit defd8af52be5183dfceb3e5cf23f78ea47d013b0
Author: coder-pig <779878443@qq.com>
Date:   Fri Jun 19 17:00:36 2015 +0800
MainActivity Delete Menu
```

依次是：

- 此次提交对应的版本号
- 提交人：姓名 邮箱
- 提交的时间
- 提交版本修改的内容：就是我们commit -m "xxx"里的xxx

### 3.5、撤销未提交的修改

比如我们刚提交了一个版本，然后又乱七八糟地写了一堆东西，突然发现不小心误删了一些东西，然后ctrl + s保存了，这个时候是不是欲哭无泪，不过有Git，只需一个checkout命令即可撤销更改，当然是你还没add的情况，比如我们在MainActivity里随便添加一条语句，然后ctrl + s保存代码！

![](https://pic3.zhimg.com/v2-0c35d9ce5c4e627928221341db8f139a_1440w.jpg)

然后命令行键入：git diff：

![](https://pica.zhimg.com/v2-7395716d0fd1e4dd2c1e9cc0259c675a_1440w.jpg)

嗯，这里可以看到我们改的内容，我们可以回去把这句代码删掉，但是如果改的有上千行你怎么改，于是乎这个时候我们可以使用

```
git checkout src/com/jay/example/testforgit/MainActivity.java
```

然后会神奇的发现，我们新写的代码没了！duang一下就没了，不信你可以自己试试

![](https://pic3.zhimg.com/v2-6b651d7448d6c7b908f433c602afb384_1440w.jpg)

当然，如果我们已经add了的话，那么checkout是没任何作用的，我们要先取消添加才可以撤回提交，使用下述指令：

```
git reset HEAD src/com/jay/example/testforgit/MainActivity.java
git checkout src/com/jay/example/testforgit/MainActivity.java
```
![](https://pica.zhimg.com/v2-d29f682d22ada44fcf2828c7d717551a_1440w.jpg)

### 3.6、版本回退

第五点我们教了大家撤销未提交的修改，但加入提交了，我们想回退到之前的某一个版本怎么办?第四点中我们可以通过git log查看我们的提交记录，我们需要从这里获取一个版本号，一般我们只需要前七位字符就够了；另外在Git中，用 **HEAD** 代表当前版本，上一个版本就是 **HEAD^** ，再上一个版本就是 **HEAD^^** 依次类推！我们先Git Log看下版本历史先！

![](https://pic4.zhimg.com/v2-d3cb7f278e50d345de0502d5ba0d30d7_1440w.jpg)

我们回到前一个提交的版本吧，依次键入下述指令：

```
git reset --hard HEAD
 git reset --hard HEAD^
 git log
```

这时看下我们的控制台：

![](https://pic2.zhimg.com/v2-cca1114b9a5918e4b8846cafc0eaa023_1440w.jpg)

可以看到我们已经回退到了前一个版本了，当然你可以直接这样写：

```
git reset --hard ad2080c
```

就是这么简单！回退后，你突然后悔了，想回退回新的那个版本，可是遗憾的是，你键入git log却发现没有了最新的那个版本号，这怎么办呢...没事，Git中给你提供了这颗"后悔药"，Git记录着你输入的每一条指令呢！键入：

```
git reflog
```

你会发现，版本号就在这里：

![](https://pica.zhimg.com/v2-0d8d737adadb280fd09a740ff02905f2_1440w.jpg)

然后键入：

```
git reset --hard ad2080c
```

可以看到我们又回到了最新的那个版本了，就是这么溜！

![](https://pic4.zhimg.com/v2-febc0d2f56c12aacd340a73be2f73647_1440w.jpg)

发布于 2023-07-02 21:02・四川