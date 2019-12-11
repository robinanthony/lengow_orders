from django.core.management.base import BaseCommand
from orders.models import Order
import requests
import xml.etree.ElementTree as et
from datetime import time, date
from dateutil import parser

URL = "http://test.lengow.io/orders-test.xml"


class Command(BaseCommand):
    help = "Va chercher le fichier disponible sur l'adresse \
            http://test.lengow.io/orders-test.xml et crée les commandes \
            disponibles dans la base de données."

    def handle(self, *args, **options):
        # Récupération du fichier xml
        response = requests.get(URL)
        data = response.content

        # Récupération de la racine du fichier XML
        xml_root = et.fromstring(data)

        # On récupère le noeud parent qui nous interesse : <orders></orders>
        orders = xml_root.find("orders")

        # On parcours les balises <order></order>
        for order_xml in orders.iter('order'):
            # Pour chaque order, on initialise une nouvelle commande
            # que l'on remplit puis sauvegarde.
            new_order = Order()

            new_order.id = order_xml.find("order_id").text
            new_order.marketplace = order_xml.find("marketplace").text
            new_order.idFlux = order_xml.find("idFlux").text
            new_order.order_amount = order_xml.find("order_amount").text

            if order_xml.find("order_purchase_date").text is not None:
                dt = parser.parse(order_xml.find("order_purchase_date").text)
                new_order.order_purchase_date = date(dt.year, dt.month, dt.day)
            if order_xml.find("order_purchase_heure").text is not None:
                dt = parser.parse(order_xml.find("order_purchase_heure").text)
                new_order.order_purchase_heure = time(dt.hour, dt.minute, dt.second)

            new_order.save()
