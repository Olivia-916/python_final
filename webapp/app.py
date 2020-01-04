from flask import Flask, render_template, request
import pandas as pd
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go
from pyecharts import options as opts
from pyecharts.charts import Geo,Map,Funnel
from pyecharts.globals import ChartType, SymbolType

app = Flask(__name__)

# 准备工作
df = pd.read_csv('D.csv',encoding='gbk')
@app.route('/',methods=['GET'])
def ge_jigou():
    data_str = df.to_html()

    with open("孤儿和机构.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
    return render_template('ge_jigou.html',
                           the_plot_all=plot_all,
                           the_res = data_str)
# 第二页面
@app.route('/yf_death',methods=['GET'])
def yf_death():
    df1 = pd.read_csv('H.csv', encoding='gbk')
    data_str = df1.to_html()
    with open("孕妇死亡率.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
    return render_template('yf_death.html',
                           the_plot_all=plot_all,
                           the_res = data_str)

# 第三页面
@app.route('/ge_data',methods=['GET'])
def ge_data():
    df2 = pd.read_csv('F.csv', encoding='gbk')
    year_available = list(df2.年份.dropna().unique())
    cf.set_config_file(offline=True, theme="ggplot")
    py.offline.init_notebook_mode()
    data_str = df2.to_html()
    return render_template('ge_data.html',
                           the_res = data_str,
                           the_select_year=year_available)
#第三页面响应✌
@app.route('/ge_data_response',methods=['POST'])
def ge_data_response() -> 'html':
    df2 = pd.read_csv('F.csv', encoding='gbk')
    year_available = list(df2.年份.dropna().unique())
    the_year = request.form["the_year_selected"]
    df1 = pd.read_csv('F.csv', encoding='gbk')
    time = list(df1['年份'].unique())
    dq = list(df1['地区'].unique())
    time.reverse()
    dfs = df2.query("年份=='{}'".format(the_year))
    def map_visualmap() -> Map:
        z = (
            Map()
                .add("人数", list(zip(dq, dfs['孤儿数'])), "china")
                .set_global_opts(
                title_opts=opts.TitleOpts(title="中国分省孤儿人数"),
                visualmap_opts=opts.VisualMapOpts(max_=60000),
            )
        )
        return z
    map_visualmap().render()
    with open("render.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
    data_str = dfs.to_html()
    return render_template('ge_data.html',
                            the_plot_all = plot_all,
                            the_res = data_str,
                            the_select_year = year_available
                           )

# 第四页面
@app.route('/zm_qwm',methods=['GET'])
def zm_qwm():
    df4 = pd.read_csv('G.csv', encoding='gbk')
    zb_available = list(df4.指标.dropna().unique())
    cf.set_config_file(offline=True, theme="ggplot")
    py.offline.init_notebook_mode()
    data_str = df4.to_html()
    return render_template('zm_qwm.html',
                           the_res = data_str,
                           the_select_year=zb_available)
#第四页面响应✌
@app.route('/zm_qwm_response',methods=['POST'])
def zm_qwm_response() -> 'html':
    df2 = pd.read_csv('G.csv', encoding='gbk')
    year_available = list(df2.指标.dropna().unique())
    the_year = request.form["the_year_selected"]
    time = list(df2['年份'].unique())
    zb = list(df2['指标'].unique())
    time.reverse()
    dfs = df2.query("指标=='{}'".format(the_year))
    a = []
    for t in time:
        df4 = dfs[dfs.年份 == t]
        a.append(sum(df4['人数']))
    del a[1]
    n = []
    for i in time:
        n.append(str(i))

    def funnel_label_inside() -> Funnel:
        c = (
            Funnel()
                .add(
                "商品",
                [list(z) for z in zip(n, a)],
                label_opts=opts.LabelOpts(position="inside"),
            )
                .set_global_opts(title_opts=opts.TitleOpts(title="重男轻女"))
        )
        return c

    funnel_label_inside().render()
    with open("render.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
    data_str = dfs.to_html()

    return render_template('zm_qwm.html',
                            the_plot_all = plot_all,
                            the_res = data_str,
                            the_select_year = year_available
                           )

if __name__ == '__main__':
    app.run(debug=True,port=8000)