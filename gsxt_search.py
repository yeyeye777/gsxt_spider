# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 11:05 上午
# @Software: PyCharm


import requests
import json
from faker import Factory
class gsxt():

    def search(self):
        ua = Factory.create().user_agent()
        print(ua)
        url = "http://app.gsxt.gov.cn/gsxt/cn/gov/saic/web/controller/PrimaryInfoIndexAppController/search?page=1"
        payload = {'searchword': '小米科技有限责任公司',
                   'conditions': '{"excep_tab": "0","ill_tab": "0","area": "0","cStatus": "0","xzxk": "0","xzcf": "0","dydj": "0"}',
                   'sourceType': 'A'}
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': 'application/json',
            'User-Agent': ua,
            'Host': 'app.gsxt.gov.cn'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)

    def detail(self):
        """基本信息"""
        ua = Factory.create().user_agent()
        print(ua)
        url = "http://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-primaryinfoapp-entbaseInfo-144632AA1A5BFB58D777EF76F959DD10A4102710271050E4A41050E4A493A8CEBBDD4C39FE1B2C98A3645FEBFC9ADA6EDAAF982C4AF8-1599805787963.html?nodeNum=110000&entType=1130&sourceType=A"
        payload = {}
        headers = {
            'Host': 'app.gsxt.gov.cn',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Origin': 'file://',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': ua,
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)

    def administrative_sanction(self):
        """行政处罚"""
        ua = Factory.create().user_agent()
        print(ua)
        url = "http://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-punishmentdetail-B54693AABB5B5A5876774E7658597C10051086108610F1E40510F1E4059309CE1ADDED395F1B8D980264FEEB5D9A7B6E7BAF392CEBF8-1594802153048.html?nodeNum=110000&entType=113&sourceType=A"
        headers = {
            'Host': 'app.gsxt.gov.cn',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Origin': 'file://',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': ua,
        }
        response = requests.request("POST", url, headers=headers)
        print(response.text)

    def List_of_anomalies(self):
        """异常名录"""
        ua = Factory.create().user_agent()
        print(ua)
        url = "http://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-entBusExcep-A04686AAAE5B4F5863775B764D596910101093109310E4E41010E4E410931CCE0FDDF8394A1B98981764EBEB489A6E6E6EAF2C2CFEF8-1594367047878.html?nodeNum=110000&entType=1&sourceType=A"
        headers = {
            'Host': 'app.gsxt.gov.cn',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Origin': 'file://',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': ua,
        }
        response = requests.request("POST", url, headers=headers)
        print(response.text)

    def dishonesty(self):
        """严重违法失信企业名单"""
        ua = Factory.create().user_agent()
        print(ua)
        url = "http://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-illInfo-CA46ECAAC45B255809773176275903107A10F910F9108EE47A108EE47A9376CE65DD9239201BF2987D6481EB229A046E04AF462C94F8-1594367525644.html?nodeNum=110000&entType=1&sourceType=A"
        headers = {
            'Host': 'app.gsxt.gov.cn',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Origin': 'file://',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': ua,
        }
        response = requests.request("POST", url, headers=headers)
        print(response.text)


if __name__ == '__main__':
    server=gsxt()
    server.search()
    server.detail()
    server.administrative_sanction()
    server.List_of_anomalies()
    server.dishonesty()






