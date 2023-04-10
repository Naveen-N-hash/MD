
from django.db import models

# create model for movies which contains name, year, description, image, rating, category and embedded link field which is the source of the video
class Movies(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    rating = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    embedded_link = models.URLField()

    def __str__(self):
        return self.name    

# now create models for TV shows which contains name, year, description, image, rating, category and each series contains a number of seasons, 
# in that seasons every season contains a number of episodes of that series and each episode contains episode name, episode number, 
# embedded link which is the source of the video note that every series contains number of seasons and each season contains a number of episodes 
# and each episode contains embedded link which is the source of the video 
class Tvshows1(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    rating = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    seasons = models.IntegerField()

    def __str__(self):
        return self.name

class Seasons(models.Model):
    tvshow = models.ForeignKey(Tvshows1, on_delete=models.CASCADE,related_name='seasons_set')
    season_number = models.IntegerField()

    def __str__(self):
        return str(self.season_number)

class Episodes(models.Model):
    season = models.ForeignKey(Seasons, on_delete=models.CASCADE)
    episode_name = models.CharField(max_length=100)
    episode_number = models.IntegerField()
    embedded_link = models.URLField()

    def __str__(self):
        return self.episode_name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
