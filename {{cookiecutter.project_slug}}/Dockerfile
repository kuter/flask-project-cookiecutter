FROM python:3.5
ADD . /{{cookiecutter.project_slug}}
WORKDIR /{{cookiecutter.project_slug}}
{% if cookiecutter.docker_pip_extra_index_ip %}
ENV PIP_EXTRA_INDEX_URL=http://{{cookiecutter.docker_pip_extra_index_ip}}/simple/
RUN pip install -r requirements/base.txt --trusted-host {{cookiecutter.docker_pip_extra_index_ip}}
{% else %}
RUN pip install -r requirements/base.txt
{% endif %}
