
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

.. _ansible_collections.ibm.cloud.ibm_schematics_workspace_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

ibm.cloud.ibm_schematics_workspace module -- Manage \ :literal:`schematics\_workspaces`\  for Schematics Service API.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This module is part of the `ibm.cloud collection <https://galaxy.ansible.com/ibm/cloud>`_ (version 0.0.1-beta0).

    To install it, use: :code:`ansible-galaxy collection install ibm.cloud`.
    You need further requirements to be able to use this module,
    see :ref:`Requirements <ansible_collections.ibm.cloud.ibm_schematics_workspace_module_requirements>` for details.

    To use it in a playbook, specify: :code:`ibm.cloud.ibm_schematics_workspace`.

.. version_added

.. versionadded:: 0.0.1-beta0 of ibm.cloud

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- This module creates, updates, or deletes a \ :literal:`schematics\_workspace`\  resource for Schematics Service API.


.. Aliases


.. Requirements

.. _ansible_collections.ibm.cloud.ibm_schematics_workspace_module_requirements:

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
      <div class="ansibleOptionAnchor" id="parameter-agent_id"></div>
      <p class="ansible-option-title"><strong>agent_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-agent_id" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>agent id which is binded to with the workspace.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-applied_shareddata_ids"></div>
      <p class="ansible-option-title"><strong>applied_shareddata_ids</strong></p>
      <a class="ansibleOptionLink" href="#parameter-applied_shareddata_ids" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>List of applied shared dataset ID.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-catalog_ref"></div>
      <p class="ansible-option-title"><strong>catalog_ref</strong></p>
      <a class="ansibleOptionLink" href="#parameter-catalog_ref" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Information about the software template that you chose from the IBM Cloud catalog. This information is returned for IBM Cloud catalog offerings only.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-catalog_ref/dry_run"></div>
      <p class="ansible-option-title"><strong>dry_run</strong></p>
      <a class="ansibleOptionLink" href="#parameter-catalog_ref/dry_run" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Dry run.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">false</span></p></li>
        <li><p><span class="ansible-option-choices-entry">true</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-catalog_ref/item_icon_url"></div>
      <p class="ansible-option-title"><strong>item_icon_url</strong></p>
      <a class="ansibleOptionLink" href="#parameter-catalog_ref/item_icon_url" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The URL to the icon of the software template in the IBM Cloud catalog.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-catalog_ref/item_id"></div>
      <p class="ansible-option-title"><strong>item_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-catalog_ref/item_id" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The ID of the software template that you chose to install from the IBM Cloud catalog. This software is provisioned with Schematics.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-catalog_ref/item_name"></div>
      <p class="ansible-option-title"><strong>item_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-catalog_ref/item_name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The name of the software that you chose to install from the IBM Cloud catalog.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-catalog_ref/item_readme_url"></div>
      <p class="ansible-option-title"><strong>item_readme_url</strong></p>
      <a class="ansibleOptionLink" href="#parameter-catalog_ref/item_readme_url" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The URL to the readme file of the software template in the IBM Cloud catalog.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-catalog_ref/item_url"></div>
      <p class="ansible-option-title"><strong>item_url</strong></p>
      <a class="ansibleOptionLink" href="#parameter-catalog_ref/item_url" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The URL to the software template in the IBM Cloud catalog.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-catalog_ref/launch_url"></div>
      <p class="ansible-option-title"><strong>launch_url</strong></p>
      <a class="ansibleOptionLink" href="#parameter-catalog_ref/launch_url" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The URL to the dashboard to access your software.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-catalog_ref/offering_version"></div>
      <p class="ansible-option-title"><strong>offering_version</strong></p>
      <a class="ansibleOptionLink" href="#parameter-catalog_ref/offering_version" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The version of the software template that you chose to install from the IBM Cloud catalog.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-catalog_ref/owning_account"></div>
      <p class="ansible-option-title"><strong>owning_account</strong></p>
      <a class="ansibleOptionLink" href="#parameter-catalog_ref/owning_account" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Owning account ID of the catalog.</p>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-dependencies"></div>
      <p class="ansible-option-title"><strong>dependencies</strong></p>
      <a class="ansibleOptionLink" href="#parameter-dependencies" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Workspace dependencies.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-dependencies/children"></div>
      <p class="ansible-option-title"><strong>children</strong></p>
      <a class="ansibleOptionLink" href="#parameter-dependencies/children" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>List of workspace children CRN identifiers.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-dependencies/parents"></div>
      <p class="ansible-option-title"><strong>parents</strong></p>
      <a class="ansibleOptionLink" href="#parameter-dependencies/parents" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>List of workspace parents CRN identifiers.</p>
    </div></td>
  </tr>

  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-description"></div>
      <p class="ansible-option-title"><strong>description</strong></p>
      <a class="ansibleOptionLink" href="#parameter-description" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The description of the workspace.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-destroy_resources"></div>
      <p class="ansible-option-title"><strong>destroy_resources</strong></p>
      <a class="ansibleOptionLink" href="#parameter-destroy_resources" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>If set to <code class='docutils literal notranslate'>true</code>, refreshI(token header configuration is required to delete all the Terraform resources, and the Schematics workspace.
      If set to <code class='docutils literal notranslate'>false</code>, you can remove only the workspace.
      Your Terraform resources are still available and must be managed with the resource dashboard or CLI.
      </p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-location"></div>
      <p class="ansible-option-title"><strong>location</strong></p>
      <a class="ansibleOptionLink" href="#parameter-location" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The location where you want to create your Schematics workspace and run the Schematics jobs.
      The location that you enter must match the API endpoint that you use.
      For example, if you use the Frankfurt API endpoint, you must specify <code class='docutils literal notranslate'>eu-de</code> as your location.
      If you use an API endpoint for a geography and you do not specify a location, Schematics determines the location based on availability.
      </p>
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
      <p>The name of your workspace. The name can be up to 128 characters long and can include alphanumeric characters, spaces, dashes, and underscores.
      When you create a workspace for your own Terraform template,
      consider including the microservice component that you set up with your Terraform template and
      the IBM Cloud environment where you want to deploy your resources in your name.
      </p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-refresh_token"></div>
      <p class="ansible-option-title"><strong>refresh_token</strong></p>
      <a class="ansibleOptionLink" href="#parameter-refresh_token" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The IAM refresh token for the user or service identity.
      The IAM refresh token is required only if you want to destroy the Terraform resources before deleting the Schematics workspace.
      If you want to delete the workspace only and keep all your Terraform resources, refresh token is not required.
      <b>Retrieving refresh token</b><em> Use C(export IBMCLOUDI(API</em>KEY=&lt;ibmcloudI(api)key&gt;),
      and execute <code class='docutils literal notranslate'>curl -X POST &quot;https://iam.cloud.ibm.com/identity/token&quot; -H &quot;Content-Type: application/x-www-form-urlencoded&quot;
      -d &quot;grantI(type=urn:ibm:params:oauth:grant-type:apikey&amp;apikey=$IBMCLOUD</code>APII(KEY&quot; -u bx:bx).)
      For more information, about creating IAM access token and API Docs, refer, [IAM access token](/apidocs/iam-identity-token-api#gettoken-password)
      and [Create API key](/apidocs/iam-identity-token-api#create-api-key).
      <b>Limitation</b> <em> If the token is expired, you can use C(refresh token</em> to get a new IAM access token.)
      The <code class='docutils literal notranslate'>refresh</code>token) parameter cannot be used to retrieve a new IAM access token.
      <em> When the IAM access token is about to expire, use the API key to create a new access token.</em>
      </p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-resource_group"></div>
      <p class="ansible-option-title"><strong>resource_group</strong></p>
      <a class="ansibleOptionLink" href="#parameter-resource_group" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The ID of the resource group where you want to provision the workspace.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-shared_data"></div>
      <p class="ansible-option-title"><strong>shared_data</strong></p>
      <a class="ansibleOptionLink" href="#parameter-shared_data" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Information about the Target used by the templates originating from the IBM Cloud catalog offerings.
      This information is not relevant for workspace created using your own Terraform template.
      </p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-shared_data/cluster_created_on"></div>
      <p class="ansible-option-title"><strong>cluster_created_on</strong></p>
      <a class="ansibleOptionLink" href="#parameter-shared_data/cluster_created_on" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Cluster created on.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-shared_data/cluster_id"></div>
      <p class="ansible-option-title"><strong>cluster_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-shared_data/cluster_id" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The ID of the cluster where you want to provision the resources of all IBM Cloud catalog templates that are included in the catalog offering.
      </p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-shared_data/cluster_name"></div>
      <p class="ansible-option-title"><strong>cluster_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-shared_data/cluster_name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The cluster name.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-shared_data/cluster_type"></div>
      <p class="ansible-option-title"><strong>cluster_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-shared_data/cluster_type" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The cluster type.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-shared_data/entitlement_keys"></div>
      <p class="ansible-option-title"><strong>entitlement_keys</strong></p>
      <a class="ansibleOptionLink" href="#parameter-shared_data/entitlement_keys" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The entitlement key that you want to use to install IBM Cloud entitled software.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-shared_data/namespace"></div>
      <p class="ansible-option-title"><strong>namespace</strong></p>
      <a class="ansibleOptionLink" href="#parameter-shared_data/namespace" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The Kubernetes namespace or OpenShift project
      where the resources of all IBM Cloud catalog templates that are included in the catalog offering are deployed into.
      </p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-shared_data/region"></div>
      <p class="ansible-option-title"><strong>region</strong></p>
      <a class="ansibleOptionLink" href="#parameter-shared_data/region" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The IBM Cloud region that you want to use for the resources of all IBM Cloud catalog templates that are included in the catalog offering.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-shared_data/resource_group_id"></div>
      <p class="ansible-option-title"><strong>resource_group_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-shared_data/resource_group_id" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The ID of the resource group that you want to use for the resources of all IBM Cloud catalog templates that are included in the catalog offering.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-shared_data/worker_count"></div>
      <p class="ansible-option-title"><strong>worker_count</strong></p>
      <a class="ansibleOptionLink" href="#parameter-shared_data/worker_count" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The cluster worker count.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-shared_data/worker_machine_type"></div>
      <p class="ansible-option-title"><strong>worker_machine_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-shared_data/worker_machine_type" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The cluster worker type.</p>
    </div></td>
  </tr>

  <tr class="row-even">
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
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-tags"></div>
      <p class="ansible-option-title"><strong>tags</strong></p>
      <a class="ansibleOptionLink" href="#parameter-tags" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>A list of tags that are associated with the workspace.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data"></div>
      <p class="ansible-option-title"><strong>template_data</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Input data for the Template.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/compact"></div>
      <p class="ansible-option-title"><strong>compact</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/compact" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>True, to use the files from the specified folder &amp; subfolder in your GitHub or GitLab repository
      and ignore the other folders in the repository. For more information,
      see [Compact download for Schematics workspace](https://cloud.ibm.com/docs/schematics?topic=schematics-compact-download&amp;interface=ui).
      </p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">false</span></p></li>
        <li><p><span class="ansible-option-choices-entry">true</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/env_values"></div>
      <p class="ansible-option-title"><strong>env_values</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/env_values" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>A list of environment variables that you want to apply during the execution of a bash script or Terraform job.
      This field must be provided as a list of key-value pairs,
      for example, <b>TFI(LOG=debug</b>. Each entry will be a map with one entry where <code class='docutils literal notranslate'>key is the environment variable name and value is value</code>.
      You can define environment variables for IBM Cloud catalog offerings that are provisioned by using a bash script.
      See [example to use special environment variable](https://cloud.ibm.com/docs/schematics?topic=schematics-set-parallelism#parallelism-example)
      that are supported by Schematics.
      </p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/env_values_metadata"></div>
      <p class="ansible-option-title"><strong>env_values_metadata</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/env_values_metadata" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Environment variables metadata.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/env_values_metadata/hidden"></div>
      <p class="ansible-option-title"><strong>hidden</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/env_values_metadata/hidden" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Environment variable is hidden.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">false</span></p></li>
        <li><p><span class="ansible-option-choices-entry">true</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/env_values_metadata/name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/env_values_metadata/name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Environment variable name.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/env_values_metadata/secure"></div>
      <p class="ansible-option-title"><strong>secure</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/env_values_metadata/secure" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Environment variable is secure.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">false</span></p></li>
        <li><p><span class="ansible-option-choices-entry">true</span></p></li>
      </ul>
    </div></td>
  </tr>

  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/folder"></div>
      <p class="ansible-option-title"><strong>folder</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/folder" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The subfolder in your GitHub or GitLab repository where your Terraform template is stored.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/init_state_file"></div>
      <p class="ansible-option-title"><strong>init_state_file</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/init_state_file" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The content of an existing Terraform statefile that you want to import in to your workspace.
      To get the content of a Terraform statefile for a specific Terraform template in an existing workspace,
      run <code class='docutils literal notranslate'>ibmcloud terraform state pull --id &lt;workspaceI(id&gt; --template &lt;template</code>id&gt;).
      </p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/injectors"></div>
      <p class="ansible-option-title"><strong>injectors</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/injectors" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Array of injectable terraform blocks.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/injectors/injection_type"></div>
      <p class="ansible-option-title"><strong>injection_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/injectors/injection_type" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Injection type. Default is &#x27;override&#x27;.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/injectors/tft_git_token"></div>
      <p class="ansible-option-title"><strong>tft_git_token</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/injectors/tft_git_token" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Token to access the git repository (Optional).</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/injectors/tft_git_url"></div>
      <p class="ansible-option-title"><strong>tft_git_url</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/injectors/tft_git_url" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Git repo url hosting terraform template files.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/injectors/tft_name"></div>
      <p class="ansible-option-title"><strong>tft_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/injectors/tft_name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Terraform template name. Maps to folder name in git repo.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/injectors/tft_parameters"></div>
      <p class="ansible-option-title"><strong>tft_parameters</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/injectors/tft_parameters" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>tft parameters</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/injectors/tft_parameters/name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/injectors/tft_parameters/name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Key name to replace.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/injectors/tft_parameters/value"></div>
      <p class="ansible-option-title"><strong>value</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/injectors/tft_parameters/value" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Value to replace.</p>
    </div></td>
  </tr>

  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/injectors/tft_prefix"></div>
      <p class="ansible-option-title"><strong>tft_prefix</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/injectors/tft_prefix" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Optional prefix word to append to files (Optional).</p>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/type"></div>
      <p class="ansible-option-title"><strong>type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/type" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The Terraform version that you want to use to run your Terraform code.
      Enter <code class='docutils literal notranslate'>terraformI(v1.1</code>) to use Terraform version 1.1, and <code class='docutils literal notranslate'>terraform</code>v1.0) to use Terraform version 1.0. This is a required variable.
      If the Terraform version is not specified, By default, Schematics selects the version from your template. For more information,
      refer to [Terraform version](https://cloud.ibm.com/docs/schematics?topic=schematics-workspace-setup&amp;interface=ui#create-workspaceI(ui).
      </p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/uninstall_script_name"></div>
      <p class="ansible-option-title"><strong>uninstall_script_name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/uninstall_script_name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Uninstall script name.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/values"></div>
      <p class="ansible-option-title"><strong>values</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/values" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>A list of variable values that you want to apply during the Helm chart installation.
      The list must be provided in JSON format.The values that you define here override the default Helm chart values.
      This field is supported only for IBM Cloud catalog offerings that are provisioned by using the Terraform Helm provider.
      </p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/values_metadata"></div>
      <p class="ansible-option-title"><strong>values_metadata</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/values_metadata" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>List of values metadata.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/values_metadata/aliases"></div>
      <p class="ansible-option-title"><strong>aliases</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/values_metadata/aliases" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The list of aliases for the variable name.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/values_metadata/cloud_data_type"></div>
      <p class="ansible-option-title"><strong>cloud_data_type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/values_metadata/cloud_data_type" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Cloud data type of the variable. eg. resourceI(group)id, region, vpcI(id.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/values_metadata/default_value"></div>
      <p class="ansible-option-title"><strong>default_value</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/values_metadata/default_value" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Default value for the variable only if the override value is not specified.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/values_metadata/description"></div>
      <p class="ansible-option-title"><strong>description</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/values_metadata/description" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The description of the meta data.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/values_metadata/group_by"></div>
      <p class="ansible-option-title"><strong>group_by</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/values_metadata/group_by" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The display name of the group this variable belongs to.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/values_metadata/hidden"></div>
      <p class="ansible-option-title"><strong>hidden</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/values_metadata/hidden" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>If <b>true</b>, the variable is not displayed on UI or Command line.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">false</span></p></li>
        <li><p><span class="ansible-option-choices-entry">true</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/values_metadata/immutable"></div>
      <p class="ansible-option-title"><strong>immutable</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/values_metadata/immutable" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Is the variable readonly ?.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">false</span></p></li>
        <li><p><span class="ansible-option-choices-entry">true</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/values_metadata/link_status"></div>
      <p class="ansible-option-title"><strong>link_status</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/values_metadata/link_status" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The status of the link.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">normal</span></p></li>
        <li><p><span class="ansible-option-choices-entry">broken</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/values_metadata/matches"></div>
      <p class="ansible-option-title"><strong>matches</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/values_metadata/matches" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The regex for the variable value.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/values_metadata/max_length"></div>
      <p class="ansible-option-title"><strong>max_length</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/values_metadata/max_length" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The maximum length of the variable value. Applicable for the string type.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/values_metadata/max_value"></div>
      <p class="ansible-option-title"><strong>max_value</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/values_metadata/max_value" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The maximum value of the variable. Applicable for the integer type.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/values_metadata/min_length"></div>
      <p class="ansible-option-title"><strong>min_length</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/values_metadata/min_length" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The minimum length of the variable value. Applicable for the string type.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/values_metadata/min_value"></div>
      <p class="ansible-option-title"><strong>min_value</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/values_metadata/min_value" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The minimum value of the variable. Applicable for the integer type.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/values_metadata/options"></div>
      <p class="ansible-option-title"><strong>options</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/values_metadata/options" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The list of possible values for this variable.
      If type is <b>integer</b> or <b>date</b>, then the array of string is converted to array of integers or date during the runtime.
      </p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/values_metadata/position"></div>
      <p class="ansible-option-title"><strong>position</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/values_metadata/position" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The relative position of this variable in a list.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/values_metadata/required"></div>
      <p class="ansible-option-title"><strong>required</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/values_metadata/required" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>If the variable required?.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">false</span></p></li>
        <li><p><span class="ansible-option-choices-entry">true</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/values_metadata/secure"></div>
      <p class="ansible-option-title"><strong>secure</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/values_metadata/secure" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Is the variable secure or sensitive ?.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">false</span></p></li>
        <li><p><span class="ansible-option-choices-entry">true</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/values_metadata/source"></div>
      <p class="ansible-option-title"><strong>source</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/values_metadata/source" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The source of this meta-data.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/values_metadata/type"></div>
      <p class="ansible-option-title"><strong>type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/values_metadata/type" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Type of the variable.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">boolean</span></p></li>
        <li><p><span class="ansible-option-choices-entry">string</span></p></li>
        <li><p><span class="ansible-option-choices-entry">integer</span></p></li>
        <li><p><span class="ansible-option-choices-entry">date</span></p></li>
        <li><p><span class="ansible-option-choices-entry">array</span></p></li>
        <li><p><span class="ansible-option-choices-entry">list</span></p></li>
        <li><p><span class="ansible-option-choices-entry">map</span></p></li>
        <li><p><span class="ansible-option-choices-entry">complex</span></p></li>
        <li><p><span class="ansible-option-choices-entry">link</span></p></li>
      </ul>
    </div></td>
  </tr>

  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/variablestore"></div>
      <p class="ansible-option-title"><strong>variablestore</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/variablestore" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>VariablesRequest -.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/variablestore/description"></div>
      <p class="ansible-option-title"><strong>description</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/variablestore/description" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The description of your input variable.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/variablestore/name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/variablestore/name" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The name of the variable.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/variablestore/secure"></div>
      <p class="ansible-option-title"><strong>secure</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/variablestore/secure" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>If set to <code class='docutils literal notranslate'>true</code>, the value of your input variable is protected and not returned in your API response.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">false</span></p></li>
        <li><p><span class="ansible-option-choices-entry">true</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/variablestore/type"></div>
      <p class="ansible-option-title"><strong>type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/variablestore/type" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p><code class='docutils literal notranslate'>Terraform v0.11</code> supports <code class='docutils literal notranslate'>string</code>, <code class='docutils literal notranslate'>list</code>, <code class='docutils literal notranslate'>map</code> data type.
      For more information, about the syntax, see [Configuring input variables](https://www.terraform.io/docs/configuration-0-11/variables.html).
      <code class='docutils literal notranslate'>Terraform v0.12</code> additionally, supports <code class='docutils literal notranslate'>bool</code>, <code class='docutils literal notranslate'>number</code> and complex data types such as
      <code class='docutils literal notranslate'>list(type</code>), <code class='docutils literal notranslate'>map(type</code>), <code class='docutils literal notranslate'>object({attribute name=type,..}</code>), <code class='docutils literal notranslate'>set(type</code>), <code class='docutils literal notranslate'>tuple([type]</code>).
      For more information, about the syntax to use the complex data type,
      see [Configuring variables](https://www.terraform.io/docs/configuration/variables.html#type-constraints).
      </p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/variablestore/use_default"></div>
      <p class="ansible-option-title"><strong>use_default</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/variablestore/use_default" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Variable uses default value; and is not over-ridden.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">false</span></p></li>
        <li><p><span class="ansible-option-choices-entry">true</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_data/variablestore/value"></div>
      <p class="ansible-option-title"><strong>value</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_data/variablestore/value" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Enter the value as a string for the primitive types such as <code class='docutils literal notranslate'>bool</code>, <code class='docutils literal notranslate'>number</code>, <code class='docutils literal notranslate'>string</code>, and <code class='docutils literal notranslate'>HCL</code> format for the complex variables,
      as you provide in a <code class='docutils literal notranslate'>.tfvars</code> file <b>You need to enter escaped string of C(HCL</b> format for the complex variable value).
      For more information, about how to declare variables in a terraform configuration file and provide value to schematics,
      see [Providing values for the declared variables](https://cloud.ibm.com/docs/schematics?topic=schematics-create-tf-config#declare-variable).
      </p>
    </div></td>
  </tr>


  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_ref"></div>
      <p class="ansible-option-title"><strong>template_ref</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_ref" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Workspace template ref.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_repo"></div>
      <p class="ansible-option-title"><strong>template_repo</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_repo" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Input variables for the Template repoository, while creating a workspace.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_repo/branch"></div>
      <p class="ansible-option-title"><strong>branch</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_repo/branch" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The repository branch.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_repo/release"></div>
      <p class="ansible-option-title"><strong>release</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_repo/release" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The repository release.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_repo/repo_sha_value"></div>
      <p class="ansible-option-title"><strong>repo_sha_value</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_repo/repo_sha_value" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The repository SHA value.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_repo/repo_url"></div>
      <p class="ansible-option-title"><strong>repo_url</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_repo/repo_url" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The repository URL.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_repo/url"></div>
      <p class="ansible-option-title"><strong>url</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_repo/url" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The source URL.</p>
    </div></td>
  </tr>

  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_repo_update_request_template_repo"></div>
      <p class="ansible-option-title"><strong>template_repo_update_request_template_repo</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_repo_update_request_template_repo" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Input to update the template repository data.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_repo_update_request_template_repo/branch"></div>
      <p class="ansible-option-title"><strong>branch</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_repo_update_request_template_repo/branch" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The repository branch.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_repo_update_request_template_repo/release"></div>
      <p class="ansible-option-title"><strong>release</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_repo_update_request_template_repo/release" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The repository release.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_repo_update_request_template_repo/repo_sha_value"></div>
      <p class="ansible-option-title"><strong>repo_sha_value</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_repo_update_request_template_repo/repo_sha_value" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The repository SHA value.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_repo_update_request_template_repo/repo_url"></div>
      <p class="ansible-option-title"><strong>repo_url</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_repo_update_request_template_repo/repo_url" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The repository URL.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-template_repo_update_request_template_repo/url"></div>
      <p class="ansible-option-title"><strong>url</strong></p>
      <a class="ansibleOptionLink" href="#parameter-template_repo_update_request_template_repo/url" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The source URL.</p>
    </div></td>
  </tr>

  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-type"></div>
      <p class="ansible-option-title"><strong>type</strong></p>
      <a class="ansibleOptionLink" href="#parameter-type" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>List of Workspace type.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-w_id"></div>
      <p class="ansible-option-title"><strong>w_id</strong></p>
      <a class="ansibleOptionLink" href="#parameter-w_id" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The ID of the workspace.  To find the workspace ID, use the <code class='docutils literal notranslate'>GET /v1/workspaces</code> API.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-workspace_status"></div>
      <p class="ansible-option-title"><strong>workspace_status</strong></p>
      <a class="ansibleOptionLink" href="#parameter-workspace_status" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>WorkspaceStatusRequest -.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-workspace_status/frozen"></div>
      <p class="ansible-option-title"><strong>frozen</strong></p>
      <a class="ansibleOptionLink" href="#parameter-workspace_status/frozen" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>If set to true, the workspace is frozen and changes to the workspace are disabled.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">false</span></p></li>
        <li><p><span class="ansible-option-choices-entry">true</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-workspace_status/frozen_at"></div>
      <p class="ansible-option-title"><strong>frozen_at</strong></p>
      <a class="ansibleOptionLink" href="#parameter-workspace_status/frozen_at" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The timestamp when the workspace was frozen.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-workspace_status/frozen_by"></div>
      <p class="ansible-option-title"><strong>frozen_by</strong></p>
      <a class="ansibleOptionLink" href="#parameter-workspace_status/frozen_by" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The user ID that froze the workspace.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-workspace_status/locked"></div>
      <p class="ansible-option-title"><strong>locked</strong></p>
      <a class="ansibleOptionLink" href="#parameter-workspace_status/locked" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>If set to true, the workspace is locked and disabled for changes.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">false</span></p></li>
        <li><p><span class="ansible-option-choices-entry">true</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-workspace_status/locked_by"></div>
      <p class="ansible-option-title"><strong>locked_by</strong></p>
      <a class="ansibleOptionLink" href="#parameter-workspace_status/locked_by" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The user ID that initiated a resource-related job, such as applying or destroying resources, that locked the workspace.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-workspace_status/locked_time"></div>
      <p class="ansible-option-title"><strong>locked_time</strong></p>
      <a class="ansibleOptionLink" href="#parameter-workspace_status/locked_time" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The timestamp when the workspace was locked.</p>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-workspace_status_msg"></div>
      <p class="ansible-option-title"><strong>workspace_status_msg</strong></p>
      <a class="ansibleOptionLink" href="#parameter-workspace_status_msg" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Information about the last job that ran against the workspace. -.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-workspace_status_msg/status_code"></div>
      <p class="ansible-option-title"><strong>status_code</strong></p>
      <a class="ansibleOptionLink" href="#parameter-workspace_status_msg/status_code" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The success or error code that was returned for the last plan, apply, or destroy job that ran against your workspace.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-workspace_status_msg/status_msg"></div>
      <p class="ansible-option-title"><strong>status_msg</strong></p>
      <a class="ansibleOptionLink" href="#parameter-workspace_status_msg/status_msg" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The success or error message that was returned for the last plan, apply, or destroy job that ran against your workspace.</p>
    </div></td>
  </tr>

  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-workspace_status_update_request_workspace_status"></div>
      <p class="ansible-option-title"><strong>workspace_status_update_request_workspace_status</strong></p>
      <a class="ansibleOptionLink" href="#parameter-workspace_status_update_request_workspace_status" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Input to update the workspace status.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-workspace_status_update_request_workspace_status/frozen"></div>
      <p class="ansible-option-title"><strong>frozen</strong></p>
      <a class="ansibleOptionLink" href="#parameter-workspace_status_update_request_workspace_status/frozen" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>If set to true, the workspace is frozen and changes to the workspace are disabled.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">false</span></p></li>
        <li><p><span class="ansible-option-choices-entry">true</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-workspace_status_update_request_workspace_status/frozen_at"></div>
      <p class="ansible-option-title"><strong>frozen_at</strong></p>
      <a class="ansibleOptionLink" href="#parameter-workspace_status_update_request_workspace_status/frozen_at" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Frozen at.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-workspace_status_update_request_workspace_status/frozen_by"></div>
      <p class="ansible-option-title"><strong>frozen_by</strong></p>
      <a class="ansibleOptionLink" href="#parameter-workspace_status_update_request_workspace_status/frozen_by" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Frozen by.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-workspace_status_update_request_workspace_status/locked"></div>
      <p class="ansible-option-title"><strong>locked</strong></p>
      <a class="ansibleOptionLink" href="#parameter-workspace_status_update_request_workspace_status/locked" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Locked status.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">false</span></p></li>
        <li><p><span class="ansible-option-choices-entry">true</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-workspace_status_update_request_workspace_status/locked_by"></div>
      <p class="ansible-option-title"><strong>locked_by</strong></p>
      <a class="ansibleOptionLink" href="#parameter-workspace_status_update_request_workspace_status/locked_by" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Locked by.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-workspace_status_update_request_workspace_status/locked_time"></div>
      <p class="ansible-option-title"><strong>locked_time</strong></p>
      <a class="ansibleOptionLink" href="#parameter-workspace_status_update_request_workspace_status/locked_time" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Locked at.</p>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-x_github_token"></div>
      <p class="ansible-option-title"><strong>x_github_token</strong></p>
      <a class="ansibleOptionLink" href="#parameter-x_github_token" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The personal access token to authenticate with your private GitHub or GitLab repository and access your Terraform template.</p>
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

    
    - name: Create ibm_schematics_workspace
      vars:
        catalog_ref_model:
        dependencies_model:
        shared_target_data_model:
        environment_values_metadata_model:
        inject_terraform_template_inner_tft_parameters_item_model:
        inject_terraform_template_inner_model:
        variable_metadata_model:
        workspace_variable_request_model:
        template_source_data_request_model:
        template_repo_request_model:
        workspace_status_request_model:
      ibm_schematics_workspace:

    - name: Update ibm_schematics_workspace
      vars:
        catalog_ref_model:
        dependencies_model:
        shared_target_data_model:
        environment_values_metadata_model:
        inject_terraform_template_inner_tft_parameters_item_model:
        inject_terraform_template_inner_model:
        variable_metadata_model:
        workspace_variable_request_model:
        template_source_data_request_model:
        template_repo_update_request_model:
        workspace_status_update_request_model:
        workspace_status_message_model:
      ibm_schematics_workspace:

    - name: Delete ibm_schematics_workspace
      ibm_schematics_workspace:




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
      If a resource was created, a <code class='docutils literal notranslate'>WorkspaceResponse</code> object is returned.
      If a resource was updated, a <code class='docutils literal notranslate'>WorkspaceResponse</code> object is returned.
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

