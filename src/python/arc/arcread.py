import arcpy
import os 

arcpy.env.overwriteOutput = True 

arcpy.env.workspace = ws = ""
out = "output" 

for cov in arcpy.ListFiles("data/arc/*.e00"): 
   arcpy.ImportFromE00_conversion(cov, ws, cov.split(".")[0])
   if not ".e00" in cov and cov != "info": 
       arcpy.env.workspace = os.path.join(ws,cov) 
       for fc in arcpy.ListFeatureClasses("*polygon"):
           shp = os.path.join(out, "%s.shp" %cov) 
           arcpy.FeatureClassToFeatureClass_conversion(fc, out) 
 
