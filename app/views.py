from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, DetailView, UpdateView

from app.forms import CreateUserForm, SubjectForm, DepartmentForm, StudentForm, FeesCollection, ExpenseForm, \
    HolidayForm, BookForm, SalaryForm, ExamForm, TeacherForm, EventForm, TimeTableForm
from app.models import Teacher, Subject, Student, Department, Fees, Expenses, Holiday, Library, Salary, Exam, Event, \
    TimeTable


# Create your views here.
class HomePageTemplateView(TemplateView):
    template_name = 'index.html'


class AddBookPageTemplateView(FormView):
    form_class = BookForm
    success_url = reverse_lazy('library_page')
    template_name = 'add-books.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddDepartmentPageTemplateView(FormView):
    template_name = 'add-department.html'
    form_class = DepartmentForm
    success_url = reverse_lazy('department_page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddEventsPageTemplateView(FormView):
    form_class = EventForm
    success_url = reverse_lazy('event_page')
    template_name = 'add-events.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddExpensesPageTemplateView(FormView):
    form_class = ExpenseForm
    success_url = reverse_lazy('expenses_page')
    template_name = 'add-expenses.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddExamPageTemplateView(FormView):
    form_class = ExamForm
    success_url = reverse_lazy('exam_page')
    template_name = 'add-exam.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddFeesPAgeTemplateView(TemplateView):
    template_name = 'add-fees.html'


class AddFeesCollectionPageTemplateView(FormView):
    form_class = FeesCollection
    success_url = reverse_lazy('fees_collection')
    template_name = 'add-fees-collection.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddHolidayPageTemplateView(FormView):
    form_class = HolidayForm
    success_url = reverse_lazy('holiday_page')
    template_name = 'add-holiday.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddRoomPageTemplateView(TemplateView):
    template_name = 'add-room.html'


class AddSalaryPageTemplateView(FormView):
    form_class = SalaryForm
    success_url = reverse_lazy('salary_page')
    template_name = 'add-salary.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddSportPageTemplateView(TemplateView):
    template_name = 'add-sports.html'


class AddStudentsPageTemplateView(FormView):
    template_name = 'add-student.html'
    form_class = StudentForm
    success_url = reverse_lazy('students_page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddSubjectPageTemplateView(FormView):
    template_name = 'add-subject.html'
    form_class = SubjectForm
    success_url = reverse_lazy('subject_page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddTimeTablePageTemplateView(FormView):
    form_class = TimeTableForm
    success_url = reverse_lazy('time_table_page')
    template_name = 'add-time-table.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddTeacherPageTemplateView(FormView):
    form_class = TeacherForm
    success_url = reverse_lazy('teachers_page')
    template_name = 'add-teacher.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddTransportPageTemplateView(TemplateView):
    template_name = 'add-transport.html'


class TeacherDashboardTemplateView(TemplateView):
    template_name = 'teacher-dashboard.html'


class StudentDashboardTemplateView(TemplateView):
    template_name = 'student-dashboard.html'


class LoginPageTemplateView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            form.add_error(None, 'Invalid username or password')
            return self.form_invalid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)


class RegisterPageTemplateView(FormView):
    template_name = 'register.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('login_page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EditBookPageTemplateView(UpdateView):
    model = Library
    form_class = BookForm
    success_url = reverse_lazy('library_page')
    template_name = 'edit-books.html'


class EditDepartmentPageTemplateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'edit-department.html'
    success_url = reverse_lazy('department_page')


class EditExamPageTemplateView(UpdateView):
    model = Exam
    form_class = ExamForm
    success_url = reverse_lazy('exam_page')
    template_name = 'edit-exam.html'


class EditFeesPageTemplateView(TemplateView):
    template_name = 'edit-fees.html'


class EditRoomPageTemplateView(TemplateView):
    template_name = 'edit-room.html'


class EditSportsPageTemplateView(TemplateView):
    template_name = 'edit-sports.html'


class EditStudentsPageTemplateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students_page')
    template_name = 'edit-student.html'


class EditSubjectPageTemplateView(UpdateView):
    queryset = Subject
    fields = 'subject_id', 'subject_class', 'subject_name'
    template_name = 'edit-subject.html'
    success_url = reverse_lazy('subject_page')


class TeachersPageTemplateView(ListView):
    template_name = 'teachers.html'
    model = Teacher
    context_object_name = 'teachers'


class FeesCollectionPageTemplateView(ListView):
    model = Fees
    template_name = 'fees-collections.html'
    context_object_name = 'fees'


class EditTeacherPageTemplateView(TemplateView):
    template_name = 'edit-teacher.html'


class EditTimeTablePageTemplateView(TemplateView):
    template_name = 'edit-time-table.html'


class EventPageTemplateView(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'event.html'


class ExamPageTemplateView(ListView):
    model = Exam
    context_object_name = 'exams'
    template_name = 'exam.html'


class ExpensesPageTemplateView(ListView):
    model = Expenses
    template_name = 'expenses.html'
    context_object_name = 'expenses'


class ForgotPasswordPageTemplateView(TemplateView):
    template_name = 'forgot-password.html'


class HolidayPageTemplateView(ListView):
    model = Holiday
    template_name = 'holiday.html'
    context_object_name = 'holidays'


class HostelPageTemplateView(TemplateView):
    template_name = 'hostel.html'


class InboxPageTemplateView(TemplateView):
    template_name = 'inbox.html'


class InvoicePageTemplateView(TemplateView):
    template_name = 'invoice.html'


class libraryPageTemplateView(ListView):
    model = Library
    context_object_name = 'books'
    template_name = 'library.html'


class ProfilePageTemplateView(TemplateView):
    template_name = 'profile.html'


class SalaryPageTemplateView(ListView):
    model = Salary
    context_object_name = 'salaries'
    template_name = 'salary.html'


class StudentDetailsPageTemplateView(DetailView):
    model = Student
    template_name = 'student-details.html'
    context_object_name = 'students'


class StudentPageTemplateView(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'students.html'


class SubjectPageTemplateView(ListView):
    model = Subject
    template_name = 'subjects.html'
    context_object_name = 'subjects'

    def get_queryset(self):
        return Subject.objects.all()


class TeacherDetailsPageTemplateView(TemplateView):
    template_name = 'teacher-details.html'


class TimeTablePageTemplateView(ListView):
    model = TimeTable
    context_object_name = 'tables'
    template_name = 'time-table.html'


class DepartmentPageTemplateView(ListView):
    model = Department
    template_name = 'departments.html'
    context_object_name = 'departments'

    def get_queryset(self):
        return Department.objects.all()
