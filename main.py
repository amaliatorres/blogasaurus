import webapp2
import jinja2
import os

post_cont = {}

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

class PostPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('/templates/new_post.html')
        self.response.write(template.render())
    def post(self):
        post_title_var = self.request.get("post_title")
        post_content_var = self.request.get("post_content")
        author_name_var = self.request.get("author_name")
        post_cont["post_title_var"] = post_title_var
        post_cont["post_content_var"] = post_content_var
        post_cont["author_name_var"] = author_name_var
        self.response.write("Thank you for Posting :) !")


class ViewPost(webapp2.RequestHandler):
    def get(self):
        view_template = the_jinja_environment.get_template('/templates/view_post.html')
        self.response.write(view_template.render(post_cont))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/post', PostPage),
    ('/new', ViewPost),

], debug=True)
