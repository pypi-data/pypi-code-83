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

import os


def get_file_content(project, fullname):
    path, filename = os.path.split(fullname)

    repository_files = project.repository_tree(path)
    repository_file = next(
        filter(
            lambda repository_file: repository_file.get("name", None) == filename, repository_files
        ),
        None,
    )
    if repository_file is None:
        return None
    else:
        return project.repository_raw_blob(repository_file["id"])
