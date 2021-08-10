#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabric
short_description: Resource module for Sda Fabric
description:
- Manage operations create and delete of the resource Sda Fabric.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  fabricName:
    description: FabricName query parameter. Fabric Name.
    type: str
  payload:
    description: Sda Fabric's payload.
    suboptions:
      fabricName:
        description: Fabric Name.
        type: str
    type: list
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Sda Fabric reference
  description: Complete reference of the Sda Fabric object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Delete all
  cisco.dnac.sda_fabric:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    fabricName: string

- name: Create
  cisco.dnac.sda_fabric:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "status": "string",
      "description": "string",
      "executionStatusUrl": "string"
    }
"""
