import os
from flask import Flask
from flask import request
from flask import render_template
import json
from jsonstore.store import EntryManager
import datetime

em = EntryManager('index.db')

if __name__ == "__main__":
    data = em.search()
    print len(data)
