import requests

def refund_order(url, r, app_id, session_id):
    # request is passed through from fast-cli
    resp = post(url, json=r, app_id=app_id, session_id=session_id)

    return resp


def post(path, json=None, app_id="", session_id="", params={}, verify=True):
    h = headers(app_id, session_id)
    resp = requests.post(path, json=json, headers=h, params=params, verify=verify)

    return resp

def headers(app_id, session_id):
    h = {
        "x-fast-app": app_id,
        "cookie": session_id,
        "user-agent": "fast-scripts"
    }

    return h
