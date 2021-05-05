"""builder.py module."""


class CDSRBuilderException(Exception):
    """CDSRBuilderException."""


def build_collection(metadata: dict) -> str:
    """Builds collection name based on metadata dict."""

    # check metadata type
    if not isinstance(metadata, dict):
        raise CDSRBuilderException(f'Metadata must be a dict, not a `{type(metadata)}`.')

    # mandatory keys
    keys = ['satellite', 'sensor', 'geo_processing', 'radio_processing']

    # get all keys that are missing inside metadata dict
    missing_keys = [k for k in keys if k not in metadata]

    if missing_keys:
        raise CDSRBuilderException(f"Missing keys inside metadata: `{', '.join(missing_keys)}`.")

    return f"{metadata['satellite']}_{metadata['sensor']}_" \
           f"L{metadata['geo_processing']}_{metadata['radio_processing']}"


# def generate_item_name_from_metadata(metadata):
#     # AMAZONIA1_WFI_037016_20210321_L2_DN

#     f"{metadata['satellite']}_"
#     pass
