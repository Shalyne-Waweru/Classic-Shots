from django.db import models

class Category(models.Model):
    categoryName=models.CharField(max_length=30)

    def __str__(self):
        return self.categoryName

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Location(models.Model):
    locationName=models.CharField(max_length=30)

    def __str__(self):
        return self.locationName

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Image(models.Model):
  image = models.ImageField(upload_to = 'gallery-images/',default='DEFAULT VALUE')
  title = models.CharField(max_length =30)
  description = models.TextField()
  #Create a foreign key column that will store the ID of the Category from the Category table
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  #Create a foreign key column that will store the ID of the Location from the Location table
  location = models.ForeignKey(Location,on_delete=models.CASCADE)
  #Automatically save the exact time and date to the database as soon as we save the model.
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return self.image