# 最新月のマネーフォワードの収支内訳取得プログラム
取得先の収支はこちら
https://moneyforward.com/cf/summary

上記URLの収支のtableをseleniumを使ってデータを取得してcsvに出力します。

# 必要ライブラリ
pandas  
selenium

# IDとパスワードの情報
.bashrcにIDとPASSWORDを登録してから実行してください。
```
export MONEYFOWARD="ID"  
export MONEYFOWARD_PASS="PASSWORD"
```

# 使用方法
```
python get_MoneyFowardHousehold.py
```

実行するとseleniumが実行され自動でマネーフォワードにログインし、データ取得します。  
取得し終わったら、収支一覧.csvは生成されます。