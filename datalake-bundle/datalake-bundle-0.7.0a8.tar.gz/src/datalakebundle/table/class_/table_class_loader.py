from injecta.module import attribute_loader


def load(table_class_path: str):
    last_dot_pos = table_class_path.rfind(".")

    if not last_dot_pos:
        raise Exception(f"Invalid class path: {table_class_path}")

    module_name = table_class_path[:last_dot_pos]
    class_name = table_class_path[last_dot_pos + 1 :]  # noqa: E203

    return attribute_loader.load(module_name, class_name)
