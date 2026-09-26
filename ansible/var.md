# 変数

## 定義と使用

`vars` や `register` に変数を定義して `{{ variable }}` で使用する。

```{literalinclude} ./samples/variables/01-basic.yml
:language: yaml
:lineno-match:
```

```sh
ansible-playbook -i ./samples/inventories/05-connection.yml ./samples/variables/01-basic.yml
```

```text
PLAY [Basic Variable] ***************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************
ok: [192.168.122.161]

TASK [Echo Variable 1] ************************************************************************************************************************************
changed: [192.168.122.161]

TASK [Display Stdout] *************************************************************************************************************************************
ok: [192.168.122.161] => {
    "result.stdout_lines": [
        "1",
        "[a, b]",
        "{key1: 1, key2: 2}"
    ]
}

PLAY RECAP ************************************************************************************************************************************************
192.168.122.161            : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

リストやオブジェクトは結合できる。

```{literalinclude} ./samples/variables/02-combine.yml
:language: yaml
:lineno-match:
```

```sh
ansible-playbook -i ./samples/inventories/05-connection.yml ./samples/variables/02-combine.yml
```

```text
PLAY [Combine Variable] ***********************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************
ok: [192.168.122.161]

TASK [Echo Variable 1] ************************************************************************************************************************************
changed: [192.168.122.161]

TASK [Display Stdout] *************************************************************************************************************************************
ok: [192.168.122.161] => {
    "result.stdout_lines": [
        "{key1: 1, key2: 2}",
        "[1, 2]"
    ]
}

PLAY RECAP ************************************************************************************************************************************************
192.168.122.161            : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## 定義箇所

変数は下記に指定できる。

1. コマンドの引数
2. ロール
3. タスク
4. ブロック
5. プレイ
6. プレイブック
7. インベントリ

優先順位は
[Variable precedence: where should I put a variable?](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable)
を参照する。

## ビルトイン変数

`_task` はタスクの情報が格納される。

```{note}
`register` にハッシュを登録するには ansible-core 2.21 以降が必要
```

```{literalinclude} ./samples/variables/03-task.yml
:language: yaml
:lineno-match:
```

```sh
ansible-playbook -i ./samples/inventories/05-connection.yml ./samples/variables/03-task.yml
```

```text
PLAY [Debug Task] *****************************************************************************************************************************************

TASK [Gathering Facts] ************************************************************************************************************************************
ok: [192.168.122.161]

TASK [Ping the Host] **************************************************************************************************************************************
ok: [192.168.122.161]

TASK [Display Task] ***************************************************************************************************************************************
ok: [192.168.122.161] => {
    "result": "{\"changed\": false, \"failed\": false, \"ping\": \"pong\"}"
}

PLAY RECAP ************************************************************************************************************************************************
192.168.122.161            : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

`ansible_facts` は収集したファクトが格納される。

```{literalinclude} ./samples/playbooks/03-facts.yml
:language: yaml
:lineno-match:
```

```sh
ansible-playbook -i ./samples/inventories/05-connection.yml ./samples/playbooks/03-facts.yml
```

```text
PLAY [Debug Facts] ***************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************
ok: [192.168.122.161]

TASK [Display facts] *************************************************************************************************************************************
ok: [192.168.122.161] => {
    "ansible_facts": {
      ...
    }
}
```

他は
[Discovering variables: facts and magic variables](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_vars_facts.html)
を参照する。
