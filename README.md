# installation et configuration :
## Installation :

Créez un fichier nommé /root/start.sh et ajoutez y:

```sh
#!/bin/bash

cd /root/python/

python main.py
```

Ensuite, créez le répertoire /root/python/  et /root/python/update/ en exécutant la commande:

```sh
sudo mkdir /root/python/ /root/python/update/
```

Puis téléchargez les librairies python pour la sense-hat :

```sh
sudo apt-get install python3 python3-sense-hat python3-psutil git -y
```

Enfin, clonez le repository en utilisant la commande :

```sh
sudo git clone https://github.com/AstralArchitect/python-sense-hat.git /root/python/
```

## Executer le script :

Pour éxécuter le script, utilisez ces commandes:

```sh
sudo su
cd ~/python
python3 main.py
```
### Executer le script automatiquement au démarrage :

Pour executer le script automatiquement au démarrage modifiez le fichier /etc/rc.local et mettez y le contenu suivant:

```sh
#! /bin/sh
# chkconfig: 345 99 10
case "$1" in
  start)
    # Executes our script
    sudo sh /root/start.sh
    ;;
  *)
    ;;
esac
exit 0
```

Ensuite il ne vous reste plus qu'a redémarrer votre ordinateur et le script s'éxécutera automatiquement!

# Documentation :

## Commandes de base :

## 1. Usage du CPU et de la mémoire :
Pour voir lusage du cpu et de la mémoire poussez le joystick de votre sense hat vers la gauche

## 2. Température, Pression et Humidité :

Pour voire la température la pression et l'humidité poussez le joystick du sense hat vers la droite

Attention: la température peut être fausse car le capteur se trouve près de votre ordinateur qui chauffe

## Date : 

Pour voir la date poussez le joystick de votre sense hat vers le haut

## Mise à jour :

Pour mettre à jour le programme appuyez sur le joystick

## Arret : 

Pour éteindre votre ordinateur poussez le joystick vers le bas