#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: configuration_template_deploy_status_info
short_description: Information module for Configuration Template Deploy Status
description:
- Get Configuration Template Deploy Status by id.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  deploymentId:
    description:
    - DeploymentId path parameter. UUID of deployment to retrieve template deployment status.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Configuration Template Deploy Status reference
  description: Complete reference of the Configuration Template Deploy Status object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get Configuration Template Deploy Status by id
  cisco.dnac.configuration_template_deploy_status_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deploymentId: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "deploymentId": "string",
      "deploymentName": "string",
      "devices": [
        {
          "detailedStatusMessage": "string",
          "deviceId": "string",
          "duration": "string",
          "endTime": "string",
          "identifier": "string",
          "ipAddress": "string",
          "name": "string",
          "startTime": "string",
          "status": "string",
          "targetType": "string"
        }
      ],
      "duration": "string",
      "endTime": "string",
      "projectName": "string",
      "startTime": "string",
      "status": "string",
      "statusMessage": "string",
      "templateName": "string",
      "templateVersion": "string"
    }
"""
