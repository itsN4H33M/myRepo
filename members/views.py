from django.views import View
from .models import Employees
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeView(View):

    def get(self, request, emp_id=None, dept=None):
        employee_model_list = []
        try:
            if emp_id:
                employee_model_list = Employees.objects.filter(employee_id=emp_id)
            elif dept:
                employee_model_list = Employees.objects.filter(dept=dept)
        except Employees.DoesNotExist:
            return JsonResponse({'status': 'failed', "employees": None}, status=400)
        employees = []
        for employee in employee_model_list:
            data = {
                "first_name" : employee.first_name,
                "last_name": employee.last_name,
                "address": employee.address,
                "roll_number": employee.employee_id,
                "mobile": employee.mobile,
                "branch": employee.dept
            }
            employees.append(data)
        return JsonResponse({'status': 'success', "employees": employees}, status=200)

    def post(self, request):
        if not request.POST.get('first_name') or not request.POST.get('last_name') or not request.POST.get('address') or  not request.POST.get('employee_id') or not request.POST.get('mobile'):
            return JsonResponse({'status': 'failed', "message" : "all fields required"}, status=500)

        Employees.objects.create(
            first_name= request.POST.get('first_name'),
            last_name= request.POST.get('last_name'),
            address= request.POST.get('address'),
            employee_id= request.POST.get('employee_id'),
            mobile= request.POST.get('mobile'),
            dept= request.POST.get('dept'))
        return JsonResponse({'status': 'sucess'}, status=200)

