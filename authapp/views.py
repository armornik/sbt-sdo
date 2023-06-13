from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import AppUserLoginForm, UserRegisterForm
from .models import AppUser


def login(request):
    title = 'вход'
    form = AppUserLoginForm(data=request.POST)
    if request.method == 'POST' and form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('info:index'))
    content = {'title': title, 'form': form}
    return render(request, 'authapp/login.html', content)


class RegisterCreateView(SuccessMessageMixin, CreateView):
    model = AppUser
    template_name = 'authapp/register.html'
    form_class = UserRegisterForm
    success_message = 'Вы успешно зарегистрировались'
    # reverse_lazy - для получения урла - для класса
    success_url = reverse_lazy('auth:login')

    def get_context_data(self, **kwargs):
        context = super(RegisterCreateView, self).get_context_data()
        context['title'] = 'СБТ - Регистрация нового пользователя'
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            messages.success(self.request, 'Вы успешно зарегистрировали нового пользователя!')
            user = form.save()
            # if send_verify_mail(user):
            #     print('success sending')
            # else:
            #     print('sending failed')
            return HttpResponseRedirect(reverse('info:index'))
        else:
            # messages.error(self.request, 'Такой пользователь или почта уже существуют!')
            return HttpResponseRedirect(reverse('authapp:register'))


#
# class RegisterCreateView(SuccessMessageMixin, CreateView):
#     model = AppUser
#     template_name = 'authapp/register.html'
#     form_class = UserRegisterForm
#     success_message = 'Вы успешно зарегистрировались'
#     # reverse_lazy - для получения урла - для класса
#     success_url = reverse_lazy('auth:login')
#
#     def get_context_data(self, **kwargs):
#         context = super(RegisterCreateView, self).get_context_data()
#         context['title'] = 'СБТ - Регистрация нового пользователя'
#         return context
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST, request.FILES)
#         print(request)
#         print(request.user.is_superuser)
#         print(traceback.format_exc())
#         if request.user.is_superuser:
#             print(1)
#             print(traceback.format_exc())
#             if form.is_valid():
#                 print(3)
#                 print(traceback.format_exc())
#                 messages.success(self.request, 'Вы успешно зарегистрировали нового пользователя!')
#                 user = form.save()
#                 # if send_verify_mail(user):
#                 #     print('success sending')
#                 # else:
#                 #     print('sending failed')
#                 return HttpResponseRedirect(reverse('authapp:login'))
#             else:
#                 print(2)
#                 print(traceback.format_exc())
#                 messages.error(self.request, 'Такой пользователь или почта уже существуют!')
#                 return HttpResponseRedirect(reverse('authapp:register'))
#         else:
#             return HttpResponseRedirect(reverse('authapp:login'))

# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user and user.is_active:
#                 auth.login(request, user)
#                 # reverse - определяет путь к странице
#                 return HttpResponseRedirect(reverse('index'))
#         else:
#             print(form.errors)
#     else:
#         form = UserLoginForm()
#     context = {'form': form}
#     return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('authapp:login'))
