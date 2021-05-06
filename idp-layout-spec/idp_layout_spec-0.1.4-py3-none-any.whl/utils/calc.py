def div(num, dem):
    """
    计算比例，保留4位有效数字
    :param num: 分子
    :param dem: 分母
    :return:
    """
    if dem == 0:
        dem = 0.01
    return round(num / dem, 4)


def aspect_ratio_match(
    src_layer_coordinate: "idp_layout_spec.coordinate.Coordinate",
    target_layer_coordinate: "idp_layout_spec.coordinate.Coordinate",
) -> bool:
    """判断 aspect ratio 是否在 1 的同边"""
    return not (
        (1 > src_layer_coordinate.aspect_ratio)
        ^ (1 > target_layer_coordinate.aspect_ratio)
    )


def aspect_ratio_same_direction(aspect_ratio_1: float, aspect_ratio_2: float) -> bool:
    """判断 aspect ratio 是否在 1 的同边"""
    return not ((1 > aspect_ratio_1) ^ (1 > aspect_ratio_2))


def aspect_ratio_distance(aspect_ratio_1: float, aspect_ratio_2: float) -> float:
    """宽高比距离, 最小为 1"""
    distance = aspect_ratio_1 / aspect_ratio_2
    return distance if distance > 1 else 1 / distance
