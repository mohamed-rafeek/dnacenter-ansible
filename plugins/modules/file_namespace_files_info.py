#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: file_namespace_files_info
short_description: Information module for File Namespace Files
description:
- Get File Namespace Files by name.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  nameSpace:
    description:
    - NameSpace path parameter. A listing of fileId's.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: File Namespace Files reference
  description: Complete reference of the File Namespace Files object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get File Namespace Files by name
  cisco.dnac.file_namespace_files_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    nameSpace: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "attributeInfo": {},
          "downloadPath": "string",
          "encrypted": true,
          "fileFormat": "string",
          "fileSize": "string",
          "id": "string",
          "md5Checksum": "string",
          "name": "string",
          "nameSpace": "string",
          "sftpServerList": [],
          "sha1Checksum": "string",
          "taskId": "string"
        }
      ],
      "version": "string"
    }
"""
