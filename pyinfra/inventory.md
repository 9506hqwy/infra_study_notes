# インベントリ

## 静的なインベントリ

Python スクリプトのインベントリファイルで管理対象ノードを定義する。

グループ名をキーにホストを指定する辞書を定義する。

```{literalinclude} ./samples/inventories/01-static.py
:language: python
:lineno-match:
```

```sh
pyinfra ./samples/inventories/01-static.py debug-inventory
```

```text
--> Loading config...
--> Loading inventory...

[192.168.122.161]
--> Groups: targets, 01-static
--> Data:
{}
--> Disconnecting from hosts...
```

グループは指定したキー名とインベントリファイル名が設定される。

```{note}
ドキュメントには `all` に自動的に含まれるとあるが `all` は存在しない？
```

## 動的なインベントリ

Python の関数で管理対象ノードを定義する。

戻り値はグループ名をキーにホストを指定する辞書を定義する。

```{literalinclude} ./samples/inventories/02-dynamic.py
:language: python
:lineno-match:
```

```sh
pyinfra samples.inventories.02-dynamic.hosts debug-inventory
```

```text
--> Loading config...
--> Loading inventory...
    Loading inventory via import function is in alpha!

[192.168.122.161]
--> Groups: targets
--> Data:
{}

--> Disconnecting from hosts...
```

## 管理対象ノードの接続情報

データで管理対象ノードに接続するための情報を定義する。

利用可能な変数は
[@ssh Connector](https://docs.pyinfra.com/en/3.x/connectors/ssh.html)
を参照する。

SSH 鍵を使用して SSH 接続する方法を指定する。

```{literalinclude} ./samples/inventories/03-connection.py
:language: python
:lineno-match:
```

```sh
pyinfra ./samples/inventories/03-connection.py exec -- echo "Hello, World!"
```

```text
--> Loading config...
--> Loading inventory...
--> Connecting to hosts...
    [192.168.122.161] Connected

--> Preparing exec operation...
    [192.168.122.161] Ready: shell

--> Beginning operation run...
--> Starting operation: server.shell (echo Hello, World!)
[192.168.122.161] Hello, World!
    [192.168.122.161] Success

--> Results:
    Operation                           Hosts   Success   Error   No Change
    server.shell (echo Hello, World!)   1       1         -       -
    Grand total                         1       1         -       -

--> Disconnecting from hosts...
```

SSH 以外に下記の接続方式がある。

- [@docker](https://docs.pyinfra.com/en/3.x/connectors/docker.html)
- [@terraform](https://docs.pyinfra.com/en/3.x/connectors/terraform.html)
- [@local](https://docs.pyinfra.com/en/3.x/connectors/local.html)
