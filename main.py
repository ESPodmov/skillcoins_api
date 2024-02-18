import requests
from requests import session
import json
import base64
# cur_session = session()
# with open("params/headers.json", "r") as file:
#     headers = json.loads(file.read())
#
# cur_session.headers = headers
# url = "https://skillbox-kazan.docrm.org/api/PaymentApi/DownloadConversionEventReport"
#
# with open("params/data_sample.json", "r") as file:
#     data = json.loads(file.read())
#
# with open("params/log.json", "r") as file:
#     params = json.loads(file.read())
#
# response = cur_session.post('https://skillbox-kazan.docrm.org/api/AccountApi/Login', params=params, headers=headers)
# print(response.json())
# print(cur_session.cookies)

############

cookies = {
    'Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6ImVtcGxveWVlLWVjYWYxMGI2LWEyYzQtNDYyMy05NGQ2LWVjYjBkYzg0ZDg2OCIsImRhdGUiOnsiX19pbnN0YW50IjoxNzA4MjY5MzA1NzQ1fX0.C84t3l1lievKfVQ55EKLClNzcMHEBLbAOswRBAtkcMI',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    # 'Cookie': 'Token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6ImVtcGxveWVlLWVjYWYxMGI2LWEyYzQtNDYyMy05NGQ2LWVjYjBkYzg0ZDg2OCIsImRhdGUiOnsiX19pbnN0YW50IjoxNzA4MjY5MzA1NzQ1fX0.C84t3l1lievKfVQ55EKLClNzcMHEBLbAOswRBAtkcMI',
    'Origin': 'https://skillbox-kazan.docrm.org',
    'Referer': 'https://skillbox-kazan.docrm.org/payment/conversioneventsreport',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}


with open("params/data_sample.json") as file:
    json_data = json.loads(file.read())
# json_data = {
#     'query': {
#         'period': {
#             'from': {
#                 '__instant': 1708203600000,
#             },
#             'to': {
#                 '__instant': 1708289999999,
#             },
#         },
#         'watchPeriod': 336,
#         'bindingType': 0,
#         'rowType': None,
#         'employeeId': None,
#         'subjectId': None,
#         'pageIx': 0,
#     },
# }

response = requests.post(
    'https://skillbox-kazan.docrm.org/api/PaymentApi/DownloadConversionEventReport',
    cookies=cookies,
    headers=headers,
    json=json_data,
)
file_data = response.json()["file"]["fileContents"]
with open("file.xlsx", 'wb') as file:
    file.write(bytes(file_data))
