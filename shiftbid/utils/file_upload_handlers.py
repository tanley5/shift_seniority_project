from datetime import date
import pandas as pd
from seniority.models import Seniority
from shift.models import Shift


def seniority_upload(file_name, report_name, datetime_created):
    report_name = report_name
    datetime_created = datetime_created
    df = pd.read_excel(file_name)

    for index, row in df.iterrows():
        agent_name = row.agent_name
        agent_email = row.agent_email
        seniority_number = row.seniority_number

        agent = Seniority.objects.create(report_name=report_name, datetime_created=datetime_created,
                                         agent_name=agent_name, agent_email=agent_email, seniority_number=seniority_number)
        agent.save()


def shift_upload(file_name, report_name, datetime_created):
    report_name = report_name
    datetime_created = datetime_created
    df = pd.read_excel(file_name)["shift"]

    for index, row in df.iteritems():
        shift_data = row

        shift = Shift.objects.create(
            report_name=report_name, datetime_created=datetime_created, shift=shift_data)
        shift.save()
