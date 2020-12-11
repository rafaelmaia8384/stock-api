from flask import Flask, jsonify
import pandas as pd
import talib
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    try:
        j = """
        [
            {
                "open": 10.0,
                "high": 12.0,
                "low": 8.0,
                "close": 9.0
            },
            {
                "open": 10.1,
                "high": 12.3,
                "low": 8.4,
                "close": 9.2
            },
            {
                "open": 10.3,
                "high": 12.6,
                "low": 8.2,
                "close": 9.1
            }
        ]
        """
        rates = json.loads(j)
        df = pd.DataFrame.from_dict(rates)
        print("##########")
        print(df)
        #talib.CDL3OUTSIDE()
        res = talib.CDL3OUTSIDE(df['open'], df['high'], df['low'], df['close'])
        print(res)
        return jsonify({"res": 10})
    except Exception as e:
        print(e)

@app.route("/pattern-candles", methods=["POST"])
def pattern_candles():
    try:
        return jsonify({"error": 0, "msg": "ok"})
    except Exception as e:
        print(e)

@app.route("/pattern-stock", methods=["POST"])
def pattern_stock():
    try:
        return jsonify({"error": 0, "msg": "ok"})
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run(debug=True, port=80)