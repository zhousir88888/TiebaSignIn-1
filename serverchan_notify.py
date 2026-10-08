import os
import requests

def serverchan_send(title, desp):
    sendkey = os.getenv("SERVERCHAN_SENDKEY")
    if not sendkey:
        print("⚠️ 未配置SERVERCHAN_SENDKEY，跳过Server酱推送")
        return
    api_url = f"https://sctapi.ftqq.com/{sendkey}.send"
    try:
        resp = requests.post(api_url, data={"title": title, "desp": desp}, timeout=10)
        print(f"✅ Server酱推送返回：{resp.json()}")
    except Exception as err:
        print(f"❌ Server酱推送失败：{str(err)}")
