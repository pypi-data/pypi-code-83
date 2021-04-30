from typing import Union

from pandas import Series


class Device:
    def __init__(self,
                 api_level: Union[int, Series] = None,
                 base_os: Union[str, Series] = None,
                 brand: Union[str, Series] = None,
                 manufacturer: Union[str, Series] = None,
                 device: Union[str, Series] = None,
                 product: Union[str, Series] = None,
                 model: Union[str, Series] = None):
        self.api_level = api_level[0] if type(api_level) == Series else api_level
        self.base_os = base_os[0] if type(base_os) == Series else base_os
        self.brand = brand[0] if type(brand) == Series else brand
        self.manufacturer = manufacturer[0] if type(manufacturer) == Series else manufacturer
        self.device = device[0] if type(device) == Series else device
        self.product = product[0] if type(product) == Series else product
        self.model = model[0] if type(model) == Series else model
