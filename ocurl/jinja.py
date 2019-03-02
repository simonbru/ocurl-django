from django.shortcuts import resolve_url
from django.templatetags.static import static
from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': static,
        'url': resolve_url,
    })

    # jinja2.ext.i18n
    env.install_null_translations(newstyle=True)

    return env
