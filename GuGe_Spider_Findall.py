
# coding: utf-8

# In[29]:


import requests
import time
from bs4 import BeautifulSoup
import lxml


# In[30]:


def Get_Html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36 Edg/86.0.622.63'}
    response = requests.get(url,headers = headers)
    if response.status_code == 200:
        return response.text
    else:
        print("请求失败")


# In[31]:


def Get_Info(html):   
    html = BeautifulSoup(html,'lxml')
    ranks = html.find_all('span',class_ = 'pc_temp_num')
    names = html.find_all('a',class_ = 'pc_temp_songname')
    times = html.find_all('span', class_ = 'pc_temp_time')
    for r,n,t in zip(ranks,names,times):
        r = r.get_text().replace('\n','').replace('\t','').replace('\r','')
        n = n.get_text()
        t = t.get_text().replace('\n','').replace('\t','').replace('\r','')
        data = {'rank':r,
               'name':n,
               'time':t}
        print(data)


# In[32]:


urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(i) for i in range(1,24)]
for url in urls:
    html = Get_Html(url)
    Get_Info(html)
    time.sleep(1)

