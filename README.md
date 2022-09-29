# IBM Cloud Collection
The Ansible IBM Cloud collection includes a variety of Ansible content to help automate the management of [IBM Cloud](https://cloud.ibm.com/) instances. This collection is maintained by IBM.

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.9.10**.

Plugins and modules within a collection may be tested with only specific Ansible versions.
A collection may contain metadata that identifies these versions.
PEP440 is the schema used to describe the versions of Ansible.
<!--end requires_ansible-->

## Python version compatibility

This collection depends on the respective IBM-Cloud service SDKs for Python ([required SDKs](./requirements.txt)).

This collection has been tested against following Ansible versions: **>=3.9**.

## Included content

<!--start collection content-->
### Modules
|Service|Name |
|--- | --- |
|Catalog Management|[ibm_cm_catalog](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_cm_catalog_module.rst)<br>[ibm_cm_offering](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_cm_offering_module.rst)<br>[ibm_cm_offering_instance](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_cm_offering_instance_module.rst)<br>[ibm_cm_version](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_cm_version_module.rst)|
|IAM Access Group | [ibm_iam_access_group](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_iam_access_group_module.rst)<br>[ibm_iam_access_group_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_iam_access_group_info_module.rst)<br>[ibm_iam_access_group_members](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_iam_access_group_members_module.rst)<br>[ibm_iam_access_group_members_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_iam_access_group_members_info_module.rst)<br>[ibm_iam_access_group_rule](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_iam_access_group_rule_module.rst)<br>[ibm_iam_access_group_rule_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_iam_access_group_rule_info_module.rst)<br>[ibm_iam_access_group_rules_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_iam_access_group_rules_info_module.rst)<br>[ibm_iam_access_groups_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_iam_access_groups_info_module.rst) |
|IAM Identity Services| [ibm_iam_service_id](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_iam_service_id_module.rst)<br>[ibm_iam_service_id_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_iam_service_id_info_module.rst)<br>[ibm_iam_service_ids_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_iam_service_ids_info_module.rst) |
|Resource Manager | [ibm_resource_group](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_resource_group_module.rst)<br>[ibm_resource_group_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_resource_group_info_module.rst)<br>[ibm_resource_groups_info ](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_resource_groups_info_module.rst)<br>[ibm_resource_quota_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_resource_quota_info_module.rst)<br>[ibm_resource_quotas_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_resource_quotas_info_module.rst) |
|Resource Controller | [ibm_resource_instance](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_resource_instance_module.rst)<br>[ibm_resource_instance_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_resource_instance_info_module.rst)<br>[ibm_resource_instances_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_resource_instances_info_module.rst)<br>[ibm_resource_key](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_resource_key_module.rst)<br>[ibm_resource_key_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_resource_key_info_module.rst)<br>[ibm_resource_keys_info ](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_resource_keys_info_module.rst)<br>[ibm_resource_alias](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_resource_alias_module.rst)<br>[ibm_resource_alias_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_resource_alias_info_module.rst)<br>[ibm_resource_aliases_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_resource_aliases_info_module.rst)<br>[ibm_resource_binding](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_resource_binding_module.rst)<br>[ibm_resource_binding_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_resource_binding_info_module.rst)<br>[ibm_resource_bindings_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_resource_bindings_info_module.rst)<br>[ibm_resource_reclamations_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_resource_reclamations_info_module.rst) |
| Schematics | [ibm_schematics_action](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_schematics_action_module.rst)<br>[ibm_schematics_action_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_schematics_action_info_module.rst)<br>[ibm_schematics_inventory](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_schematics_inventory_module.rst)<br>[ibm_schematics_inventory_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_schematics_inventory_info_module.rst)<br>[ibm_schematics_job](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_schematics_job_module.rst)<br>[ibm_schematics_job_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_schematics_job_info_module.rst)<br>[ibm_schematics_resource_query](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_schematics_resource_query_module.rst)<br>[ibm_schematics_resource_query_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_schematics_resource_query_info_module.rst)<br>[ibm_schematics_state_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_schematics_state_info_module.rst)<br>[ibm_schematics_workspace](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_schematics_workspace_module.rst)<br>[ibm_schematics_workspace_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_schematics_workspace_info_module.rst)<br>[ibm_schematics_workspace_activity_info](https://github.com/ansible-collections/ibm.cloud/blob/main/docs/ibm_schematics_workspace_activity_info_module.rst)|


<!--end collection content-->

## Installing this collection

You can install the IBM Cloud collection with the Ansible Galaxy CLI:

    ansible-galaxy collection install ibm.cloud

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: ibm.cloud
```

A specific version of the collection can be installed by using the `version` keyword in the `requirements.yml` file:

```yaml
---
collections:
  - name: ibm.cloud
    version: 1.0.0
```

The python module dependencies are not installed by `ansible-galaxy`.  They can
be manually installed using pip:

    pip install requirements.txt

or:

    pip install ibm-platform-services
    pip install ibm-schematics
    pip install ibm-cloud-sdk-core

## Working locally with this collection
### Prerequisites

1. Install [Python3]

2. [RedHat Ansible] 2.9+

    ```
    pip install "ansible>=2.9.10"
    ```

### Build and Installation
1. Build collection using below command. This will generate a tar.gz file in the current working directory
```bash
ansible-galaxy collection build -f
```
2.  Install the collection using below command.
```bash
ansible-galaxy collection install <above generated tar.gz file name> -f
```
3. The python module dependencies are not installed by ansible-galaxy. They can be manually installed using pip:
```bash
pip install requirements.txt
```

## Using this collection

You can either call modules by their Fully Qualified Collection Namespace (FQCN), such as `ibm.cloud.ibm_resource_group`, or you can call modules by their short name if you list the `ibm.cloud` collection in the playbook's `collections` keyword:

```yaml
---
- name: Create resource Group
      ibm_resource_group:
        name: "{{ resource_group_name }}"
      register: rg_create_output

```

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [IBM Cloud collection repository](https://github.com/ansible-collections/ibm.cloud).



## Release notes
<!--Add a link to a changelog.rst file or an external docsite to cover this information. -->

## Roadmap

<!-- Optional. Include the roadmap for this collection, and the proposed release/versioning strategy so users can anticipate the upgrade/update cycle. -->

## More information

- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Collection Developer Guide](https://docs.ansible.com/ansible/devel/dev_guide/developing_collections.html)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## Licensing

GNU GENERAL PUBLIC LICENSE v3.0 or later.

See [LICENSE](./LICENSE) to see the full text.
