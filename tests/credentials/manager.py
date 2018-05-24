import unittest
from yangsgoogle.credentials.manager import CredentialManager
from yangsgoogle.credentials.service_map import ServiceMap
from yangsutil import log_util
import shutil


class CredentialManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.manager = CredentialManager()

    def test_1_get_credential(self):
        self.assertIsNone(
            self.manager.test_for_get(ServiceMap.TEST, 'test', 'seiren87', '.credential'),
            msg='Empty File Test'
        )

        # print()

        # CredentialGetter.get_credential(CredentialGetter.CALENDAR, 'test', 'seiren87')
        # CredentialGetter.get_credential(CredentialGetter.MAIL, 'test', 'seiren87')
        # CredentialGetter.get_credential(CredentialGetter.DRIVER, 'test', 'seiren87')

    def test_2_get_service_info(self):
        a = ServiceMap.get_service_info('sheet')
        print(a)

    def tearDown(self):
        shutil.rmtree(log_util.LOG_ROOT)
