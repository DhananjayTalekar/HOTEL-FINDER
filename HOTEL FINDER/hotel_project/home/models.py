from django.db import models


class Ameneties(models.Model):
    amenity = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str :
        return self.amenity

class Hotel(models.Model) :
    hotel_name = models.CharField(max_length = 100)
    hotel_price = models.IntegerField()
    hotel_description = models.TextField()
    ameneties = models.ManyToManyField(Ameneties)
    banner_image = models.ImageField(upload_to="hotels")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str :
        return self.hotel_name
    
    def get_ameneties(self):
        payload = []
        for amenity in self.Ameneties.all() :
            payload.append({'id' : amenity.id, 'amenity' : amenity.amenity})
        return payload


class HotelImages(models.Model) :
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="hotels")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str :
        return self.hotel.hotel_name
# Create your models here.
