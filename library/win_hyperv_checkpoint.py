#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# this is a windows documentation stub. actual code lives in the .ps1
# file of the same name

DOCUMENTATION = '''
---
module: win_hyperv_checkpoint
version_added: "2.4"
short_description: Adds, deletes and performs power functions on Hyper-V VM's.
description:
    - Adds, deletes and performs power functions on Hyper-V VM's.
options:
  name:
    description:
      - Name of VM
    required: true
  state:
    description:
      - State of VM
    required: false
    choices:
      - present
      - absent
	  - started
	  - stopped
    default: present
  hostserver:
    description:
      - Server to host VM
    required: false
    default: null
'''

EXAMPLES = '''
  # Create a VM checkpoint for MyVM on the current Hyper-V Host machine
  win_hyperv_checkpoint:
    name: TestCheckpoint
    vm_name: MyVM

  # Create a VM checkpoint for MyVM which is hosted by HyperV1
  win_hyperv_checkpoint:
    name: TestCheckpoint
    vm_name: MyVM
    hostserver: HyperV1

  # Remove a VM checkpoint for MyVM which is hosted by HyperV1
  win_hyperv_checkpoint:
    name: TestCheckpoint
    vm_name: MyVM
    state: absent
    hostserver: HyperV1

  # Restore a VM checkpoint for MyVM which is hosted by HyperV1
  win_hyperv_checkpoint:
    name: TestCheckpoint
    vm_name: MyVM
    state: restored
    hostserver: HyperV1
'''

ANSIBLE_METADATA = {
    'status': ['preview'],
    'supported_by': 'community',
    'metadata_version': '1.1'
}
