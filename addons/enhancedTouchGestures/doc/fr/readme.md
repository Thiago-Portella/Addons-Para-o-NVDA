# Enhanced Touch Gestures #

* Auteur : Joseph Lee
* Télécharger [version stable][1]
* Compatibilité NVDA : 2022.4 et plus

Cette extension fournit des gestes supplémentaires sur l'écran tactile pour
NVDA. Elle fournit également un ensemble de gestes pour parcourir facilement
lorsque vous êtes en mode navigation.

Note : Cette extension requiert NVDA 2022.3 ou une version ultérieure
s'exécutant sur un ordinateur tactile avec Windows 10 ou 11.

## Commandes

### Disponible partout

* Double tape 4 doigts : basculer en mode aide à la saisie.
* Glisser vers la droite quatre doigts : basculer clavier tactile
  (habituellement activer celui-ci).
* Glisser vers la gauche quatre doigts : bascule de la dictée (Windows+H;
  Windows 10 Version 1709 ou version ultérieure).

### Mode objet

* Glisser vers le bas 3 doigts : lecture de la fenêtre active.
* Glisser vers la gauche 3 doigts : annonce l'objet en focus.
* Glisser vers la droite 3 doigts : annonce l'objet navigateur courant.
* Glisser vers le haut 4 doigts : annonce le titre de la fenêtre active.
* Glisser vers le bas 4 doigts : annonce le texte de la barre d'état.

## Mode web tactile

Ce mode tactile, est disponible dans le mode navigation, il vous permet de
naviguer dans le document par l'élément sélectionné. Pour basculer en mode
web, depuis le mode navigation dans le document , il faut effectuer une tape
à trois doigts. Dans ce mode, en glissant vers le haut ou vers le bas avec
un seul doigt pour parcourir entre les éléments disponibles dans les modes
de navigation, tout en glissant vers la droite ou vers la gauche avec un
seul doigt pour vous déplacer vers l'élément choisi suivant ou précédent
respectivement. Une fois que vous sortez du mode navigation dans le
document, le mode objet tactile est utilisé.

## Paramètres synthétiseur mode tactile

Vous pouvez utiliser ce mode pour modifier rapidement les paramètres du
synthétiseur telles que choisir une voix et modifier le volume. Dans ce
mode, glisser vers la gauche ou vers la droite deux doigts pour se déplacer
entre les paramètres synthétiseur et glisser vers le haut ou vers le bas
deux doigts gestes pour modifier les valeurs. Ces gestes reflètes celle des
commandes en boucle des paramètres synthétiseur sur le clavier.

## Version 23.02

* NVDA 2022.4 ou version ultérieure est requis.
* Windows 10 21H2 (November 2021 Update/build 19044) ou ultérieure est
  requise.

## Version 23.01

* NVDA 2022.3 ou version ultérieure est requis.
* Windows 10 ou ultérieure est requis car Windows 8.1 n'est plus pris en
  charge par Microsoft en janvier 2023.
* Il est possible de réassigner le clavier tactile et les commandes de
  bascule de la dictée à partir du dialogue Gestes de commandes dans la
  catégorie Enhanced Touch Gestures.
* Suppression de solution de contournement en lecture seule pour les touches
  de clavier tactile telles qu'elle est résolue dans Windows 10.

## Version 22.03

* NVDA 2021.3 ou version ultérieure est requis.
* Un message d'avertissement sera affiché lors de la tentative d'installer
  l'extension sur Windows 7, 8 et 8.1.

## Version 21.10

* NVDA 2021.2 ou version ultérieure est requis en raison de modifications de
  NVDA qui affectent cette extension.

## Version 21.08

* Prise en charge initiale de Windows 11.

## Version 21.01

* NVDA 2020.3 ou version ultérieure est requis.
* Sur Windows 10 Version 1709 et ultérieure, faire glisser vers la gauche
  quatre doigts pour basculer la dictée (Windows+H).
* Supprimer le basculment de la commande du support d'interaction tactile
  dédiée à partir de l'extension.
* Comme le support d'interaction tactile peut être basculé à partir du
  panneau des paramètres d'interaction tactile de NVDA, un panneau de
  paramètres Enhanced Touch Gestures dédié a été supprimé.

## Version 20.09

* Supprimé la possibilité de laisser NVDA désactiver l'interaction tactile
  pendant jusqu'à dix secondes (l'émulation de commande tactile).
* Suppression de la fonctionnalité d'annonce des coordonnées par des bips.

## Version 20.07

* Ajout d'une commande clavier pour basculer l'interaction tactile ou
  activer / désactiver l'émulation tactile (Control+Alt+NVDA+T).
* Comme NVDA 2020.1 et plus comprend une commande tactile pour effectuer un
  clic droit souris (une tape un doigt en maintenant appuyé), la commande a
  été supprimée de cette extension. Par conséquent, NVDA 2020.1 ou version
  ultérieure est requis.
* La possibilité de laisser NVDA désactiver l'interaction tactile pendant
  jusqu'à dix secondes (l'émulation de commande  tactile) est obsolète. À
  l'avenir, cette fonctionnalité basculera à la place l'interaction tactile.
* Dans les versions snapshots de développement de NVDA en raison des
  modifications des fonctionnalités d'interaction tactile, La fonctionnalité
  d'émulation de commande  tactile et le panneau de paramètres Enhanced
  Touch Gestures seront désactivés. La commande utilisée pour activer
  l'émulation de commande  tactile pour basculer à la place l'interaction
  tactile.
