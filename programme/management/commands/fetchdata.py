from os import unlink
from tempfile import NamedTemporaryFile
import urllib.request, urllib.error, urllib.parse

from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    args = "<URL> [session cookie]"
    help = "Fetch a dumpdata-ish JSON and load it using loaddata"

    def handle(self, url, session_cookie=None, **extra):
        req = urllib.request.Request(url)

        if session_cookie:
            req.add_header("Cookie", "sessionid=" + session_cookie)

        res = urllib.request.urlopen(req)
        data = res.read()
        res.close()

        print(data)

        f = NamedTemporaryFile(suffix=".json", delete=False)
        print(f.name)
        try:
            f.write(data)
            f.close()

            call_command("loaddata", f.name)
        finally:
            unlink(f.name)
