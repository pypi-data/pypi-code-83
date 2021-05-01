# -*- coding: utf-8 -*-
"""
Displays status of jenkins jobs.

This py3status module displays the status of desired jenkins jobs.
The desired jenkins jobs are defined by configuration. The current
status of each job is represented by the i3status colors. In default
configuration of the colors is as following:

Configuration parameters:
    cache_timeout: Renew of jenkins job status interval in seconds (default 60)
    jenkins_url: The base URL of jenkins server
    jenkins_pass_path: Path to jenkins credentials, if password-store is using.
    jenkins_username: Username for jenkins server, if unsecure credentials storage method is using.
    jenkins_password: Password for jenkins server, if unsecure credentials storage method is using.
    job_separator: Separator between the Jenkins job status.
    text_status: Text displayed for jenkins job status (default "S").
    text_not_connected: Text displayed if jenkins server is not reachable (default "-").
    text_common_error: Text displayed if an error occurred (default "E").
    jobs: List of jenkins jobs.

Configuration parameter for jobs entries:
    name: Jenkins job name.
    text_status: Text dispayls for this jenkins job status. If not set, the common text_status will be displayed.

Format placeholders:
    {status} dispay the configured jenkins job status

Color options:
    color_good: job status "SUCCESS"
    color_degraded: job status "UNSTABIL"
    color_bad: job status "FAILURE"
    color_bad: common error or jenkins server not reachable

Requires:
    pass: Recommended storage of jenkins credentials.

Example:
```
jenkins_status {
  jenkins_url = "https://myjenkins:1234"
  jenkins_pass_path = "Jenkins"
  jobs = [
    {
      "name": "job1",
      "text_status": "J1"
    },
    {
      "name": "job2",
      "text_status": "J2"
    }
  ]
}
```

@authors Andreas Schmidt
@license MIT
"""

import logging
import pypass
import jenkins
from time import time
import os
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

log = logging.getLogger("py3status-jenkins_status")

class Py3status:

    format = "JS: {status}"
    jenkins_url = ""
    cache_timeout = 60
    jenkins_pass_path = None
    jenkins_username = None
    jenkins_password = None
    jobs = []
    job_separator = ""
    text_status = "S"
    text_not_connected = "-"
    text_common_error = "E"


    def __init__(self):
        self._jenkins_server = None


    def jenkins_status(self):
        if not self._set_jenkins_server():
            return self._error_response(self.text_common_error)
        if not self._is_jenkins_available():
            return self._error_response(self.text_not_connected)
        if not isinstance(self.jobs, list):
          return self._error_response(self.text_common_error)

        jobs_status=[]
        for job in self.jobs:
            job_response = {}
            if not isinstance(job, dict):
                return self._error_response(self.text_common_error)
            error, color = self._get_job_color(job)
            text_status = job['text_status'] if 'text_status' in job.keys() else self.text_status
            if not error:
                job_response['full_text'] = self.text_common_error
                job_response['color'] = self.py3.COLOR_BAD
            else:
                job_response['full_text'] = text_status
                job_response['color'] = color
            jobs_status.append(job_response)
        job_separator = self.py3.safe_format(self.job_separator)
        print("\"{}\"".format(job_separator))
        composite = self.py3.composite_join(job_separator, jobs_status)
        return {
            'cached_until': self.py3.time_in(self.cache_timeout),
            'full_text': self.py3.safe_format(self.format, {'status': composite})
        }


    def _error_response(self, error_text: str) -> dict:
        return {
            'full_text': self.py3.safe_format(self.format, {'status': error_text}),
            'color': self.py3.COLOR_BAD
        }


    def _set_jenkins_server(self) -> bool:
        if self._jenkins_server:
            return True
        user, pw = self._get_crendentials()
        if user is None or pw is None:
            return False
        try:
            self._jenkins_server = jenkins.Jenkins(self.jenkins_url, username=user, password=pw)
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            self._jenkins_server._session.verify = False
        except Exception as e:
            log.error("Jenkins init error: {}".format(e))
            return False
        return True


    def _is_jenkins_available(self) -> bool:
        try:
            self._jenkins_server.get_whoami()
        except Exception as e:
            log.error("Jenkins communication error: {}".format(e))
            return False
        return True


    def _get_job_color(self, job : dict):
        #TODO make colors configurable in depends of jenkins status
        try:
            job_info = self._jenkins_server.get_job_info(job['name'])
            last_build_number = job_info['lastCompletedBuild']['number']
            build_info = self._jenkins_server.get_build_info(job['name'], last_build_number)

            if build_info['result'] == "SUCCESS":
                return True, self.py3.COLOR_GOOD
            elif build_info['result'] == "UNSTABLE":
                return True, self.py3.COLOR_DEGRADED
            else:
                return True, self.py3.COLOR_BAD

        except Exception as e:
            log.error("Get jenkins job info failed: {}".format(e))
            return False, self.py3.COLOR_BAD


    def _get_crendentials(self):
        if self.jenkins_pass_path:
            return self._get_pass_crendentials()
        elif self.jenkins_username and self.jenkins_password:
            return self.jenkins_username, self.jenkins_password
        else:
            log.error("No credentials information found")
            return None, None


    def _get_pass_crendentials(self):
        try:
            ps = pypass.PasswordStore()
        except Exception as e:
            log.error("Initialization of pypass failed: {}".format(e))
            return None, None
        credentials_list = ps.get_passwords_list()
        if self.jenkins_pass_path not in credentials_list:
            log.error("No credentials under path \"{}\" found".format(self.jenkins_pass_path))
            return None, None
        user = ps.get_decrypted_password(self.jenkins_pass_path, pypass.EntryType.username)
        pw = ps.get_decrypted_password(self.jenkins_pass_path, pypass.EntryType.password)
        return user, pw


if __name__ == "__main__":
    """
    Test this module by calling it directly.
    """
    from py3status.module_test import module_test

    logging.basicConfig()
    log.setLevel(logging.DEBUG)

    config = {
    #    'jenkins_pass_path': "",
    #    'jenkins_url': "",
    #    'format': 'xyz: {status}',
    #    'jobs': [
    #      {
    #        'name': "job1",
    #        'text_status': 'J1'
    #      },
    #      {
    #        'name': "job2"
    #      },
    #      {
    #        'name': "job3"
    #      }
    #    ]
    }

    module_test(Py3status, config)