* La fonctionnalité d'annonce des coordonnées par des bips est obsolète et
  sera supprimée dans une future version de l'extension.
* L'annonce de la coordonnée par des bips ne sera pas entendu lors de
  l'utilisation du clavier tactile.
* NVDA ne semblera plus ne rien faire ou jouer des tonalités d'erreur tout
  en explorant l'installation de la saisie moderne telle que le panneau des
  emojis via le tactile.
* NVDA présentera un message d'erreur si le clavier tactile ne peut pas être
  activé (glisser vers la droite quatre doigts).

## Version 20.06

* Résolu de nombreux problèmes de style de codage et des bogues potentiels
  avec Flake8.

## Version 20.04

* Le geste de clic droit souris (une tape un doigt en maintenant appuyé)
  fait désormais partie de NVDA 2020.1.

## Version 20.01

* NVDA 2019.3 ou version ultérieure est requis.
* La commande tactile de basculement (y compris l'émulation tactile) ne
  fonctionnera plus si la prise en charge tactile est complètement
  désactivée.

## Version 19.11

* Ajout des messages d'aide à la saisie pour les commandes tactiles
  supplémentaires.

## Version 19.09

* La prise en charge tactile peut désormais être désactivée de partout, pas
  seulement à partir de profils autres que le profil normal.

## Version 19.07

* Modifications internes pour la prise en charge des futures versions NVDA.

## Version 18.12

* Modifications internes pour la prise en charge des futures versions NVDA.

## Version 18.08

* Compatible avec NVDA 2018.3 et les versions futures.

## Version 18.06

* Les paramètres de l'extension sont désormais disponibles dans le nouvel
  écran Paramètres NVDA multi-catégories sous la catégorie "Enhanced Touch
  Gestures". Par conséquent, NVDA 2018.2 est requis.
* Correction de problèmes de compatibilité avec wxPython 4.

## Version 18.04

* Résout un problème où la catégorie interaction tactile dans le panneau
  Paramètres de NVDA peut provoquer l'apparition de sons d'erreur en raison
  des modifications apportées à partir de cette extension.

## Version 18.03

* NVDA 2018.1 est requis.
* Parce que NVDA 2018.1 est livré avec la case à cocher frappe tactile, la
  case à cocher n'est plus incluse dans cette extension.

## Version 17.12

* Nécessite NVDA 2017.4. Plus précisément, cette extension peut désormais
  gérer les commutateurs de profil de configuration.
* Comme NVDA 2017.4 inclut l'annonce d'orientation de l'écran, cette
  fonctionnalité ne fait plus partie de cette extension.
* Ajout d'une case à cocher masquée dans le dialogue Interaction Tactile
  pour désactiver complètement le support tactile (disponible si des profils
  autres que la configuration normale sont actifs).
* Si vous utilisez NVDA 2018.1 ou une version ultérieure le dialogue
  Interaction Tactile apparaîtra deux fois sous le menu des préférences de
  NVDA. Le deuxième élément est le dialogue accompagné de l'extension.
* Dans le dialogue Interaction Tactile de l'extension, le mode frappe
  tactile n'est plus affiché si vous utilisez NVDA 2018.1 ou une version
  ultérieure.

## Version 17.10

* En raison de la politique de support de Microsoft, Windows 8 (version
  originale) n'est plus supporté.
* NVDA n'annonce plus deux fois l'orientation de l'écran lors de l'exécution
  des versions snapshots de développement de NVDA 2017.4.

## Version 17.07.1

* Ajout d'une option dans le dialogue Interaction Tactile pour basculer
  manuellement une émulation tactile sans utilisation d'une minuterie.
* Avec le mode émulation manuelle désactivée, si l'émulation tactile  est
  activée avant l'expiration de la durée de l'émulation, l'interaction
  tactile serait activée.

## Version 17.07

* Ajout d'un nouveau dialogue intitulée Interaction Tactile dans le menu des
  préférences de NVDA pour configurer comment NVDA fonctionne avec les
  écrans tactiles.
* Après avoir installé cette version, lorsque vous appuyez sur les touches
  du clavier tactile, vous devez faire une double tape sur la touche
  désirée. Vous pouvez revenir à l'ancienne façon en activant la frappe
  tactile à partir du dialogue Interaction Tactile.
* Ajout d'une commande (non assignée) pour permettre à NVDA d'ignorer les
  gestes tactiles pendant 10 secondes maximum.
* Ajout d'une option dans le dialogue Interaction Tactile pour permettre à
  NVDA de suspendre l'interaction tactile entre 3 à 10 secondes afin
  d'effectuer des gestes d'écran tactile directement (comme si NVDA ne
  fonctionnait pas, la valeur par défaut est de 5 secondes).
* Ajout de messages de débogage lors d'un clic droit (taper et maintenir)
  pour être enregistré dans le journal NVDA (nécessite NVDA 2017.1 ou
  version ultérieure).
* En raison des modifications apportées lors de la sonorisation des
  coordonnées de l'écran, NVDA 2017.1 ou version ultérieure est requise.

##Version 17.03

* Correction d'un problème au cours duquel l'annonce de la coordonnée par
  des bips n'a pas été sonorisé ou une tonalité d'erreur a été sonorisé lors
  de l'utilisation de NVDA 2017.1 ou version ultérieure.

##Version 16.12

* Le mode web tactile fonctionne dans Microsoft Edge, Microsoft Word et
  d'autres où le mode navigation est utilisé.
* Ajout des listes et régions aux éléments du mode web tactile.

## Version 16.06

* Première version stable.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=enhancedTouchGestures
