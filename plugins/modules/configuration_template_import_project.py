#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: configuration_template_import_project
short_description: Resource module for Configuration Template Import Project
description:
- Manage operation create of the resource Configuration Template Import Project.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  doVersion:
    description: DoVersion query parameter. If this flag is true then it creates a new
      version of the template with the imported contents in case if the templates already
      exists. " If this flag is false and if template already exists, then operation
      fails with 'Template already exists' error.
    type: bool
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Configuration Template Import Project reference
  description: Complete reference of the Configuration Template Import Project object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.configuration_template_import_project:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    doVersion: true

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
