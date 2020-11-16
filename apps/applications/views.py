from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from django.views.generic.edit import UpdateView

from . import forms, utils
from .models import Application


def index(request):
    return render(request, 'applications/index.html')


def output(request):
    return render(request, 'applications/applications_output.html')


class ApplicationsOutputView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login_url')

    def get(self, request):
        application = None
        if(request.user.is_superuser or request.user.is_expert):
            application = Application.objects.all()
        elif(request.user.is_active):
            application = Application.objects.filter(user=request.user)
        return render(request, 'applications/applications_output.html', context={'application': application})


class ApplicationAddExpert(LoginRequiredMixin, UpdateView):
    model = Application
    fields = ['designated_expert']
    template_name = 'applications/applications_add_expert.html'
    login_url = reverse_lazy('login_url')
    success_url = reverse_lazy('applications_output_url')


class ApplicationsCreateView(LoginRequiredMixin, CreateView):
    model = Application
    template_name = 'applications/applications_create.html'
    form_class = forms.ApplicationCreateForm
    login_url = reverse_lazy('login_url')
    success_url = reverse_lazy('applications_output_url')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ApplicationsDetailView(LoginRequiredMixin, utils.ObjectDetailMixin, View):
    model = Application
    template_name = 'applications/applications_detail.html'
    form_class = forms.ApplicationCommentForm
    login_url = reverse_lazy('login_url')
    success_url = reverse_lazy('applications_detail_url')


class ApplicationsReportingView(LoginRequiredMixin, View):
    def get(self, request):
        application = None
        if(request.user.is_superuser or request.user.is_expert):
            application = Application.objects.all()
        elif(request.user.is_active):
            application = Application.objects.filter(user=request.user)
        return render(request, 'applications/applications_reporting.html', context={'application': application})


def switch_application_status(request, id):
    app = get_object_or_404(Application, pk=id)
    if app.user == request.user:
        if app.status:
            app.status = False
            app.save()
        else:
            app.status = True
            app.save()
    return HttpResponseRedirect(reverse_lazy('applications_output_url'))


class ApplicationUpdateView(LoginRequiredMixin, UpdateView):
    model = Application
    fields = [
        'project_name', 'project_site', 'data_project_start', 'legal_entity',
        'project_stage', 'project_description', 'businessmodel_description', 'problem_decision',
        'consumer_decision', 'product_difference', 'have_photo', 'photo_video_project', 'patentability',
        'market_size', 'marketing_description', 'sale_strategy', 'desciption_risk', 'client_count',
        'previous_investors', 'middle_cost', 'budget_development', 'middle_revenue', 'team_count',
        'fio_team', 'team_education', 'team_experience', 'position_member', 'team_create', 'ready_relocate',
        'ready_development', 'adress_company', 'inn_company', 'fio', 'email', 'upload']
    template_name = 'applications/application_update_form.html'
    login_url = reverse_lazy('login_url')
    success_url = reverse_lazy('applications_output_url')
