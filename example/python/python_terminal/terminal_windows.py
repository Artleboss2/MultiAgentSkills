#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Terminal Windows en Python
Un terminal de commande complet avec historique, autocomplétion et commandes intégrées
"""

import os
import sys
import subprocess
import shlex
from pathlib import Path
import readline
import atexit
from datetime import datetime

class Terminal:
    def __init__(self):
        self.current_dir = os.getcwd()
        self.history_file = os.path.join(os.path.expanduser("~"), ".python_terminal_history")
        self.command_history = []
        self.aliases = {
            'll': 'dir',
            'ls': 'dir',
            'clear': 'cls',
        }
        
        # Configuration de l'historique avec readline
        self.setup_history()
        
        # Variables d'environnement personnalisées
        self.env_vars = {}
        
    def setup_history(self):
        """Configure l'historique des commandes avec readline"""
        try:
            if os.path.exists(self.history_file):
                readline.read_history_file(self.history_file)
        except:
            pass
        
        # Sauvegarde automatique de l'historique à la fermeture
        atexit.register(self.save_history)
        
        # Configuration de l'autocomplétion
        readline.parse_and_bind("tab: complete")
        readline.set_completer(self.path_completer)
        
    def save_history(self):
        """Sauvegarde l'historique des commandes"""
        try:
            readline.write_history_file(self.history_file)
        except:
            pass
    
    def path_completer(self, text, state):
        """Autocomplétion des chemins et fichiers"""
        try:
            line = readline.get_line_buffer()
            
            if not text:
                completions = [f for f in os.listdir('.')]
            else:
                path = os.path.dirname(text) or '.'
                prefix = os.path.basename(text)
                
                try:
                    files = os.listdir(path)
                    completions = [
                        os.path.join(path, f) for f in files 
                        if f.startswith(prefix)
                    ]
                except:
                    completions = []
            
            return completions[state] if state < len(completions) else None
        except:
            return None
    
    def get_prompt(self):
        """Retourne le prompt personnalisé"""
        username = os.environ.get('USERNAME', 'user')
        hostname = os.environ.get('COMPUTERNAME', 'PC')
        current_path = os.getcwd()
        
        # Raccourcir le chemin si trop long
        if len(current_path) > 40:
            current_path = "..." + current_path[-37:]
        
        return f"\033[92m{username}@{hostname}\033[0m:\033[94m{current_path}\033[0m$ "
    
    def execute_builtin(self, command, args):
        """Exécute les commandes intégrées"""
        if command == 'cd':
            return self.cmd_cd(args)
        elif command == 'exit' or command == 'quit':
            return self.cmd_exit(args)
        elif command == 'pwd':
            return self.cmd_pwd(args)
        elif command == 'echo':
            return self.cmd_echo(args)
        elif command == 'set':
            return self.cmd_set(args)
        elif command == 'history':
            return self.cmd_history(args)
        elif command == 'help':
            return self.cmd_help(args)
        elif command == 'alias':
            return self.cmd_alias(args)
        elif command == 'cls' or command == 'clear':
            return self.cmd_clear(args)
        elif command == 'date':
            return self.cmd_date(args)
        elif command == 'time':
            return self.cmd_time(args)
        elif command == 'env':
            return self.cmd_env(args)
        else:
            return None
    
    def cmd_cd(self, args):
        """Change le répertoire courant"""
        try:
            if not args:
                # cd sans argument va au répertoire home
                new_dir = os.path.expanduser("~")
            else:
                new_dir = args[0]
            
            # Gérer les chemins relatifs et absolus
            if not os.path.isabs(new_dir):
                new_dir = os.path.join(os.getcwd(), new_dir)
            
            new_dir = os.path.normpath(new_dir)
            
            if os.path.isdir(new_dir):
                os.chdir(new_dir)
                self.current_dir = os.getcwd()
                return True
            else:
                print(f"Erreur: Le répertoire '{new_dir}' n'existe pas")
                return False
        except Exception as e:
            print(f"Erreur lors du changement de répertoire: {e}")
            return False
    
    def cmd_exit(self, args):
        """Quitte le terminal"""
        print("Au revoir!")
        sys.exit(0)
    
    def cmd_pwd(self, args):
        """Affiche le répertoire courant"""
        print(os.getcwd())
        return True
    
    def cmd_echo(self, args):
        """Affiche du texte"""
        print(' '.join(args))
        return True
    
    def cmd_set(self, args):
        """Définit ou affiche les variables d'environnement"""
        if not args:
            # Afficher toutes les variables
            for key, value in sorted(os.environ.items()):
                print(f"{key}={value}")
        elif len(args) == 1 and '=' in args[0]:
            # Définir une variable
            key, value = args[0].split('=', 1)
            os.environ[key] = value
            self.env_vars[key] = value
        else:
            # Afficher une variable spécifique
            for arg in args:
                value = os.environ.get(arg, '')
                if value:
                    print(f"{arg}={value}")
        return True
    
    def cmd_history(self, args):
        """Affiche l'historique des commandes"""
        try:
            history_len = readline.get_current_history_length()
            for i in range(1, history_len + 1):
                print(f"{i:4d}  {readline.get_history_item(i)}")
        except:
            for i, cmd in enumerate(self.command_history, 1):
                print(f"{i:4d}  {cmd}")
        return True
    
    def cmd_help(self, args):
        """Affiche l'aide"""
        help_text = """
Terminal Python - Commandes intégrées:

  cd [répertoire]     - Change le répertoire courant
  pwd                 - Affiche le répertoire courant
  ls / dir            - Liste les fichiers (commande système)
  echo [texte]        - Affiche du texte
  clear / cls         - Efface l'écran
  set [var=valeur]    - Définit ou affiche les variables d'environnement
  env                 - Affiche toutes les variables d'environnement
  history             - Affiche l'historique des commandes
  alias [nom=cmd]     - Définit ou affiche les alias
  date                - Affiche la date actuelle
  time                - Affiche l'heure actuelle
  help                - Affiche cette aide
  exit / quit         - Quitte le terminal

Fonctionnalités:
  - Autocomplétion avec TAB
  - Historique avec flèches ↑/↓
  - Exécution de toutes les commandes Windows
  - Support des pipes (|) et redirections (>, >>)
  - Variables d'environnement
  - Alias de commandes

Raccourcis clavier:
  TAB                 - Autocomplétion
  ↑/↓                 - Navigation dans l'historique
  Ctrl+C              - Annuler la commande courante
  Ctrl+D / exit       - Quitter le terminal
"""
        print(help_text)
        return True
    
    def cmd_alias(self, args):
        """Définit ou affiche les alias"""
        if not args:
            # Afficher tous les alias
            for name, cmd in sorted(self.aliases.items()):
                print(f"{name}={cmd}")
        elif '=' in args[0]:
            # Définir un alias
            name, cmd = args[0].split('=', 1)
            self.aliases[name] = cmd
            print(f"Alias créé: {name}={cmd}")
        else:
            # Afficher un alias spécifique
            for arg in args:
                if arg in self.aliases:
                    print(f"{arg}={self.aliases[arg]}")
        return True
    
    def cmd_clear(self, args):
        """Efface l'écran"""
        os.system('cls' if os.name == 'nt' else 'clear')
        return True
    
    def cmd_date(self, args):
        """Affiche la date actuelle"""
        print(datetime.now().strftime("%d/%m/%Y"))
        return True
    
    def cmd_time(self, args):
        """Affiche l'heure actuelle"""
        print(datetime.now().strftime("%H:%M:%S"))
        return True
    
    def cmd_env(self, args):
        """Affiche toutes les variables d'environnement"""
        for key, value in sorted(os.environ.items()):
            print(f"{key}={value}")
        return True
    
    def parse_command(self, cmd_line):
        """Parse la ligne de commande"""
        # Gérer les alias
        parts = cmd_line.split()
        if parts and parts[0] in self.aliases:
            parts[0] = self.aliases[parts[0]]
            cmd_line = ' '.join(parts)
        
        # Gérer les pipes
        if '|' in cmd_line:
            return self.execute_pipe(cmd_line)
        
        # Gérer les redirections
        if '>' in cmd_line or '>>' in cmd_line:
            return self.execute_redirect(cmd_line)
        
        # Commande simple
        try:
            parts = shlex.split(cmd_line)
        except:
            parts = cmd_line.split()
        
        if not parts:
            return True
        
        command = parts[0]
        args = parts[1:]
        
        # Essayer d'abord les commandes intégrées
        result = self.execute_builtin(command, args)
        if result is not None:
            return result
        
        # Sinon, exécuter comme commande système
        return self.execute_system(cmd_line)
    
    def execute_pipe(self, cmd_line):
        """Exécute une commande avec pipes"""
        commands = cmd_line.split('|')
        
        try:
            # Premier processus
            process = subprocess.Popen(
                commands[0].strip(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
                text=True
            )
            
            # Processus intermédiaires et final
            for cmd in commands[1:]:
                process = subprocess.Popen(
                    cmd.strip(),
                    stdin=process.stdout,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True,
                    text=True
                )
            
            stdout, stderr = process.communicate()
            
            if stdout:
                print(stdout, end='')
            if stderr:
                print(stderr, end='', file=sys.stderr)
            
            return process.returncode == 0
        except Exception as e:
            print(f"Erreur lors de l'exécution du pipe: {e}")
            return False
    
    def execute_redirect(self, cmd_line):
        """Exécute une commande avec redirection"""
        try:
            if '>>' in cmd_line:
                parts = cmd_line.split('>>')
                mode = 'a'
            else:
                parts = cmd_line.split('>')
                mode = 'w'
            
            command = parts[0].strip()
            filename = parts[1].strip()
            
            # Exécuter la commande
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True
            )
            
            # Écrire dans le fichier
            with open(filename, mode, encoding='utf-8') as f:
                f.write(result.stdout)
            
            if result.stderr:
                print(result.stderr, end='', file=sys.stderr)
            
            return result.returncode == 0
        except Exception as e:
            print(f"Erreur lors de la redirection: {e}")
            return False
    
    def execute_system(self, cmd_line):
        """Exécute une commande système"""
        try:
            result = subprocess.run(
                cmd_line,
                shell=True,
                text=True
            )
            return result.returncode == 0
        except KeyboardInterrupt:
            print("\n^C")
            return False
        except Exception as e:
            print(f"Erreur: {e}")
            return False
    
    def run(self):
        """Boucle principale du terminal"""
        print("=" * 60)
        print("  Terminal Python pour Windows")
        print("  Tapez 'help' pour obtenir de l'aide")
        print("  Tapez 'exit' ou 'quit' pour quitter")
        print("=" * 60)
        print()
        
        while True:
            try:
                # Afficher le prompt et lire la commande
                cmd_line = input(self.get_prompt()).strip()
                
                # Ignorer les lignes vides
                if not cmd_line:
                    continue
                
                # Ajouter à l'historique
                self.command_history.append(cmd_line)
                
                # Exécuter la commande
                self.parse_command(cmd_line)
                
            except KeyboardInterrupt:
                print("\n^C")
                print("Tapez 'exit' ou 'quit' pour quitter")
                continue
            except EOFError:
                print("\nAu revoir!")
                break
            except Exception as e:
                print(f"Erreur inattendue: {e}")
                continue

def main():
    """Point d'entrée principal"""
    terminal = Terminal()
    terminal.run()

if __name__ == "__main__":
    main()