# ansible.builtin.template モジュール

Jinja2 テンプレートファイルからファイルを作成する。

## ファイル作成

管理対象ノードに変数を反映させて */tmp/template.txt* を作成する。

```{literalinclude} ./samples/template-01.yml
:language: yaml
:lineno-match:
```

```sh
ansible-playbook -i ./samples/inventories/05-connection.yml ./modules/samples/template-01.yml
```

```text
PLAY [template 01] ***************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************
ok: [192.168.122.161]

TASK [Create Template File] ******************************************************************************************************************************
ok: [192.168.122.161]

PLAY RECAP ***********************************************************************************************************************************************
192.168.122.161            : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## 参考

- [ansible.builtin.template module](https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/template_module.html)
