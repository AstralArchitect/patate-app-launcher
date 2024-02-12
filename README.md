# installation et configuration :
## Installation :
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

## Commandes de base :

## 1. Usage du CPU et de la mémoire :
Pour voir lusage du cpu et de la mémoire poussez le joystick de votre sense hat vers la gauche

## 2. Température, Pression et Humidité :

Pour voire la température la pression et l'humidité poussez le joystick du sense hat vers la droite

Attention: la température peut être fausse car le capteur se trouve près de votre ordinateur qui chauffe

## 3. non attribué : 

Par défaut pousser le joystick vers le haut écrira "Vous n'avez rien installe.". Pour installer des programmes, [lisez cette page](https://github.com/AstralArchitect/pong-PatateOS)

## 4. Mise à jour :

Pour mettre à jour le programme appuyez sur le joystick

## 5. Arret : 

Pour éteindre votre ordinateur poussez le joystick vers le bas
