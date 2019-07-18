import datetime
from raptr.models import Project, Fundfy
from shared.models import Contact
from django.db.models import Sum, F, Count


def get_current_fy():
    current_fy = 2000
    if datetime.date.today().month > 9:
        current_fy = datetime.date.today().year + 1
    else:
        current_fy = datetime.date.today().year
    return current_fy


def get_by_division_data():
    bdd = Fundfy.objects.values(division=F('project_id__investigator_supported__division'))\
        .filter(fcfy=str(get_current_fy()), fund_type=1) \
        .annotate(Sum('budget')) \
        .order_by('-budget__sum')
    return bdd


def get_by_division_total():
    bdt = Fundfy.objects.values(division=F('project_id__investigator_supported__division')) \
        .filter(fcfy=str(get_current_fy()), fund_type=1) \
        .aggregate(Sum('budget'))
    return bdt


def get_by_research_program_data():
    brpd = Fundfy.objects.values(research_program=F('project_id__investigator_supported__research_program__program_short_name'))\
        .filter(fcfy=str(get_current_fy()), fund_type=1) \
        .annotate(Sum('budget'))\
        .order_by('-budget__sum')
    return brpd


def get_by_research_program_total():
    brpt = Fundfy.objects.values(research_program=F('project_id__investigator_supported__research_program__program_short_name')) \
        .filter(fcfy=str(get_current_fy()), fund_type=1) \
        .aggregate(Sum('budget'))
    return brpt


def get_open_projects_total():
    opt = Project.objects.all().filter(status=2).aggregate(Count('status'))
    return opt


def get_fy_new_funds_count():
    fnfc = Fundfy.objects.all().filter(fcfy=str(get_current_fy()), fund_type=1, project_id__status=2)\
        .aggregate(Count('fcfy'))
    return fnfc


def get_royalty_funds_received():
    rfr = Fundfy.objects.all().filter(fcfy=str(get_current_fy()), project_id__fund_code__fund_code='0096')\
        .aggregate(Sum('budget'))
    return rfr


def get_by_division_chart_data():
    bdgd = Fundfy.objects.values_list('project_id__investigator_supported__division') \
            .filter(fcfy=str(get_current_fy()), fund_type=1) \
            .annotate(Sum('budget')) \
            .order_by('-budget__sum')
    return bdgd


def get_by_research_program_chart_data():
    brpcd = Fundfy.objects.values_list('project_id__investigator_supported__research_program__program_short_name') \
            .filter(fcfy=str(get_current_fy()), fund_type=1) \
            .annotate(Sum('budget')) \
            .order_by('-budget__sum')
    return brpcd


def get_by_sponsor_type_chart_data():
    bstcd = Fundfy.objects.values_list('project_id__sponsor_id__sponsor_type_id__sponsor_type') \
            .filter(fcfy=str(get_current_fy()), fund_type=1) \
            .annotate(Sum('budget')) \
            .order_by('-budget__sum')
    return bstcd
