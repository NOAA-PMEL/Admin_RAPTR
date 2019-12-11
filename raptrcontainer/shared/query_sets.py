import datetime

from crada.models import Crada

from django.db.models import Count, F, Sum

from proposal.models import Proposal

from raptr.models import Fundfy, Project

from shared.models import Contact


def get_current_fy():
    if datetime.date.today().month > 9:
        current_fy = datetime.date.today().year + 1
    else:
        current_fy = datetime.date.today().year
    return current_fy


def get_by_division_data():
    bdd = Fundfy.objects.values(division=F('project_id__investigator_supported__division'))\
        .filter(fcfy=str(get_current_fy()), fund_type_id__fund_type='New') \
        .annotate(Sum('budget')) \
        .order_by('-budget__sum')
    return bdd


def get_by_division_total():
    bdt = Fundfy.objects.values(division=F('project_id__investigator_supported__division')) \
        .filter(fcfy=str(get_current_fy()), fund_type_id__fund_type='New') \
        .aggregate(Sum('budget'))
    return bdt


def get_by_research_program_data():
    brpd = Fundfy.objects.values(research_program=F('project_id__investigator_supported__research_program__program_short_name'))\
        .filter(fcfy=str(get_current_fy()), fund_type_id__fund_type='New') \
        .annotate(Sum('budget'))\
        .order_by('-budget__sum')
    return brpd


def get_by_research_program_total():
    brpt = Fundfy.objects.values(research_program=F('project_id__investigator_supported__research_program__program_short_name')) \
        .filter(fcfy=str(get_current_fy()), fund_type_id__fund_type='New') \
        .aggregate(Sum('budget'))
    return brpt


def get_open_projects_total():
    opt = Project.objects.all().filter(status="Open").aggregate(Count('status'))
    return opt


def get_fy_new_funds_count():
    fnfc = Fundfy.objects.all().filter(fcfy=str(get_current_fy()), fund_type=1, project_id__status='Open')\
        .aggregate(Count('fcfy'))
    return fnfc


def get_royalty_funds_received():
    rfr = Fundfy.objects.all().filter(fcfy=str(get_current_fy()), project_id__fund_code__fund_code='0096')\
        .aggregate(Sum('budget'))
    return rfr


def get_by_employee_type_data():
    emptype = Contact.objects.values_list('employee_type__employee_type')\
        .filter(active=True)\
        .annotate(total=Count('employee_type'))\
        .order_by('-total')
    return emptype


def get_employee_type_total():
    emptype_total = Contact.objects.filter(active=True)\
        .aggregate(total=Count('employee_type'))
    return emptype_total


def get_by_division_chart_data():
    bdgd = Fundfy.objects.values_list('project_id__investigator_supported__division') \
            .filter(fcfy=str(get_current_fy()), fund_type_id__fund_type='New') \
            .annotate(Sum('budget')) \
            .order_by('-budget__sum')
    return bdgd


def get_by_research_program_chart_data():
    brpcd = Fundfy.objects.values_list('project_id__investigator_supported__research_program__program_short_name') \
            .filter(fcfy=str(get_current_fy()), fund_type_id__fund_type='New') \
            .annotate(Sum('budget')) \
            .order_by('-budget__sum')
    return brpcd


def get_by_sponsor_type_chart_data():
    bstcd = Fundfy.objects.values_list('project_id__sponsor_id__sponsor_type_id__sponsor_type') \
            .filter(fcfy=str(get_current_fy()), fund_type_id__fund_type='New') \
            .annotate(Sum('budget')) \
            .order_by('-budget__sum')
    return bstcd


def get_fy_proposal_count():
    fpc = Proposal.objects.all().filter(year_proposed=str(get_current_fy()))\
        .exclude(status_id__status='Voided')\
        .aggregate(Count('year_proposed'))
    return fpc


def get_signed_crada_count():
    scc = Crada.objects.all().filter(activity_phase="Signed")\
        .aggregate(Count('activity_phase'))
    return scc
