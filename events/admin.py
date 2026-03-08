from django.contrib import admin
from .models import Registration
import openpyxl
from django.http import HttpResponse


class RegistrationAdmin(admin.ModelAdmin):

    list_display = (
        'participant_name',
        'event_name',
        'contact_number',
        'payment_method',
        'payment_status',
        'registration_date'
    )

    actions = ["export_to_excel"]

    def export_to_excel(self, request, queryset):

        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = "Participants"

        columns = [
            "Name",
            "Semester",
            "Event",
            "Contact",
            "Email",
            "Payment Method",
            "Transaction ID"
        ]

        worksheet.append(columns)

        for obj in queryset:
            worksheet.append([
                obj.participant_name,
                obj.semester_department,
                obj.event_name,
                obj.contact_number,
                obj.email,
                obj.payment_method,
                obj.transaction_id
            ])

        response = HttpResponse(
            content_type="application/ms-excel"
        )

        response['Content-Disposition'] = 'attachment; filename=participants.xlsx'

        workbook.save(response)

        return response

    export_to_excel.short_description = "Export Selected to Excel"


admin.site.register(Registration, RegistrationAdmin)