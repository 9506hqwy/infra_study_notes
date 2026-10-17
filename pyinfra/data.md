# データ

データに任意の値を定義してオペレーションで使用する。

## 優先順位

データは下記の優先順で定義できる。

1. CLI
2. ホスト
3. グループ
4. `all` グループ

```{literalinclude} ./samples/data/01-print.py
:language: python
:lineno-match:
```

```sh
pyinfra ./samples/data/01-static.py ./samples/data/01-print.py --data KEY1="CLI VALUE"
```

```text
--> Loading config...
--> Loading inventory...
--> Connecting to hosts...
    [192.168.122.161] Connected

--> Preparing operation files...
    Loading: ./samples/data/01-print.py
CLI VALUE
HOST VALUE
GROUP VALUE
ALL VALUE
    [192.168.122.161] Ready: ./samples/data/01-print.py

--> Detected changes:
    Operation   Change   Conditional Change

    Detected changes may not include every change pyinfra will execute.
    Hidden side effects of operations may alter behaviour of future operations,
    this will be shown in the results. The remote state will always be updated
    to reflect the state defined by the input operations.

    Detected changes displayed above, skip this step with -y

--> Beginning operation run...
--> Results:
    Operation     Hosts   Success   Error   No Change
    Grand total   -       -         -       -

--> Disconnecting from hosts...
```

## グループのデータ

グループのデータは下記に定義できる。

- インベントリファイル
- インベントリファイルがあるディレクトリの `group_data` ディレクトリにある *<グループ名>.py* ファイル

インベントリファイルにはグループの定義をタプルで定義する。

```python
group = (
  [
    # ホストを定義
  ],
  {
    "キー": "値",
  }
)
```

`group_data` ディレクトリにある *<グループ名>.py*　には `KEY=VALUE` 形式で定義する。

```python
キー = "値"
```

```{note}
動的インベントリの場合は既定の `group_data` ディレクトリは読み込まない。
ディレクトリを変更するには `---group-data` オプションを使用する。
```

## 環境変数

管理対象ノードに環境変数を設定して操作する。

環境変数は下記の優先順で定義できる。

1. オペレーションの `_env` 引数
2. `config.ENV`
3. `pyinfra` 実行時のコントローラノード (`config.INHERIT_ENV` で引き継ぐ環境変数を設定)

```{literalinclude} ./samples/data/02-env.py
:language: python
:lineno-match:
```

```sh
export KEY1="ENV VALUE"
export KEY2="ENV VALUE"
export KEY3="ENV VALUE"
pyinfra ./samples/data/01-static.py ./samples/data/02-env.py -y
```

```text
--> Loading config...
--> Loading inventory...
--> Connecting to hosts...
    [192.168.122.161] Connected

--> Preparing operation files...
    Loading: ./samples/data/02-env.py
    [192.168.122.161] Ready: ./samples/data/02-env.py

--> Skipping change detection
--> Beginning operation run...
--> Starting operation: Print environment KEY
    [192.168.122.161] Success

--> Starting operation: Display output
    ARG VALUE
CONFIG VALUE
ENV VALUE
    [192.168.122.161] Success

--> Results:
    Operation               Hosts   Success   Error   No Change
    Print environment KEY   1       1         -       -
    Display output          1       1         -       -
    Grand total             2       2         -       -

--> Disconnecting from hosts...
```
