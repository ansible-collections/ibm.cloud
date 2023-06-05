
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

.. _ansible_collections.ibm.cloud.ibm_iam_service_id_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

ibm.cloud.ibm_iam_service_id module -- Manage ibm\_iam\_service\_id resources.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `ibm.cloud collection <https://galaxy.ansible.com/ibm/cloud>`_ (version 0.0.1-beta1).

    To install it, use: :code:`ansible-galaxy collection install ibm.cloud`.
    You need further requirements to be able to use this module,
    see :ref:`Requirements <ansible_collections.ibm.cloud.ibm_iam_service_id_module_requirements>` for details.

    To use it in a playbook, specify: :code:`ibm.cloud.ibm_iam_service_id`.

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

- This module creates, updates, or deletes a ibm\_iam\_service\_id.
- By default the module will look for an existing ibm\_iam\_service\_id.


.. Aliases


.. Requirements

.. _ansible_collections.ibm.cloud.ibm_iam_service_id_module_requirements:

Requirements
------------
The below requirements are needed on the host that executes this module.

- IamIdentityV1






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
      <p>ID of the account the service ID belongs to.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-apikey"></div>
      <p class="ansible-option-title"><strong>apikey</strong></p>
      <a class="ansibleOptionLink" href="#parameter-apikey" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Parameters for the API key in the Create service Id V1 REST request.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-apikey/apikey"></div>
      <p class="ansible-option-title"><strong>apikey</strong></p>
      <a class="ansibleOptionLink" href="#parameter-apikey/apikey" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>You can optionally passthrough the API key value for this API key.
      If passed, NO validation of that apiKey value is done, i.e. the value can be non-URL safe.
      If omitted, the API key management will create an URL safe opaque API key value. The value of the API key is checked for uniqueness.
      Please ensure enough variations when passing in this value.
      </p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-apikey/description"></div>
      <p class="ansible-option-title"><strong>description</strong></p>
      <a class="ansibleOptionLink" href="#parameter-apikey/description" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The optional description of the API key.
      The &#x27;description&#x27; property is only available if a description was provided during a create of an API key.
      </p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-apikey/name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-apikey/name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Name of the API key. The name is not checked for uniqueness.
      Therefore multiple names with the same value can exist. Access is done via the UUID of the API key.
      </p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-apikey/store_value"></div>
      <p class="ansible-option-title"><strong>store_value</strong></p>
      <a class="ansibleOptionLink" href="#parameter-apikey/store_value" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Send true or false to set whether the API key value is retrievable in the future by using the Get details of an API key request.
      If you create an API key for a user, you must specify `false` or omit the value. We don&#x27;t allow storing of API keys for users.
      </p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">false</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">true</code></p></li>
      </ul>

    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-description"></div>
      <p class="ansible-option-title"><strong>description</strong></p>
      <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The optional description of the Service Id.
      The &#x27;description&#x27; property is only available if a description was provided during a create of a Service Id.
      </p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-entity_lock"></div>
      <p class="ansible-option-title"><strong>entity_lock</strong></p>
      <a class="ansibleOptionLink" href="#parameter-entity_lock" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Indicates if the service ID is locked for further write operations. False by default.</p>
    </div></td>
  </tr>
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
      <p>Unique ID of the service ID.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-if_match"></div>
      <p class="ansible-option-title"><strong>if_match</strong></p>
      <a class="ansibleOptionLink" href="#parameter-if_match" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Version of the service ID to be updated.
      Specify the version that you retrieved as entity_tag (ETag header) when reading the service ID.
      This value helps identifying parallel usage of this API. Pass * to indicate to update any version available. This might result in stale updates.
      </p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-include_activity"></div>
      <p class="ansible-option-title"><strong>include_activity</strong></p>
      <a class="ansibleOptionLink" href="#parameter-include_activity" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Defines if the entity&#x27;s activity is included in the response.
      Retrieving activity data is an expensive operation, so please only request this when needed.
      </p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">false</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">true</code></p></li>
      </ul>

    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-include_history"></div>
      <p class="ansible-option-title"><strong>include_history</strong></p>
      <a class="ansibleOptionLink" href="#parameter-include_history" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Defines if the entity history is included in the response.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">false</code></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">true</code></p></li>
      </ul>

    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Name of the Service Id. The name is not checked for uniqueness.
      Therefore multiple names with the same value can exist. Access is done via the UUID of the Service Id.
      </p>
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
        <li><p><code class="ansible-value literal notranslate ansible-option-default-bold">&#34;present&#34;</code> <span class="ansible-option-choices-default-mark">← (default)</span></p></li>
        <li><p><code class="ansible-value literal notranslate ansible-option-choices-entry">&#34;absent&#34;</code></p></li>
      </ul>

    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-unique_instance_crns"></div>
      <p class="ansible-option-title"><strong>unique_instance_crns</strong></p>
      <a class="ansibleOptionLink" href="#parameter-unique_instance_crns" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Optional list of CRNs (string array) which point to the services connected to the service ID.</p>
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

