# インベントリ

## 暗黙的なインベントリ

`localhost`, `127.0.0.1`, `::1` はインベントリの定義がない場合は自動的に生成される。

```sh
ansible --list-hosts 127.0.0.1
```

```text
[WARNING]: No inventory was parsed, only implicit localhost is available
  hosts (1):
    127.0.0.1
```

## 静的なインベントリ

ini または yaml 形式のインベントリファイルで管理対象ノードを定義する。

インベントリファイルの既定のパスは */etc/ansible/hosts* となる。
インベントリファイルを指定する場合は `-i` オプションを使用する。

```{literalinclude} ./samples/inventories/01-static.yml
:language: yaml
:lineno-match:
```

```sh
ansible --list-hosts -i ./samples/inventories/01-static.yml targets
```

```text
  hosts (1):
    192.168.122.161
```

## 動的なインベントリ

JSON 形式の出力で管理対象ノードを指定するスクリプトや
インベントリプラグインを利用して管理対象ノードを定義する。

スクリプトの場合は
[ansible.builtin.script inventory](https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/script_inventory.html#script-inventory)
を利用して実装する。

```{literalinclude} ./samples/inventories/02-dynamic.sh
:language: sh
:lineno-match:
```

```sh
ansible --list-hosts -i ./samples/inventories/02-dynamic.sh targets
```

```text
  hosts (1):
    192.168.122.161
```

## グループ

管理対象ノードを 0 個以上のグループに分類して管理できる。

`all`, `ungrouped` はビルトインのグループで `all` はすべてのノード、`ungrouped` はグループに属していないノードが分類される。

グループは親子関係を定義できる。

```{literalinclude} ./samples/inventories/03-group.yml
:language: yaml
:lineno-match:
```

すべてのノードを指定する。

```sh
ansible --list-hosts -i ./samples/inventories/03-group.yml all
```

```text
  hosts (8):
    192.168.255.1
    192.168.255.2
    192.168.2.1
    192.168.2.2
    192.168.1.1
    192.168.1.2
    192.168.3.1
    192.168.3.2
```

グループに属していないノードを指定する。

```sh
ansible --list-hosts -i ./samples/inventories/03-group.yml ungrouped
```

```text
  hosts (2):
    192.168.255.1
    192.168.255.2
```

`group1` に含まれるノードを指定する。

```sh
ansible --list-hosts -i ./samples/inventories/03-group.yml group1
```

```text
  hosts (2):
    192.168.1.1
    192.168.1.2
```

`groupa` に含まれるノードを指定する。

```sh
ansible --list-hosts -i ./samples/inventories/03-group.yml groupa
```

```text
  hosts (5):
    192.168.2.1
    192.168.1.1
    192.168.1.2
    192.168.3.1
    192.168.3.2
```

`group1` または `group2` に含まれるノードを指定する。区切り文字は `,`, `:` が利用できる。

```sh
ansible --list-hosts -i ./samples/inventories/03-group.yml 'group1,group2'
```

```text
  hosts (4):
    192.168.1.1
    192.168.1.2
    192.168.2.1
    192.168.2.2
```

`group2` で `groupa` に含まれているノードを指定する。

```sh
ansible --list-hosts -i ./samples/inventories/03-group.yml 'group2,&groupa'
```

```text
  hosts (1):
    192.168.2.1
```

`group2` で `groupa` に含まれていないノードを指定する。

```sh
ansible --list-hosts -i ./samples/inventories/03-group.yml 'group2,!groupa'
```

```text
  hosts (1):
    192.168.2.2
```

ワイルドカードで複数のノードを指定する。

```sh
ansible --list-hosts -i ./samples/inventories/03-group.yml '192.168.1.*'
```

```text
  hosts (2):
    192.168.1.1
    192.168.1.2
```

## 範囲指定

`[M:N]` の形式で複数のノードを定義できる。

```{literalinclude} ./samples/inventories/04-range.yml
:language: yaml
:lineno-match:
```

```sh
ansible --list-hosts -i ./samples/inventories/04-range.yml targets
```

```text
  hosts (10):
    192.168.0.1
    192.168.0.2
    192.168.0.3
    192.168.0.4
    192.168.0.5
    192.168.0.6
    192.168.0.7
    192.168.0.8
    192.168.0.9
    192.168.0.10
```

## 管理対象ノードの接続情報

変数で管理対象ノードに接続するための情報を定義する。

利用可能な変数は
[Connecting to hosts: behavioral inventory parameters](https://docs.ansible.com/projects/ansible/latest/inventory_guide/intro_inventory.html#connecting-to-hosts-behavioral-inventory-parameters)
を参照する。

SSH 鍵を使用して SSH 接続する方法を指定する。

```{literalinclude} ./samples/inventories/05-connection.yml
:language: yaml
:lineno-match:
```

```sh
ansible -i ./samples/inventories/05-connection.yml targets -m ping
```

```text
192.168.122.161 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```
