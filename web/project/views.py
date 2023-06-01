from flask import render_template, Blueprint
from web.project.models import PROJECTS

project = Blueprint("project", __name__)

@project.route("/projects")
@project.route("/projects/index")
def index():
    return render_template('projects/index.html', projects = PROJECTS)
