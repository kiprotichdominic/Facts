
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# def usersignup(request):
#     if request.method == 'POST':
#         form =CustomUserCreationForm (request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             current_site = get_current_site(request)
#             email_subject = 'Activate Your Account'
#             message = render_to_string('users/activate_account.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             to_email = form.cleaned_data.get('email')
#             email = EmailMessage(email_subject, message, to=[to_email])
#             email.send()
#             return HttpResponse('We have sent you an email, please confirm your email address to complete registration')
#     else:
#         form = CustomUserCreationForm ()
#     return render(request, 'registration/signup.html', {'form': form})

# def activate_account(request, uidb64, token):
#     try:
#         uid = force_bytes(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         return HttpResponse('Your account has been activate successfully')
#     else:
#         return HttpResponse('Activation link is invalid!')