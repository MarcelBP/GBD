#!/usr/bin/python2

import os
import httplib2
import keyring
from oauth2client.client import OAuth2WebServerFlow

class AuthManager:

    def __init__(self, appname, client_id, client_secret, scope, redirect_uri):
        self.appname = appname
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = scope
        self.redirect_uri = redirect_uri

    def request_credentials(self):

        flow = OAuth2WebServerFlow(
                client_id = self.client_id,
                client_secret = self.client_secret,
                scope = self.scope,
                redirect_uri = self.redirect_uri)

        auth_uri = flow.step1_get_authorize_url()
        print("Please visit `{0}' to get secret code.".format(auth_uri))

        code = input("Enter the code: ").strip()
        return flow.step2_exchange(code)

    def get_credentials(self):

        credentials = self.request_credentials()
        return credentials

    def get_auth_http(self, credentials=None):
        if not credentials or credentials.invalid:
            credentials = self.get_credentials()
        return credentials.authorize(httplib2.Http())
