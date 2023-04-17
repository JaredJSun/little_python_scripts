import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# 读取CSV文件
csv_file = 'xxx.csv'
movie_codes = pd.read_csv(csv_file, header=None, names=['Index', 'Code'])

# 定义搜索引擎的URL
search_url = 'https://xxx.com/search?q='

# 创建一个空的DataFrame来存储结果
results = pd.DataFrame(columns=['Index', 'Movie Code', 'Movie URL'])

# 创建自定义请求头，模拟浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# 遍历影片识别码
for index, row in movie_codes.iterrows():
    code = row['Code']
    query_url = search_url + code
    response = requests.get(query_url, headers=headers)  # 添加 headers 参数
    soup = BeautifulSoup(response.text, 'html.parser')

    # 从网页中提取第一个影片链接
    movie_link = soup.find('a', {'class': 'box'})  # 更新选择器

    # 如果找到影片链接，获取完整的URL
    if movie_link is not None:
        movie_url = 'https://xxx.com' + movie_link['href']
    else:
        movie_url = 'Not Found'

    # 将结果添加到DataFrame
    results = results.append({'Index': row['Index'], 'Movie Code': code, 'Movie URL': movie_url}, ignore_index=True)

    # 为避免触发反爬虫策略，暂停一段时间
    time.sleep(1)

# 保存结果到CSV文件
results.to_csv('xxx_results.csv', index=False)