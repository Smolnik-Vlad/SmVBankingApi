from rest_framework import serializers
from social_core.backends import username

from users.models import UserProfile, Client


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.SlugField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserProfile
        fields = (
            "username", "first_name", "last_name", "patronymic", "passport_series", "passport_id", "email",
            "last_login", "telephone_number", "password",)

        read_only_fields = ("username", "last_login")

        lookup_fields = "username"
        extra_kwargs = {
            "url": {
                "lookup_field": "username"
            }
        }


class ClientSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    username = serializers.SlugField(read_only=True)

    class Meta:
        model = Client
        fields = ('user', 'username', 'work_place', 'user_info')
        read_only_fields = ('username',)
        lookup_field = "username"

        extra_kwargs = {
            "url": {
                "lookup_field": "username",
            }
        }

    def create(self, validated_data):
        user_profile_data = validated_data.pop('user')
        password = user_profile_data.pop('password')
        print(user_profile_data)
        new_user_profile = UserProfile(**user_profile_data)
        new_user_profile.set_password(password)
        new_user_profile.save()

        validated_data['user'] = new_user_profile
        client = Client(**validated_data)
        client.save()
        return client

    def update(self, instance, validated_data):


        user_data = validated_data.pop('user')
        user_serializer = UserProfileSerializer(instance=instance.user, data=user_data, partial=True)
        if user_serializer.is_valid():
            user_serializer.update(instance.user, user_data)
        return super().update(instance, validated_data)
