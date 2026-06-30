# 🚀 详细操作手册 — 从零到接到第一单

---

## 第一步：注册 Upwork（15 分钟）

### 1.1 打开网站
浏览器打开：https://www.upwork.com

### 1.2 点击右上角 "Sign Up"
- 选择 "I'm a freelancer, looking for work"
- 用 Google 账号登录（你已有 jechan502@gmail.com）或直接邮箱注册

### 1.3 验证邮箱
Upwork 会发验证码到你的邮箱，去 Gmail 收件箱找到验证码填进去。

---

## 第二步：填写 Profile（照着填，一字不改也行）

### 2.1 姓名
- First Name: `Jesse`
- Last Name: `Chan`（或你的真实姓）

### 2.2 头像
找一面白墙，白天自然光，穿纯色衬衫，手机拍一张：
- 肩膀以上
- 正视镜头
- 微笑
- 背景干净
截图裁剪成正方形上传。

### 2.3 Title（职业头衔）
复制粘贴这段：
```
Python Web Scraping & Data Extraction Specialist
```

### 2.4 Overview（个人简介）
直接复制下面全部内容，粘贴到 Upwork 的 Description 框：

```
I help businesses collect and organize web data so they can make smarter decisions.

What I do:
- Web Scraping — Extract product data, pricing, leads, real estate listings, and more
- Data Cleaning — Turn messy HTML/JSON into clean CSV/Excel spreadsheets
- Automation — Automate repetitive tasks like form filling, file organization, report generation
- API Integration — Connect your app to third-party services

My toolkit: Python, Requests, BeautifulSoup, Selenium, lxml, Pandas, Regex

Recent work samples:
https://jechanoo.github.io/portfolio/

Why hire me:
- Clean, well-documented code — you can maintain it yourself later
- Fast turnaround — small projects delivered in 24-48 hours
- Clear English communication — no misunderstandings
- Free 7-day bug fix guarantee

I'm offering competitive rates to build my reputation on Upwork. 
Let's start with a small task so you can see the quality of my work risk-free.

Message me with your project details — I respond within 1 hour.
```

### 2.5 Skills（技能标签）
在 Skills 输入框依次搜索并添加（至少 10 个）：
```
Python
Web Scraping
Data Extraction
Data Mining
Automation
Selenium
BeautifulSoup
Data Processing
CSV
Excel
Web Crawler
API
Lead Generation
Scripting
Regex
```

### 2.6 Hourly Rate（时薪）
填：`$10.00/hr`（前期低价吸引客户，有 5 个好评后提到 $20+）

### 2.7 Portfolio（作品展示）
点 "Add Portfolio Item"：
- Title: `E-commerce Product Data Scraper`
- Description: `Python-based web scraper that extracts product names, prices, ratings, and availability from e-commerce websites. Handles pagination, rate limiting, and error recovery. Outputs clean CSV and JSON files.`
- URL: `https://jechanoo.github.io/portfolio/`
- Skills: 选 Python, Web Scraping, Data Extraction

### 2.8 其他设置
- English Proficiency: `Fluent`
- Education: 有就填，没有跳过
- Employment History: 有就填，没有跳过
- Other Experience: 填 `Embedded Systems (STM32, C/C++)` 如果有

点 "Submit Profile" 提交。

---

## 第三步：找单子（每天花 30 分钟）

### 3.1 搜索
Upwork 顶部搜索框输入：
```
web scraping
```
然后点 "Most Recent" 排序（不是 "Best Match"）。

### 3.2 筛选条件
左边 Filters：
- Fixed Price: $10 - $100
- Number of Proposals: Less than 5
- Client History: 不限（新客户反而竞争少）

### 3.3 选单子标准（新手友好）

✅ 优先投这些：
- "Scrape product data from X website"
- "Extract business contacts from Y directory"
- "Convert data from PDF/website to Excel"
- "Data entry" 类任务（用 Python 自动做，实际几分钟搞定）
- 搜索标题包含 "simple scrape"、"basic data"、"help with python"

