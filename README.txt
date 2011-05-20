==========
guillotine
==========

`guillotine` is a WSGI middleware which allows for HEAD requests to be properly
handled by your WSGI pipeline.  `guillotine` is intended to be placed as the
first, or topmost component in a WSGI pipeline, such that all other middelware
is downstream.  For an incoming request, `guillotine` converts the request
method from 'HEAD' to 'GET' before handing the request off to the next
downstream middleware or application.  `guillotine` then takes responsiblity
for discarding the response body before returning to the application server.

For more information about why you might want to do this see Graham Dumpleton's
article, `WSGI issues with HTTP HEAD requests.
<http://blog.dscpl.com.au/2009/10/wsgi-issues-with-http-head-requests.html>`_


Using `guillotine` with Paster
------------------------------

`guillotine` provides an entry point for Paster allowing it to be used as a
middleware in a pipeline::

    [pipeline:example_app]
    pipeline =
        egg:guillotine#guillotine
        egg:example#some_middleware
        example_app

Using `guillotine` "by hand"
----------------------------

If you compose your WSGI pipeline in Python code, `guillotine` can be
constructed directly::

    from guillotine import Guillotine

    middleware = Guillotine(app)  # app is some WSGI application or pipeline

