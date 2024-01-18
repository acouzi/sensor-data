import json
import random
from kafka import KafkaProducer
import time

cities = ["CityA", "CityB", "CityC", "CityD", "CityE"]
producer = KafkaProducer(bootstrap_servers='kafka:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))


while True:
    for city in cities:
        sensor_data = {
            'city': city,
            'temperature': random.uniform(20, 30),
            'humidity': random.uniform(40, 60),
            'pressure': random.uniform(1000, 1010),
            'air_quality': random.randint(1, 100),
            'wind_speed': random.uniform(0, 10)
        }
        print(sensor_data)
        producer.send('dev-sensor-data-create', value=sensor_data)
    time.sleep(30)
