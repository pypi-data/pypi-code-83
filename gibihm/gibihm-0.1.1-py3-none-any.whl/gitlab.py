# Copyright 2021 Dominik George <nik@naturalnet.de>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""GitLab Issue Bot for Isochronal Heads-up Monitoring - GitLab API wrapper"""

import logging
import os
from functools import lru_cache

from gitlab.client import Gitlab

from . import __version__

logger = logging.getLogger("gibihm")


@lru_cache
def get_gitlab() -> Gitlab:
    """Get a GitLab API client ready to use.

    Configured using environment variables:

    - GIBIHM_API_URL or CI_API_V4_URL for the API endpoint URL
    - GIBIHM_API_TOKEN for the access token
    """
    api_url = os.environ.get("GIBIHM_API_URL", None) or os.environ.get("CI_API_V4_URL", None)
    if api_url:
        # python-gitlab takes only root URL; GitLab CI/CD has /api/v4 suffix in pre-defined variable
        api_url = api_url.removesuffix("/api/v4")
    else:
        raise RuntimeError("GIBIHM_API_URL or CI_API_V4_URL must be set")

    api_token = os.environ.get("GIBIHM_API_TOKEN", None)
    if not api_token:
        raise RuntimeError("GIBIHM_API_TOKEN must be set")

    user_agent = f"gibihm/{__version__}"

    logger.info("Authenticating to GitLab API under %s", api_url)
    gitlab = Gitlab(api_url, private_token=api_token, user_agent=user_agent)
    gitlab.auth()
    logger.info("Authenticated as %s", gitlab.user.name)

    return gitlab
