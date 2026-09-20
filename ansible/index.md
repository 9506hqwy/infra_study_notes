# Ansible

## インストール

コントロールノードに ansible をインストールする。

```sh
pip install ansible
```

インストールされた ansible のバージョンを確認する。

```sh
pip list
```

```text
Package             Version
------------------- -------
ansible             8.7.0
ansible-core        2.15.13
cffi                2.0.0
cryptography        50.0.1
importlib-resources 5.0.7
Jinja2              3.1.6
MarkupSafe          3.0.3
packaging           26.3
pip                 26.0.1
pycparser           2.23
PyYAML              6.0.3
resolvelib          1.0.1
setuptools          53.0.0
typing_extensions   4.16.0
```

## 実行

```{toctree}
./inventory.md
./playbook.md
./role.md
./collection.md
```

## 参考

- [Ansible community documentation](https://docs.ansible.com/)
  - [Indexes of all modules and plugins](https://docs.ansible.com/projects/ansible/latest/collections/all_plugins.html)
  - [Collection Index](https://docs.ansible.com/projects/ansible/latest/collections/index.html)
- [Jinja](https://jinja.palletsprojects.com/en/stable/)
