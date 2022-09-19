
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

.. _ansible_collections.ibm.cloud.ibm_schematics_resource_query_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

ibm.cloud.ibm_schematics_resource_query module -- Manage \ :literal:`schematics\_resource\_querys`\  for Schematics Service API.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `ibm.cloud collection <https://galaxy.ansible.com/ibm/cloud>`_ (version 1.0.0-beta0).

    To install it, use: :code:`ansible-galaxy collection install ibm.cloud`.
    You need further requirements to be able to use this module,
    see :ref:`Requirements <ansible_collections.ibm.cloud.ibm_schematics_resource_query_module_requirements>` for details.

    To use it in a playbook, specify: :code:`ibm.cloud.ibm_schematics_resource_query`.

.. version_added

.. versionadded:: 1.0.0 of ibm.cloud

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module creates, updates, or deletes a \ :literal:`schematics\_resource\_query`\  resource for Schematics Service API.


.. Aliases


.. Requirements

.. _ansible_collections.ibm.cloud.ibm_schematics_resource_query_module_requirements:

Requirements
------------
The below requirements are needed on the host that executes this module.

- SchematicsV1






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
      <div class="ansibleOptionAnchor" id="parameter-force"></div>
      <p class="ansible-option-title"><strong>force</strong></p>
      <a class="ansibleOptionLink" href="#parameter-force" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Equivalent to -force options in the command line.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">false</span></p></li>
        <li><p><span class="ansible-option-choices-entry">true</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Resource query name.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-propagate"></div>
      <p class="ansible-option-title"><strong>propagate</strong></p>
      <a class="ansibleOptionLink" href="#parameter-propagate" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Auto propagate the chaange or deletion to the dependent resources.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">false</span></p></li>
        <li><p><span class="ansible-option-choices-entry">true</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-queries"></div>
      <p class="ansible-option-title"><strong>queries</strong></p>
      <a class="ansibleOptionLink" href="#parameter-queries" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>queries</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-queries/query_condition"></div>
      <p class="ansible-option-title"><strong>query_condition</strong></p>
      <a class="ansibleOptionLink" href="#parameter-queries/query_condition" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>query_condition</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-queries/query_condition/description"></div>
      <p class="ansible-option-title"><strong>description</strong></p>
      <a class="ansibleOptionLink" href="#parameter-queries/query_condition/description" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Description of resource query param variable.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-queries/query_condition/name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-queries/query_condition/name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Name of the resource query param.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-queries/query_condition/value"></div>
      <p class="ansible-option-title"><strong>value</strong></p>
      <a class="ansibleOptionLink" href="#parameter-queries/query_condition/value" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Value of the resource query param.</p>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-queries/query_select"></div>
      <p class="ansible-option-title"><strong>query_select</strong></p>
      <a class="ansibleOptionLink" href="#parameter-queries/query_select" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>List of query selection parameters.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-queries/query_type"></div>
      <p class="ansible-option-title"><strong>query_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-queries/query_type" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Type of the query(workspaces).</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">workspaces</span></p></li>
      </ul>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-query_id"></div>
      <p class="ansible-option-title"><strong>query_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-query_id" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Resource query Id.  Use <code class='docutils literal notranslate'>GET /v2/resourceI(query</code> API to look up the Resource query definition Ids  in your IBM Cloud account.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-state"></div>
      <p class="ansible-option-title"><strong>state</strong></p>
      <a class="ansibleOptionLink" href="#parameter-state" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Should the resource be present or absent.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-default-bold">present</span> <span class="ansible-option-default">← (default)</span></p></li>
        <li><p><span class="ansible-option-choices-entry">absent</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-type"></div>
      <p class="ansible-option-title"><strong>type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-type" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Resource type (cluster, vsi, icd, vpc).</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">vsi</span></p></li>
      </ul>
    </div></td>
  </tr>
  </tbody>
  </table>



.. Attributes


.. Notes

Notes
-----

.. note::
   - Authenticate this module by using an IBM Cloud API key.
     For more information about working with IBM Cloud API keys, see \ :emphasis:`Managing API keys`\ : \ https://cloud.ibm.com/docs/account?topic%3Daccount-manapikey\ .

   - To configure the authentication, set your IBM Cloud API key on the \ :literal:`IC\_API\_KEY`\  environment variable.
     The API key will be used to authenticate all IBM Cloud modules that use this environment variable.


.. Seealso

See Also
--------

.. seealso::

   `IBM Cloud Schematics docs <U(https://cloud.ibm.com/docs/schematics)>`_
       Use Schematics to run your Ansible playbooks to provision, configure, and manage IBM Cloud resources.

.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create ibm_schematics_resource_query
      vars:
        resource_query_param_model:
        resource_query_model:
      ibm_schematics_resource_query:

    - name: Update ibm_schematics_resource_query
      vars:
        resource_query_param_model:
        resource_query_model:
      ibm_schematics_resource_query:

    - name: Delete ibm_schematics_resource_query
      ibm_schematics_resource_query:




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
      <div class="ansibleOptionAnchor" id="return-msg"></div>
      <p class="ansible-option-title"><strong>msg</strong></p>
      <a class="ansibleOptionLink" href="#return-msg" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>A dictionary that represents the result.
      If a resource was created, a <code class='docutils literal notranslate'>ResourceQueryRecord</code> object is returned.
      If a resource was updated, a <code class='docutils literal notranslate'>ResourceQueryRecord</code> object is returned.
      If a resource was deleted, the <code class='docutils literal notranslate'>id</code> and <code class='docutils literal notranslate'>status</code> fields are returned.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> always</p>
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

