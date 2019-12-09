from django.core.management.base import BaseCommand, CommandError
from orders.models import Order
import requests
import xml.etree.ElementTree as ET
from datetime import time, date

from dateutil import parser

class Command(BaseCommand):
    help = "Va chercher le fichier disponible sur l'adresse \
            http://test.lengow.io/orders-test.xml et crée les commandes \
            disponibles dans la base de données."

    def handle(self, *args, **options):
        URL = "http://test.lengow.io/orders-test.xml"

        # Récupération du fichier xml
        response = requests.get(URL)
        data = response.content

        # Récupération de la racine du fichier XML
        xml_root = ET.fromstring(data)

        # On récupère le noeud parent qui nous interesse : <orders></orders>
        orders = xml_root.find("orders")

        # On parcours les balises <order></order>
        for order in orders.iter('order'):
            # Pour chaque order, on initialise une nouvelle commande
            # que l'on remplit puis sauvegarde.
            actual_order = Order()

            actual_order.id = order.find("order_id").text
            actual_order.marketplace = order.find("marketplace").text
            actual_order.idFlux = order.find("idFlux").text
            actual_order.order_amount = order.find("order_amount").text

            if (order.find("order_purchase_date").text is not None):
                dt = parser.parse(order.find("order_purchase_date").text)
                actual_order.order_purchase_date = date(dt.year, dt.month, dt.day)
            if (order.find("order_purchase_heure").text is not None):
                dt = parser.parse(order.find("order_purchase_heure").text)
                actual_order.order_purchase_heure = time(dt.hour, dt.minute, dt.second)

            actual_order.save()
