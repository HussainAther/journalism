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
          var mtable = new google.visualization.Table(
                    document.getElementByld("table_div"));
          mytable.draw(json_data, {showRowNumber: true})
    }
    </script>
    <body>
       <H1>Median Monthly Disposable Salary World Countries</H1>
    <div id="map_div"></div>
    <hr/>
    <div id="table_div"></div>
    <div id="source">
    <hr/>
    <small>
    Source:
        <a href="http://www.numbeo.com/cost-of-living/prices_by_-country.jsp?display-rency=EUR$itemId=105">
        http://www.numbeo.com/cost-of-living/prices_by_-country.jsp?display-rency=EUR$itemId=105
    </a>
    </small>
    </div>
