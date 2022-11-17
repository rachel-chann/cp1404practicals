"""
CP5632 Practical
Tests for Unreliable Car
"""
from prac_09.unreliable_car import UnreliableCar

reliable_car = UnreliableCar("Reliable Car", 100, 80)
unreliable_car = UnreliableCar("Unreliable Car", 100, 10)

for i in range(1, 10):
    print(f"Attempting to drive {i}km:")
    print(f"{reliable_car.name:12} drove {reliable_car.drive(i):2}km")
    print(f"{unreliable_car.name:12} drove {unreliable_car.drive(i):2}km")

print(reliable_car)
print(unreliable_car)

