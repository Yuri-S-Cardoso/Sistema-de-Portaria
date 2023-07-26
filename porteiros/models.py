from django.db import models


class Porteiro(models.Model):
    NIVEL_CHOICES = (
        ('gerente', 'Gerente'),
        ('funcionario', 'Funcionário'),
    )
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=10)
    senha = models.CharField(max_length=100)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES)
    tipo = models.CharField(max_length=20)


class Veiculo(models.Model):
    placa = models.CharField(max_length=50)
    veiculo = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)


class Motorista(models.Model):
    nome = models.CharField(max_length=100)


class CadastroInter(models.Model):
    placa = models.CharField(max_length=20)
    veiculo = models.CharField(max_length=50)
    data = models.DateTimeField()
    km_saida = models.IntegerField()
    lacre_saida = models.CharField(max_length=20)
    nfs_saida = models.IntegerField()
    motorista = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    carga = models.CharField(max_length=20)
    qtde_malotes_saida = models.IntegerField()
    carga_extra = models.CharField(max_length=5)
    especificacao_carga = models.CharField(max_length=100, null=True, blank=True)
    outrosDestinos = models.CharField(max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Converte a lista de destinos em uma string separada por vírgulas
        if self.outrosDestinos_list:
            self.outrosDestinos = ",".join(self.outrosDestinos_list)
        super(CadastroInter, self).save(*args, **kwargs)

    @property
    def outrosDestinos_list(self):
        # Retorna a lista de destinos a partir da string armazenada no campo
        if self.outrosDestinos:
            return self.outrosDestinos.split(", ")
        return []

    def __str__(self):
        return f"{self.placa} - {self.destino}"


class CadastroInterEntrada(models.Model):
    placa_entrada = models.CharField(max_length=20)
    data_entrada = models.DateTimeField()
    km_entrada = models.IntegerField()
    lacre_entrada = models.CharField(max_length=20)
    nfs_entrada = models.IntegerField()
    qtde_malotes_entrada = models.IntegerField()


class CadastroTerceiros(models.Model):
    placa_entrada = models.CharField(max_length=10)
    veiculo_entrada = models.CharField(max_length=20)
    data = models.DateTimeField()
    cnpj = models.CharField(max_length=20)
    carga = models.CharField(max_length=20)
    motorista = models.CharField(max_length=50)
    ajudante = models.IntegerField()
    paletes = models.IntegerField()
    chapelex = models.IntegerField()
    nfs_prefixo = models.IntegerField()
    nfs_de = models.IntegerField()
    nfs_ate = models.IntegerField()
    nfs_exceto = models.IntegerField()
    nfs_apenas = models.IntegerField()


class EmpresaTerceiros(models.Model):
    cnpj = models.IntegerField()
    nome = models.CharField(max_length=50)


class CadastroTerceirosSaida(models.Model):
    placa_saida = models.CharField(max_length=10)
    data_saida = models.DateTimeField()
    descarga = models.CharField(max_length=5)
    motivo = models.CharField(max_length=100, null=True, blank=True)
    descarga_paga = models.CharField(max_length=5)
    paletes_saida = models.IntegerField()
    chapelex_saida = models.IntegerField()
    nfs_prefixo_saida = models.IntegerField()
    nfs_de_saida = models.IntegerField()
    nfs_ate_saida = models.IntegerField()
    nfs_exceto_saida = models.IntegerField()
    nfs_apenas_saida = models.IntegerField()
