# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, Response
import requests
import os
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 日本語のエスケープ防止

@app.route("/post/<int:number>", methods=["GET"])
def get_post(number):
    API_URL = "https://script.google.com/macros/s/AKfycbxdCarkggYZJvshEx07ItNVIV2B3zQ4N910AIjWsUyQ_IGCmo51Gceq_uqimJS1C365eA/exec"
    response = requests.get(API_URL)

    if response.status_code != 200:
        return Response(json.dumps({"error": "APIのデータ取得に失敗しました"}, ensure_ascii=False), content_type="application/json"), 500

    # ✅ レスポンスのエンコーディングをUTF-8に明示的に設定
    response.encoding = "utf-8"
    data = response.json()

    if 0 <= number < len(data):
        return Response(json.dumps(data[number], ensure_ascii=False), content_type="application/json")  # ✅ 修正
    else:
        return Response(json.dumps({"error": "投稿が見つかりません"}, ensure_ascii=False), content_type="application/json"), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Renderの環境変数 PORT を適用
    app.run(host="0.0.0.0", port=port, threaded=True)  # ✅ Render用設定
