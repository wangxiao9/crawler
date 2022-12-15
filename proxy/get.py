import requests, pandas, random
import time, datetime, eventlet

def func_set_time(time):
    def decorator(func):
        def wrapper(*args, **kwargs):
            eventlet.monkey_patch()
            with eventlet.Timeout(time, False):
                while True:
                    func(*args, **kwargs)
        return wrapper
    return decorator


class GetProxy:
    def __init__(self):
        self.csv = pandas.read_csv("..//proxy//proxies.csv")

    # @func_set_time(10)
    def get_vaild_ip(self):
        col = self.csv.shape[0]
        # proxy = self.csv.iloc[random.randint(0, col)][0]
        for i in range(0, col):
            proxy = self.csv.iloc[i][0]
            try:
                result = requests.get('https://ip.seeip.org/jsonip?',
                                          proxies={'http': proxy, 'https': proxy},
                                          timeout=5)
                print(f"{proxy} vaild")
                return proxy
            except:
                print(f"{proxy} invalid")
        return None




# ip = '61.216.185.88:60808'
# res = requests.get(url="https://ip.seeip.org/jsonip?", proxies={'http': ip, 'https': ip}, timeout=5)
# print(res.json())


if __name__ == '__main__':
    #GetProxy().run()
    # starttime = datetime.datetime.now()
    GetProxy().get_vaild_ip()