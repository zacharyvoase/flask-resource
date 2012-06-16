Flask-Resource
==============

Flask-Resource is a Flask extension which makes it easy to create
standards-compliant, resource-oriented Web applications. It adopts a strong
**convention-over-configuration** approach, which means you get to write less
code overall.

These are a few features:


Conventions
-----------

`Cool URIs don't change <http://www.w3.org/Provider/Style/URI.html>`_. Some
conventions have arisen on the Web for creating long-lasting, meaningful URLs.
When you use a framework which knows about these conventions, you don't have to
spend time crafting well-formed URIs—it's done for you.

Likewise, when you model your Web application around resources, some decisions
become trivial—how to name URLs (for Flask's built-in URL building), what
template to render for an action on a URL, et cetera. By using Flask-Resource,
you get these things automatically.


Content Negotiation
-------------------

If you structure your application well, you don't need a separate ``/api/`` URL
to talk JSON or XML—you can do it at the same URLs as the rest of your
application. With Flask-Resource, you split up your functions into an action
part and a rendering part. This means you can process a form, then respond in
HTML for browsers and JSON for JavaScript and API clients, without any extra
work or ugly nested ``if`` statements.


Quickstart
----------

Jump into the :doc:`quickstart <quickstart>` now, to see how easily you can
build a resource-oriented application with Flask.


Contents:

.. toctree::
   :maxdepth: 2

   quickstart



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

