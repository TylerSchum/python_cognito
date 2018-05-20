#!/usr/bin/python3

""" Module for Connecting to Cognito"""


# ===================== Imports =======================
from warrant import Cognito
# =====================================================
COGNITO_JWKS = 'https://cognito-idp.us-east-2.amazonaws.com/us-east-2_0OPtPekr3/.well-known/jwks.json'

class Connection:
  # ========== Constants =================
  USER_POOL_ID = 'us-east-2_1G6GlgFai'
  CLIENT_ID = 'ojbn3kpl93fsk2rn0mor9mhrp'
  def __init__(self):
    self.user_pool_info = [self.USER_POOL_ID, self.CLIENT_ID]

  def authenticateUser(self, username, password):
    """Method to authenticate user"""
    u = Cognito(self.USER_POOL_ID, self.CLIENT_ID,
                username=username)
    u.authenticate(password=password)
    return u

  def registerUser(self, username, password, email, given_name, family_name, zip_code, timestamp):
    u = Cognito(self.USER_POOL_ID, self.CLIENT_ID)
    u.add_base_attributes(
        email=email, given_name=given_name, family_name=family_name
    )
    u.add_custom_attributes(
      zip_code=zip_code,
      timestamp=timestamp
    )
    u.register(username, password)
    return u

  def login(self, username, password):
    u = Cognito(self.USER_POOL_ID, self.CLIENT_ID, username=username)
    u.authenticate(password=password)
    return u

  def verifyUser(self, username, verificationNumber):
    u = Cognito(self.USER_POOL_ID, self.CLIENT_ID)
    u.confirm_sign_up(verificationNumber, username=username)
    return u

  def updateProfile(self, id_token, refresh_token, access_token, attr_map):
    u = Cognito(self.USER_POOL_ID, self.CLIENT_ID, id_token=id_token, refresh_token=refresh_token, access_token=access_token)
    u.update_profile(attr_map)

  def getUserData(self, username, attr_map):
    u = Cognito(self.USER_POOL_ID, self.CLIENT_ID)
    user = u.get_user(attr_map)
    return user
