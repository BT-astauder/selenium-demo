# -*- coding: utf-8 -*-

import openerp.tests
from openerp.addons.robotframework.RobotframeworkTest import RobotframeworkTest


@openerp.tests.common.at_install(False)
@openerp.tests.common.post_install(True)
class TestUi(RobotframeworkTest):
    def test_01_robot(self):
        self.robot("/", "tests/mytest.robot", login="admin", fastfail=False)

        # assert 2 == 1
