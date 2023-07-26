from django.shortcuts import render
from .models import Porteiro, Veiculo, Motorista, CadastroInter
from .models import CadastroInterEntrada, CadastroTerceiros, EmpresaTerceiros
from .models import CadastroTerceirosSaida
from django.shortcuts import redirect
from django.http import JsonResponse
import json
from datetime import date
import datetime
from django.utils import timezone


def login(request):
    if request.method == 'POST':
        matricula = request.POST['matricula']
        senha = request.POST['senha']
        try:
            porteiro = Porteiro.objects.get(matricula=matricula, senha=senha)
            request.session['nivel'] = porteiro.nivel
            return redirect('cadastro')

        except Porteiro.DoesNotExist:
            error_message = 'Matrícula ou senha inválidas. Tente novamente.'
            return render(request, 'porteiros/paginas/login.html', {'error_message': error_message})

    return render(request, 'porteiros/paginas/login.html')


def cadastro(request):
    return render(request, 'porteiros/paginas/cadastro.html')


def cadastro_inter(request):
    if request.method == 'POST':
        placa = request.POST.get('placa')
        veiculo = request.POST.get('veiculo')
        data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        km_saida = request.POST.get('km_saida')
        lacre_saida = request.POST.get('lacre_saida')
        nfs_saida = request.POST.get('nfs_saida')
        motorista = request.POST.get('nome')
        carga = request.POST.get('carga')
        qtde_malotes_saida = request.POST.get('qtde_malotes_saida')
        carga_extra = request.POST.get('carga_extra')
        especificacao_carga = request.POST.get('especificacao_carga')

        hoje = date.today()
        entrada_existente = CadastroInter.objects.filter(placa=placa, data__date=hoje).exists()

        if entrada_existente:
            return render(request, 'porteiros/paginas/cadastro_inter_entrada.html')

        destino_list = request.POST.getlist('destino')  
        destino = ",".join(destino_list) if destino_list else None

        outros_destinos = request.POST.get('outrosDestinos')
        if outros_destinos:
            destino = destino + ',' + outros_destinos

        registro_saida = CadastroInter(
            placa=placa,
            veiculo=veiculo,
            data=data,
            km_saida=km_saida,
            lacre_saida=lacre_saida,
            nfs_saida=nfs_saida,
            motorista=motorista,
            destino=destino,
            carga=carga,
            qtde_malotes_saida=qtde_malotes_saida,
            carga_extra=carga_extra,
            especificacao_carga=especificacao_carga
        )
        registro_saida.save()

        return redirect('cadastro')

    veiculos = Veiculo.objects.all()
    motoristas = Motorista.objects.all()
    agora = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    contexto = {'veiculos': veiculos, 'motoristas': motoristas, 'data_hora_atual': agora}
    return render(request, 'porteiros/paginas/cadastro_inter.html', contexto)


