# -*- coding: utf-8 -*-

# from jinja2 import Template

# templates = Template("is in {{ platform }}")
# print templates.render(platform='win32')

import sys, os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, 'site-packages/jinja2'))  # 必须添加到jinja2？namibox\share\settings_share.build_django_and_jinja_enviorment中为什么只到jct-site？

from jinja2 import Environment, PackageLoader

def render_to_response(template_name, render):
    env = Environment(loader=PackageLoader('index', 'templates'))  # 加载所有模板到环境中
    template = env.get_template(template_name)  # 从环境中获取模板对象
    return template.render(render)  # 将变量渲染进模板对象

print render_to_response('index.html', {})
print render_to_response('user.html', {'module': 'user'})
print render_to_response('manage.html', {'module': 'manage', 'basehtml': 'user.html'})
