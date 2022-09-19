
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

.. _ansible_collections.ibm.cloud.ibm_iam_access_groups_info_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

ibm.cloud.ibm_iam_access_groups_info module -- Manage ibm\_iam\_access\_groups info.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `ibm.cloud collection <https://galaxy.ansible.com/ibm/cloud>`_ (version 1.0.0-beta0).

    To install it, use: :code:`ansible-galaxy collection install ibm.cloud`.
    You need further requirements to be able to use this module,
    see :ref:`Requirements <ansible_collections.ibm.cloud.ibm_iam_access_groups_info_module_requirements>` for details.

    To use it in a playbook, specify: :code:`ibm.cloud.ibm_iam_access_groups_info`.

.. version_added

.. versionadded:: 1.0.0 of ibm.cloud

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module retrieves one or more ibm\_iam\_access\_groups(s).


.. Aliases


.. Requirements

.. _ansible_collections.ibm.cloud.ibm_iam_access_groups_info_module_requirements:

Requirements
------------
The below requirements are needed on the host that executes this module.

- IamAccessGroupsV2






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
      <div class="ansibleOptionAnchor" id="parameter-account_id"></div>
      <p class="ansible-option-title"><strong>account_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-account_id" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Account ID of the API keys(s) to query.
      If a service IAM ID is specified in iam_id then account_id must match the account of the IAM ID.
      If a user IAM ID is specified in iam_id then then account_id must match the account of the Authorization token.
      </p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-hide_public_access"></div>
      <p class="ansible-option-title"><strong>hide_public_access</strong></p>
      <a class="ansibleOptionLink" href="#parameter-hide_public_access" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>If hide_public_access is true, do not include the Public Access Group in the results.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">false</span></p></li>
        <li><p><span class="ansible-option-choices-entry">true</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-iam_id"></div>
      <p class="ansible-option-title"><strong>iam_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-iam_id" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Return groups for member ID (IBMid, service ID or trusted profile ID).</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-limit"></div>
      <p class="ansible-option-title"><strong>limit</strong></p>
      <a class="ansibleOptionLink" href="#parameter-limit" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Return up to this limit of results where limit is between 0 and 100.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-offset"></div>
      <p class="ansible-option-title"><strong>offset</strong></p>
      <a class="ansibleOptionLink" href="#parameter-offset" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The offset of the first result item to be returned.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-show_federated"></div>
      <p class="ansible-option-title"><strong>show_federated</strong></p>
      <a class="ansibleOptionLink" href="#parameter-show_federated" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>If show_federated is true, each group listed will return an is_federated value that is set to true if rules exist for the group.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">false</span></p></li>
        <li><p><span class="ansible-option-choices-entry">true</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-sort"></div>
      <p class="ansible-option-title"><strong>sort</strong></p>
      <a class="ansibleOptionLink" href="#parameter-sort" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Sort the results by id, name, description, or is_federated flag.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-transaction_id"></div>
      <p class="ansible-option-title"><strong>transaction_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-transaction_id" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>An optional transaction ID can be passed to your request, which can be useful for tracking calls through multiple services by using one identifier.
      The header key must be set to Transaction-Id and the value is anything that you choose.
      If no transaction ID is passed in, then a random ID is generated.
      </p>
    </div></td>
  </tr>
  </tbody>
  </table>



.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    Examples coming soon.




.. Facts


.. Return values


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

