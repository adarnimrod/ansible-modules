#!/usr/bin/python
DOCUMENTATION = '''
'''

EXAMPLES = '''
'''


def main():
    module = AnsibleModule(argument_spec={})
    result = {'changed': False, 'ansible_facts': {}}
    module.exit_json(**result)

from ansible.module_utils.basic import AnsibleModule
main()
