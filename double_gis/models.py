from django.db import models

class Data(models.Model):
    organization_name       = models.CharField(max_length = 100, blank = True, null = True)
    city                    = models.CharField(max_length = 100, blank = True, null = True)
    address                 = models.CharField(max_length = 100, blank = True, null = True)
    mobile                  = models.CharField(max_length = 100, blank = True, null = True)
    mail                    = models.CharField(max_length = 100, blank = True, null = True)
    url                     = models.CharField(max_length = 100, blank = True, null = True)
    social                  = models.CharField(max_length = 100, blank = True, null = True)
    main_category           = models.CharField(max_length = 100, blank = True, null = True)
    sub_category            = models.CharField(max_length = 100, blank = True, null = True)
    
class Locality(models.Model):
    address                 = models.TextField(blank = True, null = True)
    longitude               = models.DecimalField(max_digits = 10, decimal_places = 6, blank = True, null = True)
    latitude                = models.DecimalField(max_digits = 10, decimal_places = 6, blank = True, null = True)
    
class MetroStation(models.Model):
    name                    = models.TextField(blank = True, null = True)
    coordinates_json        = models.TextField(blank = True, null = True)
    
class Company(models.Model):
    name                    = models.TextField(blank = True, null = True)
    name_synonyms           = models.TextField(blank = True, null = True)
    address                 = models.TextField(blank = True, null = True)
    main_category           = models.TextField(blank = True, null = True)
    sub_category            = models.TextField(blank = True, null = True)
    city                    = models.TextField(blank = True, null = True)
    time_points_json        = models.TextField(blank = True, null = True)
    coordinates_json        = models.TextField(blank = True, null = True)
    metro_distances_json    = models.TextField(blank = True, null = True)
    contracts_json          = models.TextField(blank = True, null = True)