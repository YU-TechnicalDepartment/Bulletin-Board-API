# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import requests
import os  # ← 環境変数の利用に必要

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 日本語のエスケープ防止

@app.route("/post/<int:number>", methods=["GET"])
def get_post(number):
    API_URL = "https://script.google.com/macros/s/AKfycbxdCarkggYZJvshEx07ItNVIV2B3zQ4N910AIjWsUyQ_IGCmo51Gceq_uqimJS1C365eA/exec"
    response = requests.get(API_URL)
    data = response.json()

    if 0 <= number < len(data) - 1:
        return jsonify(data[number + 1])
    else:
        return jsonify({"error": "投稿が見つかりません"}), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Renderの環境変数 PORT を適用
    app.run(host="0.0.0.0", port=port, threaded=True)  # ✅ JavaScriptコードを削除
