ansible-sentry
===========
[![Build Status](https://travis-ci.org/futurice/ansible-sentry.svg?branch=master)](https://travis-ci.org/futurice/ansible-sentry)

Ansible role for [Sentry](https://github.com/getsentry/sentry).

Requirements
------------

Customize Sentry configuration in templates/conf.py


Role Variables
--------------

```yaml
---
repo: https://github.com/futurice/sentry-skeleton.git
sentry_release_path: /var/www/sentry/
```

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: futurice.sentry }

License
-------

BSD
