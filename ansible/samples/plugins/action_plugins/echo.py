from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp  # https://github.com/ansible/ansible/pull/35747

        msg = self._task.args.get("msg", None)

        result["echo"] = msg * 2
        return result
