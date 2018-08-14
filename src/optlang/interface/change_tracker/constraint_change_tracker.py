# -*- coding: utf-8 -*-

# Copyright 2017 Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

import logging

from optlang.interface.change_tracker.name_change_tracker import (
    NameChangeTracker,)
from optlang.interface.change_tracker.bounds_change_tracker import (
    BoundsChangeTracker,)
from optlang.interface.change_tracker.expression_change_tracker import (
    ExpressionChangeTracker,)

__all__ = ("ConstraintChangeTracker",)

LOGGER = logging.getLogger(__name__)


class ConstraintChangeTracker(ExpressionChangeTracker, BoundsChangeTracker,
                              NameChangeTracker):

    def __init__(self, **kwargs):
        super(ConstraintChangeTracker, self).__init__(**kwargs)