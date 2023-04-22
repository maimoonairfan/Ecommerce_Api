from rest_framework import serializers
from authority.models import Authority

class AuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Authority
        fields = "__all__"