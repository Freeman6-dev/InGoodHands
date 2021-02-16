from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from charity_donation_app.models import Donation, Institution, Category
from user_app.models import MyUser


class IndexView(View):

    def get(self, request):
        donations = Donation.objects.all()
        bags = 0
        for object in donations:
            bags += object.quantity
        institutions_helped = donations.count()
        institutions = Institution.objects.all()
        foundations = []
        non_governmental_institution = []
        local_collection = []
        for object in institutions:
            if object.type == 1:
                foundations.append(object)
            elif object.type == 2:
                non_governmental_institution.append(object)
            else:
                local_collection.append(object)

        context = {'bags': bags, 'institutions_helped': institutions_helped, 'foundations': foundations,
                   'non_governmental_institution': non_governmental_institution, 'local_collection': local_collection}
        return render(request, 'index.html', context)


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        form = {
            'email': request.POST['email'],
            'password': request.POST['password']
        }
        user = authenticate(request, username=form['email'], email=form['email'], password=form['password'])
        if user is not None:
            login(request, user)
            return redirect('index')
        return redirect('register')


class RegisterView(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = {
            'first_name': request.POST['name'],
            'last_name': request.POST['surname'],
            'email': request.POST['email'],
            'password': request.POST['password'],
            'password2': request.POST['password2']
        }
        if form['password'] == form['password2']:
            try:
                user = MyUser.objects.create(first_name=form['first_name'], last_name=form['last_name'],
                                             email=form['email'], username=form['email'])
                user.save()
                user.set_password(form['password'])
                user.save()
                return redirect('login')
            except Exception as e:
                message = f'Ten adres email został już użyty do rejestracji lub dane są niepoprawne.'
        else:
            message = 'Hasła muszą być takie same!'
        return render(request, 'register.html', {'message': message})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('index')


class AddDonationView(LoginRequiredMixin, View):

    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        context = {'categories': categories, 'institutions': institutions}
        return render(request, 'form.html', context)


class RemindPasswordView(View):
    pass


class UserSettingsView(View):

    def get(self, request):
        return render(request, 'user_settings.html')

    def post(self, request):
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        user = MyUser.objects.get(pk=request.user.pk)
        if user.check_password(password):
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            message = 'Twoje dane zostały zaktualizowane'
        else:
            message = 'Aby zaktualizować dane musisz podać poprawne hasło!'
        return render(request, 'user_settings.html', {'message': message})


class UserProfileView(View):

    def get(self, request):
        user_donations = Donation.objects.filter(user=request.user.id).order_by('is_taken')
        return render(request, 'user_profile.html', {'user_donations': user_donations})


class ChangeUserPasswordView(View):

    def get(self, request):
        return render(request, 'change_password.html')

    def post(self, request):
        old_pass = request.POST['old_pass']
        new_pass = request.POST['new_pass']
        new_pass2 = request.POST['new_pass2']
        user = MyUser.objects.get(pk=request.user.pk)
        if user.check_password(old_pass):
            if new_pass == new_pass2:
                user.set_password(new_pass)
                user.save()
                message = 'Hasło zostało zmienione'
            else:
                message = 'Musisz podać 2 razy takie samo hasło!'
        else:
            message = 'Wpisałeś niepoprawne aktualne hasło!'
        return render(request, 'change_password.html', {'message': message})


class DonationTakenView(View):

    def get(self, request, pk):
        donation = Donation.objects.get(pk=pk)
        if donation.is_taken:
            donation.is_taken = False
            donation.save()
        else:
            donation.is_taken = True
            donation.save()
        return redirect('user_profile')
