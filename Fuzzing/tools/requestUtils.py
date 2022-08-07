import requests


def request_code(url, header):
    t = requests.head(url, headers=header)
    code_request = t.status_code
    return code_request


def request_content(url, header):
    text_content = requests.get(url, headers=header).text
    return text_content


def request_header(url, header):
    t2 = requests.get(url, headers=header)
    request_headers = t2.headers
    return request_headers
