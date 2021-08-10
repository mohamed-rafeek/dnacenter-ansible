#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_multicast_info
short_description: Information module for Sda Multicast
description:
- Get all Sda Multicast.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  fabricSiteNameHierarchy:
    description:
    - FabricSiteNameHierarchy query parameter.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Sda Multicast reference
  description: Complete reference of the Sda Multicast object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Sda Multicast
  cisco.dnac.sda_multicast_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    fabricSiteNameHierarchy: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "fabricSiteNameHierarchy": "string",
      "multicastMethod": "string",
      "muticastType": "string",
      "multicastVnInfo": {
        "virtualNetworkName": "string",
        "ipPoolName": "string",
        "externalRpIpAddress": "string",
        "ssmInfo": {},
        "ssmGroupRange": "string",
        "ssmWildcardMask": "string"
      }
    }
"""
