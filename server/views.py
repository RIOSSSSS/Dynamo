from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from django.views.generic import TemplateView



def home(request):
    return render(request, 'menu.html')  # Supondo que você tem um template 'home.html'
def menu_views(request):
    return render(request, 'menu.html')  # Supondo que você tem um template 'home.html'

from .forms import CustomUserCreationForm

def cadastro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'cadastro.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login




from django.contrib.auth.decorators import login_required

from django.contrib import messages

import logging

logger = logging.getLogger(__name__)


from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            django_login(request, user)
            messages.success(request, "Login realizado com sucesso.")
            return redirect('menu')
        else:
            messages.error(request, "Usuário ou senha incorretos.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def item1_view(request):
    # Sua lógica de visualização aqui
    return render(request, 'item1.html') 

def item2_view(request):
    # Sua lógica de visualização aqui
    return render(request, 'item2.html') 

def item3_view(request):
    # Sua lógica de visualização aqui
    return render(request, 'item3.html') 

def item4_view(request):
    # Sua lógica de visualização aqui
    return render(request, 'item4.html') 

def item5_view(request):
    # Sua lógica de visualização aqui
    return render(request, 'item5.html') 

def novo1_view(request):
    # Sua lógica de visualização aqui
    return render(request, 'novo1.html') 

def novo2_view(request):
    # Sua lógica de visualização aqui
    return render(request, 'novo2.html') 

def novo3_view(request):
    # Sua lógica de visualização aqui
    return render(request, 'novo3.html') 

def novo4_view(request):
    # Sua lógica de visualização aqui
    return render(request, 'novo4.html') 

def novo5_view(request):
    # Sua lógica de visualização aqui
    return render(request, 'novo5.html') 




from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from .models import UserProfile

@method_decorator(login_required, name='dispatch')
class MeusDadosView(TemplateView):
    template_name = 'dados.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        context['user_profile'] = user_profile
        return context
    
    


# views.py
from .models import UserProfile
from django.contrib.auth.decorators import login_required



@login_required
def my_data(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'dados.html', {'user_profile': user_profile, 'user': request.user})



from django.shortcuts import render

def sucesso(request):
    return render(request, 'sucesso.html')  # Substitua 'sucesso.html' pelo nome real do seu template de sucesso

def falha(request):
    return render(request, 'falha.html')  # Substitua 'falha.html' pelo nome real do seu template de falha



from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import stripe
import logging

logger = logging.getLogger(__name__)

# Configure the Stripe API key.
stripe.api_key = "sk_test_51OIaNcFVm1TF86fp47xAdFyuN9L08AxPYZB0FYlMbGRC2ESsULwWTUcIO2hL4yzOLJSh8YIzKcJkCEwiwXqyn1PU00uXCvPTrM"
# This is your Stripe CLI webhook secret for testing your endpoint locally.
endpoint_secret = 'whsec_a405ca5981b0441e497b494eb20add74335f49503c11c19c67c53c6feba80c43'

# ...

@require_POST
@csrf_exempt
def webhook(request):
    payload = request.body
    sig_header = request.headers.get('Stripe-Signature')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        logger.error('Invalid payload: {}'.format(str(e)))
        return JsonResponse({'success': False}, status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        logger.error('Invalid signature: {}'.format(str(e)))
        return JsonResponse({'success': False}, status=400)
    except Exception as e:
        # Log other exceptions
        logger.error('Error handling webhook: {}'.format(str(e)))
        return JsonResponse({'success': False}, status=500)

    # Handle the event
    logger.info('Received event of type: {}'.format(event['type']))

    # Adicione esta parte para redirecionar com base no tipo de evento
    if event['type'] == 'payment_intent.succeeded':
        logger.info('Redirecionando para sucesso')
        return redirect('url_sucesso')  # Substitua 'url_sucesso' pela URL desejada após o pagamento bem-sucedido
    elif event['type'] == 'payment_intent.payment_failed':
        logger.info('Redirecionando para falha')
        return redirect('url_falha')     # Substitua 'url_falha' pela URL desejada após o pagamento falhar

    return JsonResponse({'success': True})



from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)
    return redirect('menu')

    
    
from django.shortcuts import render

def enderecos_cadastrados(request):
    # Sua lógica para endereços cadastrados aqui
    return render(request, 'enderecos_cadastrados.html')  # Ou substitua por seu template correspondente

def meus_pedidos(request):
    # Sua lógica para meus pedidos aqui
    return render(request, 'meus_pedidos.html')  # Ou substitua por seu template correspondente


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DadosUsuario

@login_required
def enderecos_cadastrados(request):
    # Sua lógica para endereços cadastrados aqui
    return render(request, 'enderecos_cadastrados.html')

def favoritos(request):
    # Recupera os itens favoritos do localStorage
    favorites = request.session.get('favorites', [])

    # Renderiza a página favoritos.html e passa os itens favoritos para o template
    return render(request, 'favoritos.html', {'favorites': favorites})

def minhas_compras(request):
    # Lógica para exibir as compras do usuário aqui
    return render(request, 'minhas_compras.html')


import json

from django.http import JsonResponse

def atualizar_informacoes(request):
    if request.method == 'POST':
        # Tente carregar os dados do corpo da solicitação como JSON
        try:
            dados = json.loads(request.body)
            # Agora você pode acessar os dados como um dicionário Python
            nome = dados.get('nome')
            email = dados.get('email')
            
            # Substitua estas linhas pela lógica real que você precisa para atualizar o modelo
            # Supondo que você tenha um modelo User personalizado
            user = request.user  # Se você está usando a autenticação integrada do Django
            user.username = nome
            user.email = email
            user.save()

            # Retorna uma resposta de sucesso (pode ser ajustado conforme necessário)
            return JsonResponse({'mensagem': 'Informações atualizadas com sucesso!'})
        except json.JSONDecodeError:
            # Se houver um erro ao analisar o JSON, retorne uma resposta de erro
            return JsonResponse({'erro': 'Erro ao analisar os dados JSON'}, status=400)

    # Se a solicitação não for POST, retorne uma resposta de erro
    return JsonResponse({'erro': 'Método de requisição não permitido'}, status=405)


