import csv  # 保存数据的工具
import pymysql
import requests
from bs4 import BeautifulSoup

# 建立连接
conn = pymysql.connect(host='192.168.96.128', user='root', password='123456', charset='utf8')
# 建立游标
cursor = conn.cursor()


# (1)定义一个格式化的sql语句
def init_database():
    # (3)操作
    try:
        sql = 'create database boss;'
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()  # 回滚
    try:
        sql = 'use boss;'
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()  # 回滚
    try:
        cursor.execute("create table policy(href varchar(150), title varchar(150)) charset=utf8;")
        conn.commit()
        print('创建表成功')
    except Exception as e:
        print(e)
        conn.rollback()  # 回滚


with open('policy.csv', mode='a', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['链接', '文件名'])


def get_next():
    headers = {
        'Cookie': 'route=1b87f4f38a4ffcf82f6ae785dffd490e; 1_vq=5',
        'Host': 'chinajob.mohrss.gov.cn',
        'Referer': 'http://chinajob.mohrss.gov.cn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39'
    }

    lst = [''] + [f'_{i}' for i in list(range(2, 10 + 1))]
    for l in lst:
        resp = requests.get(f'http://chinajob.mohrss.gov.cn/zcfg/zxzc/index{l}.shtml')
        html = resp.text
        main_page = BeautifulSoup(html, "html.parser")
        lis = main_page.find('div', {'class': 'list_con_left fl'}).ul.find_all('li')
        for li in lis:
            href = "http://chinajob.mohrss.gov.cn" + li.a.attrs['href']
            title = li.a.attrs['title']
            print(href, title, sep='\t')

            # 4. 保存数据
            with open('policy.csv', mode='a', encoding='utf-8', newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow([href, title])
            # 数据库操作
            # (1)定义一个格式化的sql语句
            sql = 'insert into policy(href, title) values(%s,%s) '
            # (2)准备数据
            data = (href, title)
            # (3)操作
            try:
                cursor.execute(sql, data)
                conn.commit()
            except Exception as e:
                print('插入数据失败', e)
                conn.rollback()  # 回滚


init_database()
get_next()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()
