__author__ = 'wangxiao'

import requests
import re
# 爬取boss职位信息

class CrawlerBoss:
    def __init__(self, searchdata):
        self.url = "https://www.zhipin.com/c101190400/?query=" + searchdata + "&page={num}&ka=page-{num}"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
            "cookie": "Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1598318942,1598578484,1599528305; __g=-; lastCity=101190400; __c=1599528308; __l=l=%2Fwww.zhipin.com%2Fsuzhou%2F&r=&g=&friend_source=0&friend_source=0; __a=59673664.1598318944.1598578484.1599528308.14.3.8.12; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1599529094; __zp_stoken__=67f6bCxtMJjkKMUF%2FRWt5cAt4b1VTdzV1Clsla3p4bg0PdicbVzYeQUZeMUg7SkI6Wjs6EwgwCCR3QEAaISMnQylAe0cQVDkKFDBldG0uDGIHGD0rIWFoVx9BNxZrJVRWXGpHdUxOdVt2PAl5JQ%3D%3D; __zp_sseed__=h8jznVVvFQhnMg5cieZ/1//btYytS1ZO7IzJ5CGcMD0=; __zp_sname__=ce475149; __zp_sts__=1599529295912"
        }

    def get_request_text(self, i):
        newUrl = self.url.format(num=i)
        res = requests.get(newUrl, headers=self.headers).text
        return res

    def operation_need_data(self, res):
        company_expression = '<h3 class="name"><a.*?>(.*?)</a></h3>'
        salary_expression = '<span class="red">(.*?)</span>'
        jobs_expression = '<span class="job-name"><a href="(.*?)" title=.*?</span>'
        company_list = re.findall(company_expression, res, re.S)
        salary_list = re.findall(salary_expression, res, re.S)
        jobs_url_list = re.findall(jobs_expression, res, re.S)
        return company_list, salary_list, jobs_url_list

    def run(self, file):
        for num in range(1, 10):
            res = self.get_request_text(num)
            company_list, salary_list, jobs_url_list = self.operation_need_data(res)
            for i in range(0, len(company_list)):
                url = "https://www.zhipin.com"
                newUrl = url + jobs_url_list[i]
                data = company_list[i] + ":" + salary_list[i] + ':' + newUrl
                print(data)
                with open(file, 'a+', encoding='utf-8') as f:
                    f.write(data + '\n')
        print("写入数据成功")


if __name__ == '__main__':
    CrawlerBoss('测试开发').run('测试开发.txt')