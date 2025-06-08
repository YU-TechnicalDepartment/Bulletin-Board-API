# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import requests
import os
import json  # ← 追加

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # ← 日本語のエスケープ防止

@app.route("/post/<int:number>", methods=["GET"])
def get_post(number):
    API_URL = "https://script.google.com/macros/s/AKfycbxdCarkggYZJvshEx07ItNVIV2B3zQ4N910AIjWsUyQ_IGCmo51Gceq_uqimJS1C365eA/exec"
    response = requests.get(API_URL)
    
    if response.status_code != 200:
        return json.dumps({"error": "APIのデータ取得に失敗しました"}, ensure_ascii=False), 500

    data = response.json()

    # 🔹 指定された投稿ナンバーのデータを取得（`+1` を削除）
    if 0 <= number < len(data):
        return json.dumps(data[number], ensure_ascii=False)  # ← 修正
    else:
        return json.dumps({"error": "投稿が見つかりません"}, ensure_ascii=False), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Renderの環境変数 PORT を適用
    app.run(host="0.0.0.0", port=port, threaded=True)  # ✅ Render用設定
