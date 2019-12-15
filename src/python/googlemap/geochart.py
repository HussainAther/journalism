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
      google.load("visualization"", "1", {packages:["geochart", "table"]});
      google.setOnLoadCallback(drawMap);
      function drawMap() {
          var json_dta = new google.visualization.DataTable(%s, .6);
          var options = {colorAxis: {colors: ["#eee", "green"]}};
          var mymap = new google.visualization.GeoChart(
                    document.getElementByld("map_div"));
          mymap.draw(json_data, options);

