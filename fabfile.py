
from fabric.api import env, sudo, run, local
from fabric.context_managers import cd
import os
from fabric.decorators import roles
from fabric.api import settings
from datetime import datetime
from time import strftime
import ntpath

env.roledefs = {
    'dev' : ['dev@cw.smithandrobot.com'],
    # 'prod' : ['dev@'],
}


@roles('dev')
def uptime():
    run('uptime')

@roles('dev')
def dev_deploy():
    run('cd /var/www/drupal/sites/all && git pull origin dev')
    clear_cache()

@roles('dev')
def clear_cache():
    run('cd /var/www/drupal/ && drush cc all')

@roles('dev')
def dev_flush():
    sudo('/etc/init.d/memcached restart')
