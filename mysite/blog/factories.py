import email
import factory
from faker import Factory as FakerFactory
from django.utils.timezone import now
from django.contrib.auth.models import User



from blog.models import Post
faker = FakerFactory.create()

class UserFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = User
    
  email = factory.Factory("safe_email")
  username = factory.LazyAttribute(lambda x: faker.name())
  
  @classmethod
  def _preapre(cls, create, **kwargs):
    password = kwargs.pop("password", None)
    user = super(UserFactory, cls)._prepare(create, **kwargs)
    if password:
      user.set_password(password)
      if create:
        user.save()
    return user


class PostFactory(factory.django.DjangoModelFactory):
  title = factory.LazyAttribute(lambda x: faker.sentence())
  created_on = factory.LazyAttribute(lambda x: now())
  author = factory.SubFactory(UserFactory)
  status = 0
  
  class Meta:
    model = Post