# ATTENTION !!!

Ne fonctionne que sur raspberry pi.\
Ce programme doit avoir les droits de root pour pouvoir installer patateOS.\
Ne pas installer sur votre ordinateur personnel. Risque de perdre vos donnés personnelles.\
Utillisez un ordinateur (personnelement j'utilise un raspberry pi 2) dédié pour tourner patateOS.

# Introdduction à PatateOS : 
Ceci est un "os", pour raspberry pi 2, il utilise la [raspberry pi sense hat](https://www.kubii.com/fr/modules-capteurs/1081-raspberry-pi-sense-hat-kubii-640522710799.html) et affiche des informations dessus tels que la température, l'usage du CPU et de la méméoire, la pression et l'humidité. On peut aussi y installer d'autres programmes tel que [pong](https://github.com/AstralArchitect/pong-patateOS).

# Materiel Requis : 
  1. Un raspberry Pi avec au choix soit Raspbian, Debian ou Ubuntu déja installé (personnelement j'utilise un raspberry pi 2 avec raspbian)
  2. Une Raspberry Pi Sense Hat.

# installation et configuration :
## Installation :
### note :
Veuillez d'abord configurer votre raspberry pi de façon à ce qu'il n'ai pas d'interface graphique
###


déplacez vous dans /root/

```
cd /root/
```
Créez le répertoir /root/installation/
```
mkdir ./installation/
```
Ensuit installez python3 et git:

```
sudo apt install python3 python3-sense-hat git -y
```

Clonez le repo dans /root/installation/ en tapant les commandes : 
```
sudo git clone https://github.com/AstralArchitect/patateOS.git /root/installation/
```

Puis déplacez vous dans le dossier:
```
cd /root/installation/
```
Enfin executez le script d'installation :
```
sudo python3 installation/Installation.py
```

## Executer le script automatiquement au démarrage :

Si vous avez installé le programme via installation.py, le script s'éxécutera automatiquement au démmarrage !

# Documentation :
## Attention: Grosse mise à jour en cours, ces information peuvent être fausse. Elle seront mise à jour quand la mise à jour n'aura plus de beuges. Merci de votre compréhension.

## Commandes de base :

## 1. Usage du CPU et de la mémoire :
Pour voir l'usage du cpu et de la mémoire poussez le joystick de votre sense hat vers la gauche

## 2. Température, Pression et Humidité :

Pour voire la température la pression et l'humidité poussez le joystick du sense hat vers la droite

Attention: la température peut être fausse car le capteur se trouve près de votre ordinateur qui chauffe

## 3. Non attribué : 

Par défaut pousser le joystick vers le haut écrira "Vous n'avez rien installe.". Pour installer des programmes, [lisez cette page](https://github.com/AstralArchitect/pong-patateOS/blob/main/README.md#cr%C3%A9er-dautres-programmes-sur-patateos-)

## 4. Mise à jour :

Pour mettre à jour le programme appuyez sur le joystick

## 5. Arret : 

Pour éteindre votre ordinateur poussez le joystick vers le bas

