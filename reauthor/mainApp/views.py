from django.shortcuts import render, redirect
from mainApp.secrets import *
from .models import Profile
import requests

def main(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def kakao(request):
    url = "https://kauth.kakao.com/oauth/authorize?response_type=code"
    client_id = REST_API_KEY
    redirect_uri = REDIRECT_URI

    url += "&client_id=" + client_id
    url += "&redirect_uri=" + redirect_uri

    return redirect(url)

def oauth(request):
    client_id = REST_API_KEY
    redirect_uri = REDIRECT_URI
    code = request.GET.get('code')

    token_url = requests.post('https://kauth.kakao.com/oauth/token', data = {'grant_type':'authorization_code', 'cliend_id':client_id, 'redirect_uri':redirect_uri, 'code':code})
    token_json = token_url.json()
    # error = token_json.get('error',None)
    access_token = token_json.get('access_token')

    # 사용자 정보 요청
    profile_request = requests.get('https://kapi.kakao.com/v2/user/me', headers={'Authorization':'Bearer {access_token}'})
    profile_json = profile_request.json()

    kakao_account = profile_json.get('kakao_account')
    # email = kakao_account.get('email')
    kakao_id = profile_json.get('id')

    
    return redirect('/')

def signup(request):
    return render(request, 'signup.html')

def upload1(request):
    return render(request,'upload1.html')

def upload2(request):
    return render(request,'upload2.html')

def upload3(request):
    return render(request,'upload3.html')