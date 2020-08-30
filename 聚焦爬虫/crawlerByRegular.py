__author__ = 'wangxiao'

import requests
import re
# 爬取boss职位信息

class CrawlerBoss:
    def __init__(self, searchdata):
        self.url = "https://www.zhipin.com/c101190400/?query=" + searchdata + "&page={num}&ka=page-{num}"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
            "cookie": "bl_uid=Xqky8e0ReCw0Xglg7rF05eyynn19; __fid=92b28f666cdbd2cb5c42935e2701e5b0; lastCity=101190400; __zp_seo_uuid__=0ac6db27-9850-4cec-ba94-c05541716e01; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1598774042,1598774055,1598774217,1598774402; __c=1598774036; __l=l=%2Fwww.zhipin.com%2Fjob_detail%2Fd2c126b70b013f7d33R609i0EVY~.html&r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DEGdiKsrkjMmwpfUvh27xcgxKlPcyBvKkrnv-7AmtkG7ZkcvoY-bbz0v1HktFKvcu%26wd%3D%26eqid%3Dfc0425e300010a29000000055f4b5b11&g=&friend_source=0&friend_source=0; __a=77256038.1590834359.1598602362.1598774036.45.3.17.10; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1598774561; __zp_stoken__=951fbWAQ2dDwUdXZKWBMLIDtjSQEZf0UXPAVSSwpuOzQsOl1IUA0vERsaQFwePiIFGmRCQBd6OnRBfgguf2FAS3xNQ2UDa2pQTWMyXVEHVDBuKD94IQwEC31HBD1CDGJuHDU%2FJlcbIAA0A0FNBw%3D%3D; __zp_sseed__=T2F1iWYbxD/aYss7g04hslBhvPYAgqK7+yQwq7nZkiY=; __zp_sname__=864328f8; __zp_sts__=1598775112036"
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
    # url = "https://www.zhipin.com/c101190400/?query=软件测试&page={num}&ka=page-{num}"
    # for i in range(1, 10):
    #     newUrl = url.format(num=i)
    #     print(newUrl)