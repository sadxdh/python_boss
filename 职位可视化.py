import pandas as pd
import re
from pyecharts.charts import *
from pyecharts import options as opts
# from pyecharts.charts import Bar
# from pyecharts.charts import Pie
import jieba
# from pyecharts.charts import WordCloud
import os

# 导入数据
boss = pd.read_csv('boss.csv', engine='python', encoding='utf-8')
print(boss.head())
print(boss.shape)  # 返回df形状 表格行列 元组
# 数据处理  =======================================================
# 查看重复值
print(boss.duplicated().sum())  # 查找并显示数据表中有多少的重复值
print(boss.drop_duplicates(inplace=True))
print(boss.duplicated().sum())
# 查看缺省值
print(boss.isnull().sum())
# 缺省值处理
print(boss['公司福利'].fillna('无', inplace=True))
print(boss.isnull().sum())
# 地区列处理-----------------------------
print(boss['职位地址'].unique())
boss['职位地址'] = boss['职位地址'].apply(lambda x: x.split('·')[0])
print(boss['职位地址'].unique())
# 经验列处理-----------------------------
print(boss['学历经验要求'].unique())
boss['学历'] = boss['学历经验要求'].apply(lambda x: x[-2:])
print(boss.head())
boss['经验'] = boss['学历经验要求'].apply(
    lambda x: x[:-2].replace('学历', '').replace('应届生', '经验不限').replace('在校/应届', '经验不限').replace('初中及', ''))
boss['经验'] = boss['经验'].apply(lambda x: re.sub('.*天/.*月', '1年以内', x))
print(boss.head())
print(boss['学历'].unique())
print(boss['经验'].unique())
# 薪资列处理-----------------------------
boss['薪资'] = boss['薪资'].apply(lambda x: re.sub('.*元/天', '4-6K', x))
print(boss['薪资'].unique())
boss['bottom'] = boss['薪资'].str.extract('^(.*?)-.*?')
boss['top'] = boss['薪资'].str.extract('^.*?-(\d\d\.\d|\d\d)')
boss['bottom'] = boss['bottom'].astype('float64')
boss['top'] = boss['top'].astype('float64')
boss['工资平均'] = (boss['bottom'] + boss['top']) / 2
print(boss.head())


# 数据可视化 ==========================================================
# 薪资区间-------------------------------
def tranform_price(x):
    if x <= 8.0:
        return '6k以下'
    elif x <= 12:
        return '8-12k'
    elif x <= 15.0:
        return '12k-15k'
    elif x <= 20:
        return '15-20k'
    elif x <= 25:
        return '20-25k'
    else:
        return '25k以上'


boss['薪资分级'] = boss['工资平均'].apply(lambda x: tranform_price(x))
price_1 = boss['薪资分级'].value_counts()
datas_pair_1 = [(i, int(j)) for i, j in zip(price_1.index, price_1.values)]
print(datas_pair_1)
pie1 = (
    Pie(init_opts=opts.InitOpts(theme='dark', width='1000px', height='600px'))

        .add('', datas_pair_1, radius=['35%', '60%'])
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%"))
        .set_global_opts(
        title_opts=opts.TitleOpts(
            title="python职位\n\n薪资区间",
            pos_left='center',
            pos_top='center',
            title_textstyle_opts=opts.TextStyleOpts(
                color='#F0F8FF',
                font_size=20,
                font_weight='bold'
            ),
        )
    )
        .set_colors(['#EF9050', '#3B7BA9', '#6FB27C', '#FFAF34', '#D8BFD8', '#00BFFF', '#7FFFAA'])
        .render("薪资区间.html")
)
# 经验学历要求情况------------------------------------
boss_1 = boss['经验'].value_counts()
x = boss_1.index.tolist()
y = boss_1.values.tolist()
boss_2 = boss['学历'].value_counts()
x_2 = boss_2.index.tolist()
y_2 = boss_2.values.tolist()
data_pair_1 = [list(z) for z in zip(x, y)]
data_pair_2 = [list(z) for z in zip(x_2, y_2)]
c = (
    Pie(init_opts=opts.InitOpts(width="1000px", height="600px", bg_color="#2c343c"))
        .add(
        series_name="经验需求占比",
        data_pair=data_pair_1,
        rosetype="radius",
        radius="55%",
        center=["25%", "50%"],
        label_opts=opts.LabelOpts(is_show=False, position="center", color="rgba(255, 255, 255, 0.3)"),
    )
        .add(
        series_name="学历需求占比",
        data_pair=data_pair_2,

        radius="55%",
        center=["75%", "50%"],
        label_opts=opts.LabelOpts(is_show=False, position="center", color="rgba(255, 255, 255, 0.3)"),
    )
        .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
        label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(
            title="经验、学历需求占比",
            pos_left="center",
            pos_top="20",
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        legend_opts=opts.LegendOpts(is_show=False),
    )
        .set_colors(["#D53A35", "#334B5C", "#61A0A8", "#D48265", "#749F83"])
        .render("经验学历要求情况.html")
)
# 经验要求和薪资情况的情况----------------------------------
mean = boss.groupby('经验')['工资平均'].mean().sort_values()
x = mean.index.tolist()
y = mean.values.tolist()
b1 = (
    Bar()
        .add_xaxis(x)
        .add_yaxis(
        "工作经验",
        y,
        markpoint_opts=opts.MarkPointOpts(
            data=[opts.MarkPointItem(name="3-5年经验", coord=[x[3], y[3]], value=y[3])]
        )
    )
        .set_global_opts(title_opts=opts.TitleOpts(title="不同工作经验的平均薪资"))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .render("经验要求和薪资情况.html")
)
# 学历要求和薪资情况的情况-----------------------------------
mean = boss.groupby('学历')['工资平均'].mean().sort_values()
x = mean.index.tolist()
y = mean.values.tolist()
b2 = (
    Bar()
        .add_xaxis(x)
        .add_yaxis(
        "学历",
        y,
        markpoint_opts=opts.MarkPointOpts(
            data=[opts.MarkPointItem(name="学历不限", coord=[x[1], y[1]], value=y[1])]
        )
    )
        .set_global_opts(title_opts=opts.TitleOpts(title="不同学历的平均薪资"))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .render("学历要求和薪资情况.html")
)
# 公司福利---------------------------------------------------
text = boss['公司福利'].dropna().to_string()
print(text)
words = jieba.lcut(text)
# 通过遍历words的方式,统计出每个词出现的频次
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
new = []
for i in items:
    if i[1] > 3:
        new.append(i)
c = (
    WordCloud()
        .add(series_name="热点分析", data_pair=new, word_size_range=[6, 66])
        .set_global_opts(
        title_opts=opts.TitleOpts(
            title="公司福利", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
        .render("公司福利.html")
)
