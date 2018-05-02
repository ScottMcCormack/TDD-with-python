import random
from fabric.contrib.files import append, exists
from fabric.api import cd, env, local, run

REPO_URL = "https://github.com/ScottMcCormack/TDD-with-python.git"

def deploy():
    site_folder = "/home/{0}/sites/{1}".format(env.user, env.host)
    run("mkdir - p {0}".format(site_folder))
    with cd(site_folder):
        _get_latest_source()
        _update_virtualenv()
        _create_or_update_dotenv()
        _update_static_files()
        _update_database()

def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run("git clone {0} .".format(REPO_URL))
    current_commit = local("git long -n 1 --format=%H", capture=True)
    run("git reset --hard {0}".format(current_commit))

def _update_virtualenv():
    if not exists('virtualenv/bin/pip'):
        run("python3.6 -m venv virtualenv")
    run("./virtualenv/bin/pip install -r requirements.txt")

def _create_or_update_dotenv():
    append(".env", "DJANGO_DEBUG_FALSE=y")
    append(".env", "SITENAME={0}".format(env.host))
    current_contents = run('cat .env')
    if 'DJANGO_SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghijklmnopqrstuvwxyz0123456789', k=50
        ))
        append('.env', 'DJANGO_SECRET_KEY={0}'.format(new_secret))

def _update_static_files():
    run('./virtualenv/bin/python manage.py collectstatic --noinput')

def _update_database():
    run('./virtualenv/bin/python manage.py migrate --noinput')