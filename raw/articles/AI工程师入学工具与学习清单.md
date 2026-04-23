

AI 工程师入学：工具与学习清单  
适用：课题组研究生（入学初）(陈科明 课题组） 目标：建立统一工具习惯，为后续工程与科研打地基。 说明：下列第 1 项涉及网络访问，请遵守国家法律法规与学校、课题组相关规定，仅用于学习与技术文档访问等正当用途。  

1. 科学上网与 Clash（优先完成）  
控制台链接： [https://sakuracat-1.com/dashboard](https://sakuracat-1.com/dashboard)  
要求：  
●在服务商页面完成注册、选购套餐、获取订阅。  
●Windows 推荐：Clash Verge（或服务商文档指定的 Clash 系客户端）；按说明导入订阅、选择节点、开启系统代理。  
●关闭代理后若浏览器报错 ERR_PROXY_CONNECTION_FAILED，需关闭系统代理或重置 WinHTTP（见课题组常见问题说明）。  
详细图文步骤（购买、下载、一键导入 Clash 等）： 见同目录下的 [科学上网配置说明.md](https://thingcom.yuque.com/hhbmft/te650k/%E7%A7%91%E5%AD%A6%E4%B8%8A%E7%BD%91%E9%85%8D%E7%BD%AE%E8%AF%B4%E6%98%8E.md)。  

2. NotebookLM 与 Obsidian  

|   |   |   |
|---|---|---|
|工具|用途（建议）|最低要求|
|NotebookLM|针对上传的 PDF/文档做摘要、问答、学习笔记；适合读论文、读手册。|能上传一份课程/论文 PDF，生成笔记并试一次追问。|
|Obsidian|本地知识库、双向链接、长期沉淀；可与文件夹同步方案配合使用。|建一个库，用文件夹分类；至少会新建笔记、搜索、插链接。|

习惯： 重要资料不要只放在浏览器收藏夹；Obsidian 或仓库里的 Markdown 各有一份更好。  

3. 安装与使用 Cursor  
●安装：从官网下载安装 [Cursor](https://cursor.com/)，用常用邮箱登录。  
●会用：打开文件夹作为工作区；Chat 与 Agent/Composer 的区别；能根据提示运行终端命令时，注意 审批提示 与 勿把 API Key 写入仓库。  
●与第 4 项结合：在 Cursor 里直接编辑 .md、.py，养成「可复现」的小项目结构。  

4. Markdown（.md）与材料保存  
要掌握：  
●标题层级（#～###）、列表、代码块、链接、图片、引用。  
●材料、会议纪要、周报、读书笔记优先用 .md 保存，便于 Git 与版本管理。  
推荐练习： 为本清单每一项写 5 行学习记录，放在一个 notes/ 目录里。  

5. Python 学习  
阶段目标（入学第一学期可参考）：  
●环境：Python 3.10+，会用 venv 虚拟环境；会 pip install。  
●语法：变量、控制流、函数、文件读写、简单 json/csv 处理。  
●工程习惯：requirements.txt、简单 README.md、脚本可从命令行运行。  
与 AI 结合： 用 Cursor 写小脚本时，自己运行并看懂输出；把「模型写的代码」当作初稿，必须能解释每一行在干什么。  

6. 大模型：多试用、会比较  
建议在合规前提下，至少亲自注册并试用下列几类（名称以各平台最新为准）：  

|   |   |   |
|---|---|---|
|系列|常见入口（示例）|建议体验|
|GPT|OpenAI / 合规渠道|长对话、工具调用、代码生成。|
|Claude|Anthropic / 合规渠道|长文阅读、代码与结构化输出。|
|Gemini|Google AI|多模态、与 Google 生态联动（视账号与地区而定）。|
|Kimi|月之暗面 Kimi|长上下文、中文资料。|
|Qwen|通义千问等|中文与开源生态、国内 API。|

工程意识：  
●对比同一任务（例如「解释一段 Python」「写单元测试」），记录哪家更稳、谁更爱编故事（幻觉）。  
●保密：课题数据、未公开论文、企业敏感信息，默认不进公网模型；确需使用时须按课题组规定脱敏或经导师同意。  

7. 电子书与公版书资源（站点备忘）  
以下站点多用于检索 PDF/公版书/免费读本，域名与可用性可能变化，请自行甄别。请遵守著作权与学校、课题组对资料使用的规定；优先使用作者/出版社开放获取与公版资源（如 Project Gutenberg、Standard Ebooks）。  

|   |   |
|---|---|
|说明|链接|
|Z-Library 镜像（之一）|[z-library.sk](https://z-library.sk/)|
|免费电子书聚合|[manybooks.net](https://manybooks.net/)|
|PDF 检索（注意版权）|[pdfdrive.com](https://www.pdfdrive.com/)|
|PDF 检索（注意版权）|[pdfcoffee.com](https://pdfcoffee.com/)|
|PDF 检索（注意版权）|[pdfroom.com](https://pdfroom.com/)|
|公版书（英文经典）|[gutenberg.org](https://www.gutenberg.org/)|
|开放图书馆目录|[openlibrary.org](https://openlibrary.org/)|
|公版书精排版（EPUB 等）|[standardebooks.org](https://standardebooks.org/)|

习惯： 技术书尽量买正版或图书馆借阅；下载文件先杀毒再打开；重要书目在 Obsidian 里记 书名、版本、获取方式，方便写文献与复盘。  

8. Google Pro、Claude、GPT 等付费账号（补充说明）  
坊间存在通过 闲鱼 等二手平台购买「共享/代充」类 Google One / Gemini、ChatGPT Plus、Claude Pro 等账号或服务的现象。  
课题组建议：  
●优先使用各平台 官网订阅、教育优惠、官方 API 按量计费  
●二手平台购买存在 违反平台用户协议、账号被封、诈骗与隐私泄露 等风险；  

9. OpenRouter（聚合 API 与免费模型）  
●OpenRouter（[openrouter.ai](https://openrouter.ai/)）提供多家模型的 统一 API 入口，页面上会标注部分模型的 免费额度或低价试用；适合练手「换模型、比输出」而不必先为每家单独开号。  
●注意： 仍须注册并妥善保管 API Key，勿提交到 Git；调用前阅读各模型提供方的 使用条款与数据策略。  

10. 多看社区：Reddit、知乎与拓展信源  
社区帖子 不等于 论文或官方文档，但能帮助你知道「大家在用什么工具、踩过什么坑」。请养成 交叉验证 习惯：同一结论至少对照 官方文档、发行说明或可追溯来源。  

你已熟悉的  

|   |   |
|---|---|
|类型|说明|
|Reddit|英文实时讨论多；可按话题进 Subreddit（见下表）。|
|知乎|中文长文与行业视角多；注意甄别营销与过时回答，看 发布时间 与 评论区纠偏。|

Reddit 入门可逛（示例）  

|   |   |
|---|---|
|Subreddit|大致内容|
|[r/MachineLearning](https://www.reddit.com/r/MachineLearning/)|论文讨论、研究向动态（偏学术）|
|[r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/)|本地大模型、量化、推理框架|
|[r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/) / [r/OpenAI](https://www.reddit.com/r/OpenAI/)|产品使用与生态|
|[r/programming](https://www.reddit.com/r/programming/)|泛编程新闻与讨论|
|[r/learnpython](https://www.reddit.com/r/learnpython/)|Python 入门互助|

导师补充推荐（可与 Reddit/知乎对照着看）  

|   |   |
|---|---|
|站点|特点|
|[Hacker News](https://news.ycombinator.com/)|科技创业与工程热点，评论区常有高质量技术补充。|
|[V2EX](https://www.v2ex.com/)|中文程序员社区，节点分明，适合看工具与职场讨论。|
|[掘金](https://juejin.cn/)|中文技术文章与教程较多，适合前端/工程向检索。|
|[Lobsters](https://lobste.rs/)|偏链接聚合，质量门槛相对较高（需邀请注册，可读公开页）。|
|[Stack Overflow](https://stackoverflow.com/)|具体问题优先搜；错误信息 + 关键词 往往比泛泛提问有效。|
|[少数派](https://sspai.com/)|效率工具、软件与工作流，偏「把工具用顺」。|

X（Twitter）偏工程：可关注类型与示例账号  
X 上信息极碎、节奏快，适合跟 发版说明、安全公告、会议幻灯链接；不适合替代文档。建议用 列表（Lists） 把下面几类分开关注，避免时间线被无关热点淹没。  
1）平台、云与开发者工具（官方）  

|   |   |
|---|---|
|账号|备注|
|[@GitHub](https://x.com/github)|产品更新、安全通告、Universe 等|
|[@vercel](https://x.com/vercel)|前端部署、Edge、框架生态|
|[@cursor_ai](https://x.com/cursor_ai)|Cursor 编辑器相关动态|
|[@Docker](https://x.com/docker)|容器与镜像生态|
|[@Cloudflare](https://x.com/cloudflare)|网络、Workers、安全与性能|
|[@flydotio](https://x.com/flydotio)|边缘部署与应用运行|

2）AI / ML 工程（官方与强相关）  

|   |   |
|---|---|
|账号|备注|
|[@AnthropicAI](https://x.com/AnthropicAI)|Claude 与 API 公告|
|[@OpenAI](https://x.com/OpenAI)|模型与开发者产品动态|
|[@huggingface](https://x.com/huggingface)|模型、数据集、推理与开源工具|
|[@GoogleDeepMind](https://x.com/GoogleDeepMind)|研究进展（偏研究，但发版与博客常值得扫一眼）|
|[@PyTorch](https://x.com/PyTorch)|训练/部署栈更新|

3）语言与运行时（官方）  

|   |   |
|---|---|
|账号|备注|
|[@rustlang](https://x.com/rustlang)|Rust 发版与基金会|
|[@golang](https://x.com/golang)|Go 语言与工具链|
|[@nodejs](https://x.com/nodejs)|Node.js LTS 与生态|
|[@deno_land](https://x.com/deno_land)|Deno 运行时|

4）工程实践与架构（个人向，择一二即可，勿当权威）  

|   |   |
|---|---|
|账号|备注|
|[@rauchg](https://x.com/rauchg)|Vercel / 前端与基础设施观点|
|[@kelseyhightower](https://x.com/kelseyhightower)|云原生与工程文化|
|[@ThePrimeagen](https://x.com/ThePrimeagen)|工程实践与工具链（风格鲜明，按需关注）|

中文技术向（可选）： 如 [@dotey](https://x.com/dotey)（宝玉）等，多讨论 AI 产品与提示工程，可与英文官方账号对照。  
说明： 账号可能改名、停更或被限流；推文不等于文档，重要参数以官网与 API 文档为准。  

Discord：偏工程的官方/大型社区（从落地页进入）  
Discord 邀请链接会过期，请优先从 各项目官网页脚或文档「Community / Discord」 进入；下表为 相对稳定落地页（若打不开，以官网最新入口为准）。  

|   |   |
|---|---|
|社区|建议入口（工程向用途）|
|Python|[Python Discord 官网](https://pythondiscord.com/) — 语言互助、作业级问题可搜频道历史|
|Rust|[Rust 社区页](https://www.rust-lang.org/community) — 从官方链接进 Discord，适合系统与性能向|
|Node.js|[Node.js Get Involved](https://nodejs.org/en/about/get-involved) — 运行时与包生态讨论|
|Hugging Face|[加入 Hugging Face Discord](https://huggingface.co/join/discord) — 模型、推理、数据集与开源协作|
|Vercel|[Vercel 社区说明](https://vercel.com/discord)（或官网页脚 Discord）— 部署、Next.js、边缘函数|
|Discord 开发者|[Discord 开发者门户](https://discord.com/developers) — 若做 Bot、Webhook、OAuth 等再深入相关官方服务器|

习惯： 在 Discord 提问前先看 频道置顶与 #rules；尽量带 环境版本、最小复现、报错全文。可与 Reddit/知乎/X 的信息 交叉验证。  

11. 推荐书籍与长文（职业视野 + 工程打底）  
下列为拓展阅读，用于建立路径感与行业语境，不是课程指定教材；具体以教务、导师与课题组要求为准。技术书优先图书馆借阅或正版渠道；长文以作者官网、arXiv、会议博客为准。  

职业发展与求职心智（建议优先）  

|   |   |
|---|---|
|资源|说明|
|Andrew Ng, How to Build Your Career in AI（吴恩达《如何在 AI 领域发展职业》）|英文短篇电子书：技能积累、项目组合、求职与社区参与等非技术性建议，适合入学初通读一遍。官方获取页：[DeepLearning.AI — How to Build Your Career in AI](https://info.deeplearning.ai/how-to-build-a-career-in-ai-book)（页面说明为免费下载，按站点流程填写信息即可）。|

经典短文与趋势讨论（偏「为什么」）  

|   |   |
|---|---|
|资源|说明|
|Richard Sutton, The Bitter Lesson|讨论「规模化学习与算力」的历史规律，偏研究视角，有助于理解产业叙事，但不是工程操作手册。[原文](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)|
|Joseph Rocca, Understanding Deep Learning 系列（Towards Data Science 等）|网上有多篇可视化向入门长文，适合配合课程建立直觉（检索作者名 + 主题即可，注意文章年份）。|

机器学习与深度学习（教材与手册）  

|   |   |
|---|---|
|资源|说明|
|Aurélien Géron, Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow|工程向入门：传统 ML + 深度学习，配套代码，适合作为动手主线之一。|
|李沐等《动手学深度学习》|中文教材 + 代码，可与视频/课程对照。[项目与电子版](https://zh.d2l.ai/)|
|Ian Goodfellow 等《Deep Learning》（花书）|理论参考与系统梳理，适合查阅章节，不必从头到尾啃完。|

大模型与系统方向（入学后按需）  

|   |   |
|---|---|
|资源|说明|
|Jay Alammar, The Illustrated Transformer 等图解长文|图解 Transformer/注意力等概念，适合读论文前的直觉铺垫。[博客入口](https://jalammar.github.io/)|
|Chip Huyen 博客（如 Architecting LLM Applications 等）|偏 ML/LLM 产品与系统实践，文章会更新，读时留意发布时间。[站点](https://huyenchip.com/)|
|Eugene Yan 博客|机器学习工程化、部署与职业向文章较多，可作「工程师视角」补充。[站点](https://eugeneyan.com/)|

习惯： 每读完一本书或一篇长文，在 Obsidian 里记 一句 takeaway + 是否值得推荐给师弟师妹，避免只收藏不消化。  

修订记录  

|   |   |
|---|---|
|日期|说明|
|2026-04-14|新增「11. 推荐书籍与长文」：含吴恩达 How to Build Your Career in AI、经典短文与 ML/LLM 工程向延伸阅读。|
|2026-04-11|初稿；补充电子书站点（含 Gutenberg/Open Library/Standard Ebooks 等）、闲鱼购号风险提示、OpenRouter 免费模型说明；验收项可选扩展。|