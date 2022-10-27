# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:30:02 2022

@author: VARUN
"""

from countryinfo import CountryInfo
name = 'India'
country = CountryInfo(name)
data1 = country.alt_spellings()
print(data1)
data2 = country.capital()
print(data2)
data3 = country.capital_latlng()
print(data3)
data4 = country.area()
print(data4)
data5 = country.provinces()
print(data5)
data6 = country.borders()
print(data6)
data7 = country.calling_codes()
print(data7)
data8 = country.currencies()
print(data8)
data9 = country.population()
print(data9)
data10 = country.timezones()
print(data10)
data11 = country.region()
print(data11)
data12 = country.subregion()
print(data12)
data13 = country.wiki()
print(data13)
data14 = country.tld()
print(data14)
data15 = country.info()
for key, value in data15.items():
    print(key, ":", value)
    