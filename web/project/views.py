from flask import render_template, Blueprint, request, url_for, redirect
from web.project.models import Project
from web import db


project = Blueprint("project", __name__)

@project.route("/projects")
@project.route("/projects/index")
def index():
    results = Project.query.all()
    db.session.commit()
    return render_template('projects/index.html', results = results)
    # return "cargar modelo"


@project.route("/projects/create")
def create():
    return render_template('projects/create.html')



@project.route("/projects/insert", methods=["POST"])
def insert():
    title = request.form.get('title')
    description = request.form.get('description')

    project = Project(title, description)

    db.session.add(project)
    db.session.commit()

    return redirect(url_for('project.index'))


@project.route("/projects/edit/<int:id>")
def edit(id):
    result = Project.query.get_or_404(id)
    return render_template('projects/edit.html', result = result)


@project.route("/projects/update/<int:id>", methods=["POST"])
def update(id):
    result = Project.query.get_or_404(id)
    result.title = request.form.get('title')
    result.description = request.form.get('description')

    db.session.add(result)
    db.session.commit()

    return redirect(url_for('project.index'))
