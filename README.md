server
======================

サーバー構成を管理するAnsibleのコードをここで管理しています。

環境変数
----------------------

このリポジトリを利用するには、以下の環境園数を設定が必要です

| 環境変数名                   | 内容                                                                                      |
| ---------------------------- | ----------------------------------------------------------------------------------------- |
| MACKEREL_API_KEY             | [Mackerel](https://mackerel.io/)のAPIキーを設定します                                     |
| LEXICON_SAKURACLOUD_USERNAME | [さくらのクラウド](https://cloud.sakura.ad.jp/)のアクセストークンを設定します。<br>この設定はLet's EncryptのDNS認証で利用します。             |
| LEXICON_SAKURACLOUD_TOKEN    | [さくらのクラウド](https://cloud.sakura.ad.jp/)のアクセストークンシークレットを設定します。<br>この設定はLet's EncryptのDNS認証で利用します。 |


テスト
----------------------

```
py.test --hosts='ansible://all' -v tests/test_default.py
```

※要[testinfra](https://testinfra.readthedocs.io/)
