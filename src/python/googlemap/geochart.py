import csv
import gviz_api

"""
Visualize disposable median monthly salary per country on the world map
projection using Google Geochart and Table Visualization.
"""

def gettemplate():
    pagetemplate = """
    <html>
          <script src="https://www.google.com/jsapi" type="text/javascript"></script>
     <script>
      google.load("visualization"", "1", {packages:
