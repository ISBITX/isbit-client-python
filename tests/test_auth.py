# coding:utf-8
import unittest2
from isbit_client import auth

class AuthTestCase(unittest2.TestCase):
  def setUp(self):
    self.auth = auth.Auth(
      access_key = "accesskey",
      secret_key = "secretkey")

  def test_signed_challenge(self):
    access_key = "abc"
    challenge = "def"
    secret_key = "ghi"
    a = auth.Auth(
      access_key = access_key,
      secret_key = secret_key)
    signature = a.signed_challenge(challenge)
    self.assertEqual(signature, {
      "auth": {
        "access_key": access_key,
        "answer": "52ca0e5beab532532c62155e78d81c7dc8ad6d6f744cf3797668cf52dd2f9a41",}})

  def test_signed_params(self):
    params = self.auth.signed_params(
      "GET", "/api/v2/orders", params={
        "tonce": 1234567})
    self.assertEqual(params, {
      "tonce": 1234567,
      "access_key": "accesskey",
      "signature": "1b89e3a984c25eacb7439ae644be253b55975e35529ee665966e3b9d8e3dcb2f",})

  def test_sign(self):
    sign = self.auth.sign(
      verb = "get",
      path = "/api/v2/orders",
      params = {
        "tonce": 1234567,
        "access_key": "accesskey",})
    self.assertEqual(sign, "1b89e3a984c25eacb7439ae644be253b55975e35529ee665966e3b9d8e3dcb2f")

  def test_payload(self):
    payload = auth.payload(
      verb = "get",
      path = "/api/v2/markets",
      params = {
        "tonce": 123456789,
        "access_key": "xxx",
        "foo": "bar",})
    self.assertEqual(payload, "GET|/api/v2/markets|access_key=xxx&foo=bar&tonce=123456789")

if __name__ == "__main__":
  unittest2.main()
