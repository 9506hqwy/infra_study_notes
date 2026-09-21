# モジュール

モジュールは管理対象ノード上で動作する Ansible を拡張する機能になる。

## 配置

モジュールは下記に配置する。

- Ansible Collection
- [DEFAULT_MODULE_PATH](https://docs.ansible.com/projects/ansible/latest/reference_appendices/config.html#default-module-path) のディレクトリ
- ロールディレクトリにあるプラグイン種別ごとのサフィックス *library* のディレクトリ
- プレイブックのディレクトリにあるプラグイン種別ごとのサフィックス *library* のディレクトリ

## 使用

ローカルディレクトリにあるモジュールを使用する。

```{literalinclude} ./samples/modules/01-mini.yml
:language: yaml
:lineno-match:
```

```sh
ansible-playbook -i ./samples/inventories/05-connection.yml ./samples/modules/01-mini.yml
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
        "echo": "Hello, World! Hello, World! Hello, World! ",
        "failed": false
    }
}

PLAY RECAP ***********************************************************************************************************************************************
192.168.122.161            : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

プレイブックなしでモジュールを使用する。
モジュールにパスを通すため *library* ディレクトリがあるディレクトリを `--playbook-dir` に指定する。

```sh
ansible -i ./samples/inventories/05-connection.yml --playbook-dir ./samples/modules targets -m echo -a "msg=Hello, "
```

```text
192.168.122.161 | SUCCESS => {
    "changed": false,
    "echo": "Hello,Hello,Hello,"
}
```

## 確認

モジュールの一覧を確認する。

```sh
ansible-doc --playbook-dir ./samples/modules -l | grep echo | head -n 1
```

```text
ansible.legacy.echo
```

モジュールのドキュメントを確認する。

```sh
ansible-doc --playbook-dir ./samples/modules -t module ansible.legacy.echo
```

```text
> ECHO    (/root/projects/infra_study_notes/ansible/samples/modules/library/echo.py)

        This is echo module to output message three times.

ADDED IN: version 0.1.0

OPTIONS (= is mandatory):

= msg
        This is the message to output.
        type: str


AUTHOR: 9506hqwy (97424592+9506hqwy@users.noreply.github.com)
```