❌ 跳过这些：
- 要求登录网站的（法律风险）
- 预算 < $5 的
- 描述很模糊只有一句话的
- 超过 20 个竞标的
- 要求 "fastest"、"ASAP"、"urgent" 的疯子客户

---

## 第四步：投递第一单

### 4.1 选一个单子
找到合适的后，点进去看清楚要求，确认你能做。

### 4.2 点 "Submit a Proposal"

### 4.3 Bid Amount（报价）
- 如果客户预算 $20-30 → 你报 $20
- 如果客户没有写预算 → 你报 $25
- 策略：前 5 单比别人便宜 20%，抢好评

### 4.4 Cover Letter（投递信）
直接复制下面模板，改 `[ ]` 里的内容：

```
Hi [把客户名字写在这里],

I read your job posting and I can do this.

Plan:
1. Build a Python scraper for [把客户要爬的网站写在这里]
2. Extract [客户要的数据：比如 product names, prices, ratings]
3. Deliver a clean CSV file you can open directly in Excel

To prove my quality — I'll send you a FREE SAMPLE of the first 20 rows 
before you release any payment. You only pay when satisfied.

My recent work: https://jechanoo.github.io/portfolio/

I can start right now and deliver within 24 hours.

What's the website URL? I'll send you a sample within a few hours.

Jesse
```

### 4.5 点 "Submit Proposal"

---

## 第五步：接到单后怎么交付

### 5.1 客户回复后
客户可能在 Upwork 聊天中问你问题。回复模板：
```
Sure! Here's what I need to get started:
1. The exact website URL
2. What specific data fields you want (name, price, etc.)
3. How many pages/items

I'll send you a free sample within a few hours after receiving this info.
```

### 5.2 客户提供信息后
1. 打开你电脑里的 `C:\Users\86189\portfolio\sample-project\scraper.py`
2. 修改代码适配客户的网站（我可以帮你改）
3. 跑脚本，生成 CSV
4. 发前 20 行给客户确认
5. 客户满意后 → 发完整数据
6. 客户在 Upwork 点 "Release Payment"

### 5.3 交付时的消息模板
```
Here's the completed data delivery:

- Total items scraped: [写数量]
- Format: CSV (opens directly in Excel)
- Fields included: [列出字段]
- Attached: [文件名].csv

Please review and let me know if you need any changes. 
If everything looks good, please release the milestone payment.

Thank you for the project!
Jesse
```

---

## 第六步：收到钱

- Upwork 托管资金 → 客户确认后释放
- 提现方式：PayPal 或 Wire Transfer（银行电汇）
- 建议注册一个 PayPal 账号（用 jechan502@gmail.com）
- Upwork 提现到 PayPal → PayPal 提现到中国银行卡
- Upwork 抽成 10%

---

## 📅 每日 Routine

| 时间 | 做什么 |
|------|--------|
| 早 8:00 | 打开 Upwork，搜 "web scraping"，按 Newest 排序 |
| 早 8:10 | 找到 3-5 个合适的单子 |
| 早 8:20 | 各投一封信（用模板，改名字和网站即可） |
| 晚 9:00 | 再搜一次，补投 2-3 个 |

每天投 5-8 个，3 天内必能接到第一单。

---

## 🔧 遇到技术问题？

把客户的需求发给我，我帮你：
- 修改爬虫代码适配目标网站
- 解决反爬问题
- 清洗数据格式
- 写交付说明

---

## ⚠️ 重要提醒

1. **所有沟通留在 Upwork 平台内** — 不要私下加微信/Skype/WhatsApp，被封号
2. **先收到里程碑付款再干活** — 固定价项目要求客户先 funded
3. **绝不碰**：银行账号、密码、身份证、政府网站、付费内容、版权内容
4. **免费样本策略是核心竞争力** — 客户没风险，你拿好评，双赢
5. **前 5 单目标不是赚钱，是拿 5 个五星好评** — 之后价格翻倍

---

*把这个文件加到收藏夹，每天打开照着做。第一周最重要。*
