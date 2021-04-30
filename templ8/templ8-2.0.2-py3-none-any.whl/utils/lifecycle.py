def lifecycle_stage(key: int) -> str:
    """
    >>> lifecycle_stage(1)
    'Planning'

    >>> lifecycle_stage(0)
    'Unknown'
    """
    levels = {
        1: "Planning",
        2: "Pre-Alpha",
        3: "Alpha",
        4: "Beta",
        5: "Production/Stable",
        6: "Mature",
        7: "Inactive",
    }
    return levels[key] if key in range(1, 7) else "Unknown"
