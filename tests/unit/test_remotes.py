# Copyright 2016 Intel
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import tempfile

import testtools

from syntribos.utils.config_fixture import ConfFixture
from syntribos.utils import remotes


@remotes.cache
def fake_method_taking_long_time(name):
    """Fake method to check caching."""
    return 3


class TestRemotes(testtools.TestCase):
    """Basic unit test for testing remote methods."""
    def test_cache(self):
        self.useFixture(ConfFixture())
        self.assertEqual(3, fake_method_taking_long_time("fake"))

    def test_extract_tar(self):
        temp_fh, temp_fn = tempfile.mkstemp()
        abs_path = os.path.abspath(temp_fn)
        path = remotes.extract_tar(abs_path)
        self.assertEqual(abs_path, path)
        os.remove(path)