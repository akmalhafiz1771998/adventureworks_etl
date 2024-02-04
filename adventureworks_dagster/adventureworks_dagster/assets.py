from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets
from dagster_airbyte import load_assets_from_airbyte_instance

from .constants import dbt_manifest_path
from .constants import airbyte_instance


@dbt_assets(manifest=dbt_manifest_path)
def adventureworks_dwh_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()

airbyte_assets = load_assets_from_airbyte_instance( airbyte_instance,  key_prefix=["public"])  # for key prefix use source schema to make sure there is lineage between dbt model and loaded airbyte dataset