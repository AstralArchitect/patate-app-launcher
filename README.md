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

# Documentation ...