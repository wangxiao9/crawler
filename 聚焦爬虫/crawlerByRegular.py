__author__ = 'wangxiao'

import requests
import re
# 爬取boss职位信息

class CrawlerBoss:
    def __init__(self):
        self.url = "https://www.zhipin.com/c101190400/?query=软件测试&page={num}&ka=page-{num}"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
            "cookie": "lastCity=101190400; __zp_seo_uuid__=d87d3773-044e-4b23-9635-c08dff4c8ff7; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1598602362,1598602374; toUrl=https%3A%2F%2Fwww.zhipin.com%2F%2Fjob_detail%2F9b2736777888c09e1H1y2NS7E1c%7E.html; JSESSIONID=""; _bl_uid=Xqky8e0ReCw0Xglg7rF05eyynn19; __c=1598602362; __l=l=%2Fwww.zhipin.com%2F%2Fjob_detail%2F9b2736777888c09e1H1y2NS7E1c~.html&r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DDIWmSMfVjvR3hNh8rSKjhosnIK9wNat7r5ACkzvc6lVJum5elNDKve5d6amWQ8v4%26wd%3D%26eqid%3Dd000fa1900000cfc000000055f48bc78&g=&friend_source=0&friend_source=0; __a=77256038.1590834359.1590834359.1598602362.27.2.24.24; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1598607923; __zp_stoken__=395dbZzNjL3grbnkUd2F%2FIx1jNj5BXzJJJDNhUGx7Jk1hSlA3MFh0VSQBKFcZLxUGPGQ9fyBHCiV%2FHUI1YnYdTj4sF0IqSCR9N28GREEJSURycSJHFnNbLlIHNyYkGX86OjVAGWBOe0QLGHJWYQ%3D%3D; __zp_sseed__=T2F1iWYbxD/aYss7g04hsqoJi+8IcUimczGbuZ0NOZg=; __zp_sname__=5e1648a1; __zp_sts__=1598607968366"
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

    def run(self):
        for num in range(1, 10):
            res = self.get_request_text(num)
            company_list, salary_list, jobs_url_list = self.operation_need_data(res)
            for i in range(0, len(company_list)):
                url = "https://www.zhipin.com"
                newUrl = url + jobs_url_list[i]
                data = company_list[i] + ":" + salary_list[i] + ':' + newUrl
                print(data)
                with open('boss.txt', 'a+', encoding='utf-8') as f:
                    f.write(data + '\n')
        print("写入数据成功")


if __name__ == '__main__':
    CrawlerBoss().run()
    # url = "https://www.zhipin.com/c101190400/?query=软件测试&page={num}&ka=page-{num}"
    # for i in range(1, 10):
    #     newUrl = url.format(num=i)
    #     print(newUrl)