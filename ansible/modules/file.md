# ansible.builtin.file モジュール

管理対象ノードにあるファイルを操作する。

## ファイル削除

管理対象ノードにファイル */tmp/test.txt* を削除する。

```{literalinclude} ./samples/file-01.yml
:language: yaml
:lineno-match:
```

```sh
ansible-playbook -i ./samples/inventories/05-connection.yml ./modules/samples/file-01.yml
```

```text
PLAY [file 01] *******************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************
ok: [192.168.122.161]

TASK [Remove File] ***************************************************************************************************************************************
changed: [192.168.122.161]

PLAY RECAP ***********************************************************************************************************************************************
192.168.122.161            : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## 参考

- [ansible.builtin.file module](https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/file_module.html)
