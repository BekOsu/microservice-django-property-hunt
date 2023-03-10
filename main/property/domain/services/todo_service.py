from django.utils import timezone
from datetime import timedelta
from django_q.tasks import schedule


def schedule_task():
    after_3_days = timezone.now() + timedelta(minutes=1)
    send_rejection_email_fuc = "property.domain.Tasks.send_rejection_email"
    hook = "property.domain.Tasks.print_result"

    schedule(send_rejection_email_fuc, 1, [1], hook=hook, next_run=timezone.now())
    schedule(send_rejection_email_fuc, 1, [1], hook=hook, next_run=after_3_days)
