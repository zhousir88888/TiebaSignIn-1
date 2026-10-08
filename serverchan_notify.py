import os
import requests

def serverchan_send(title, desp):
    sendkey = os.getenv("SERVERCHAN_SENDKEY")
    if not sendkey:
        print("未配置SERVERCHAN_SENDKEY，跳过Server酱推送")
        return
    url = f"https://sctapi.ftqq.com/{sendkey}.send"
    data = {
        "title": title,
        "desp": desp
    }
    try:
        res = requests.post(url, data=data, timeout=10)
        print("Server酱推送结果：", res.json())
    except Exception as e:
        print("Server酱推送失败：", str(e))
