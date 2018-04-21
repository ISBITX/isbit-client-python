# coding:utf-8
import unittest2
from isbit_client import StreamingIsbitClient, IsbitClientError

class StreamingIsbitClientTestCase(unittest2.TestCase):
  def test_init(self):
    sc = StreamingIsbitClient(
      access_key= "access",
      secret_key = "secret")
    self.assertEqual("access", sc.access_key)
    self.assertEqual("secret", sc.secret_key)
