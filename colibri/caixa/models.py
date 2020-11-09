from django.db import models


class Produto(models.Model):
    cod = models.IntegerField(max_length=999, null=False)
    nome = models.CharField(max_length=20, null=False)
    preco = models.IntegerField(max_length=999, null=False)

    class Meta:
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome


class Mesa(models.Model):
    numero = models.CharField(max_length=999, null=False)

    class Meta:
        verbose_name_plural = 'Mesas'

    def __str__(self):
        return self.numero


class Produtolancado(models.Model):
    cod = models.IntegerField(max_length=999, null=False)
    nome = models.CharField(max_length=20, null=False)
    preco = models.IntegerField(max_length=999, null=False)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name_plural = 'Produtos Lancados'

    def __str__(self):
        return self.nome
