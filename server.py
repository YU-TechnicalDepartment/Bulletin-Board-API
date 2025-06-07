# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # これで日本語などの非 ASCII 文字をエスケープせず返します

@app.route("/post/<int:number>", methods=["GET"])
def get_post(number):
    # APIデータを取得（Google Apps ScriptのAPIからデータを取得）
    API_URL = "https://script.google.com/macros/s/AKfycbxdCarkggYZJvshEx07ItNVIV2B3zQ4N910AIjWsUyQ_IGCmo51Gceq_uqimJS1C365eA/exec"
    response = requests.get(API_URL)
    data = response.json()

    # 指定された投稿ナンバー+1のデータを取得
    if 0 <= number < len(data) - 1:
        return jsonify(data[number + 1])
    else:
        return jsonify({"error": "投稿が見つかりません"}), 404

if __name__ == "__main__":
    app.run(port=3000, threaded=True)n(PORT, () => console.log(`Server running on port ${PORT}`));
