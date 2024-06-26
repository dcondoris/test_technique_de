from sqlalchemy import Table, Column, Float, String, MetaData, create_engine

from transform.process_hostel import process_data_hostel

pl_df = process_data_hostel

engine = create_engine('sqlite://technical_test.db', echo=True)

meta = MetaData()

connection = engine.raw_connection()

cursor = connection.cursor()

hotel = Table(
    "hotel", meta,
    Column("data_de_classement", String),
    Column("classement", String),
    Column("nom_commercial", String),
    Column("adresse", String),
    Column("code_postal", String),
    Column("commune", String),
    Column("nombre_de_chambres", String),
    Column("concat", String),
    Column("code_postal_dept", String),
    Column("x", Float),
    Column("y", Float),
    Column("lon", Float),
    Column("lat", Float),
)

pl_df.to_pandas().to_sql("hotel", con=engine)