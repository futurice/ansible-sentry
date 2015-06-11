ansible-sentry
===========
[![Build Status](https://travis-ci.org/futurice/ansible-sentry.svg?branch=master)](https://travis-ci.org/futurice/ansible-sentry)

Ansible role for [Sentry](https://github.com/getsentry/sentry).

Requirements
------------

- git clone https://github.com/futurice/sentry-skeleton
- customize inventory to match your target server(s)
- customise conf.py, see [Sentry configuration](http://sentry.readthedocs.org/en/latest/getting-started/index.html)
 - SENTRY_ADMIN_EMAIL
 - SENTRY_URL_PREFIX
- deploy sentry project using ansible



Role Variables
--------------

```yaml
---
```

Example Playbook
----------------

    - hosts: all
      roles:
         - { role: futurice.sentry }

License
-------

BSD
