# python_final_test 18网新Python期末项目

- [**项目代码Github URL**](https://github.com/fangwenxi/python_final_test/tree/master/webapp)

- **项目pythonanywhere URL**

- **数据传递描述:** 用户在前端下拉框选择年份或想要查看的数据后，点击**DO it!** 后，会反馈到HTML文件中的
```
<select name="the_year_selected">

```
之后传递到python文件中的

```
 the_year = request.form["the_year_selected"]
```
request会向前端请求数据后，通过

```
dfs = df2.query("指标=='{}'".format(the_year))
```
选取数据进行画图。

- **基本交互功能的HTML5控件使用:**

- **在项目中，我实现了：**

   1.HTML档：
   
   2.Python档：
   
   3.Web App动作描述：
