import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.conf import settings

@csrf_exempt
def sign_in(request):
    if request.user.is_authenticated:
        return redirect('todos_home')
    
    return render(request, 'sign_in.html')

@csrf_exempt
def auth_receiver(request):
    """
    Google calls this URL after the user has signed in with their Google account.
    """
    print('Inside')
    token = request.POST['credential']

    try:
        user_data = id_token.verify_oauth2_token(
            token, requests.Request(), settings.GOOGLE_OAUTH_CLIENT_ID
        )
    except ValueError:
        return HttpResponse(status=403)

    # Save user data to session
    request.session['user_data'] = user_data
    
    # Get or create a Django user based on the Google account
    email = user_data['email']
    user, created = User.objects.get_or_create(
        username=email,
        defaults={
            'email': email,
            'first_name': user_data.get('given_name', ''),
            'last_name': user_data.get('family_name', '')
        }
    )
    
    # Log in the user using Django's authentication system
    login(request, user)

    # Redirect to the home page
    return redirect('todos_home')

def sign_out(request):
    
    # Clear the session data
    if 'user_data' in request.session:
        del request.session['user_data']
    
    # Logout the user from Django's authentication system
    logout(request)
    
    return redirect('sign_in')