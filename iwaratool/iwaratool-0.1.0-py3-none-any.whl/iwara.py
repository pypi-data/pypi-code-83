import requests
import re
import json

class iwaratool():
    def __init__(self):
        self.downApi = 'https://www.iwara.tv/api/video/'
        self.url = ''
        self.jsonp = False #False:直接返回字典类型 True:直接返回json文本
        self.user = {
            'videos':{
                'name':'?',
                'id':[],
                'title':[],
                'url':[],
                'look':[],
                'like':[],
                'down':[]
            }
        } #json
        self.verify = True # ssl证书
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'} # 请求头
        self.proxies = {} # 设置代理
        self.other = False # 获取其他信息（如简介，标签等）；默认为False不获取 未完成，进度：做到获取简介的正则 但未完成
        self.expression = {'user':{
            'about':'<div class=".* views-field-field-about">.*>(.*?)\n', #关于 也是用户简介
            'name':'<span.*><h2>(.*?)</h2>',#用户名称
            'JoinDate':'Join date.*<span.*>(.*?)</span>', #加入时间
            'LastSeen':'Last seen.*<span.*><.*">(.*?)</em>(.*?)</span>', #最后一次上线，这里列表有2个
            'Url-Title':'<h3.*<a href="(.*)">(.*)</a></h3>',#包含视频图片标题和地址 单数标题，双数地址（包括0）
            'VideosID':'/videos/(\w.*)"><img' #视频ID
        },
        'videos':{
            'name':'<.*class="username">(.*?)</a>',
            'Url-Title':'<h3.*<a href="(.*)">(.*)</a></h3>',#包含视频图片标题和地址 单数标题，双数地址（包括0）
            'VideosID':'/videos/(\w.*)"><img', #视频ID  
            'like':'class="glyphicon glyphicon-heart"></i> (.*?)\t*</div>',
            'look':'class="glyphicon glyphicon-eye-open"></i> (.*?)\t*</div>'          
        }
        } #如无特别情况请勿修改这些正则表达式
    def userVideos(self,url='', page=0, down=True):
        r'''直接获取视频，不获取其他多余数据
        如果page = -1 将获取全部 不填默认为0 则第一页
        down 是否获取下载地址（注意，设置了代理的下载也需要设置一样的代理 否则会下载失败）
        '''
        
        if url != '':
            self.url = url
        elif self.url == '':
            raise ValueError('url参数为空！')
        r = requests.get(self.url,headers=self.headers, proxies=self.proxies, verify=self.verify)
        videos = re.findall(self.expression['videos']['Url-Title'], r.text)
        videosID = re.findall(self.expression['videos']['VideosID'], r.text)
        like = re.findall(self.expression['videos']['like'], r.text)
        look = re.findall(self.expression['videos']['look'], r.text)
        Title = []
        url = []
        download = []

        self.user['videos']['name'] = re.findall(self.expression['videos']['name'], r.text)[0]
        for i in range(len(videos)):
            Title.append(videos[i][1])
            url.append('https://www.iwara.tv' + videos[i][0])
            if down:
                r = requests.get(self.downApi + videosID[i], headers=self.headers, proxies=self.proxies, verify=self.verify)
                download.append(r.json())
        self.user['videos']['title'] = Title
        self.user['videos']['url'] = url
        self.user['videos']['id'] = videosID
        self.user['videos']['like'] = like
        self.user['videos']['look'] = look
        self.user['videos']['down'] = download
        
        if self.jsonp:
            return json.dumps(self.user)
        else:
            return self.user
    def userImages(self,url='', page=0):
        r'''直接获取图片地址，不获取其他多余数据
        如果page = -1 将获取全部 不填默认为0 则第一页
        '''
        if url != '':
            self.url = url
        elif self.url == '':
            raise ValueError('url参数为空！')
        pass
    def userHome(self,url=''):
        r'''这里会获取作者主页全部内容
        包括但不限于：图片 视频 简介 名称
        url参数清输入作者主页
        '''
        if url != '':
            self.url = url
        elif self.url == '':
            raise ValueError('url参数为空！')
        pass

