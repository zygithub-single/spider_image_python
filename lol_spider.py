#!/usr/bin/python3
#coding=utf-8
import requests
import os

url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2781457'#英雄联盟官方链接

def get_skin_image(url):

    res = requests.get(url)
    for i in res.json()['hero']:
        tmp_url = f'''https://game.gtimg.cn/images/lol/act/img/js/hero/{str(i['heroId'])}.js''' #每一个英雄的链接
        get_image_url_res = requests.get(tmp_url)
        for image_url in get_image_url_res.json()['skins']:
            if image_url['mainImg']:
                hero_name = image_url['heroName'].replace(' ','').replace('/','') #获取英雄名称
                skin_name = image_url['name'].replace(' ','').replace('/','') #获取皮肤名称
                new_url = image_url['mainImg'].replace(' ','') #获取皮肤链接
                print(hero_name)
                print(new_url)
                if os.path.exists(f'lol_image'): #判断lol_image目录是否存在，不存在则添加一个Lol_image目录
                    pass
                else:
                    os.mkdir(f'lol_image')

                if os.path.exists(f'lol_image/{hero_name}'): #判断英雄目录是否存在，不存在则添加
                    pass
                else:
                    os.mkdir(f'lol_image/{hero_name}')

                if os.path.exists(f'lol_image/{hero_name}/{skin_name}.jpg'): #判断图片是否存在，不存在则添加
                    print(f'图片：lol_image/{hero_name}/{skin_name}.jpg 已经存在！')
                    pass
                else:
                    with open(f'lol_image/{hero_name}/{skin_name}.jpg','wb') as f:
                        print(f'正在写入:./lol_image/{hero_name}/{skin_name}.jpg')
                        image = requests.get(new_url).content #获取图片内容
                        f.write(image)
if __name__ == '__main__':
    get_skin_image(url)
