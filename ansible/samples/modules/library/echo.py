#!/usr/bin/env python

from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = r'''
---
module: echo
short_description: This is echo module.
description: This is echo module to output message three times.
version_added: "0.1.0"
author:
    - 9506hqwy (97424592+9506hqwy@users.noreply.github.com)
options:
    msg:
        description: This is the message to output.
        required: true
        type: str
'''


def run_module():
    module_args = dict(msg=dict(type="str", required=True))

    result = dict(changed=False, echo="")

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if module.check_mode:
        module.exit_json(**result)

    msg = module.params["msg"]
    result["echo"] = msg * 3

    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
