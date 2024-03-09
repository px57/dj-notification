"""
This file contains the views for the notification app.
"""

from django.shortcuts import render

from kernel.http import Response
from kernel.http import load_response

@load_response()
def __empty__(request, res):
    res = Response()
    return res.success()