def cadastro_terceiros(request):
    if request.method == 'POST':
        placa_entrada = request.POST.get('placa_entrada')
        veiculo_entrada = request.POST.get('veiculo_entrada')
        data = timezone.now()
        cnpj = request.POST.get('cnpj')
        carga = request.POST.get('carga_entrada')
        motorista = request.POST.get('motorista')
        ajudante = request.POST.get('ajudante')
        paletes = request.POST.get('paletes')
        chapelex = request.POST.get('chapelex')
        nfs_prefixo = request.POST.get('nfs_prefixo')
        nfs_de = request.POST.get('nfs_de')
        nfs_ate = request.POST.get('nfs_ate')
        nfs_exceto = request.POST.get('nfs_exceto')
        nfs_apenas = request.POST.get('nfs_apenas')

        arquivo = CadastroTerceiros(
            placa_entrada=placa_entrada,
            veiculo_entrada=veiculo_entrada,
            data=data,
            cnpj=cnpj,
            carga=carga,
            motorista=motorista,
            ajudante=ajudante,
            paletes=paletes,
            chapelex=chapelex,
            nfs_prefixo=nfs_prefixo,
            nfs_de=nfs_de,
            nfs_ate=nfs_ate,
            nfs_exceto=nfs_exceto,
            nfs_apenas=nfs_apenas
        )
        arquivo.save()

        agora = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        if EmpresaTerceiros.objects.filter(cnpj=cnpj).exists():
            mensagem = f"O CNPJ {cnpj} já está cadastrado."
        else:
            mensagem = f"O CNPJ {cnpj} está disponível para cadastro."

        contexto = {
            'data_hora': agora,
            'mensagem': mensagem,
        }

        contexto_cupom = {
            'placa_entrada': placa_entrada,
            'veiculo_entrada': veiculo_entrada,
            'data': data,
            'cnpj': cnpj,
            'carga': carga,
            'motorista': motorista,
            'ajudante': ajudante,
            'paletes': paletes,
            'chapelex': chapelex,
            'nfs_prefixo': nfs_prefixo,
            'nfs_de': nfs_de,
            'nfs_ate': nfs_ate,
            'nfs_exceto': nfs_exceto,
            'nfs_apenas': nfs_apenas,
        }

        # Renderize o template "cupom.html" e retorne a resposta
        return render(request, 'porteiros/paginas/cupom.html', contexto_cupom)

    agora = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    contexto = {'data_hora_atual': agora}
    return render(request, 'porteiros/paginas/cadastro_terceiros.html', contexto)


def cadastro_veiculo(request):
    if request.method == 'POST':
        placa = request.POST['placa']
        veiculo = request.POST['veiculo']
        empresa = request.POST['empresa']

        veiculos = Veiculo(placa=placa, veiculo=veiculo, empresa=empresa)
        veiculos.save()

        return redirect('cadastro')

    return render(request, 'porteiros/paginas/cadastro_veiculo.html')


