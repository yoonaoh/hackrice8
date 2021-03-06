#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import time
from google.appengine.api import users
from google.appengine.ext import ndb

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'));

class HomePage(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('homepage.html')
        self.response.write(template.render())

class Dashboard(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('dashboard.html')
        self.response.write(template.render())

class NewEvent(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('new_event.html')
        self.response.write(template.render())

class PersonalAvailability(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('personal_availability.html')
        self.response.write(template.render())

class GroupAvailability(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('group_availability.html')
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/dashboard', Dashboard),
    ('/new_event', NewEvent),
    ('/personal', PersonalAvailability),
    ('/group', GroupAvailability)
], debug=True)
