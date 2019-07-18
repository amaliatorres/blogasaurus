import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('/templates/index.html')
        want_png = {
            "image_url":"/static/images/transparent_pusheen.png",
        }
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render(want_png))

app = webapp2.WSGIApplication([
    ('/', MainPage),

], debug=True)
