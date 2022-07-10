import factory
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from users.models import Profile


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = get_user_model()

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')
    profile = factory.RelatedFactory(
        'users.tests.factories.ProfileFactory', factory_related_name='user'
    )


@factory.django.mute_signals(post_save)
class ProfileFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory, profile=None)
