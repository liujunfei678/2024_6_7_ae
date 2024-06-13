### 获取ae服装网站中的图片以及搭配图
#### 目标网站：https://www.ae.com/us/en/c/women/womens
- get_all_url.py
主要功能为获取所有的商品链接
  - getfirst()：获取第一页的推荐的商品，这部分就放在原始请求中
  - getlater(n,d)
    - 检查发现数据存放在：https://www.ae.com/ugp-api/catalog/v1/category/mens?No={n}&Nrpp=30&prevPageGroupId={id}；其中的n为页数，id为此商品所在的类
    - 手动收集商品的页数范围以及所在的类，保存到csv文件中
- get_main_pic.py
主要功能为获取主要的商品的主要图片，相关搭配的链接
  - 请求头：经过测试，请求头应该包括，User-Agent以及X-Access-Token；后者可能需要一定时间进行验证
  - get_main_pic:获取主要图片
  - getother：获取搭配的链接
  - get_pic:获取该商品服装下所有的图片，包括其他链接下的主图
  - 随后进行多进程下载
    
