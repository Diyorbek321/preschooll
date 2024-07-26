from django.contrib.auth.views import LoginView
from django.urls import path

from app.views import HomePageTemplateView, AddBookPageTemplateView, AddDepartmentPageTemplateView, \
    AddEventsPageTemplateView, AddExamPageTemplateView, AddExpensesPageTemplateView, AddFeesCollectionPageTemplateView, \
    AddFeesPAgeTemplateView, AddHolidayPageTemplateView, AddRoomPageTemplateView, AddSalaryPageTemplateView, \
    AddSportPageTemplateView, AddStudentsPageTemplateView, AddSubjectPageTemplateView, \
    AddTimeTablePageTemplateView, AddTransportPageTemplateView, TeacherDashboardTemplateView, \
    StudentDashboardTemplateView, LoginPageTemplateView, RegisterPageTemplateView, \
    EditBookPageTemplateView, EditDepartmentPageTemplateView, EditExamPageTemplateView, EditFeesPageTemplateView, \
    EditRoomPageTemplateView, EditSportsPageTemplateView, \
    EditStudentsPageTemplateView, EditSubjectPageTemplateView, EditTeacherPageTemplateView, \
    EditTimeTablePageTemplateView, EventPageTemplateView, ExamPageTemplateView, ExpensesPageTemplateView, \
    ProfilePageTemplateView, \
    HolidayPageTemplateView, ForgotPasswordPageTemplateView, TeacherDetailsPageTemplateView, SalaryPageTemplateView, \
    StudentDetailsPageTemplateView, StudentPageTemplateView, SubjectPageTemplateView, HostelPageTemplateView, \
    InboxPageTemplateView, \
    InvoicePageTemplateView, TimeTablePageTemplateView, DepartmentPageTemplateView, libraryPageTemplateView, \
    TeachersPageTemplateView, \
    FeesCollectionPageTemplateView, AddTeacherPageTemplateView

urlpatterns = [
    # Dashboard section
    path('', HomePageTemplateView.as_view(), name='home_page'),
    path('teacher_dashboard/', TeacherDashboardTemplateView.as_view(), name='teacher_page'),
    path('student_page/', StudentDashboardTemplateView.as_view(), name='student_page'),

    #     Add section
    path('add_book/', AddBookPageTemplateView.as_view(), name='add_book'),
    path('add_department/', AddDepartmentPageTemplateView.as_view(), name='add_department'),
    path('add_event/', AddEventsPageTemplateView.as_view(), name='add_event'),
    path('add_exam/', AddExamPageTemplateView.as_view(), name='add_exam'),
    path('add_expenses/', AddExpensesPageTemplateView.as_view(), name='add_expenses'),
    path('add_fees/', AddFeesPAgeTemplateView.as_view(), name='add_fees'),
    path('add_fees_collection/', AddFeesCollectionPageTemplateView.as_view(), name='add_fees_collection'),
    path('add_holiday/', AddHolidayPageTemplateView.as_view(), name='add_holiday'),
    path('add_room/', AddRoomPageTemplateView.as_view(), name='add_room'),
    path('add_salary/', AddSalaryPageTemplateView.as_view(), name='add_salary'),
    path('add_sports/', AddSportPageTemplateView.as_view(), name='add_sport'),
    path('add_student/', AddStudentsPageTemplateView.as_view(), name='add_student'),
    path('add_subject/', AddSubjectPageTemplateView.as_view(), name='add_subject'),
    path('add_teacher/', AddTeacherPageTemplateView.as_view(), name='add_teacher'),
    path('add_transport/', AddTransportPageTemplateView.as_view(), name='add_transport'),
    path('add_timtable/', AddTimeTablePageTemplateView.as_view(), name='add_timetabler'),

    #     Authentication
    path('login/',
         LoginView.as_view(template_name='login.html', next_page='home_page', redirect_authenticated_user=True),
         name='login_page'),
    path('register/', RegisterPageTemplateView.as_view(), name='register_page'),
    path('forgot_password/', ForgotPasswordPageTemplateView.as_view(), name='forgot_password'),

    #     Edit section
    path('edit_book/<int:pk>', EditBookPageTemplateView.as_view(), name='edit_book'),
    path('edit_department/<int:pk>', EditDepartmentPageTemplateView.as_view(), name='edit_department'),
    path('edit_exam/<int:pk>', EditExamPageTemplateView.as_view(), name='edit_exam'),
    path('edit_fees/', EditFeesPageTemplateView.as_view(), name='edit_fees'),
    path('edit_room/', EditRoomPageTemplateView.as_view(), name='edit_room'),
    path('edit_sport/', EditSportsPageTemplateView.as_view(), name='edit_sport'),
    path('edit_student/<int:pk>', EditStudentsPageTemplateView.as_view(), name='edit_student'),
    path('edit_subject/<int:pk>/edit/', EditSubjectPageTemplateView.as_view(), name='edit_subject'),
    path('edit_teacher/', EditTeacherPageTemplateView.as_view(), name='edit_teacher'),
    path('edit_time_table/', EditTimeTablePageTemplateView.as_view(), name='edit_time_table'),

    #     Other
    path('event/', EventPageTemplateView.as_view(), name='event_page'),
    path('exam/', ExamPageTemplateView.as_view(), name='exam_page'),
    path('expenses/', ExpensesPageTemplateView.as_view(), name='expenses_page'),
    path('profile/', ProfilePageTemplateView.as_view(), name='profile_page'),

    path('hostel/', HostelPageTemplateView.as_view(), name='hostel_page'),
    path('holiday/', HolidayPageTemplateView.as_view(), name='holiday_page'),
    path('teacher_detail/', TeacherDetailsPageTemplateView.as_view(), name='teacher_detail_page'),
    path('salary/', SalaryPageTemplateView.as_view(), name='salary_page'),
    path('student_detail/<int:pk>', StudentDetailsPageTemplateView.as_view(), name='student_detail_page'),
    path('student/', StudentPageTemplateView.as_view(), name='students_page'),
    path('subject/', SubjectPageTemplateView.as_view(), name='subject_page'),
    path('inbox/', InboxPageTemplateView.as_view(), name='inbox_page'),
    path('invoice/', InvoicePageTemplateView.as_view(), name='invoice_page'),
    path('timetable/', TimeTablePageTemplateView.as_view(), name='time_table_page'),
    path('department/', DepartmentPageTemplateView.as_view(), name='department_page'),
    path('library/', libraryPageTemplateView.as_view(), name='library_page'),
    path('teachers/', TeachersPageTemplateView.as_view(), name='teachers_page'),
    path('fees_collection', FeesCollectionPageTemplateView.as_view(), name='fees_collection')
]
