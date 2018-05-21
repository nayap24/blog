from flask import render_template
from . import errors
from .. import db


@errors.app_errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403


@errors.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@errors.app_errorhandler(500)
def internal_error(e):
    db.session.rollback()
    return render_template('500.html'), 500

