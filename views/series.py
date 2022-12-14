# 모듈 호출
from flask import Blueprint
from flask import render_template

# 앱 설정
branch = "series"
blueprint = Blueprint(branch, __name__, url_prefix=f'/{branch}')


# 프로젝트 메인
@blueprint.route("/")
def series_main():
    return render_template(f"/{branch}/index.html")
