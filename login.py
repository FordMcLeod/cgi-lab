#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
from templates import login_page, secret_page, after_login_incorrect
from secret import username, password
import os

cookie_string = os.environ.get("HTTP_COOKIE")
cookie_pairs = cookie_string.split(";")
for pair in cookie_pairs:
    key,val - pair.split("=")
    if "username" in key:
        c_username = val
    elif "password" in key:
        c_password = val


print("Content-Type:text/html")
if c_username == username and c_password ==password:
    print("\n\n")
    print(secretpage(username,password))
# print form post data
else if os.environ.get("REQUEST_METHOD", "GET") == "POST":
    form = cgi.FieldStorage()
    f_username = form.getvalue("username")
    f_password = form.getvalue("password")
    if f_username ==username and f_password ==password:
        print("Set-Cookie: username={}; ".format(username))
        print("Set-Cookie: password={}; ".format(password))
        print("\n\n")
        print(secret_page(username,password))
    else:
        print("\n\n")
        print(after_login_incorrect())
else:
    print("\n\n")
    #    print("<h1>"+ os.environ.get("HTTP_COOKIE")+"</h1>")
    print(login_page())
