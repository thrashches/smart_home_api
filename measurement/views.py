# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementCreateSerializer
from .models import Sensor, Measurement


class SensorListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()


class SensorCreateAPIView(generics.CreateAPIView):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()


class SensorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SensorDetailSerializer
    queryset = Sensor.objects.all()


class MeasurementCreateView(generics.CreateAPIView):
    serializer_class = MeasurementCreateSerializer
    queryset = Measurement.objects.all()
