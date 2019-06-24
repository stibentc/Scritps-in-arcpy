#This just to export your current projecto to PDF

mxd = arcpy.mapping.MapDocument("CURRENT")
arcpy.mapping.ExportToPDF(mxd, "C:/Users/etarazona/Desktop/TSF8.pdf")

#Batch of MXD to PDF
#Setting all of MXD in the same path use the script below to export to PDF

import arcpy, os  

folderPath = r"C:\Users\etarazona\Desktop\ACRP"  
for filename in os.listdir(folderPath):  
    fullpath = os.path.join(folderPath, filename)  
    if os.path.isfile(fullpath):  
        basename, extension = os.path.splitext(fullpath)  
        if extension.lower() == ".mxd":  
            mxd = arcpy.mapping.MapDocument(fullpath)  
            arcpy.mapping.ExportToPDF(mxd, basename + '.pdf')  
            
            
#The files will be saved with the native name of MXD file. 
