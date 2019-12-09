# lengow_orders

Problématique

Le but de ce test est de comprendre votre utilisation de Django. Il n'y a pas de piège, nous voulons simplement mesurer votre niveau technique.
Le but est de récupérer des produits provenant d'un flux xml et de les manipuler. Vous pouvez utiliser le SGBD que vous souhaitez.


Tâches
Chaque tâche doit être faite avec les bonnes pratiques et en respectant la PEP8.
- Créer un projet Django
- Créer une app "orders".
- Créer un modèle "Order" reflétant les données présentent dans l'API: http://test.lengow.io/orders-test.xml Vous n'êtes pas obligé de gérer tout les champs, 4-5 champs suffisent.
- Dans cette app créer une commande Django permettant de récupérer les commandes de l'API suivante et de les enregistrer en utilisant le modèle que vous venez de créer.
- Créer les vues nécessaires pour lister les commandes, lister 1 commande et rechercher selon les champs du modèle et afficher les résultats.

Pour aller plus loin

Au choix :
- Ajouter/modifier une commande
- Utiliser Django Rest Framework pour mettre à disposition les commandes précédemment enregistrées en base de données via une API
