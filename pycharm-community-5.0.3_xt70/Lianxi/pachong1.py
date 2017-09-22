from urllib import request
from bs4 import BeautifulSoup as bs
import re
import jieba
import pandas as pd

resp = request.urlopen("https://movie.douban.com/cinema/nowplaying/hangzhou/")
html_data = resp.read().decode("utf-8")
# print(html_data)
soup=bs(html_data,"html.parser")
nowplaying_movie=soup.find_all('div',id='nowplaying')
nowplaying_movie_list=nowplaying_movie[0].find_all('li',class_='list-item')
# print(nowplaying_movie_list[0])
nowplaying_list=[]
for item in nowplaying_movie_list:
    nowplaying_dict={}
    nowplaying_dict['id']=item['data-subject']
    for tag_img_item in item.find_all('img'):
        nowplaying_dict['name']=tag_img_item['alt']
        nowplaying_list.append(nowplaying_dict)
# print(nowplaying_list)
requrl="https://movie.douban.com/subject/"+nowplaying_list[0]['id']+'/comments'+'?'+'status=P'
resp=request.urlopen(requrl)
html_data=resp.read().decode('utf-8')
soup=bs(html_data,'html.parser')
comment_div_lists=soup.find_all('div',class_='comment')
eachCommentList=[]
for item in comment_div_lists:
    if item.find_all('p')[0].string is not None:
        eachCommentList.append(item.find_all('p')[0].string)
#输入评论
# print(eachCommentList)
# 数据清洗
comments=''
for k in range(len(eachCommentList)):
    comments=comments+(str(eachCommentList[k])).strip()
# print(comments)
# 清除标点符号
pattern=re.compile(r'[\u4e00-\u9fa5]+')
filterdata=re.findall(pattern,comments)
cleaned_comments=''.join(filterdata)
# print(cleaned_comments)
segment=jieba.lcut(cleaned_comments)
words_df=pd.DataFrame({'segment':segment})
words_df.head()
stopwords=pd.read_csv("stopwords.txt",index_col=False,quoting=3,sep="\t",names=['stopword'],encoding='utf-8')
words_df=words_df[~words_df.segment.isin(stopwords.stopword)]
words_df.head()

