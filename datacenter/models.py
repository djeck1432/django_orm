from django.db import models
import django


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard,on_delete='passcode')
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )


    def get_duration(self):
      if not self.leaved_at:
        time_now = django.utils.timezone.now()
        duration_in_storage = time_now - self.entered_at
      else:
        duration_in_storage = self.leaved_at - self.entered_at
      return duration_in_storage

    def format_duration(self):
      time_delta = self.get_duration()
      minutes = time_delta.seconds // 60
      seconds = (minutes*60) - time_delta.seconds
      formatted_duration = '{} мин {} сек '.format(minutes,seconds)
      if minutes>= 60 and  minutes <= 1440:
        hours = minutes // 60
        remaining_minutes = minutes - (hours * 60)
        formatted_duration = '{} час {} мин {} сек '.format(hours,remaining_minutes,seconds)
      return formatted_duration
        

    def is_visit_long(self, seconds=3600):
      visit_in_seconds = self.get_duration()
      days = visit_in_seconds.days
      return visit_in_seconds.seconds > seconds and days == 0

