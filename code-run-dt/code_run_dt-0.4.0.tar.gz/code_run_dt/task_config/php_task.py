from enum import Enum

from pydantic import BaseModel, Field

from .shared import GenericRunConfig

__all__ = ["PHPTaskConfig", "PHPVersion"]


class PHPVersion(str, Enum):
    """PHP 版本"""

    v8_0_3 = "v8.0.3"
    v8_0_5 = "v8.0.5"


class PHPTaskConfig(BaseModel):
    """PHP 语言任务配置"""

    code: str = Field(..., title="PHP语言代码")
    version: PHPVersion = Field(PHPVersion.v8_0_5, title="PHP版本")
    run: GenericRunConfig = Field(GenericRunConfig(), title="运行配置")
