from shift.models import Shift


def handle_response_submission(report_name, shift_chosen, email):
    shift = Shift.objects.get(pk=shift_chosen)
    shift.agent_email = email
    shift.save()
