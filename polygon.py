import csv
import simplekml
import subprocess # open kml in google earth
import pandas as pd

kml = simplekml.Kml()

pol = kml.newpolygon(name="Atrium Garden",
                     outerboundaryis=[(18.43348,-33.98985), (18.43387,-33.99004),
                                      (18.43410,-33.98972), (18.43371,-33.98952),
                                      (18.43348,-33.98985)])

kml_path = './polygon.kml'
kml.save(kml_path)

# open with Google Earth Pro
subprocess.call(['open', kml_path]);