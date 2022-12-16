from selenium import webdriver  # 导入模块 webdriver可以操作各种浏览器的驱动
import csv  # 保存数据的工具
import pymysql

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
        print('建库失败', e)
        conn.rollback()  # 回滚
    try:
        sql = 'use boss;'
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print('选择库失败', e)
        conn.rollback()  # 回滚
    try:
        cursor.execute("create table boss(job_name varchar(20), job_area varchar(20), job_salary varchar(20), job_empirical varchar(20), company_name varchar(20), job_info varchar(100), _desc varchar(100), href varchar(90)) charset=utf8;")
        conn.commit()
    except Exception as e:
        print('建表失败', e)
        conn.rollback()  # 回滚

with open('boss.csv', mode='a', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['职位名称', '职位地址', '薪资', '学历经验要求', '公司名称', '公司信息', '公司福利', '详情页链接'])

city_list = [101010100, 101280600, 101020100, 101280100, 101210100, 101030100, 101110100, 101230200, 101160100]
# 1. 打开谷歌浏览器
driver = webdriver.Chrome()


def get_next():
    lis = driver.find_elements_by_css_selector('.job-primary')
    # 3. 提取数据
    for li in lis:
        # 每一个岗位的招聘信息(代码)
        # css_selector 类选择器
        # 命名规则
        job_name = li.find_element_by_css_selector('.job-name a').text
        job_area = li.find_element_by_css_selector('.job-area').text
        job_salary = li.find_element_by_css_selector('.job-limit.clearfix span').text
        job_empirical = li.find_element_by_css_selector('.job-limit.clearfix p').text
        company_name = li.find_element_by_css_selector('.company-text h3').text
        job_info = li.find_element_by_css_selector('.company-text p').text
        desc = li.find_element_by_css_selector('.info-desc').text
        href = li.find_element_by_css_selector('.job-name a').get_attribute('href')
        print(job_name, job_area, job_salary, job_empirical, company_name, job_info, desc, href)
        # 4. 保存数据
        with open('boss.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([job_name, job_area, job_salary, job_empirical, company_name, job_info, desc, href])
        # 数据库操作
        # (1)定义一个格式化的sql语句
        sql = 'insert into boss(job_name, job_area, job_salary, job_empirical, company_name, job_info, _desc, href) values(%s,%s,%s,%s,%s,%s,%s,%s) '
        # (2)准备数据
        data = (job_name, job_area, job_salary, job_empirical, company_name, job_info, desc, href)
        # (3)操作
        try:
            cursor.execute(sql, data)
            conn.commit()
        except Exception as e:
            print('插入数据失败', e)
            conn.rollback()  # 回滚


init_database()
for city in city_list:
    driver.get(f'https://www.zhipin.com/c{city}/?query=python&ka=sel-city-{city}')
    for page in range(1, 10):
        get_next()
        driver.find_element_by_css_selector('.next').click()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()
