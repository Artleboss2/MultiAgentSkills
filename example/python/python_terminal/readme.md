\# Terminal Windows en Python



Un terminal de commande complet écrit en Python pour Windows, avec toutes les fonctionnalités d'un terminal moderne.



\## 🚀 Fonctionnalités



\### Commandes Intégrées

\- `cd \[répertoire]` - Change le répertoire courant

\- `pwd` - Affiche le répertoire courant

\- `echo \[texte]` - Affiche du texte

\- `clear` / `cls` - Efface l'écran

\- `set \[var=valeur]` - Gère les variables d'environnement

\- `env` - Affiche toutes les variables d'environnement

\- `history` - Affiche l'historique des commandes

\- `alias \[nom=cmd]` - Crée des alias de commandes

\- `date` - Affiche la date actuelle

\- `time` - Affiche l'heure actuelle

\- `help` - Affiche l'aide

\- `exit` / `quit` - Quitte le terminal



\### Fonctionnalités Avancées

✅ \*\*Autocomplétion\*\* - Utilisez TAB pour autocomplèter les chemins et fichiers

✅ \*\*Historique\*\* - Naviguez avec ↑/↓ dans l'historique des commandes

✅ \*\*Pipes\*\* - Support des pipes (`|`) pour chaîner les commandes

✅ \*\*Redirections\*\* - Support des redirections (`>` et `>>`)

✅ \*\*Alias\*\* - Créez des raccourcis pour vos commandes favorites

✅ \*\*Variables d'environnement\*\* - Gestion complète des variables

✅ \*\*Prompt personnalisé\*\* - Affiche utilisateur, machine et chemin actuel

✅ \*\*Commandes Windows\*\* - Exécute toutes les commandes système Windows



\## 📦 Installation



\### Prérequis

\- Python 3.6 ou supérieur

\- Windows (testé sur Windows 10/11)



\### Installation rapide

```bash

\# 1. Téléchargez le fichier terminal\_windows.py



\# 2. (Optionnel) Installez readline pour Windows si pas déjà installé

pip install pyreadline3

```



\## 🎯 Utilisation



\### Lancer le terminal

```bash

python terminal\_windows.py

```



\### Exemples d'utilisation



\#### Navigation

```bash

\# Changer de répertoire

cd C:\\Users\\VotreNom\\Documents

cd ..

cd /



\# Afficher le répertoire courant

pwd

```



\#### Lister les fichiers

```bash

\# dir est une commande Windows native

dir

dir /w

dir \*.txt



\# Vous pouvez aussi créer un alias

alias ls=dir

ls

```



\#### Utiliser les pipes

```bash

\# Exemple avec findstr (équivalent de grep sous Windows)

dir | findstr ".txt"

type fichier.txt | findstr "recherche"

```



\#### Redirections

```bash

\# Écrire la sortie dans un fichier

dir > liste\_fichiers.txt

echo Bonjour le monde > message.txt



\# Ajouter à un fichier existant

echo Nouvelle ligne >> message.txt

```



\#### Variables d'environnement

```bash

\# Définir une variable

set MA\_VARIABLE=valeur



\# Afficher une variable

set MA\_VARIABLE



\# Afficher toutes les variables

env

```



\#### Alias de commandes

```bash

\# Créer un alias

alias ll=dir /w

alias cls=clear



\# Utiliser l'alias

ll



\# Voir tous les alias

alias

```



\#### Historique

```bash

\# Afficher l'historique complet

history



\# Naviguer avec les flèches ↑ et ↓

```



\## ⌨️ Raccourcis Clavier



| Raccourci | Action |

|-----------|--------|

| `TAB` | Autocomplétion des chemins/fichiers |

| `↑` / `↓` | Navigation dans l'historique |

| `Ctrl+C` | Annuler la commande en cours |

| `Ctrl+D` | Quitter le terminal |

| `Ctrl+L` | Effacer l'écran (équivalent à `clear`) |



\## 📝 Exemples Avancés



\### Recherche de fichiers

```bash

\# Chercher tous les fichiers .py dans le répertoire courant

dir \*.py /s



\# Compter le nombre de fichiers

dir | findstr /c:"fichier(s)"

```



\### Travailler avec des fichiers texte

```bash

\# Afficher le contenu d'un fichier

type fichier.txt



\# Rechercher dans un fichier

type fichier.txt | findstr "mot-clé"



\# Créer un fichier rapidement

echo Contenu du fichier > nouveau.txt

```



\### Commandes système Windows

```bash

\# Toutes les commandes Windows fonctionnent

ipconfig

tasklist

systeminfo

netstat -an

ping google.com

```



\## 🔧 Personnalisation



\### Modifier les alias par défaut

Éditez le fichier `terminal\_windows.py` et modifiez le dictionnaire `aliases` dans `\_\_init\_\_`:



```python

self.aliases = {

&nbsp;   'll': 'dir',

&nbsp;   'ls': 'dir',

&nbsp;   'clear': 'cls',

&nbsp;   # Ajoutez vos alias ici

&nbsp;   'edit': 'notepad',

&nbsp;   'python3': 'python',

}

```



\### Modifier le prompt

Modifiez la méthode `get\_prompt()` pour personnaliser l'apparence:



```python

def get\_prompt(self):

&nbsp;   # Personnalisez ici

&nbsp;   return f"MonTerminal> "

```



\## 🐛 Dépannage



\### Module readline non trouvé

Sur Windows, installez `pyreadline3`:

```bash

pip install pyreadline3

```



\### Erreur d'encodage

Si vous avez des problèmes d'affichage de caractères spéciaux, assurez-vous que votre terminal est configuré en UTF-8:

```bash

chcp 65001

```



\### Les flèches ne fonctionnent pas pour l'historique

Installez `pyreadline3` qui est spécifiquement conçu pour Windows.



\## 📋 Fichiers



\- `terminal\_windows.py` - Le terminal principal

\- `.python\_terminal\_history` - Fichier d'historique (créé automatiquement dans votre dossier utilisateur)



\## 💡 Astuces



1\. \*\*Autocomplétion intelligente\*\*: Commencez à taper un nom de fichier et appuyez sur TAB

2\. \*\*Historique persistant\*\*: Votre historique est sauvegardé entre les sessions

3\. \*\*Commandes longues\*\*: Utilisez les alias pour raccourcir les commandes fréquentes

4\. \*\*Pipes multiples\*\*: Vous pouvez chaîner plusieurs commandes avec `|`

5\. \*\*Redirection d'erreurs\*\*: Utilisez `2>` pour rediriger les erreurs



\## 🔜 Améliorations Futures



\- \[ ] Support des scripts batch

\- \[ ] Coloration syntaxique

\- \[ ] Suggestion de commandes

\- \[ ] Support des jobs en arrière-plan

\- \[ ] Intégration Git

\- \[ ] Thèmes de couleurs personnalisables



\## 📄 Licence



Ce projet est libre d'utilisation et de modification.



\## 🤝 Contribution



N'hésitez pas à améliorer ce terminal et à partager vos modifications !



---



\*\*Bon terminal ! 🚀\*\*

