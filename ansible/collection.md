# コレクション

## 作成

コレクションのひな型を作成する。

```sh
ansible-galaxy collection init local.collection_01
```

```text
- Collection local.collection_01 was created successfully
```

## インストール

ローカルのファイルシステムにあるコレクションをインストールする。

```sh
ansible-galaxy collection install ./local/collection_01
```

```text
Starting galaxy collection install process
Process install dependency map
Starting collection install process
Installing 'local.collection_01:0.1.0' to '/root/.ansible/collections/ansible_collections/local/collection_01'
Created collection for local.collection_01:0.1.0 at /root/.ansible/collections/ansible_collections/local/collection_01
local.collection_01:0.1.0 was installed successfully
```

*requirements.yml* を使用してコレクションをインストールする。

```sh
ansible-galaxy collection install -r requirements.yml
```

```text
Starting galaxy collection install process
Process install dependency map
Starting collection install process
Installing 'local.collection_01:0.1.0' to '/root/.ansible/collections/ansible_collections/local/collection_01'
Created collection for local.collection_01:0.1.0 at /root/.ansible/collections/ansible_collections/local/collection_01
local.collection_01:0.1.0 was installed successfully
```

インストールを確認する。

```sh
ansible-galaxy collection list local.collection_01
```

```text
# /root/.ansible/collections/ansible_collections
Collection          Version
------------------- -------
local.collection_01 0.1.0
```

## アンインストール

コレクションをアンインストールする。

```sh
rm -rf /root/.ansible/collections/ansible_collections/local/collection_01
```

## 使用

```{note}
FQDN で指定できない？
```

プレイレベルにコレクションのロールを使用する。

```{literalinclude} ./samples/collections/01-play.yml
:language: yaml
:lineno-match:
```

```sh
ansible-playbook -i ./samples/inventories/05-connection.yml ./samples/collections/01-play.yml
```

```text
PLAY [Minimal Ansible Playbook] **************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************
ok: [192.168.122.161]

TASK [local.collection_01.01-role : Ping the host] *******************************************************************************************************
ok: [192.168.122.161]

PLAY RECAP ***********************************************************************************************************************************************
192.168.122.161            : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

タスクレベルにコレクションのロールを使用する。

```{literalinclude} ./samples/collections/02-task.yml
:language: yaml
:lineno-match:
```

タスクを確認する。

```sh
ansible-playbook -i ./samples/inventories/05-connection.yml --list-tasks ./samples/collections/02-task.yml
```

```text
playbook: ./samples/collections/02-task.yml

  play #1 (all): Minimal Ansible Playbook       TAGS: []
    tasks:
      local.collection_01.01-role : Ping the host       TAGS: []
      Dynamic Role Include      TAGS: []
```

実行する。

```sh
ansible-playbook -i ./samples/inventories/05-connection.yml ./samples/collections/02-task.yml
```

```text
PLAY [Minimal Ansible Playbook] **************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************
ok: [192.168.122.161]

TASK [local.collection_01.01-role : Ping the host] *******************************************************************************************************
ok: [192.168.122.161]

TASK [Dynamic Role Include] ******************************************************************************************************************************

TASK [local.collection_01.01-role : Ping the host] *******************************************************************************************************
ok: [192.168.122.161]

PLAY RECAP ***********************************************************************************************************************************************
192.168.122.161            : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
