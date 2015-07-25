from django.db import models

# Create your models here.
    
class Advisors(models.Model):

    dly_advisor_dashboard_key = models.IntegerField()
    advisor_key = models.ForeignKey('Dim_Advisor', limit_choices_to={'current_flag': 'Y'})
    event_date = models.DateField(auto_now=False)
    week_of = models.DateField(auto_now=False)
    fscl_year_nbr = models.IntegerField()
    fscl_month_name = models.CharField(max_length=20)
    advisor_email = models.CharField(max_length=255)
    advisor_first_name = models.CharField(max_length=255)
    advisor_last_name = models.CharField(max_length=255)
    staff_grp = models.CharField(max_length=255)
    manager_first_name = models.CharField(max_length=100)
    manager_last_name = models.CharField(max_length=100)
    advisor_language = models.CharField(max_length=100)
    advisor_tier = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=255)
    region_name = models.CharField(max_length=100)
    contact_cbr = models.CharField(max_length=255)
    product_name = models.CharField(max_length=100)
    channel_name = models.CharField(max_length=100)
    platform_name = models.CharField(max_length=100)
    contact_language = models.CharField(max_length=100)
    ctgry_name = models.CharField(max_length=100)
    total_no_of_handled = models.IntegerField()
    acw = models.DecimalField(max_digits=20, decimal_places=7)
    handle_time = models.DecimalField(max_digits=20, decimal_places=7)
    no_of_positive_surveys = models.IntegerField()
    no_of_resolutions_surveys = models.IntegerField()
    no_survey_response_received = models.IntegerField()

    def __str__(self):
        return str(self.advisor_key)

class Dim_Advisor(models.Model):
    advisor_key = models.IntegerField()
    advisor_email = models.CharField(max_length=255)
    advisor_first_name = models.CharField(max_length=255)
    advisor_last_name = models.CharField(max_length=255)
    staff_grp = models.CharField(max_length=255)
    manager_first_name = models.CharField(max_length=255)
    manager_last_name = models.CharField(max_length=255)
    advisor_language = models.CharField(max_length=100)
    advisor_language = models.CharField(max_length=100)
    advisor_tier = models.CharField(max_length=100)
    vendor_name = models.CharField(max_length=255)
    region_name = models.CharField(max_length=100)
    current_flag = models.CharField(max_length=1)

    def __str__(self):
        return self.advisor_email
