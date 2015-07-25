from django.contrib import admin

# Register your models here.
from .models import Advisors
from .models import Dim_Advisor

class AdvisorsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Advisor_Dimensions', {'fields': ('advisor_key','advisor_first_name','advisor_last_name','advisor_email','advisor_language','staff_grp','manager_first_name','manager_last_name','advisor_tier','vendor_name','region_name')}),
        ('Contact_Dimensions', {'fields': ('dly_advisor_dashboard_key', 'event_date', 'week_of','fscl_year_nbr','fscl_month_name','channel_name','contact_language','ctgry_name','product_name','platform_name','contact_cbr','acw','handle_time','total_no_of_handled','no_survey_response_received','no_of_positive_surveys','no_of_resolutions_surveys')}),
    )

class Dim_AdvisorAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dimensions', {'fields': ('advisor_key','advisor_first_name','advisor_last_name','advisor_email','advisor_language','staff_grp','manager_first_name','manager_last_name','advisor_tier','region_name','vendor_name')}),
    )

admin.site.register(Advisors, AdvisorsAdmin)
admin.site.register(Dim_Advisor, Dim_AdvisorAdmin)
