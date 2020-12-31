import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

import logging
import os

import firebase_admin
from firebase_admin import auth as firebase_auth
from google.appengine.ext.webapp import template
import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        template_path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(template_path, {}))


app = webapp2.WSGIApplication([('/', MainPage)])
