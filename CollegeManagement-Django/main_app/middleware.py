from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import redirect

class LoginCheckMiddleWare(MiddlewareMixin):
    ADMIN = '1'
    HOD = '2'
    STAFF = '3'
    STUDENT = '4'

    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user

        # Allow access to the login page and authentication-related views
        if not user.is_authenticated:
            if request.path in [reverse('login_page'), reverse('user_login')] or modulename == 'django.contrib.auth.views':
                return None
            return redirect(reverse('login_page'))

        if user.user_type == self.ADMIN:
            if modulename == 'main_app.student_views':
                return redirect(reverse('admin_home'))
        elif user.user_type == self.HOD:
            if modulename == 'main_app.student_views':
                return redirect(reverse('hod_home'))
        elif user.user_type == self.STAFF:
            if modulename in ['main_app.student_views', 'main_app.hod_views']:
                return redirect(reverse('staff_home'))
        elif user.user_type == self.STUDENT:
            if modulename in ['main_app.hod_views', 'main_app.staff_views']:
                return redirect(reverse('student_home'))

        return None
