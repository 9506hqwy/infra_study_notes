# プラグイン

プラグインはコントロールノード上で動作する Ansible を拡張する機能になる。

## 配置

プラグインは下記に配置する。

- Ansible Collection
- 既定の *plugins* ディレクトリ
  - プラグインの種別ごとにディレクトリは異なる ([Ansible Configuration Settings](https://docs.ansible.com/projects/ansible/latest/reference_appendices/config.html) を参照)。
- ロールディレクトリにあるプラグイン種別ごとのサフィックス *_plugins* のディレクトリ
- プレイブックのディレクトリにあるプラグイン種別ごとのサフィックス *_plugins* のディレクトリ

## 使用

ローカルディレクトリにある `Action` プラグインを使用する。

```{literalinclude} ./samples/plugins/01-mini.yml
:language: yaml
:lineno-match:
```

```sh
ansible-playbook -i ./samples/inventories/05-connection.yml ./samples/plugins/01-mini.yml
```

```text
PLAY [Minimal Ansible Playbook] **************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************
ok: [192.168.122.161]

TASK [Echo a message] ************************************************************************************************************************************
ok: [192.168.122.161]

TASK [Display the result] ********************************************************************************************************************************
ok: [192.168.122.161] => {
    "result": {
        "changed": false,
        "echo": "Hello, World! Hello, World! ",
        "failed": false
    }
}

PLAY RECAP ***********************************************************************************************************************************************
192.168.122.161            : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

```{note}
 `Action` プラグインはリストには表示されない ([Action plugins](https://docs.ansible.com/projects/ansible/latest/plugins/action.html) を参照)。
```
