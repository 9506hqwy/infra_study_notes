# オペレーション

Python スクリプトで必要な処理を定義する。

オペレーションは準備と実行の 2 段階で実行される。
準備ではオペレーションによってどのような処理が行われ、どのような変更が発生するか確認する。
実行では実際に処理を実行する。

```{literalinclude} ./samples/operations/01-mini.py
:language: python
:lineno-match:
```

```sh
pyinfra @local samples/operations/01-mini.py -y
```

```text
--> Loading config...
--> Loading inventory...
--> Connecting to hosts...
    [@local] Connected

--> Preparing operation files...
    Loading: samples/operations/01-mini.py
    [@local] Ready: samples/operations/01-mini.py

--> Skipping change detection
--> Beginning operation run...
--> Starting operation: server.shell (commands=echo Hello, World!)
    [@local] Success

--> Results:
    Operation                                    Hosts   Success   Error   No Change
    server.shell (commands=echo Hello, World!)   1       1         -       -
    Grand total                                  1       1         -       -

--> Disconnecting from hosts...
```

Python スクリプトを使用せず直接オペレーションを指定できる。

```sh
pyinfra @local server.shell commands='echo "Hello, World!"' -y
```

```text
--> Loading config...
--> Loading inventory...
--> Connecting to hosts...
    [@local] Connected

--> Preparing operation func...
    [@local] Ready: shell

--> Skipping change detection
--> Beginning operation run...
--> Starting operation: server.shell (commands=echo "Hello, World!")
    [@local] Success

--> Results:
    Operation                                      Hosts   Success   Error   No Change
    server.shell (commands=echo "Hello, World!")   1       1         -       -
    Grand total                                    1       1         -       -

--> Disconnecting from hosts...
```

## ビルトインコマンド

### debug-inventory

インベントリの情報を出力する。

```sh
pyinfra @local debug-inventory
```

```text
--> Loading config...
--> Loading inventory...

[@local]
--> Groups: @local, @local
--> Data:
{}
--> Disconnecting from hosts...
```

### fact

ファクトを取得する。

```sh
pyinfra @local fact server.LinuxName
```

```text
--> Loading config...
--> Loading inventory...
--> Connecting to hosts...
    [@local] Connected

--> Gathering facts...
    [@local] Loaded fact server.LinuxDistribution

--> Fact data for: server.LinuxName
{
    "@local": "CentOS"
}

--> Disconnecting from hosts...
```

### exec

シェルを実行する。

```sh
pyinfra @local exec -- echo "Hello, World!"
```

```text
--> Loading config...
--> Loading inventory...
--> Connecting to hosts...
    [@local] Connected

--> Preparing exec operation...
    [@local] Ready: shell

--> Beginning operation run...
--> Starting operation: server.shell (echo Hello, World!)
[@local] Hello, World!
    [@local] Success

--> Results:
    Operation                           Hosts   Success   Error   No Change
    server.shell (echo Hello, World!)   1       1         -       -
    Grand total                         1       1         -       -

--> Disconnecting from hosts...
```

## コンディション

Python スクリプトのため `if` 文で分岐できる。

ただし、真偽が処理内で動的に変わる場合は `if` 文ではなく `_if` パラメータを使用する必要がある。
Python スクリプトは準備と実行の両方で実行されるが準備のときは実際に変更は発生しないため
動的に変更される条件を `if` 文にすると処理される内容が異なる。

```{literalinclude} ./samples/operations/02-if.py
:language: python
:lineno-match:
```

```sh
pyinfra @local samples/operations/02-if.py  -y
```

```text
--> Loading config...
--> Loading inventory...
--> Connecting to hosts...
    [@local] Connected

--> Preparing operation files...
    Loading: samples/operations/02-if.py
    [@local] Ready: samples/operations/02-if.py

--> Skipping change detection
--> Beginning operation run...
--> Starting operation: server.shell (commands=echo Static Condition)
    [@local] Success

--> Starting operation: server.shell (commands=echo Dynamic Condition1)
    [@local] No changes

--> Starting operation: files.file (/tmp/test.txt)
    [@local] Success

--> Starting operation: server.shell (commands=echo Dynamic Condition2)
    [@local] Success

--> Results:
    Operation                                         Hosts   Success   Error   No Change
    server.shell (commands=echo Static Condition)     1       1         -       -
    server.shell (commands=echo Dynamic Condition1)   1       -         -       1
    files.file (/tmp/test.txt)                        1       1         -       -
    server.shell (commands=echo Dynamic Condition2)   1       1         -       -
    Grand total                                       4       3         -       1

--> Disconnecting from hosts...
```

