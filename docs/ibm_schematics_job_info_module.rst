
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

.. _ansible_collections.ibm.cloud.ibm_schematics_job_info_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

ibm.cloud.ibm_schematics_job_info module -- Manage \ :literal:`schematics\_job`\  for Schematics Service API.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `ibm.cloud collection <https://galaxy.ansible.com/ibm/cloud>`_ (version 1.0.0-beta0).

    To install it, use: :code:`ansible-galaxy collection install ibm.cloud`.
    You need further requirements to be able to use this module,
    see :ref:`Requirements <ansible_collections.ibm.cloud.ibm_schematics_job_info_module_requirements>` for details.

    To use it in a playbook, specify: :code:`ibm.cloud.ibm_schematics_job_info`.

.. version_added

.. versionadded:: 1.0.0 of ibm.cloud

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module retrieves one or more \ :literal:`schematics\_job`\  for Schematics Service API.


.. Aliases


.. Requirements

.. _ansible_collections.ibm.cloud.ibm_schematics_job_info_module_requirements:

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
      <div class="ansibleOptionAnchor" id="parameter-job_id"></div>
      <p class="ansible-option-title"><strong>job_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-job_id" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Job Id. Use <code class='docutils literal notranslate'>GET /v2/jobs</code> API to look up the Job Ids in your IBM Cloud account.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-profile"></div>
      <p class="ansible-option-title"><strong>profile</strong></p>
      <a class="ansibleOptionLink" href="#parameter-profile" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Level of details returned by the get method.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">summary</span></p></li>
        <li><p><span class="ansible-option-choices-entry">detailed</span></p></li>
        <li><p><span class="ansible-option-choices-entry">ids</span></p></li>
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

    
    - name: Read ibm_schematics_job
      ibm_schematics_job_info:




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
      In case of &quot;read&quot;, it&#x27;s a <code class='docutils literal notranslate'>Job</code>.</p>
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

