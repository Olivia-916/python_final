# python_final_test 18网新Python期末项目

- [**项目代码Github URL**](https://github.com/fangwenxi/python_final_test/tree/master/webapp)

- [[**项目pythonanywhere URL**]](http://kegen.pythonanywhere.com/)

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



- **在项目中，我实现了：**

   1.HTML档：
   
   - 设计导航栏，并为导航栏增添CSS样式。
   
   - 其中两个页面为可交互，两个页面为固定图表；交互页面需要向前端发送请求，后再响应，非交互界面则不用。
   
   - 加入了文本内容
   
   - 链接了static文档中的CSS文件，让四个页面的样式相同，整体更加美观。
   
   2.Python档：
   
   （1）调用模块
   
   - flask
   
   - pandas
   
   - plotly
   
   - pyecharts
   
   （2）使用pyecharts绘制图表
   
   - 第一个页面和第四个页面（条形图和折线图组合图表）
   
   ![first](https://github.com/fangwenxi/python_final_test/blob/master/%E7%AC%AC%E4%B8%80%E9%A1%B5%E9%9D%A2.png)
   
   ![fourth](https://github.com/fangwenxi/python_final_test/blob/master/%E7%AC%AC%E5%9B%9B%E9%A1%B5%E9%9D%A2.png)
   
   - 第二页面（中国地图）
   
   ![second](https://github.com/fangwenxi/python_final_test/blob/master/%E7%AC%AC%E4%BA%8C%E9%A1%B5%E9%9D%A2.png)
   
   ![second](https://github.com/fangwenxi/python_final_test/blob/master/%E7%AC%AC%E4%BA%8C%E9%A1%B5%E9%9D%A22.png)
   
   - 第三页面（漏斗图）
   
   ![third](https://github.com/fangwenxi/python_final_test/blob/master/%E7%AC%AC%E4%B8%89%E9%A1%B5%E9%9D%A2.png)
   
   ![third](https://github.com/fangwenxi/python_final_test/blob/master/%E7%AC%AC%E4%B8%89%E9%A1%B5%E9%9D%A22.png)
   
   （3）自定义函数，条件设置
 
   ![hs](https://github.com/fangwenxi/python_final_test/blob/master/%E8%87%AA%E5%AE%9A%E4%B9%89%E5%87%BD%E6%95%B0.png)
   
   ![hs](https://github.com/fangwenxi/python_final_test/blob/master/%E8%87%AA%E5%AE%9A%E4%B9%89%E5%87%BD%E6%95%B02.png)   
   
   （4)for循环
   
   ![xh](https://github.com/fangwenxi/python_final_test/blob/master/%E5%BE%AA%E7%8E%AF.png)
   
   （5)交互实现
   
   ![jh](https://github.com/fangwenxi/python_final_test/blob/master/GET.png)
   
   ![jh](https://github.com/fangwenxi/python_final_test/blob/master/POST.png)
   
   （6）嵌套及交互
   
   ![qt](https://github.com/fangwenxi/python_final_test/blob/master/%E5%B5%8C%E5%A5%97.png)
   
   ![qt](https://github.com/fangwenxi/python_final_test/blob/master/%E4%BA%A4%E4%BA%92.png)
   
   
   3.Web App动作描述：
   
   - 上方设有导航栏，可自行选择四个页面，每个页面故事不同，第一页面和第四页面是不同的两组数据的不同图表对比，可以筛选其中某个数据查看图表。第二页面是中国地图，可放大缩小，也可以在下拉框中选中年份，点击DO it！查看不同年份的中国地图图表，同时下面的列表也会随之改变；第三页面为漏斗图，在下拉框中可以选中不同的指标，点击DO it！查看不同指标下不同年份的数据对比，同时下面的列表也会随之改变。

