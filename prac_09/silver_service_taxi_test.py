"""
CP5632 Practical
Tests for SilverServiceTaxi class
"""

from prac_09.silver_service_taxi import SilverServiceTaxi

fancy_taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
fancy_taxi.drive(18)
print(fancy_taxi)
print({fancy_taxi.get_fare()})
