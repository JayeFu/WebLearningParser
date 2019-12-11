# Introduction

可以用来导出网络学堂中的**课程名**，**课程号**， **课序号**。

# Dependency

beautifulsoup4
```bash
pip install beautifulsoup4
```

xlsxwriter
```bash
pip install xlsxwriter
```

# Usage
1. 进入网络学堂
2. 在网络学堂的页面上保存当前页面为`html`格式，并存于此repo的文件夹下。一般保存下来的名字是`Web Learning of Tsinghua University.html`。
3. 将`WebLearningParser.py`中第**5**行的路径名称改为当前repo的绝对路径，并保存。
   * 如`C:\Users\Jaye Fu\Desktop\WebLearningParser`$\rightarrow$`xxx\WebLearningParser`
4. 启动`WebLearningParser.py`。
5. 在生成的`WebLearning.xlsx`中
   1. 第1列是课程名称
   2. 第2列是课程号
   3. 第3列是课序号