![image](https://github.com/AstralArchitect/patateOS/assets/154975712/c505561e-35a8-435c-9385-2f8121c49162)
# ATTENTION !!!

Ne fonctionne que sur raspberry pi.\
Ce programme doit avoir les droits de root pour pouvoir installer patate-app-launcher.\
Ne pas installer sur votre ordinateur personnel. Risque de perdre vos donnés personnelles.\
Utillisez un ordinateur (personnelement j'utilise un raspberry pi 2) dédié pour tourner patateOS.

# Introduction à PatateOS : 
Ceci est un "os", pour raspberry pi 2, il utilise la [raspberry pi sense hat](https://www.kubii.com/fr/modules-capteurs/1081-raspberry-pi-sense-hat-kubii-640522710799.html) et affiche des informations dessus tels que la température, l'usage du CPU et de la méméoire, la pression et l'humidité. On peut aussi y installer d'autres programmes tel que [pong](https://github.com/AstralArchitect/pong-patateOS).

# Materiel Requis : 
  1. Un raspberry Pi avec au choix soit Raspbian, Debian ou Ubuntu déja installé (personnelement j'utilise un raspberry pi 2 avec Raspbian)
  2. Une Raspberry Pi Sense Hat.

# 1. Installation de patateOS:
### note :
Veuillez d'abord configurer votre raspberry pi de façon à ce qu'il n'ai pas d'interface graphique


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
sudo git clone https://github.com/AstralArchitect/patate-app-launcher.git /root/installation/
```

Puis déplacez vous dans le dossier:
```
cd /root/installation/
```
Enfin executez le script d'installation :
```
sudo python3 installation/Installation.py
```

# 2. Démmarer patate-app-launcher :

Pour démmarer patate-app-launcher, Allumez votre raspberry pi. D'abord, le Sense Hat va se mettre en multicolor. Attendez un petit moment et les lumières vont s'éteindres et enfin une foit que vous voyez défiler "Bonjour." alors Patate-app-launcher à démmaré.

# 3. Utiliser patate-app-launcher :

## 3.1 Afficher les programmes installés :

Pour afficher les programmes installés poussez le joystick vers le haut. Pour voir le suivant repoussez vers le haut une fois que le nom du premier a finit de déffiler et ainsi de suite(une fois que vous avez fait déffilé tout les programmes, la liste repartira du début).

### 3.1.1 Éxécuter le progarmme séléctionnné :

Pour éxécuter le programme séléctionné appuyez sur le joystck de la Sense Hat AVANT que le nom ai finit de déffiler( Si vous le faite apprès, vous mettrez patate-app-launcher à jour).

### 3.1.2 Désinstaller le programme séléctonné :

Pour Désinsaller le programme séléctionné poussez le joystick de la Sense Hat vers la gauche avant que le nom est fini de déffiler.

## 3.2 Mettre à jour patate-app-launcher :

Pour mettre à jour patate-app-launcher appuyez sur le joystick de la Sense Hat.

## 3.3 Éteindre votre ordinateur :

Pour éteindre l'ordinateur poussez le joystick de la Sense Hat vers le bas
