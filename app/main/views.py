from . import main
from flask import render_template, redirect, url_for, abort


@main.route('/')
def index():
   '''
   view root page function that returns index page & data
   '''


   title = 'profile'

   return render_template('profile.html')