## ループ

Python スクリプトの `for` 文を使用すると循環参照になる可能性があるため　`host.loop()` を使用する。

```{literalinclude} ./samples/operations/03-loop.py
:language: python
:lineno-match:
```

```sh
pyinfra @local samples/operations/03-loop.py -y
```

```text
--> Loading config...
--> Loading inventory...
--> Connecting to hosts...
    [@local] Connected

--> Preparing operation files...
    Loading: samples/operations/03-loop.py
    [@local] Ready: samples/operations/03-loop.py

--> Skipping change detection
--> Beginning operation run...
--> Starting operation: server.shell (commands=echo 0)
    [@local] Success

--> Starting operation: server.shell (commands=echo 2)
    [@local] Success

--> Results:
    Operation                        Hosts   Success   Error   No Change
    server.shell (commands=echo 0)   1       1         -       -
    server.shell (commands=echo 2)   1       1         -       -
    Grand total                      2       2         -       -

--> Disconnecting from hosts...
```

## オペレーションのステータス

オペレーションの実行結果を次のオペレーションで使用する。

```{literalinclude} ./samples/operations/04-status.py
:language: python
:lineno-match:
```

```sh
rm -f /tmp/test.txt
pyinfra @local samples/operations/04-status.py -y
```

```text
--> Loading config...
--> Loading inventory...
--> Connecting to hosts...
    [@local] Connected

--> Preparing operation files...
    Loading: samples/operations/04-status.py
    [@local] Ready: samples/operations/04-status.py

--> Skipping change detection
--> Beginning operation run...
--> Starting operation: files.file (/tmp/test.txt)
    [@local] Success

--> Starting operation: files.file (/tmp/test.txt, present=False)
    [@local] Success

--> Results:
    Operation                                   Hosts   Success   Error   No Change
    files.file (/tmp/test.txt)                  1       1         -       -
    files.file (/tmp/test.txt, present=False)   1       1         -       -
    Grand total                                 2       2         -       -

--> Disconnecting from hosts...
```

1 つめのオペレーションで変更がない場合は 2 つめのオペレーションは実行されない。

```sh
touch /tmp/test.txt
pyinfra @local samples/operations/04-status.py -y
```

```text
--> Loading config...
--> Loading inventory...
--> Connecting to hosts...
    [@local] Connected

--> Preparing operation files...
    Loading: samples/operations/04-status.py
    [@local] Ready: samples/operations/04-status.py

--> Skipping change detection
--> Beginning operation run...
--> Starting operation: files.file (/tmp/test.txt)
    [@local] No changes

--> Starting operation: files.file (/tmp/test.txt, present=False)
    [@local] No changes

--> Results:
    Operation                                   Hosts   Success   Error   No Change
    files.file (/tmp/test.txt)                  1       -         -       1
    files.file (/tmp/test.txt, present=False)   1       -         -       1
    Grand total                                 2       -         -       2

--> Disconnecting from hosts...
```

## オペレーションの結果

オペレーションの戻り値を利用して標準出力や標準エラーを次のオペレーションで使用する。
オペレーションの結果を解析する場合はコールバックを使用する。

```{literalinclude} ./samples/operations/05-result.py
:language: python
:lineno-match:
```

```sh
pyinfra @local samples/operations/05-result.py -y
```

```text
--> Loading config...
--> Loading inventory...
--> Connecting to hosts...
    [@local] Connected

--> Preparing operation files...
    Loading: samples/operations/05-result.py
    [@local] Ready: samples/operations/05-result.py

--> Skipping change detection
--> Beginning operation run...
--> Starting operation: server.shell (commands=echo Hello, World!)
    [@local] Success

--> Starting operation: python.call (function=output, result=OperationMeta(executed=False, maybeChange=None, hash=18996c2767e7142774328ef0b335b99342919a9e))
    Starting nested operation: server.shell (commands=echo Hello, World!)
    [@local] nested Success
    [@local] Success

--> Results:
    Operation                                                                                                                              Hosts   Success   Error   No Change
    server.shell (commands=echo Hello, World!)                                                                                             1       1         -       -
    python.call (function=output, result=OperationMeta(executed=False, maybeChange=None, hash=18996c2767e7142774328ef0b335b99342919a9e))   1       1         -       -
    server.shell (commands=echo Hello, World!)                                                                                             1       1         -       -
    Grand total                                                                                                                            3       3         -       -

--> Disconnecting from hosts...
```
