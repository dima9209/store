from users.models import User
from products.models import Basket
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import messages
from django.urls import  reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super(UserLoginView,self).get_context_data()
        context['title'] = 'Store - Авторизация'
        return context


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super(UserRegistrationView,self).get_context_data()
        context['title'] = 'Store - Регистрация'
        return context


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'


    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.request.user.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView,self).get_context_data()
        context['title'] = 'Store - Профиль'
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context

# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Поздравляем! Вы успешно зарегистрированы!')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistrationForm()
#     content = {
#         'title': 'Store - Регистрация',
#         'form': form
#     }
#     return render(request, 'users/register.html', content)


#@login_required
#def profile(request):
#    if request.method == 'POST':
#        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect(reverse('users:profile'))
#    else:
#        form = UserProfileForm(instance=request.user)
#    context = {
#        'title': 'Store - Профиль',
#        'form': form,
#        'baskets': Basket.objects.filter(user=request.user)
#    }
#    return render(request, 'users/profile.html', context)
