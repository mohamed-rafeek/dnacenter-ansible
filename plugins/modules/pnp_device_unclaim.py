#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_device_unclaim
short_description: Resource module for Pnp Device Unclaim
description:
- Manage operation create of the resource Pnp Device Unclaim.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  deviceIdList:
    description: Pnp Device Unclaim's deviceIdList.
    elements: str
    type: list
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Pnp Device Unclaim reference
  description: Complete reference of the Pnp Device Unclaim object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.pnp_device_unclaim:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceIdList:
    - string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "jsonArrayResponse": [],
      "jsonResponse": {},
      "message": "string",
      "statusCode": 0
    }
"""
