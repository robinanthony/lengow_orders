from django.db import models


# Les commentaires représentent un exemple des lignes choisies
class Order(models.Model):
    # <order_id>111-2222222-3333333</order_id>
    # Je suis parti du principe que ce champs est l'identifiant d'une commande
    id = models.CharField(primary_key=True, max_length=50)

    # <marketplace>amazon</marketplace>
    marketplace = models.CharField(max_length=75)

    # <idFlux>88827</idFlux>
    idFlux = models.IntegerField()

    # <order_purchase_date>2014-10-21</order_purchase_date>
    order_purchase_date = models.DateField(null=True)

    # <order_purchase_heure>14:59:51</order_purchase_heure>
    order_purchase_heure = models.TimeField(null=True)

    # <order_amount>34.5</order_amount>
    # Au vu des exemples, un chiffre après la virgule suffit.
    # J'ai peut-être vu gros avec 5 chiffres ...
    order_amount = models.DecimalField(decimal_places=1, max_digits=5)

    class Meta:
        verbose_name = "Commande"
        ordering = ['order_purchase_date']

    def __str__(self):
        return "Commande d'id {}, effectuée sur {} au sein du flux {} le {} à {} en quantité {}.".format(
            self.id, self.marketplace, self.idFlux, self.order_purchase_date,
            self.order_purchase_heure, self.order_amount)
