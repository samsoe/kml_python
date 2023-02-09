import simplekml
import subprocess
import pandas as pd

names = ['Dr. James A. Dillon Park Frisbee Golf Course',
         'Avon Town Hall Park Frisbee Golf Course',
         'Brookside Park Frisbee Golf Course',
         'Hazel Landing Park Frisbee Golf Course',
         'Washington Park Frisbee Golf Course']
longitudes = [-86.0655897, -86.4080829, -86.1070623, -86.071248, -86.1129077]
latitudes = [40.003252, 39.7636057, 39.7897185, 39.9416887, 39.8107904]

locations = pd.DataFrame({'names': names,
                          'longitudes': longitudes,
                          'latitudes': latitudes})

points_kml = simplekml.Kml()
for i in locations.itertuples():
    points_kml.newpoint(name=i.names, coords=[(i.longitudes, i.latitudes)])
points_kml_path = './points.kml'
points_kml.save(points_kml_path)

subprocess.call(['open', points_kml_path]);