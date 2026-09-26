# ansible.builtin.script モジュール

管理対象ノードにあるファイルを転送してスクリプトとして実行する。

## スクリプト実行

管理対象ノードでスクリプト *./samples/script-01.sh* を実行する。

```{literalinclude} ./samples/script-01.yml
:language: yaml
:lineno-match:
```

```sh
ansible-playbook -i ./samples/inventories/05-connection.yml ./modules/samples/script-01.yml
```

```text
LAY [script 01] *****************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************
ok: [192.168.122.161]

TASK [Execute Script] ************************************************************************************************************************************
changed: [192.168.122.161]

TASK [Display the result] ********************************************************************************************************************************
ok: [192.168.122.161] => {
    "result": {
        "changed": true,
        "failed": false,
        "rc": 0,
        "stderr": "Shared connection to 192.168.122.161 closed.\r\n",
        "stderr_lines": [
            "Shared connection to 192.168.122.161 closed."
        ],
        "stdout": "Hello, World!\r\n",
        "stdout_lines": [
            "Hello, World!"
        ]
    }
}

PLAY RECAP ***********************************************************************************************************************************************
192.168.122.161            : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## 参考

- [ansible.builtin.script module](https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/script_module.html)
