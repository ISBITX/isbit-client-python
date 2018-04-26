# coding: utf-8
import requests
from .auth import Auth
from .error import IsbitClientError

class IsbitClient:
  def __init__(self, endpoint = "https://isbit.co", access_key = None, secret_key = None, timeout = 60):
    self.endpoint = endpoint
    self.timeout = timeout

    if access_key and secret_key:
      self.access_key = access_key
      self.secret_key = secret_key
      self.auth = Auth(access_key, secret_key)
    else:
      self.auth = False

  def check_auth(self):
    if not self.auth:
      raise IsbitClientError("Missing access key and/or secret key")

  def get_public(self, path, params = None):
    if params is None:
      params = {}
    url = "%s%s" % (self.endpoint, path)

    response = requests.get(url,
      params = params,
      timeout = self.timeout,
      verify = self.endpoint.startswith("https://"))

    return self.response_to_dict(response)

  def get(self, path, params = None):
    if params is None:
      params = {}
    self.check_auth()
    url = "%s%s" % (self.endpoint, path)
    params = self.auth.signed_params("get", path, params)

    response = requests.get(url,
      params = params,
      timeout = self.timeout,
      verify = self.endpoint.startswith("https://"))

    return self.response_to_dict(response)


  def post(self, path, params=None):
    if params is None:
      params = {}
    self.check_auth()
    url = "%s%s" % (self.endpoint, path)
    params = self.auth.signed_params("post", path, params)

    response = requests.post(url,
      data = params,
      timeout = self.timeout,
      verify = self.endpoint.startswith("https://"))

    return self.response_to_dict(response)

  def response_to_dict(self, response):
    # Check the status of the respone
    if str(response.status_code)[0] == '2' : #Every 2xx status is a request success
      try:
        return response.json()
      except ValueError:
        raise IsbitClientError("Invalid response json format: " + response.text) #return the response in plain text
    #if the request does not have success, give the user some light in the matter. 
    # Printing an error code and the response in plain text. 
    # Helps in debugging requests
    elif response.status_code == 500 :
      #the server just returned an error
      raise IsbitClientError('Server internal error 500: \n' + response.text) #return the error
    elif response.status_code == 404 :
      raise IsbitClientError('Not Found. Error: 404')
    #TODO: Verify if exists use case
    #elif response.status_code == 403 :
      #raise IsbitClientError('Wrong place!. Error: 403')
    elif response.status_code == 401 :
      raise IsbitClientError('Unauthorized.  Error 401. Response:  \n' + response.text)
    else:
      raise IsbitClientError('Unknoun error retry in a moment. Error: '+ str(response.status_code) +' \n Response: ' + response.text)

