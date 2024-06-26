#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_dynamic_interface
short_description: Resource module for Wireless Dynamic Interface
description:
- Manage operations create and delete of the resource Wireless Dynamic Interface.
- API to create or update an dynamic interface.
- Delete a dynamic interface.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  interfaceName:
    description: Dynamic-interface name.
    type: str
  vlanId:
    description: Vlan Id.
    type: int
requirements:
- dnacentersdk >= 2.6.0
- python >= 3.9
seealso:
- name: Cisco DNA Center documentation for Wireless CreateUpdateDynamicInterface
  description: Complete reference of the CreateUpdateDynamicInterface API.
  link: https://developer.cisco.com/docs/dna-center/#!create-update-dynamic-interface
- name: Cisco DNA Center documentation for Wireless DeleteDynamicInterface
  description: Complete reference of the DeleteDynamicInterface API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-dynamic-interface
notes:
  - SDK Method used are
    wireless.Wireless.create_update_dynamic_interface,
    wireless.Wireless.delete_dynamic_interface,

  - Paths used are
    post /dna/intent/api/v1/wireless/dynamic-interface,
    delete /dna/intent/api/v1/wireless/dynamic-interface/{interfaceName},

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.wireless_dynamic_interface:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    headers: '{{my_headers | from_json}}'
    interfaceName: string
    vlanId: 0

- name: Delete by name
  cisco.dnac.wireless_dynamic_interface:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    headers: '{{my_headers | from_json}}'
    interfaceName: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  sample: >
    [
      {
        "executionId": "string",
        "executionUrl": "string",
        "message": "string"
      }
    ]
"""
