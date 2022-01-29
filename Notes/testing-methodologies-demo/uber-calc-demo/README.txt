UberCalc
========

A simple, sample project to show off front-end testing.

First, make a virtual environment and install the required
software::

    virtualenv env
    source env/bin/activate
    pip3 install -r requirements.txt

Then, install Chrome and ChromeDriver by following these instructions:
https://docs.google.com/document/d/1NYAjxA0tvqaxoTSptKO0dAfP8ZmvfpRRMdfFFK0dATw/

Then, you can start the server with::

    python3 server.py jstest

You can run the Jasmine-based unit tests by just looking
at the rendered page; they appear there.

To run the Selenium-based functional tests, run this in another terminal (keeping the server running)::

    python3 tests.py

Or you can run the equivalent Selenium-based functional
tests written as a Docfile with::

    python3 -m doctest tests.txt

Happy testing!
