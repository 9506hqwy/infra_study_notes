# ansible.builtin.tempfile モジュール

一時ファイルまたはディレクトリを作成する。

## 一時ファイル作成

管理対象ノードの */tmp* に一時ファイルを作成する。

```{literalinclude} ./samples/tempfile-01.yml
:language: yaml
:lineno-match:
```

```sh
ansible-playbook -i ./samples/inventories/05-connection.yml ./modules/samples/tempfile-01.yml
```

```text
PLAY [tempfile 01] ***************************************************************************************************************************************

TASK [Gathering Facts] ***********************************************************************************************************************************
ok: [192.168.122.161]

TASK [Create Temp File] **********************************************************************************************************************************
changed: [192.168.122.161]

TASK [Display the result] ********************************************************************************************************************************
ok: [192.168.122.161] => {
    "result": {
        "changed": true,
        "failed": false,
        "gid": 0,
        "group": "root",
        "mode": "0600",
        "owner": "root",
        "path": "/tmp/ansible.1x7jox1g",
        "secontext": "unconfined_u:object_r:user_tmp_t:s0",
        "size": 0,
        "state": "file",
        "uid": 0
    }
}

PLAY RECAP ***********************************************************************************************************************************************
192.168.122.161            : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## 参考

- [ansible.builtin.tempfile module](https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/tempfile_module.html)
