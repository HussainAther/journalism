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
      google.load("visualization", "1", {packages:["geochart", "table"]});
      google.setOnLoadCallback(drawMap);
      function drawMap() {
          var json_data = new google.visualization.DataTable(%s, .6);
          var options = {colorAxis: {colors: ["#eee", "green"]}};
          var mymap = new google.visualization.GeoChart(
                    document.getElementById("map_div"));
          mymap.draw(json_data, options);
          var mtable = new google.visualization.Table(
                    document.getElementById("table_div"));
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
        <a href="http://www.numbeo.com/cost-of-living/prices_by_country.jsp?display-rency=EUR$itemId=105">
        http://www.numbeo.com/cost-of-living/prices_by_country.jsp?display-rency=EUR$itemId=105
    </a>
    </small>
    </div>
    </body>
    </html>
    """
    return pagetemplate 

def main():
    """
    Load data from a .csv file and visualize it.
    """
    afile = "data/googlemap/median-dpi-countries.csv"
    datarows = []
    with open(afile, "r") as f:
        reader = csv.reader(f)
        reader.next() # Skip the header.
        for row in reader:
            datarows.append(row)
            # Describe data.
            description = {"country":("string", "Country"),
                           "dpi": ("number", "EUR"),}
            # Build list of dictionaries.
            data = []
            for each in datarows:
                data.append({"country": each[0],
                        "dpi":(float(each[1]), each[1])})
            # Instantiate DataTable with structure defined in 'description'.
            datatable = gviz_api.DataTable(description)
            # Load it into gviz_api.DataTable.
            datatable.LoadData(data)
            # Create a JSon string.
            json = datatable.ToJSon(columns_order=("country", "dpi"), order_by="country",)
            # Put JSON string into the template
            # and save to output.html. 
            with open("output/googlemap/output.html", "w") as out:
                out.write(gettemplate() % (json,))

main()
