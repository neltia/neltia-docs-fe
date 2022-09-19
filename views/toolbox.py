# flask lib
from flask import Blueprint
from flask import render_template
from flask import request


# 앱 설정
branch = "tools"
blueprint = Blueprint(branch, __name__, url_prefix=f'/{branch}')


# 메인 페이지
@blueprint.route("/")
def project_main():
    return render_template(f"/{branch}/index.html")
