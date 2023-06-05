
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
.. role:: ansible-option-choices-default-mark
.. role:: ansible-option-default-bold
.. role:: ansible-option-configuration
.. role:: ansible-option-returned-bold
.. role:: ansible-option-sample-bold

.. Anchors

.. _ansible_collections.ibm.cloud.ibm_resource_quota_info_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

ibm.cloud.ibm_resource_quota_info module -- Manage \ :literal:`resource\_quota`\  for Resource Manager.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `ibm.cloud collection <https://galaxy.ansible.com/ibm/cloud>`_ (version 0.0.1-beta1).

    To install it, use: :code:`ansible-galaxy collection install ibm.cloud`.
    You need further requirements to be able to use this module,
    see :ref:`Requirements <ansible_collections.ibm.cloud.ibm_resource_quota_info_module_requirements>` for details.

    To use it in a playbook, specify: :code:`ibm.cloud.ibm_resource_quota_info`.

.. version_added

.. rst-class:: ansible-version-added

New in ibm.cloud 0.0.1-beta0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module retrieves one or more \ :literal:`resource\_quota`\  for Resource Manager.


.. Aliases


.. Requirements

.. _ansible_collections.ibm.cloud.ibm_resource_quota_info_module_requirements:

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
      <p>The id of the quota.</p>
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

    

    - name: List ibm_resource_quota
      ibm_resource_quota_info:
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
      <div class="ansibleOptionAnchor" id="return-created_at"></div>
      <p class="ansible-option-title"><strong>created_at</strong></p>
      <a class="ansibleOptionLink" href="#return-created_at" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The date when the quota was initially created.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-default_number_of_instances_per_lite_plan"></div>
      <p class="ansible-option-title"><strong>default_number_of_instances_per_lite_plan</strong></p>
      <a class="ansibleOptionLink" href="#return-default_number_of_instances_per_lite_plan" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">float</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Default number of instances per lite plan.</p>
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
      <p>An alpha-numeric value identifying the quota.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-instance_memory"></div>
      <p class="ansible-option-title"><strong>instance_memory</strong></p>
      <a class="ansibleOptionLink" href="#return-instance_memory" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The total memory of app instance.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-instances_per_app"></div>
      <p class="ansible-option-title"><strong>instances_per_app</strong></p>
      <a class="ansibleOptionLink" href="#return-instances_per_app" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">float</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The total instances limit per app.</p>
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
      <p>The human-readable name of the quota.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-number_of_apps"></div>
      <p class="ansible-option-title"><strong>number_of_apps</strong></p>
      <a class="ansibleOptionLink" href="#return-number_of_apps" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">float</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The total app limit.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-number_of_service_instances"></div>
      <p class="ansible-option-title"><strong>number_of_service_instances</strong></p>
      <a class="ansibleOptionLink" href="#return-number_of_service_instances" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">float</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The total service instances limit per app.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-resource_quotas"></div>
      <p class="ansible-option-title"><strong>resource_quotas</strong></p>
      <a class="ansibleOptionLink" href="#return-resource_quotas" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The resource quotas associated with a quota definition.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-resource_quotas/crn"></div>
      <p class="ansible-option-title"><strong>crn</strong></p>
      <a class="ansibleOptionLink" href="#return-resource_quotas/crn" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The full CRN (cloud resource name) associated with the quota. For more on this format, see https://cloud.ibm.com/docs/account?topic=account-crn.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-resource_quotas/id"></div>
      <p class="ansible-option-title"><strong>id</strong></p>
      <a class="ansibleOptionLink" href="#return-resource_quotas/id" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>An alpha-numeric value identifying the quota.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-resource_quotas/limit"></div>
      <p class="ansible-option-title"><strong>limit</strong></p>
      <a class="ansibleOptionLink" href="#return-resource_quotas/limit" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">float</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The limit number of this resource.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-resource_quotas/resource_id"></div>
      <p class="ansible-option-title"><strong>resource_id</strong></p>
      <a class="ansibleOptionLink" href="#return-resource_quotas/resource_id" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The human-readable name of the quota.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-total_app_memory"></div>
      <p class="ansible-option-title"><strong>total_app_memory</strong></p>
      <a class="ansibleOptionLink" href="#return-total_app_memory" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The total app memory capacity.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-type"></div>
      <p class="ansible-option-title"><strong>type</strong></p>
      <a class="ansibleOptionLink" href="#return-type" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The type of the quota.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-updated_at"></div>
      <p class="ansible-option-title"><strong>updated_at</strong></p>
      <a class="ansibleOptionLink" href="#return-updated_at" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The date when the quota was last updated.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> on success for list operation</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-vsi_limit"></div>
      <p class="ansible-option-title"><strong>vsi_limit</strong></p>
      <a class="ansibleOptionLink" href="#return-vsi_limit" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">float</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The VSI limit.</p>
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

