# ansible.builtin.copy モジュール

コントローラノードと管理対象ノードの間でファイルまたはディレクトリを転送する。

## ファイルコピー

管理対象ノードにファイル *./samples/copy-01.txt* を転送する。

```{literalinclude} ./samples/copy-01.yml
:language: yaml
:lineno-match:
```

```sh
ansible-playbook -i ./samples/inventories/05-connection.yml ./modules/samples/copy-01.yml
```

```text
PLAY [copy 01] *******************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************
ok: [192.168.122.161]

TASK [Copy File] *****************************************************************************************************************************************
changed: [192.168.122.161]

PLAY RECAP ***********************************************************************************************************************************************
192.168.122.161            : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## 参考

- [ansible.builtin.copy module](https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/copy_module.html)
