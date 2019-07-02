from raptr.models import Project, Fundfy
from django.db.models import Sum
from shared.models import Contact


def funds_by_divison():
    by_division = Project.objects.select_related('fundfy', 'investigator_supported')\
        .values('investigator_supported__division')\
        .filter(fundfy__fcfy="2019", fundfy__fund_type=1)\
        .annotate(Sum('fundfy__budget'))
