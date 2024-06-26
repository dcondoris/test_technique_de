from process_adress import process_data_adress
from process_hostel import process_data_hostel

pl_hotel = process_data_hostel()
pl_adress = process_data_adress()

pl_join = pl_hotel.join(pl_adress, on="KEY", how="left").select(["DATE DE CLASSEMENT", "CLASSEMENT", "NOM COMMERCIAL", "ADRESSE", "CODE POSTAL","COMMUNE", "NOMBRE DE CHAMBRES", "KEY", "DEP", "x","y","lon","lat"])
pl_join = pl_join.rename({"DATE DE CLASSEMENT": "date_classement", "CLASSEMENT": "classement", "NOM COMMERCIAL": "nom_commercial", "ADRESSE": "adresse", "CODE POSTAL": "code_postal", "COMMUNE": "commune", "NOMBRE DE CHAMBRES": "nombre_chambres", "KEY": "key", "DEP": "code_postal_dept","x": "x", "y": "y", "lon": "lon", "lat": "lat"})

print(pl_join.head())