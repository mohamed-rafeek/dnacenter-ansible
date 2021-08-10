#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: system_performance_info
short_description: Information module for System Performance
description:
- Get all System Performance.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  kpi:
    description:
    - Kpi query parameter. Valid values cpu,memory,network.
    type: str
  function:
    description:
    - Function query parameter. Valid values sum,average,max.
    type: str
  startTime:
    description:
    - >
      StartTime query parameter. This is the epoch start time in milliseconds from which performance indicator
      need to be fetched.
    type: int
  endTime:
    description:
    - >
      EndTime query parameter. This is the epoch end time in milliseconds upto which performance indicator need to
      be fetched.
    type: int
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: System Performance reference
  description: Complete reference of the System Performance object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all System Performance
  cisco.dnac.system_performance_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    kpi: string
    function: string
    startTime: 0
    endTime: 0
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "hostName": "string",
      "version": "string",
      "kpis": {
        "cpu": {
          "units": "string",
          "utilization": "string"
        },
        "memory": {
          "units": "string",
          "utilization": "string"
        },
        "network tx_rate": {
          "units": "string",
          "utilization": "string"
        },
        "network rx_rate": {
          "units": "string",
          "utilization": "string"
        }
      }
    }
"""
