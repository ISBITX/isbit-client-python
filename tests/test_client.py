# coding:utf-8
import unittest2
from isbit_client import IsbitClient, IsbitClientError

class IsbitClientTestCase(unittest2.TestCase):
  def test_access_private_apis_without_keys(self):
    with self.assertRaises(IsbitClientError):
      client = IsbitClient().post("")

  def test_init_with_options(self):
    c = IsbitClient(access_key="access", secret_key="secret")
    self.assertEqual("access", c.access_key)
    self.assertEqual("secret", c.secret_key)

