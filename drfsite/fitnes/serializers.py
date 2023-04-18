from rest_framework import serializers

from fitnes.models import CatDirection, CatCoach, CatSession, Session


class CatDirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatDirection
        fields = "__all__"


class CatCoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatCoach
        fields = "__all__"


class CatSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatSession
        fields = "__all__"


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = (
            "title",
            "session",
            "date_start",
            "date_end",
            "coach",
            "direction",
        )


class SessionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"