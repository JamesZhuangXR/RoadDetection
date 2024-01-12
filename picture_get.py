import re
import requests
import os
import time
num=0
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
         'Cookie':'BIDUPSID=EE5A2040115E73074DFD7B9B7F08A9AC; PSTM=1658795372; BDUSS=mZZWVEwa1VybHZYZE9ITTFnRXFBbTRQYm1RWE0wRk9LQWpTZGU2YU9WdUR3Z1pqRVFBQUFBJCQAAAAAAAAAAAEAAADWREchbmp6aHVhbmd4cgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIM132KDNd9iY; BDUSS_BFESS=mZZWVEwa1VybHZYZE9ITTFnRXFBbTRQYm1RWE0wRk9LQWpTZGU2YU9WdUR3Z1pqRVFBQUFBJCQAAAAAAAAAAAEAAADWREchbmp6aHVhbmd4cgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIM132KDNd9iY; BAIDUID=EE5A2040115E7307EE3F1ADEB2E5935E:SL=0:NR=10:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=8lah0g84ag012h2085alptc71he6g8d17; delPer=0; PSINO=3; ZFY=1v4QkCb:A74JpOIJMculSXCaZeOg2uOogBjfCNFY9IqA:C; BAIDUID_BFESS=1F0BD0C9869C1DB7ADDA63AA87DCBB78:FG=1; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; ab_sr=1.0.1_ZGFmNGVkZDJmMjhlZGFkNmYxYjQ4OWM1N2VkYzQ3Nzc1M2NkNGFlMGQwMGRiNWI1NmE3NTllNWNhYTMyMzQ3NjlhZmJlM2U4ZWY4YzYyY2MzZjM1ODVmNTgyZDY2MGM4ODYxOGU5NmZiN2VmYmIyZDgyMDFmZTNiZmY3ZjgyZjRjZDE5YzY1ZTcwMzU3ODAyNGZhODg3ZjI0YTliNTkxNQ==; H_PS_PSSID=36542_36463_36255_36725_36413_36668_36955_36947_36165_36918_36807_36786_36966_36745_26350_36681_36865',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
         'Accept-Encoding': 'gzip, deflate, br',
         'Accept-Language': 'zh-CN,zh;q=0.9'}

if __name__ == '__main__':

    title = input("Input a title:")

    for j in range(0,120,30):
    
        url=f'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwzLDEsNSw0LDIsOCw3LDYsOQ%3D%3D&word={title}&pn={j}'
    
        time.sleep(3)
        html=requests.get(url,headers=header)
    
        html.encoding='utf-8'
        print(html.text)
    
        html=html.text
        pachong_picture_path=f'{title}_pictures'

        if not os.path.exists(pachong_picture_path):
           os.mkdir(pachong_picture_path)

        res=re.findall('"objURL":"(.*?)"',html)
        for i in res:
            if 'gimg2.baidu.com/image_search/' not in i:
                num=num+1
                try:
                    picture=requests.get(i)
                    print(f'{num}:{i}')
                    file_name=f'{pachong_picture_path}\\{title}_{num}.jpg'
                    f=open(file_name,'wb')
                    f.write(picture.content)
                    
                except:
                    pass
    
        f.close()

