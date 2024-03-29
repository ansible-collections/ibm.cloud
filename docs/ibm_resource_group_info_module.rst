
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. role:: ansible-attribute-support-label
.. role:: ansible-attribute-support-property
.. role:: ansible-attribute-support-full
.. role:: ansible-attribute-support-partial
.. role:: ansible-attribute-support-none
.. role:: ansible-attribute-support-na
.. role:: ansible-option-type
.. role:: ansible-option-elements
.. role:: ansible-option-required
.. role:: ansible-option-versionadded
.. role:: ansible-option-aliases
.. role:: ansible-option-choices
.. role:: ansible-option-choices-entry
.. role:: ansible-option-default
.. role:: ansible-option-default-bold
.. role:: ansible-option-configuration
.. role:: ansible-option-returned-bold
.. role:: ansible-option-sample-bold

.. Anchors

.. _ansible_collections.ibm.cloud.ibm_resource_group_info_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

ibm.cloud.ibm_resource_group_info module -- Manage \ :literal:`resource\_group`\  for Resource Manager.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `ibm.cloud collection <https://galaxy.ansible.com/ibm/cloud>`_ (version 0.0.1-beta1).

    To install it, use: :code:`ansible-galaxy collection install ibm.cloud`.
    You need further requirements to be able to use this module,
    see :ref:`Requirements <ansible_collections.ibm.cloud.ibm_resource_group_info_module_requirements>` for details.

    To use it in a playbook, specify: :code:`ibm.cloud.ibm_resource_group_info`.

.. version_added

.. versionadded:: 0.0.1-beta0 of ibm.cloud

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module retrieves one or more \ :literal:`resource\_group`\  for Resource Manager.


.. Aliases


.. Requirements

.. _ansible_collections.ibm.cloud.ibm_resource_group_info_module_requirements:

Requirements
------------
The below requirements are needed on the host that executes this module.

- ResourceManagerV2






.. Options

Parameters
----------


.. raw:: html

  <table class="colwidths-auto ansible-option-table docutils align-default" style="width: 100%">
  <thead>
  <tr class="row-odd">
    <th class="head"><p>Parameter</p></th>
    <th class="head"><p>Comments</p></th>
  </tr>
  </thead>
  <tbody>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-id"></div>
      <p class="ansible-option-title"><strong>id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-id" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The short or long ID of the alias.</p>
    </div></td>
  </tr>
  </tbody>
  </table>



.. Attributes


.. Notes

Notes
-----

.. note::
   - Authenticate this module by using an IBM Cloud API key. For more information about working with IBM Cloud API keys, see \ :emphasis:`Managing API keys`\ : \ https://cloud.ibm.com/docs/account?topic%3Daccount-manapikey\ .
   - To configure the authentication, set your IBM Cloud API key on the \ :literal:`IC\_API\_KEY`\  environment variable. The API key will be used to authenticate all IBM Cloud modules that use this environment variable.

.. Seealso

See Also
--------

.. seealso::

   `IBM Cloud Schematics docs <https://cloud.ibm.com/docs/schematics>`_
       Use Schematics to run your Ansible playbooks to provision, configure, and manage IBM Cloud resources.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    

    - name: List ibm_resource_group
      ibm_resource_group_info:
        id: 'testString'




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

  <table class="colwidths-auto ansible-option-table docutils align-default" style="width: 100%">
  <thead>
  <tr class="row-odd">
    <th class="head"><p>Key</p></th>
    <th class="head"><p>Description</p></th>
  </tr>
  </thead>
  <tbody>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-account_id"></div>
      <p class="ansible-option-title"><strong>account_id</strong></p>
      <a class="ansibleOptionLink" href="#return-account_id" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>An alpha-numeric value identifying the account ID.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-created_at"></div>
      <p class="ansible-option-title"><strong>created_at</strong></p>
      <a class="ansibleOptionLink" href="#return-created_at" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The date when the resource group was initially created.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-crn"></div>
      <p class="ansible-option-title"><strong>crn</strong></p>
      <a class="ansibleOptionLink" href="#return-crn" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The full CRN (cloud resource name) associated with the resource group. For more on this format, see [Cloud Resource Names](https://cloud.ibm.com/docs/account?topic=account-crn).</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-default"></div>
      <p class="ansible-option-title"><strong>default</strong></p>
      <a class="ansibleOptionLink" href="#return-default" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Identify if this resource group is default of the account or not.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-id"></div>
      <p class="ansible-option-title"><strong>id</strong></p>
      <a class="ansibleOptionLink" href="#return-id" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>An alpha-numeric value identifying the resource group.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-msg"></div>
      <p class="ansible-option-title"><strong>msg</strong></p>
      <a class="ansibleOptionLink" href="#return-msg" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>an error message that describes what went wrong</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on error</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#return-name" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The human-readable name of the resource group.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-payment_methods_url"></div>
      <p class="ansible-option-title"><strong>payment_methods_url</strong></p>
      <a class="ansibleOptionLink" href="#return-payment_methods_url" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The URL to access the payment methods details that associated with the resource group.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-quota_id"></div>
      <p class="ansible-option-title"><strong>quota_id</strong></p>
      <a class="ansibleOptionLink" href="#return-quota_id" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>An alpha-numeric value identifying the quota ID associated with the resource group.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-quota_url"></div>
      <p class="ansible-option-title"><strong>quota_url</strong></p>
      <a class="ansibleOptionLink" href="#return-quota_url" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The URL to access the quota details that associated with the resource group.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-resource_linkages"></div>
      <p class="ansible-option-title"><strong>resource_linkages</strong></p>
      <a class="ansibleOptionLink" href="#return-resource_linkages" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>An array of the resources that linked to the resource group.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-state"></div>
      <p class="ansible-option-title"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#return-state" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The state of the resource group.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-teams_url"></div>
      <p class="ansible-option-title"><strong>teams_url</strong></p>
      <a class="ansibleOptionLink" href="#return-teams_url" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The URL to access the team details that associated with the resource group.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-updated_at"></div>
      <p class="ansible-option-title"><strong>updated_at</strong></p>
      <a class="ansibleOptionLink" href="#return-updated_at" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The date when the resource group was last updated.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  </tbody>
  </table>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Kavya Handadi (@kavya498)



.. Extra links

Collection links
~~~~~~~~~~~~~~~~

.. raw:: html

  <p class="ansible-links">
    <a href="https://github.com/ansible-collections/ibm.cloud/issues" aria-role="button" target="_blank" rel="noopener external">Issue Tracker</a>
    <a href="https://github.com/ansible-collections/ibm.cloud" aria-role="button" target="_blank" rel="noopener external">Repository (Sources)</a>
  </p>

.. Parsing errors

