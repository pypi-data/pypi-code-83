def fields_from_schema(schema_class) -> [str]:
    return [field.name for field in schema_class.fields]
