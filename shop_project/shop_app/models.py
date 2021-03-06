from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=264)
  price = models.DecimalField(max_digits=5, decimal_places=2)
  description = models.TextField()
  image = models.ImageField(default='static/images/shoes/1_qbmveEK_mFkRHG5.jpeg', upload_to='static/images/shoes/')

  def __str__(self):
    return self.name

  def __repr__(self):
    return "<Product {}>".format(self.name)


class Client(models.Model):
   first_name = models.CharField(max_length=264)
   last_name = models.CharField(max_length=264)
   password = models.CharField(max_length=50)
   email = models.EmailField(max_length=264, unique=True)
   profil_picture = models.ImageField(default="static/images/profile.jpg", upload_to='static/images/profiles_picture/')

   def __str__(self):
    return self.email

   def __repr__(self):
    return "<Client {}>".format(self.email)



class Comment(models.Model):
  username = models.CharField(max_length=264)
  text = models.TextField(max_length=264)
  date = models.DateField()
  product = models.ForeignKey(Product, on_delete=models.CASCADE)

  def __str__(self):
    return self.username

  def __repr__(self):
    return "<Comment {}>".format(self.username)


class Question(models.Model):
  username = models.CharField(max_length=264, default="")
  title = models.CharField(max_length=264)
  text = models.TextField(max_length=264)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)

  def __str__(self):
    return self.username

  def __repr__(self):
    return "<Question {}>".format(self.username)

class Response(models.Model):
  username = models.CharField(max_length=264)
  text = models.TextField(max_length=264)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)

  def __str__(self):
    return self.username

  def __repr__(self):
    return "<Response {}>".format(self.username)
    


    




