from django.urls import path
from .views import SensorListCreateAPIView, SensorRetrieveUpdateDestroyAPIView, MeasurementCreateView

app_name = 'measurement'

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorListCreateAPIView.as_view(), name='sensor_create'),
    path('sensors/<int:pk>/', SensorRetrieveUpdateDestroyAPIView.as_view(), name='sensor_retrieve_update_delete'),
    path('measurements/', MeasurementCreateView.as_view(), name='measurement_create'),
]
