[收录于 · CodeLab-编程学习](https://www.zhihu.com/column/c_1284881096879484928)

158 人赞同了该文章

为了保证最佳阅读效果，推荐大家 [在此](https://link.zhihu.com/?target=https%3A//4bashguide.codelab.club/) 阅读这四篇指南。

## 开篇

**[Bash](https://zhida.zhihu.com/search?content_id=161029569&content_type=Article&match_order=1&q=Bash&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzcwOTMxNjcsInEiOiJCYXNoIiwiemhpZGFfc291cmNlIjoiZW50aXR5IiwiY29udGVudF9pZCI6MTYxMDI5NTY5LCJjb250ZW50X3R5cGUiOiJBcnRpY2xlIiwibWF0Y2hfb3JkZXIiOjEsInpkX3Rva2VuIjpudWxsfQ.Ofvlgs3t_dSYob2JDYo8dvei9EAkT-KrYhqY02m7gUU&zhida_source=entity) 是什么，它活在哪里？**

简介 Bash，以及如何安装和启动它；终端，键盘及结果显示；程序，进程以及他们内部 [流](https://zhida.zhihu.com/search?content_id=161029569&content_type=Article&match_order=1&q=%E6%B5%81&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzcwOTMxNjcsInEiOiLmtYEiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoxNjEwMjk1NjksImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.RBpbcPHehc3NHUGB1dLNg0BFS7rkSplnQuFD4cn7Vis&zhida_source=entity) 动的信息如何被连接在一起

---

## Bash 是什么，我为什么会需要它？

欢迎来到 Bash 指南。既然已开始阅读，想必关于 Bash 是什么以及用它来干什么，其实你心中已有模糊的想法了。

如果你对 Bash 有一定的认识，在继续向下阅读之前，我想先劝你试着忘记所有那些你已知的东西。围绕 Bash、它的语法还有它在你电脑系统中的位置，有太多错误信息浮荡在我们四周。如果你能抹除先前的经验，以白板状态重新开始，这份 Bash 指南的效果就能发挥至最大。

### 那么 Bash 到底是什么呢？

长话短说：Bash 也是一种跑在你电脑里的 *程序* (program)，但它的设计使你能轻松地与之“对话”(talk)。

在你电脑里的每个程序都能做很多不同的事：读取文档、启动其他程序、数学运算、控制设备。Bash 这个程序，与他们最大的不同在于，它并不执行某种特定的任务，而是听从你这个用户的命令。为此，一种“语言”被特意创造出来，使你可以与 Bash 对话，告诉它该做什么。这种语言就是 Bash shell 语言，你之后会与它熟悉亲近起来。

*Shell* 这类程序，本质上是为你提供一个与其他程序交互的界面(interface)。这类程序数量也非常多，每一个都有它自己配套使用的语言，如其中比较流行的 *C shell (csh)* 、 *Z shell (zsh)* 、 *Korn shell (ksh)* 、 *Bourne shell* 、 *Almquist shell (dash)* 等。目前最主流的就是 Bash (也作 Bourne Again shell) 。需留意，所有这些 shell 使用的语法看起来都很相似，当你实际写代码输入命令时，一定要清楚自己当前正在使用哪种 shell。之后，你可能会经常听到人们用“shell 代码”称呼他们所写的代码，而这种表达的笼统含糊就相当于用“源码”指代你具体的 Java 代码。这份指南要教你的是如何写 bash shell 代码，它也仅适用于 bash 这种 shell。

> **Bash 是一种 [Shell 程序](https://zhida.zhihu.com/search?content_id=161029569&content_type=Article&match_order=1&q=Shell+%E7%A8%8B%E5%BA%8F&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzcwOTMxNjcsInEiOiJTaGVsbCDnqIvluo8iLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoxNjEwMjk1NjksImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.VwAP1F5ykgRt2GCFOT2B11dWiDvcElQai2kiVzmDNyM&zhida_source=entity) ，它被设计用来听从我的命令，做我让它做的事**

### 那我用它做什么呢？

你们多数人都有丰富的电脑操作经验，通过使用鼠标和键盘与各种程序交互，十之八九，这些操作都发生在一个由按钮、组件、文本框、图片等构成的视觉界面中。这就是 [图形用户界面](https://zhida.zhihu.com/search?content_id=161029569&content_type=Article&match_order=1&q=%E5%9B%BE%E5%BD%A2%E7%94%A8%E6%88%B7%E7%95%8C%E9%9D%A2&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzcwOTMxNjcsInEiOiLlm77lvaLnlKjmiLfnlYzpnaIiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoxNjEwMjk1NjksImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.PKaEsIrW9u5SAGWczllVy2tII9ETKlkFMInj_VQz7PU&zhida_source=entity) (graphical user interface, GUI)，其俨然已成为绝大多数人与电脑交互方式的核心。

但是，除此之外还有其他与电脑交互的方式。Bash 采用的方法就与图形用户界面的概念完全相对：它运行在一个只支持文本的“控制台” (console)内，在这里，交互主要指显示在你屏幕上的字符以及读取你从键盘上输入的字符。如果你尚不熟悉这种交互环境，就会觉得非常怪异、原始、受限。

其实并非如此。基于文本的交互界面在信息呈现上确实相对受限（它显然不适合呈现图片），但这种简洁性使我们更容易在信息中发现稳定一致的结构，无论是界面中显示的文本还是我们自己发出的命令。你会发现，那些最熟练的计算机用户使用基于文本的界面，执行相同任务时，对比图形界面，效率高的惊人。你也很快就会了解，bash shell 语言的简洁性正是关键所在。

那么你用 bash 做什么呢？你会使用它查出计算机内都存放了哪些文件，文件里又是什么内容。你会使用它来运行别的程序，这些程序可以对计算机作出各种改变：从编辑文件和图片到转化他们，从移动、复制文件到创建自动备份，从下载新程序的源码到编译、运行他们。若你为此而感到兴奋的话，请先别激动，一定要记住 **bash 是一种工具** ，而且只是程序工具箱内的一种。仅 Bash 自己只能帮你对文件或其他程序做一些基本操作，你还需要理解系统工具箱内的其他所有工具。这部分知识很多，学习起来不会很快，你一定要付出时间把他们学好，而不是对所有工具了解个大概后明天就把腿摔断（或更可能发生的，毁了你电脑内的音乐或家庭照片收藏）。

> **Bash 是庞大程序工具箱中的一种简单工具，使我通过基于文本的界面与计算机系统交互**

## 我在哪可以找到 Bash，又如何使用它？

我们已经知道 bash 不过是你电脑里的一个程序，随时等待你启动它并向它发出操作指令。我们也已知道与 bash 的交互通常发生在一个基于文本的界面内，在这里，你使用 bash shell 语言编写你要“说”的命令，其他程序的输出内容或运行结果也以文本形式呈现反馈给你。

在我们深入 Bash 之前，先站稳脚跟。你需要理解： bash 通常呆在哪儿，如何激活它，所处的环境是什么，能力的边界在哪儿，当根据你的指令执行任务时可以召唤哪些朋友过来帮忙。

### 我在哪可以找到 Bash？我要如何开始使用它？

如果你的操作系统自带 bash，你就会发现它是一个简单可执行的程序，存放在系统的标准二进制文件路径下。二进制文件是一种可执行程序，其中包含有操作系统内核可以直接执行的二进制代码 (binary code)。如果你当前使用的操作系统没有默认安装 bash，如 FreeBSD 或 Windows 系统，你就需要从分发平台上下载安装，或是取得源码后自己编译二进制文件。FreeBSD 用户可以使用 [ports](https://link.zhihu.com/?target=https%3A//www.freebsd.org/doc/handbook/ports-using.html) ，Windows 用户可以使用 [cygwin](https://link.zhihu.com/?target=https%3A//www.cygwin.com/) ，也有其他发行版。源码可以从 [GNU.org](https://link.zhihu.com/?target=https%3A//ftp.gnu.org/gnu/bash/) 官网上下载。如果以上方法都不适用，请借助互联网的力量找到安装 bash 的有效方法。

> **如果你倾向于在另一台远程电脑上实验 bash shell, 或是当前无法在自己的电脑上安装 bash，那你可能会对远程 shell 服务感兴趣，如 [The Super Dimension Fortress (SDF)](https://link.zhihu.com/?target=https%3A//sdf.org/)**

bash 安装就绪后，我们可以运行二进制文件启动它。在启动之前，需要特别注意 bash shell 支持以下两种不同的操作模式：

***交互模式***

交互模式下，bash shell 会等待你发出命令然后再执行他们。Bash 会执行你的每一条命令，且在它执行这条命令的期间，你将无法和 bash shell 交互。一旦它执行完这条命令，你就可以继续向它发出你的下一条指令。

***非交互模式***

bash shell 也可以执行脚本。所谓脚本，就是提前写好的一系列指令，bash 可以直接执行它们而无需停下来询问你下一步要做什么。脚本通常以文件形式保存，多用来自动化执行各种任务。

除了 bash 执行的命令来源不同，这两种模式非常相似。现在基本可以这样总结：如果 bash 等待你给出执行任务的指令，你就处于交互模式中；如果它执行的是存在某文件中的指令，那它就是在非交互模式下运行一个脚本。

还要记得，bash 程序通常都运行在基于文本的界面中。因为它没有可供你与之交互的图形界面，这就意味着，如果你现在正处于某图形界面中，那在与 bash 开始任何有意义的互动之前，你首先需要打开一个基于文本的界面，标准方式就是打开 ***终端*** (terminal)。过去，终端是我们连接电脑并与电脑交互所需的硬件设备。当下，绝大多数终端都是“模拟性的”。也就是说，他们都是运行在你电脑中的程序，无论是图形还是文本性的，他们以软件的形式“模拟”曾经实体的终端，提供一个文本性的界面供你使用。 [终端模拟器](https://zhida.zhihu.com/search?content_id=161029569&content_type=Article&match_order=1&q=%E7%BB%88%E7%AB%AF%E6%A8%A1%E6%8B%9F%E5%99%A8&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzcwOTMxNjcsInEiOiLnu4jnq6_mqKHmi5_lmagiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoxNjEwMjk1NjksImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.TP8EfKosZ98A2NF0u6W3ph5oFcIYCKHjLkel8ZxQtkw&zhida_source=entity) 有很多种，具体哪些可用取决于你当前电脑的操作系统。Linux 与 BSD 用户可以使用 **[rxvt](https://link.zhihu.com/?target=https%3A//sourceforge.net/projects/rxvt/)** ， **[xterm](https://link.zhihu.com/?target=https%3A//invisible-island.net/xterm/)** ， **[gnome terminal](https://link.zhihu.com/?target=https%3A//help.gnome.org/users/gnome-terminal/stable/)** ，或 **[konsole](https://link.zhihu.com/?target=https%3A//konsole.kde.org/)** 。IOS 用户可能使用 **[Terminal](https://link.zhihu.com/?target=https%3A//en.wikipedia.org/wiki/Terminal_%28macOS%29)** 或 **[iTerm 2](https://link.zhihu.com/?target=https%3A//www.iterm2.com/%23/section/home)** 。Windows 用户可以使用 **[cmd.exe](https://link.zhihu.com/?target=https%3A//en.wikipedia.org/wiki/Cmd.exe)**,**[Console 2](https://link.zhihu.com/?target=https%3A//sourceforge.net/projects/console/)** 或 **[mintty](https://link.zhihu.com/?target=https%3A//code.google.com/archive/p/mintty/)** 。总之，每一种操作系统都有很多适用的选择。找出你喜欢的一种，安装并启动，然后继续阅读。

现在让我们 bash 起来！

首先，打开你的终端或终端模拟器，确认自己处于基于文本的界面中。一旦你进入这样的界面，就需要找到一种运行程序的方式。就像在不同的图形界面中有不同的启动程序的方式， [文本界面](https://zhida.zhihu.com/search?content_id=161029569&content_type=Article&match_order=1&q=%E6%96%87%E6%9C%AC%E7%95%8C%E9%9D%A2&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzcwOTMxNjcsInEiOiLmlofmnKznlYzpnaIiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoxNjEwMjk1NjksImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.w8UhyGL6eMniy6ZvcPQs7kWx7EJ11YHoHir-VkF4sqg&zhida_source=entity) 中也是如此。好在，绝大多数终端都被设置为打开后自动启动 shell 程序。还记得 bash 就是一种 shell 程序吗？所以通常，当你的终端启动时，bash 也已经同时运行其中了。但有些终端并非这样，一些操作系统默认选用的 shell 程序可能是 `cmd.exe` ， `sh` ， `dash` ， `csh` 或 `zsh` 。所有这些 shell 程序都不是 `bash` ，本教程也不会涉及他们的使用（如果你需要了解其他这些 shell，还是建议你借助互联网的力量自行搜索）。为了查看你当前终端运行的是否是 bash shell，现在让我们来输入 **第一条 bash 命令** ！

```
echo "$BASH_VERSION"
```

备注：既然已输入第一组 shell 代码，让我们花点时间来说明一下这篇指南使用的语法。所有的代码会如此 `标注` 。如果是像上方那样一组代码，我们会同时显示你在终端内输入的命令以及返回的输出结果。我们还会区分你输入的文本以及终端本身显示的文本，你键入的文本会 `这样标识` （即文本下方有虚线下划线）。而且，需要你输入的文本通过 `单击它` 就能轻易选中。看上方的代码组块，现在你就会明白那个 `$` 符号并非你要输入的文本，它代表命令提示符，当 shell 等待你输入命令时，它就会出现在终端内，而你终端内实际提示符的样子可能会与这个不同。在命令提示符那里，你输入以下文本： `echo "$BASH_VERSION"` ，然后单击回车确认。在你按下回车确认这条指令后，bash shell 立即就会执行它，并将结果返回显示在下一行 (实际返回的版本号可能与此有别)。

如果输入以上命令后没有返回任何结果或错误信息（假设你的输入完全正确），那说明你的终端很可能运行的不是 bash shell。你需要手动启动 bash shell，然后再输入上面的命令试试看。在绝大多数 shell 中，启动 bash 仅仅需要执行 `bash` 命令。如果 bash 仍没有启动，你就需要去查阅系统、终端或是 shell 文档了，或是借助互联网的力量找出如何在你的终端内运行 bash shell。

如果你觉得还没有完全理解上面那条命令是如何工作的，不要担心。在后面的章节里，我们会逐渐深入 bash 命令。在那之前，你会时不时看到一些简单的代码，他们都很直白，要做的事也不难理解。现在，不用担心。bash shell 语言的一个优点就是它简短的语句相对容易理解。

> **bash shell 是一个二进制程序，通常运行在由终端模拟器提供的基于文本的界面中，有交互式或非交互式两种运行方式**

### 这里是怎么一回事？文本，终端，bash，程序，输入，输出！

在上一部分接近尾声的时候，你或许留意到我们提速了一点。可能因速度加快（或其他什么）你还觉得有些晕，我们现在就退后一步，从整体上对所有这一切形成一个清晰的图景。取决于你对这些内容的熟悉程度，这里也许有不少新概念。即使你对他们并非全然陌生，也可能并不清楚该以怎样的框架组织他们的关系。如果你想完全理解运行代码时计算机内究竟发生了什么，理解这些不同概念间的关系就至关重要。

![](https://pic1.zhimg.com/v2-2ad2d579c86e6760ca4d3126fe1068b2_1440w.jpg)

当你在图形用户界面中打开一个终端模拟程序时，就会看到一个带有文本内容的窗口弹出。这个窗口内呈现的文本，既有终端里程序运行后输出的结果，还有你通过键盘向这些程序输入的指令。bash 程序只是运行在终端内的众多程序中的一个，所以要记住 *并不是 bash 使文本呈现在你的屏幕上* 。是终端在负责这项工作，它从 bash 那里获得文本内容并将它呈现在窗口中给你看。终端也会为其他运行在它内部的程序做这项工作，如邮件程序或 IRC 客户端，这与 bash 没一点关系。

![](https://pic4.zhimg.com/v2-ffa3cea8086a5544faf35b462d1a7e11_1440w.jpg)

有时候，终端里正在运行什么程序并不好判断。在上面这个例子中，你通过键盘输入的文本，经一长串的程序，最终抵达目的地（运行在另一台 IP 地址为 `192.168.1.1` 的电脑里的 `mail` 程序）。

在此我不会展开解释这些程序，这里的关键点是终端内的程序都是相互连通(inter-connect)、协同工作的。因为关于当前正在发生什么，并没有太多视觉上的提示，所以关于他们什么时候启动、连通、终止，你自己对此要逐渐形成清楚的认识。这样你就会理解，在基于文本的用户界面中，向各种程序输入指令或是接收他们返回的结果，是怎么一回事。

简单地说，上面这个例子使用 `bash` 程序运行 `ssh` 程序，从而与另一台电脑建立连接。在另外那台电脑上，一个新的 `bash` shell 会被启动，它的输入与输出通过两台电脑间的连接往返。接下来我们在远端电脑的 bash 中运行 `screen` 程序，这是一个 `终端复用器` 。这种程序可以在一个基于文本的终端内，模拟多个终端，他们共用同一终端显示 (使用热建来回切换显示当前活跃的终端，或是用分屏同时呈现所有终端)。 `screen` 程序又会在它的某个模拟终端内启动一个 `bash` shell。在这第三个 bash shell 中，我们运行 `mail` 程序，输入想通过邮件发送的内容。

注：需要说明的是我们这里使用的“文本” (text)，在计算机世界中，更通常的叫法是“字符串” (string)。顾名思义，就是一长串字符。一个名称，如 `Leonard Cohen` 就是一个字符串，一首长诗也是一个字符串，只不过更长，包含更多行的文本。之后，每当我们使用 *字符串* 这个概念时，请记住我们谈论的其实就是任一种文本而已。

> **在终端内，许多基于终端的程序可以同时运行，连成长串，你输入的命令与他们输出的结果就在其中往返流动。**

### 那么程序到底是什么？它又如何与其他程序连通？

之所以要回答以上两个问题，一方面，程序到底是什么，乍一想似乎很清楚，但仔细想一下，可能多数人又无从回答。另一方面，在这份指南中，至少在我们关心的主题域内，我会竭力避免出现未加解释的概念，如程序之间如何“连通” (connect)的问题。

简言之，程序就是你的操作系统内核可以执行的、已提前编写好的指令集合。程序会直接对内核下指令。本质上，内核也是一个程序，只不过它会持续运行并负责与你的硬件交互。

![](https://pica.zhimg.com/v2-b7b0c31b38baefda1e887b634d91efd0_1440w.jpg)

程序通常都呆在你的磁盘里，等待着被启动。当你运行(run 或 execute)某个程序时，你的系统内核会为它创建一个进程 (process)来加载已提前编写好的指令（即代码）。我们在前面已简单提及，你的程序可以同时运行多次，每一个实例都是这个程序运行着的进程。如果把程序比做巧克力蛋糕食谱，那么你烘焙蛋糕的过程就是程序的进程。进程将你程序中的指令传递给内核。同时，进程使用一些被称作 *[文件描述符](https://zhida.zhihu.com/search?content_id=161029569&content_type=Article&match_order=1&q=%E6%96%87%E4%BB%B6%E6%8F%8F%E8%BF%B0%E7%AC%A6&zd_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ6aGlkYV9zZXJ2ZXIiLCJleHAiOjE3NzcwOTMxNjcsInEiOiLmlofku7bmj4_ov7DnrKYiLCJ6aGlkYV9zb3VyY2UiOiJlbnRpdHkiLCJjb250ZW50X2lkIjoxNjEwMjk1NjksImNvbnRlbnRfdHlwZSI6IkFydGljbGUiLCJtYXRjaF9vcmRlciI6MSwiemRfdG9rZW4iOm51bGx9.iEiAE2OrWZu7hOFBQVLna5RD1kVPR4TqcjlpH9PRpYk&zhida_source=entity) (file descriptors)* 的挂钩 (hooks) 与外界连通,他们本质上就是连接这个进程与其他文件、设备或进程的插件 (plug)。虽然大多数巧克力蛋糕食谱没有，但有些食谱可能会包含这样一份表格，例如根据蛋糕供应的需求量查询所需原料的用量。参照这样的食谱，产出量会随投入量的变化而变化。文件描述符都是用数字标识，但最前面的三个有标准的名字：

***标准输入 (standard input)***

***文件描述符 0*** 也被称作 *标准输入* 。绝大多数进程都从这里接收他们的输入。默认地，你终端内的进程都将他们的标准输入与你的键盘连接，更具体地说，是与你终端程序接收到的输入连接。

***标准输出 (standard output)***

***文件描述符 1*** 也被称作 *标准输出* 。绝大多数的进程将他们的输出发送至此。默认地，你终端内的进程都将他们的输出与你的显示器相连，更具体地说，是你的终端程序会把他们的输出显示在终端窗口中。

***标准错误输出(standard error)***

***文件描述符 2*** 也被称作 *标准错误输出* 。绝大多数的进程将他们的错误信息输出至此。默认地，你终端内的进程都将它与你的显示器相连，正如 *标准输出* 。一定要明白，标准错误输出只是另一个插件 (plug)。它也不仅限于输出错误信息，实际上，bash 会把它用在绝大多数的信息消息中， *包括你的终端提示符！*

除以上这三种文件描述符外，进程还可以根据需要用自身编号创建新的文件描述符，并把他们与其他文件、设备或进程相连。

如果一个程序需要把它的输出发送到另一个程序的输入，而不是发至你的显示器，这个程序就会命令内核把它的标准输出与另一个程序的标准输入连通。如此一来，所有发送至标准输出文件描述符的信息都会流向另一个程序的标准输入文件描述符。信息在文件、设备和进程间的这种流动被称作 *流 (stream)* 。

流指的就是在一个运行着的系统中，信息（更具体地， *字节 (bytes)* ）通过连接 (links) 在文件、设备和进程中的流动。流可以携带任何类型的字节信息，接收端则必须按照发送顺序吸收这些字节。假设我有一个程序会向另一个相连的程序输出名字，那么第二个程序只有首先读取了流中的第一个名字才能看到第二个名字是什么。读取第二个名字后，下一个就是流中的第三个名字。当程序从流中读取某个名字后，可以把它存储在某个地方以备之后所需。从流中读取某个名字就会吸收掉流中的这些字节，流会继续向前。流不会倒转，被读取后的名字也不能被再次读取。

![](https://pic4.zhimg.com/v2-cc8d996fe3cebf83816322f6130e06f1_1440w.jpg)

在上面这个例子中，两个 bash 进程通过流连接在一起。第一个 bash 进程从键盘读取它的输入，然后把输出同时发送至标准输出与标准错误输出。其中，标准错误输出与终端显示相连，而标准输出则与第二个进程相连。注意看上图中，进程一的 `FD 1` 连着进程二的 `FD 0` 。当进程二从它的标准输入读取信息时，就会吸收掉进程一的标准输出。进程二的标准输出与终端的显示相连。运行以上代码后，终端中会有如下内容显示出来：

```
Your name?
Maarten Billemont
Hello, Maarten Billemont
```

注意看，终端仅显示这些文本：与终端显示相连的命令执行结果，以及在终端内发送给程序的输入信息。

一定要理解， ***文件描述符是特定于每个进程的*** ：只有同时指明具体某个进程，提及“标准输出”才有意义。在上面例子中，你会注意到，进程一的标准输入与进程二的标准输入是不同的。你也会看到，进程一的 FD 1 (标准输出)连接的是进程二的 FD 0 (标准输入)。文件描述符并不会描述连接进程的流本身，他们描述的只是连接得以实现的进程的插件。

> **每当启动一个程序，系统就会为它创建一个运行的 *进程* 。进程都有插件，被称作 *文件描述符* ，他们使得进程可以连通流从而抵达其他文件、设备或进程。**

发布于 2020-12-03 12:34