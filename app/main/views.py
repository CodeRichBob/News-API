from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_news,news_from_source,get_sources, search_topic, search_from_source