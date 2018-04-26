# coding:utf-8
import unittest2, sys, io
from isbit_client import IsbitClient, IsbitClientError

def foo(inStr):
    print ("hi"+inStr)

class IsbitClientTestErrorsCase(unittest2.TestCase):
    
  def test_access_bad_request(self):
    with self.assertRaises(IsbitClientError):
      #404
      client = IsbitClient().get_public("/not/a/valid/url")
    #TODO: Verify text in error
    #self.assertTrue('Not Found. Error: 404' in 'Not Found.')

  def test_server_error(self):
    with self.assertRaises(IsbitClientError):
      #500
      client = IsbitClient().get_public('/api/v2/order_book.json/?hello_world=nope&market=btcmx%%B')
    #TODO: Verify text in error
    #self.assertTrue('Server internal error 500: ' in client)

  def test_Unauthorized(self):
    with self.assertRaises(IsbitClientError):
      #401
      client = IsbitClient().get_public('/api/v2/members/me/?access_key=test&tonce=123456789&signature=none')
    #TODO: Verify text in error
    #self.assertTrue('Unauthorized.  Error 401' in context.exception)
    
  #TODO: Error 403 unit test  
    #with self.assertRaises(IsbitClientError):
      #403 No testcase yet!
      #client = IsbitClient().get_public('/api/v2/me.json/?hello_world=nope&market=btcmx%%B')

if __name__ == '__main__':
     unittest2.main()