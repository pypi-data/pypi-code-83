from django.shortcuts import get_object_or_404
from rest_framework import serializers

from huscy.participations.models import Attendance, Participation
from huscy.participations.services import create_participation
from huscy.pseudonyms.services import get_subject
from huscy.subjects.models import Subject


class AttendanceSerializer(serializers.ModelSerializer):
    planned_end = serializers.DateTimeField(source='booking.timeslot.end', read_only=True)
    planned_start = serializers.DateTimeField(source='booking.timeslot.start', read_only=True)

    class Meta:
        model = Attendance
        fields = 'end', 'planned_end', 'planned_start', 'start', 'status'


class ParticipationSerializer(serializers.ModelSerializer):
    attendances = serializers.SerializerMethodField()
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    subject = serializers.CharField(write_only=True)
    subject_group_name = serializers.CharField(source='subject_group.name', read_only=True)

    class Meta:
        model = Participation
        fields = (
            'attendances',
            'status',
            'status_display',
            'subject',
            'subject_group',
            'subject_group_name'
        )
        read_only_fields = 'subject_group',

    def get_attendances(self, participation):
        attendances = participation.attendance_set.all()
        return AttendanceSerializer(attendances, many=True).data

    def to_representation(self, participation):
        representation = super().to_representation(participation)
        representation['subject'] = get_subject(participation.pseudonym).id
        return representation

    def create(self, validated_data):
        subject = get_object_or_404(Subject, pk=validated_data.pop('subject'))
        subject_group = self.context.get('subject_group')
        return create_participation(subject_group=subject_group, subject=subject, **validated_data)
