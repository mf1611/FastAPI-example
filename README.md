## FastAPI example
---
Irisの入力データをPOSTして、予測クラスを返してくれるAPIを作成

1. 環境構築
    ```
    $ poetry install
    ```

2. モデルファイルを作成
    ```
    $ cd app
    $ poetry run train.py
    ```

3. dockerコンテナ上で、fastapiを起動
    ```
    $ cd ..
    $ docker compose up
    ```
    - ローカルで作成したpython環境をpoetryを使って、dockerイメージに移植
    - コンテナを作成し、fastapiを80番ポートで起動
    - コンテナの80番ポートをローカル80番ポートにフォワード
    

4. 下記でテスト
    ```
    $ curl -X POST "http://127.0.0.1:80/predict" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -d "{\"data\":[[4.8,3,1.4,0.3],[2,1,3.2,1.1]]}"
    ```
    - 上記jsonは、シングルクォーテーションだとエラーになるらしく、ダブルクォーテーションにしないとダメっぽい。


    - 下記のレスポンスが返ってくる
    ```
    {"prediction":[0,1],"prediction_proba":[[0.9332040279379453,0.0667941151631344,1.8568989203942778e-06],[0.21173647300340748,0.718823695120584,0.06943983187600865]]}
    ```