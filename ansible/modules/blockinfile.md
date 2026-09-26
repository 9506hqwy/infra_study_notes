# ansible.builtin.blockinfile モジュール

`marker` で囲まれたでテキストブロックを挿入する。

## テキストブロック挿入

管理対象ノードに下記をファイル */tmp/test.txt* を用意する。

```text
line 0
line 3
```

`line 0` の次の行にテキストブロックを挿入する。

```{literalinclude} ./samples/blockinfile-01.yml
:language: yaml
:lineno-match:
```

```sh
ansible-playbook -i ./samples/inventories/05-connection.yml ./modules/samples/blockinfile-01.yml
```

```text
PLAY [blockinfile 01] ************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************
ok: [192.168.122.161]

TASK [Insert Text Block] *********************************************************************************************************************************
changed: [192.168.122.161]

PLAY RECAP ***********************************************************************************************************************************************
192.168.122.161            : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

結果は下記になる。

```text
line 0
# BEGIN ANSIBLE MANAGED BLOCK
line 1
line 2
# END ANSIBLE MANAGED BLOCK
line 3
```

## 参考

- [ansible.builtin.blockinfile module](https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/blockinfile_module.html)