def cadastro_usuario(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        matricula = request.POST['matricula']
        senha = request.POST['senha']
        nivel = request.POST['nivel']

        porteiro = Porteiro(nome=nome, matricula=matricula, senha=senha, nivel=nivel)
        porteiro.save()
        return redirect('cadastro')

    return render(request, 'porteiros/paginas/cadastro_usuario.html')


def cadastro_motorista(request):
    if request.method == 'POST':
        nome = request.POST['nome']

        motoristas = Motorista(nome=nome)
        motoristas.save()
        return redirect('cadastro')

    return render(request, 'porteiros/paginas/cadastro_motorista.html')


def cadastro_inter_entrada(request):
    if request.method == 'POST':
        placa_entrada = request.POST.get('placa_entrada')
        data_entrada = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        km_entrada = request.POST.get('km_entrada')
        lacre_entrada = request.POST.get('lacre_entrada')
        nfs_entrada = request.POST.get('nfs_entrada')
        qtde_malotes_entrada = request.POST.get('qtde_malotes_entrada')

        registro_entrada = CadastroInterEntrada(
            placa_entrada=placa_entrada,
            data_entrada=data_entrada,
            km_entrada=km_entrada,
            lacre_entrada=lacre_entrada,
            nfs_entrada=nfs_entrada,
            qtde_malotes_entrada=qtde_malotes_entrada
        )
        registro_entrada.save()

        return redirect('cadastro')

    agora = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    contexto = {'data_hora_atual': agora}
    return render(request, 'porteiros/paginas/cadastro_inter_entrada.html', contexto)


def verificar_entrada(request):
    if request.method == 'POST':
        placa = request.POST.get('placa')
        hoje = date.today()
        entrada_cadastro_inter = CadastroInter.objects.filter(placa=placa, data__date=hoje).exists()
        entrada_cadastro_inter_entrada = CadastroInterEntrada.objects.filter(placa_entrada=placa, data_entrada__date=hoje).exists()

        return JsonResponse({
            'existe_entrada': entrada_cadastro_inter,
            'existe_entrada_inter': entrada_cadastro_inter_entrada
        })


def buscar_veiculo(request):
    placa = request.POST.get('placa')
    veiculo = Veiculo.objects.filter(placa=placa).first()

    if veiculo:
        response = {
            'veiculo': veiculo.veiculo,
        }
    else:
        response = {
            'veiculo': '',
        }

    return JsonResponse(response)


def cadastro_cnpj_terceiros(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cnpj = request.POST.get('cnpj')

        empresa = EmpresaTerceiros(
            nome=nome,
            cnpj=cnpj,
        )
        empresa.save()

        return redirect('cadastro_terceiros')

    return render(request, 'porteiros/paginas/cadastro_cnpj_terceiros.html')


def verificar_cnpj(request):
    if request.method == 'POST':
        cnpj = request.POST.get('cnpj')

        try:
            empresa = EmpresaTerceiros.objects.get(cnpj=cnpj)
            response = {'nome': empresa.nome}
        except EmpresaTerceiros.DoesNotExist:
            response = {'error': 'CNPJ inválido.'}

        return JsonResponse(response)

    # Em caso de solicitação GET ou outros métodos, retorne um erro
    return JsonResponse({'error': 'Método inválido'})


def verificar_placa(request):
    if request.method == 'POST':
        placa = request.POST.get('placa')
        data_atual = timezone.now().date()

        try:
            registro = CadastroTerceiros.objects.get(placa_entrada=placa, data=data_atual)
            return JsonResponse({'placa_existente': True, 'registro': registro.placa_entrada})
        except CadastroTerceiros.DoesNotExist:
            return JsonResponse({'placa_existente': False})

    return JsonResponse({'placa_existente': False})


def relatorio(request):
    return render(request, 'porteiros/paginas/relatorio.html')


def relatorio_inter_saida(request):
    selected_data_inicio = request.GET.get('data_inicio', date.today())
    selected_data_fim = request.GET.get('data_fim', date.today())
    selected_placa = request.GET.get('placa')

    data = CadastroInter.objects.all()

    if selected_data_inicio:
        data = data.filter(data__date__gte=selected_data_inicio)

    if selected_data_fim:
        data = data.filter(data__date__lte=selected_data_fim)

    if selected_placa:
        data = data.filter(placa=selected_placa)

    placas = CadastroInter.objects.filter(data__date__range=[selected_data_inicio, selected_data_fim]).values_list('placa', flat=True).distinct()

    return render(request, 'porteiros/paginas/relatorio_inter_saida.html', {'placas': placas, 'selected_data_inicio': selected_data_inicio, 'selected_data_fim': selected_data_fim, 'selected_placa': selected_placa, 'data': data})


def relatorio_inter_entrada(request):
    selected_data_inicio = request.GET.get('data_inicio', date.today().strftime('%Y-%m-%d'))
    selected_data_fim = request.GET.get('data_fim', date.today().strftime('%Y-%m-%d'))
    selected_placa = request.GET.get('placa')

    data = CadastroInterEntrada.objects.all()

    if selected_data_inicio:
        data = data.filter(data_entrada__date__gte=selected_data_inicio)

    if selected_data_fim:
        data = data.filter(data_entrada__date__lte=selected_data_fim)

    if selected_placa:
        data = data.filter(placa_entrada=selected_placa)

    placas = CadastroInterEntrada.objects.filter(data_entrada__date__range=[selected_data_inicio, selected_data_fim]).values_list('placa_entrada', flat=True).distinct()

    return render(request, 'porteiros/paginas/relatorio_inter_entrada.html', {'placas': placas, 'selected_data_inicio': selected_data_inicio, 'selected_data_fim': selected_data_fim, 'selected_placa': selected_placa, 'data': data})


def relatorio_terceiros_entrada(request):
    selected_data_inicio = request.GET.get('data_inicio', date.today().strftime('%Y-%m-%d'))
    selected_data_fim = request.GET.get('data_fim', date.today().strftime('%Y-%m-%d'))
    selected_placa = request.GET.get('placa')

    data = CadastroTerceiros.objects.all()

    if selected_data_inicio:
        data = data.filter(data__date__gte=selected_data_inicio)

    if selected_data_fim:
        data = data.filter(data__date__lte=selected_data_fim)

    if selected_placa:
        data = data.filter(placa_entrada=selected_placa)

    placas = CadastroTerceiros.objects.filter(data__date__range=[selected_data_inicio, selected_data_fim]).values_list('placa_entrada', flat=True).distinct()

    return render(request, 'porteiros/paginas/relatorio_terceiros_entrada.html', {'placas': placas, 'selected_data_inicio': selected_data_inicio, 'selected_data_fim': selected_data_fim, 'selected_placa': selected_placa, 'data': data})


def relatorio_terceiros_saida(request):
    selected_data_inicio = request.GET.get('data_inicio', date.today().strftime('%Y-%m-%d'))
    selected_data_fim = request.GET.get('data_fim', date.today().strftime('%Y-%m-%d'))
    selected_placa = request.GET.get('placa')

    data = CadastroTerceirosSaida.objects.all()

    if selected_data_inicio:
        data = data.filter(data_saida__date__gte=selected_data_inicio)

    if selected_data_fim:
        data = data.filter(data_saida__date__lte=selected_data_fim)

    if selected_placa:
        data = data.filter(placa_saida=selected_placa)

    placas = CadastroTerceirosSaida.objects.filter(data_saida__date__range=[selected_data_inicio, selected_data_fim]).values_list('placa_saida', flat=True).distinct()

    return render(request, 'porteiros/paginas/relatorio_terceiros_saida.html', {'placas': placas, 'selected_data_inicio': selected_data_inicio, 'selected_data_fim': selected_data_fim, 'selected_placa': selected_placa, 'data': data})


def cadastro_terceiros_saida(request):
    if request.method == 'POST':
        placa_saida = request.POST.get('placa_saida')
        data_saida = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        descarga = request.POST.get('descarga')
        motivo = request.POST.get('motivo')
        descarga_paga = request.POST.get('descarga_paga')
        paletes_saida = request.POST.get('paletes_saida')
        chapelex_saida = request.POST.get('chapelex_saida')
        nfs_prefixo_saida = request.POST.get('nfs_prefixo_saida')
        nfs_de_saida = request.POST.get('nfs_de_saida')
        nfs_ate_saida = request.POST.get('nfs_ate_saida')
        nfs_exceto_saida = request.POST.get('nfs_exceto_saida')
        nfs_apenas_saida = request.POST.get('nfs_apenas_saida')

        arquivo = CadastroTerceirosSaida(
            placa_saida=placa_saida,
            data_saida=data_saida,
            descarga=descarga,
            motivo=motivo,
            descarga_paga=descarga_paga,
            paletes_saida=paletes_saida,
            chapelex_saida=chapelex_saida,
            nfs_prefixo_saida=nfs_prefixo_saida,
            nfs_de_saida=nfs_de_saida,
            nfs_ate_saida=nfs_ate_saida,
            nfs_exceto_saida=nfs_exceto_saida,
            nfs_apenas_saida=nfs_apenas_saida
        )
        arquivo.save()

        return redirect('cadastro')

    ultimo_cadastro = CadastroTerceiros.objects.last()
    contexto = {'cadastro': ultimo_cadastro}
    return render(request, 'porteiros/paginas/cadastro_terceiros_saida.html', contexto)


def busca_terceiros(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        placa_entrada = data.get('placa', '').strip().upper()
        current_date = timezone.now().date()

        entrada_existente = CadastroTerceiros.objects.filter(placa_entrada=placa_entrada, data__date=current_date).exists()
        saida_existente = CadastroTerceirosSaida.objects.filter(placa_saida=placa_entrada, data_saida__date=current_date).exists()

        data = {'placa_entrada_existente': entrada_existente, 'placa_saida_existente': saida_existente}
        return JsonResponse(data)

    return JsonResponse({})


def cupom(request):
    return render(request, 'porteiros/paginas/cupom.html')
