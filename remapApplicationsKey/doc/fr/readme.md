# Remapper la touche applications


## Information
* Auteurs : Rui Fontes basé sur le travail de Héctor J. Benítez Corredera
* Mis à jour le 22/03/2024
* Télécharger [version stable][1]
* Compatibilité NVDA : version 2019.3 et ultérieure


## Présentation
Une extension simple pour ces ordinateurs qui n'apportent pas la touche d'applications ou que votre touche d'applications ne fonctionne pas.
Nous devrons assigner la touche ou la combinaison de touches que nous souhaitons pour avoir à nouveau la touche Applications.
Dans NVDA / Préférences / Gestes de commandes... / RemapApplicationsKey nous pouvons attribuer la combinaison que nous souhaitons.


## Observations
Lors de l'affectation d'une combinaison de touches ou d'une seule touche, nous devons prendre en compte que ladite  combinaison ou touche n'est utilisé dans aucune application.
Par exemple Ctrl + Flèche bas cela pourrait fonctionner dans la plupart du système, mais cela nous donnerait une erreur dans Google Chrome en laissant pas afficher le menu contextuel.
En mettant un exemple moi je mets habituellement la touche "impression écran" qui est généralement dans la rangée supérieure du côté droit et celle-ci est généralement la deuxième ou la troisième touche.
Eh bien, nous pouvons savoir quelle est si nous utilisons l'aide des commandes de NVDA, pour cela, nous appuyons sur la touche NVDA + & et nous commençons à explorer les touches sur le clavier, quand  il nous dit "impression écran" celle-ci sera la touche que nous recherchions. nous pouvons sortir de l'aide des commandes  de NVDA en appuyant à nouveau sur NVDA + &.
Ceci est un exemple laissant au goût de l'utilisateur le choix de ça touche ou combinaison de touches.


## Traducteurs et contributeurs:
* Espagnol : Rémy Ruiz
* Français : Rémy Ruiz
* Russe : Valentin Kupriyanov
* Ukrainien : VovaMobile
* Turc : Umut Korkmaz


## Journal des changements


### Version 2023.09.02
* Maintenant l'extension est maintenu par Rui Fontes et l'équipe portugaise de NVDA
* Maintenant le code est basé en anglais.


### Version 0.4
* Ajout des langues russes, ukrainiennes et turques.
* Ajout de la compatibilité avec NVDA 2023.1


### Version 0.3
* Changé la façon d'invoquer la touche applications native de NVDA par la native de Windows, car il s'agit d'une méthode plus fiable et plus directe.
* Ajout de la possibilité du clic gauche et droit de la souris au focus.
Nous devrons assigner les combinaisons de touches correspondantes dans la boîte de dialogue Gestes de commandes.
Lorsque nous exécutons l'action, la souris se déplacera au focus et fera le clic correspondant, et un son sera entendu indiquant que le clic a été exécuté.


### Version 0.2
* Compatibilité avec NVDA 2022


### Version 0.1.5
* Correction d'un problème dans les extensions de NVDA.
* Ajout de la traduction française.


### Version 0.1
* Version initiale.
[1]: https://github.com/ruifontes/RemapKeyAplication-para-NVDA/releases/download/2025.07.14/remapApplicationsKey-2025.07.14.nvda-addon
