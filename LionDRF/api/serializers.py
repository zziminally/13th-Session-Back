from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password']) #암호화 한 후 저장
        user.save()

        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)

            if not user.check_password(password):
                raise serializers.ValidationError()
            else:
                token = RefreshToken.for_user(user)
                refresh = str(token)
                access = str(token.access_token)

                data = {
                    'id': user.id,
                    'email': user.email ,
                    'access_token': access
                }
                return data
