import requests


url = "https://car2.autoimg.cn/cardfs/product/g26/M06/94/6F/120x90_0_q95_autohomecar__ChxkjmLxIqCAIiLGADGm4MesSO8115.jpg"

res = requests.get(url)

file_name = url.split('/')[-1]

with open(file_name, 'wb') as f:
    f.write(res.content)

f.close()