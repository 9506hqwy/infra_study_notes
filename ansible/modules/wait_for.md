# ansible.builtin.wait_for モジュール

条件が整うまで待つ。

## スリープ

コントローラノードでスリープする。

```{literalinclude} ./samples/wait_for-01.yml
:language: yaml
:lineno-match:
```

```sh
ansible-playbook -i ./samples/inventories/05-connection.yml ./modules/samples/wait_for-01.yml
```

```text
PLAY [wait_for 01] ***************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************
ok: [192.168.122.161]

TASK [Wait for Timeout on Controller] ********************************************************************************************************************
ok: [192.168.122.161 -> localhost]

PLAY RECAP ***********************************************************************************************************************************************
192.168.122.161            : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## 参考

- [ansible.builtin.wait_for module](https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/wait_for_module.html)
