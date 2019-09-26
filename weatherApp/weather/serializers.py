"""
Serializer module for the weather App
"""


__author__ = 'Kalenshi Katebe'

from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    """Serializes a city field for accessing the weather api"""
    city = serializers.CharField(max_length=50,
                                 required=True,
                                 style={'placeholder': "Enter a city name"}
                                 )
