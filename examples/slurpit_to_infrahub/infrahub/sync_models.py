from __future__ import annotations

from typing import Any

from infrahub_sync.adapters.infrahub import InfrahubModel


# -------------------------------------------------------
# AUTO-GENERATED FILE, DO NOT MODIFY
#  This file has been generated with the command `infrahub-sync generate`
#  All modifications will be lost the next time you reexecute this command
# -------------------------------------------------------
class InfraDevice(InfrahubModel):
    _modelname = "InfraDevice"
    _identifiers = ("hostname",)
    _attributes = ("manufacturer", "location", "device_type", "platform", "fqdn")
    hostname: str
    fqdn: str | None = None
    manufacturer: str | None = None
    location: str | None = None
    device_type: str | None = None
    platform: str | None = None

    local_id: str | None = None
    local_data: Any | None = None


class InfraHardwareInfo(InfrahubModel):
    _modelname = "InfraHardwareInfo"
    _identifiers = ("device", "serial")
    _attributes = ("name", "description", "product", "version")
    name: str
    description: str | None = None
    product: str | None = None
    serial: str | None = None
    version: str | None = None
    device: str

    local_id: str | None = None
    local_data: Any | None = None


class InfraIPAddress(InfrahubModel):
    _modelname = "InfraIPAddress"
    _identifiers = ("address", "prefix")
    _attributes = ("interface",)
    address: str
    interface: str | None = None
    prefix: str | None = None

    local_id: str | None = None
    local_data: Any | None = None


class InfraInterface(InfrahubModel):
    _modelname = "InfraInterface"
    _identifiers = ("device", "name")
    _attributes = ("description", "mac_address")
    name: str
    description: str | None = None
    mac_address: str | None = None
    device: str

    local_id: str | None = None
    local_data: Any | None = None


class InfraPlatform(InfrahubModel):
    _modelname = "InfraPlatform"
    _identifiers = ("name",)
    _attributes = ()
    name: str

    local_id: str | None = None
    local_data: Any | None = None


class InfraPrefix(InfrahubModel):
    _modelname = "InfraPrefix"
    _identifiers = ("vrf", "prefix")
    _attributes = ()
    prefix: str
    vrf: str | None = None

    local_id: str | None = None
    local_data: Any | None = None


class InfraVLAN(InfrahubModel):
    _modelname = "InfraVLAN"
    _identifiers = ("vlan_id", "name")
    _attributes = ()
    name: str | None = None
    vlan_id: int

    local_id: str | None = None
    local_data: Any | None = None


class InfraVRF(InfrahubModel):
    _modelname = "InfraVRF"
    _identifiers = ("name",)
    _attributes = ()
    name: str

    local_id: str | None = None
    local_data: Any | None = None


class InfraVersion(InfrahubModel):
    _modelname = "InfraVersion"
    _identifiers = ("version",)
    _attributes = ("file",)
    version: str
    file: str | None = None

    local_id: str | None = None
    local_data: Any | None = None


class LocationGeneric(InfrahubModel):
    _modelname = "LocationGeneric"
    _identifiers = ("name",)
    _attributes = ("description", "number", "street", "zipcode", "country", "phonenumber", "city", "county", "state")
    name: str
    description: str | None = None
    number: str | None = None
    street: str | None = None
    zipcode: str | None = None
    country: str | None = None
    phonenumber: str | None = None
    city: str | None = None
    county: str | None = None
    state: str | None = None

    local_id: str | None = None
    local_data: Any | None = None


class OrganizationGeneric(InfrahubModel):
    _modelname = "OrganizationGeneric"
    _identifiers = ("name",)
    _attributes = ("type",)
    name: str
    type: str | None = None

    local_id: str | None = None
    local_data: Any | None = None


class TemplateDeviceType(InfrahubModel):
    _modelname = "TemplateDeviceType"
    _identifiers = ("name",)
    _attributes = ("manufacturer",)
    name: str
    manufacturer: str | None = None

    local_id: str | None = None
    local_data: Any | None = None
