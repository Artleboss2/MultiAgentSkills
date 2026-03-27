#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Terminal Windows Avancé en Python
Version avec colorisation, suggestions et fonctionnalités étendues
"""

import os
import sys
import subprocess
import shlex
from pathlib import Path
import readline
import atexit
from datetime import datetime
import json
import platform

# Codes ANSI pour les couleurs (fonctionne sur Windows 10+)
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Couleurs de base
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Couleurs vives
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

class AdvancedTerminal:
    def __init__(self):
        self.current_dir = os.getcwd()
        self.history_file = os.path.join(os.path.expanduser("~"), ".python_terminal_history")
        self.config_file = os.path.join(os.path.expanduser("~"), ".python_terminal_config.json")
        self.command_history = []
        self.last_exit_code = 0
        
        # Activer les couleurs ANSI sur Windows
        if platform.system() == 'Windows':
            os.system('')  # Active le support ANSI
        
        # Charger la configuration
        self.config = self.load_config()
        
        # Alias par défaut
        self.aliases = self.config.get('aliases', {
            'll': 'dir',
            'ls': 'dir',
            'clear': 'cls',
            'cat': 'type',
            'rm': 'del',
            'cp': 'copy',
            'mv': 'move',
            'mkdir': 'md',
            'rmdir': 'rd',
        })
        
        # Configuration de l'historique avec readline
        self.setup_history()
        
        # Variables d'environnement personnalisées
        self.env_vars = {}
        
        # Commandes favorites (pour suggestions)
        self.favorite_commands = self.config.get('favorites', [])
        
    def load_config(self):
        """Charge la configuration depuis le fichier"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {}
    
    def save_config(self):
        """Sauvegarde la configuration"""
        try:
            self.config['aliases'] = self.aliases
            self.config['favorites'] = self.favorite_commands
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
        except:
            pass
        
    def setup_history(self):
        """Configure l'historique des commandes avec readline"""
        try:
            if os.path.exists(self.history_file):
                readline.read_history_file(self.history_file)
        except:
            pass
        
        atexit.register(self.save_history)
        readline.parse_and_bind("tab: complete")
        readline.set_completer(self.smart_completer)
        
    def save_history(self):
        """Sauvegarde l'historique et la configuration"""
        try:
            readline.write_history_file(self.history_file)
            self.save_config()
        except:
            pass
    
    def smart_completer(self, text, state):
        """Autocomplétion intelligente"""
        try:
            line = readline.get_line_buffer()
            
            # Si on est au début de la ligne, suggérer des commandes
            if line.strip() == text and not os.path.sep in text:
                # Commandes intégrées + commandes favorites
                commands = ['cd', 'pwd', 'echo', 'set', 'history', 'help', 'alias', 
                           'clear', 'cls', 'date', 'time', 'env', 'exit', 'quit',
                           'mkdir', 'tree', 'grep', 'find', 'which', 'calc', 
                           'sysinfo', 'color', 'theme']
                commands.extend(self.aliases.keys())
                commands.extend(self.favorite_commands)
                completions = [cmd for cmd in set(commands) if cmd.startswith(text)]
            else:
                # Complétion de fichiers/dossiers
                if not text:
                    completions = [f for f in os.listdir('.')]
                else:
                    path = os.path.dirname(text) or '.'
                    prefix = os.path.basename(text)
                    
                    try:
                        files = os.listdir(path)
                        completions = []
                        for f in files:
                            if f.startswith(prefix):
                                full_path = os.path.join(path, f)
                                if os.path.isdir(full_path):
                                    completions.append(full_path + os.sep)
                                else:
                                    completions.append(full_path)
                    except:
                        completions = []
            
            return completions[state] if state < len(completions) else None
        except:
            return None
    
    def get_prompt(self):
        """Retourne le prompt colorisé personnalisé"""
        username = os.environ.get('USERNAME', 'user')
        hostname = os.environ.get('COMPUTERNAME', 'PC')
        current_path = os.getcwd()
        
        # Raccourcir le chemin si trop long
        if len(current_path) > 50:
            parts = Path(current_path).parts
            if len(parts) > 3:
                current_path = os.path.join(parts[0], '...', *parts[-2:])
        
        # Indicateur de statut (vert si succès, rouge si erreur)
        status_color = Colors.BRIGHT_GREEN if self.last_exit_code == 0 else Colors.BRIGHT_RED
        status = "✓" if self.last_exit_code == 0 else "✗"
        
        prompt = (
            f"{status_color}{status}{Colors.RESET} "
            f"{Colors.BRIGHT_CYAN}{username}@{hostname}{Colors.RESET}"
            f":{Colors.BRIGHT_BLUE}{current_path}{Colors.RESET}"
            f"{Colors.BRIGHT_YELLOW}${Colors.RESET} "
        )
        
        return prompt
    
    def print_success(self, message):
        """Affiche un message de succès"""
        print(f"{Colors.BRIGHT_GREEN}✓{Colors.RESET} {message}")
    
    def print_error(self, message):
        """Affiche un message d'erreur"""
        print(f"{Colors.BRIGHT_RED}✗ Erreur:{Colors.RESET} {message}")
    
    def print_warning(self, message):
        """Affiche un avertissement"""
        print(f"{Colors.BRIGHT_YELLOW}⚠{Colors.RESET} {message}")
    
    def print_info(self, message):
        """Affiche une information"""
        print(f"{Colors.BRIGHT_CYAN}ℹ{Colors.RESET} {message}")
    
    def execute_builtin(self, command, args):
        """Exécute les commandes intégrées"""
        builtin_commands = {
            'cd': self.cmd_cd,
            'exit': self.cmd_exit,
            'quit': self.cmd_exit,
            'pwd': self.cmd_pwd,
            'echo': self.cmd_echo,
            'set': self.cmd_set,
            'history': self.cmd_history,
            'help': self.cmd_help,
            'alias': self.cmd_alias,
            'cls': self.cmd_clear,
            'clear': self.cmd_clear,
            'date': self.cmd_date,
            'time': self.cmd_time,
            'env': self.cmd_env,
            'tree': self.cmd_tree,
            'grep': self.cmd_grep,
            'find': self.cmd_find,
            'which': self.cmd_which,
            'calc': self.cmd_calc,
            'sysinfo': self.cmd_sysinfo,
            'color': self.cmd_color,
            'theme': self.cmd_theme,
        }
        
        if command in builtin_commands:
            return builtin_commands[command](args)
        return None
    
    def cmd_cd(self, args):
        """Change le répertoire courant"""
        try:
            if not args:
                new_dir = os.path.expanduser("~")
            elif args[0] == '-':
                # cd - retourne au répertoire précédent
                new_dir = os.environ.get('OLDPWD', os.path.expanduser("~"))
            else:
                new_dir = args[0]
            
            if not os.path.isabs(new_dir):
                new_dir = os.path.join(os.getcwd(), new_dir)
            
            new_dir = os.path.normpath(new_dir)
            
            if os.path.isdir(new_dir):
                os.environ['OLDPWD'] = os.getcwd()
                os.chdir(new_dir)
                self.current_dir = os.getcwd()
                self.last_exit_code = 0
                return True
            else:
                self.print_error(f"Le répertoire '{new_dir}' n'existe pas")
                self.last_exit_code = 1
                return False
        except Exception as e:
            self.print_error(f"Changement de répertoire: {e}")
            self.last_exit_code = 1
            return False
    
    def cmd_exit(self, args):
        """Quitte le terminal"""
        print(f"\n{Colors.BRIGHT_CYAN}Au revoir! 👋{Colors.RESET}")
        sys.exit(0)
    
    def cmd_pwd(self, args):
        """Affiche le répertoire courant"""
        print(f"{Colors.BRIGHT_BLUE}{os.getcwd()}{Colors.RESET}")
        self.last_exit_code = 0
        return True
    
    def cmd_echo(self, args):
        """Affiche du texte avec support de couleurs"""
        text = ' '.join(args)
        # Support basique de couleurs avec -c
        if text.startswith('-c '):
            text = text[3:]
        print(text)
        self.last_exit_code = 0
        return True
    
    def cmd_set(self, args):
        """Définit ou affiche les variables d'environnement"""
        if not args:
            for key, value in sorted(os.environ.items()):
                print(f"{Colors.BRIGHT_GREEN}{key}{Colors.RESET}={value}")
        elif len(args) == 1 and '=' in args[0]:
            key, value = args[0].split('=', 1)
            os.environ[key] = value
            self.env_vars[key] = value
            self.print_success(f"Variable '{key}' définie")
        else:
            for arg in args:
                value = os.environ.get(arg, '')
                if value:
                    print(f"{Colors.BRIGHT_GREEN}{arg}{Colors.RESET}={value}")
        self.last_exit_code = 0
        return True
    
    def cmd_history(self, args):
        """Affiche l'historique des commandes"""
        try:
            # Options: -c pour effacer, -n pour limiter
            if args and args[0] == '-c':
                readline.clear_history()
                self.command_history = []
                self.print_success("Historique effacé")
                return True
            
            limit = None
            if args and args[0] == '-n' and len(args) > 1:
                try:
                    limit = int(args[1])
                except:
                    pass
            
            history_len = readline.get_current_history_length()
            start = 1 if limit is None else max(1, history_len - limit + 1)
            
            for i in range(start, history_len + 1):
                cmd = readline.get_history_item(i)
                print(f"{Colors.BRIGHT_BLACK}{i:4d}{Colors.RESET}  {cmd}")
                
            self.last_exit_code = 0
        except Exception as e:
            self.print_error(f"Historique: {e}")
            self.last_exit_code = 1
        return True
    
    def cmd_help(self, args):
        """Affiche l'aide avec coloration"""
        help_sections = {
            "Navigation": [
                ("cd [dir]", "Change de répertoire"),
                ("cd -", "Retourne au répertoire précédent"),
                ("pwd", "Affiche le répertoire courant"),
            ],
            "Fichiers": [
                ("ls/dir", "Liste les fichiers"),
                ("tree [dir]", "Affiche l'arborescence"),
                ("find [motif]", "Recherche des fichiers"),
                ("grep [motif]", "Recherche dans les fichiers"),
            ],
            "Système": [
                ("echo [texte]", "Affiche du texte"),
                ("clear/cls", "Efface l'écran"),
                ("sysinfo", "Informations système"),
                ("env", "Variables d'environnement"),
                ("which [cmd]", "Trouve une commande"),
            ],
            "Utilitaires": [
                ("calc [expr]", "Calculatrice"),
                ("date", "Affiche la date"),
                ("time", "Affiche l'heure"),
                ("color/theme", "Change les couleurs"),
            ],
            "Configuration": [
                ("alias [nom=cmd]", "Crée un alias"),
                ("history [-c|-n]", "Gère l'historique"),
                ("set [var=val]", "Définit une variable"),
            ],
        }
        
        print(f"\n{Colors.BOLD}{Colors.BRIGHT_CYAN}{'='*60}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BRIGHT_YELLOW}  Terminal Python - Aide{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BRIGHT_CYAN}{'='*60}{Colors.RESET}\n")
        
        for section, commands in help_sections.items():
            print(f"{Colors.BOLD}{Colors.BRIGHT_MAGENTA}{section}:{Colors.RESET}")
            for cmd, desc in commands:
                print(f"  {Colors.BRIGHT_GREEN}{cmd:20s}{Colors.RESET} {desc}")
            print()
        
        print(f"{Colors.BRIGHT_YELLOW}Raccourcis:{Colors.RESET}")
        print(f"  TAB            Autocomplétion")
        print(f"  ↑/↓            Navigation historique")
        print(f"  Ctrl+C         Annuler")
        print(f"  Ctrl+D         Quitter")
        print(f"\n{Colors.BRIGHT_CYAN}Tapez une commande suivie de --help pour plus d'info{Colors.RESET}\n")
        
        self.last_exit_code = 0
        return True
    
    def cmd_alias(self, args):
        """Définit ou affiche les alias"""
        if not args:
            if not self.aliases:
                self.print_info("Aucun alias défini")
            else:
                print(f"\n{Colors.BRIGHT_YELLOW}Alias définis:{Colors.RESET}")
                for name, cmd in sorted(self.aliases.items()):
                    print(f"  {Colors.BRIGHT_GREEN}{name:15s}{Colors.RESET} → {cmd}")
                print()
        elif '=' in args[0]:
            name, cmd = args[0].split('=', 1)
            self.aliases[name] = cmd
            self.print_success(f"Alias créé: {name} → {cmd}")
        else:
            for arg in args:
                if arg in self.aliases:
                    print(f"{Colors.BRIGHT_GREEN}{arg}{Colors.RESET}={self.aliases[arg]}")
        
        self.last_exit_code = 0
        return True
    
    def cmd_clear(self, args):
        """Efface l'écran"""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.last_exit_code = 0
        return True
    
    def cmd_date(self, args):
        """Affiche la date actuelle"""
        now = datetime.now()
        print(f"{Colors.BRIGHT_CYAN}{now.strftime('%A %d %B %Y')}{Colors.RESET}")
        self.last_exit_code = 0
        return True
    
    def cmd_time(self, args):
        """Affiche l'heure actuelle"""
        now = datetime.now()
        print(f"{Colors.BRIGHT_CYAN}{now.strftime('%H:%M:%S')}{Colors.RESET}")
        self.last_exit_code = 0
        return True
    
    def cmd_env(self, args):
        """Affiche toutes les variables d'environnement"""
        for key, value in sorted(os.environ.items()):
            print(f"{Colors.BRIGHT_GREEN}{key:30s}{Colors.RESET} = {value}")
        self.last_exit_code = 0
        return True
    
    def cmd_tree(self, args):
        """Affiche l'arborescence des répertoires"""
        def print_tree(directory, prefix="", max_depth=3, current_depth=0):
            if current_depth >= max_depth:
                return
            
            try:
                entries = sorted(os.listdir(directory))
                dirs = [e for e in entries if os.path.isdir(os.path.join(directory, e))]
                files = [e for e in entries if os.path.isfile(os.path.join(directory, e))]
                
                for i, d in enumerate(dirs):
                    is_last = (i == len(dirs) - 1) and len(files) == 0
                    print(f"{prefix}{'└── ' if is_last else '├── '}{Colors.BRIGHT_BLUE}{d}{Colors.RESET}/")
                    new_prefix = prefix + ("    " if is_last else "│   ")
                    print_tree(os.path.join(directory, d), new_prefix, max_depth, current_depth + 1)
                
                for i, f in enumerate(files):
                    is_last = i == len(files) - 1
                    print(f"{prefix}{'└── ' if is_last else '├── '}{f}")
            except PermissionError:
                print(f"{prefix}[Permission refusée]")
        
        start_dir = args[0] if args else '.'
        print(f"{Colors.BRIGHT_BLUE}{os.path.abspath(start_dir)}{Colors.RESET}/")
        print_tree(start_dir)
        self.last_exit_code = 0
        return True
    
    def cmd_grep(self, args):
        """Recherche dans des fichiers"""
        if len(args) < 2:
            self.print_error("Usage: grep [motif] [fichiers...]")
            self.last_exit_code = 1
            return False
        
        pattern = args[0]
        files = args[1:]
        
        for filepath in files:
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    for i, line in enumerate(f, 1):
                        if pattern in line:
                            print(f"{Colors.BRIGHT_MAGENTA}{filepath}{Colors.RESET}:"
                                  f"{Colors.BRIGHT_YELLOW}{i}{Colors.RESET}:"
                                  f"{line.rstrip()}")
            except Exception as e:
                self.print_error(f"{filepath}: {e}")
        
        self.last_exit_code = 0
        return True
    
    def cmd_find(self, args):
        """Recherche des fichiers"""
        pattern = args[0] if args else "*"
        start_dir = args[1] if len(args) > 1 else '.'
        
        import fnmatch
        
        for root, dirs, files in os.walk(start_dir):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    path = os.path.join(root, name)
                    print(f"{Colors.BRIGHT_CYAN}{path}{Colors.RESET}")
        
        self.last_exit_code = 0
        return True
    
    def cmd_which(self, args):
        """Trouve l'emplacement d'une commande"""
        if not args:
            self.print_error("Usage: which [commande]")
            self.last_exit_code = 1
            return False
        
        cmd = args[0]
        
        # Vérifier si c'est une commande intégrée
        if cmd in ['cd', 'pwd', 'echo', 'set', 'history', 'help', 'alias', 'clear', 'env']:
            print(f"{Colors.BRIGHT_GREEN}{cmd}{Colors.RESET}: commande intégrée")
            self.last_exit_code = 0
            return True
        
        # Vérifier si c'est un alias
        if cmd in self.aliases:
            print(f"{Colors.BRIGHT_YELLOW}{cmd}{Colors.RESET}: alias de '{self.aliases[cmd]}'")
            self.last_exit_code = 0
            return True
        
        # Chercher dans le PATH
        try:
            result = subprocess.run(['where', cmd], capture_output=True, text=True)
            if result.returncode == 0:
                print(result.stdout.strip())
                self.last_exit_code = 0
            else:
                self.print_error(f"'{cmd}' non trouvé")
                self.last_exit_code = 1
        except:
            self.print_error("Commande 'where' non disponible")
            self.last_exit_code = 1
        
        return True
    
    def cmd_calc(self, args):
        """Calculatrice simple"""
        if not args:
            self.print_error("Usage: calc [expression]")
            self.last_exit_code = 1
            return False
        
        expr = ' '.join(args)
        try:
            result = eval(expr, {"__builtins__": {}}, {})
            print(f"{Colors.BRIGHT_CYAN}{expr}{Colors.RESET} = {Colors.BRIGHT_GREEN}{result}{Colors.RESET}")
            self.last_exit_code = 0
        except Exception as e:
            self.print_error(f"Expression invalide: {e}")
            self.last_exit_code = 1
        
        return True
    
    def cmd_sysinfo(self, args):
        """Affiche les informations système"""
        info = {
            "Système": platform.system(),
            "Version": platform.version(),
            "Architecture": platform.machine(),
            "Processeur": platform.processor(),
            "Python": platform.python_version(),
            "Utilisateur": os.environ.get('USERNAME', 'N/A'),
            "Machine": os.environ.get('COMPUTERNAME', 'N/A'),
            "Répertoire": os.getcwd(),
        }
        
        print(f"\n{Colors.BRIGHT_CYAN}{'='*50}{Colors.RESET}")
        print(f"{Colors.BOLD}Informations Système{Colors.RESET}")
        print(f"{Colors.BRIGHT_CYAN}{'='*50}{Colors.RESET}\n")
        
        for key, value in info.items():
            print(f"{Colors.BRIGHT_YELLOW}{key:15s}{Colors.RESET}: {value}")
        print()
        
        self.last_exit_code = 0
        return True
    
    def cmd_color(self, args):
        """Affiche les couleurs disponibles"""
        print(f"\n{Colors.BOLD}Couleurs disponibles:{Colors.RESET}\n")
        
        colors = [
            ("BLACK", Colors.BLACK),
            ("RED", Colors.RED),
            ("GREEN", Colors.GREEN),
            ("YELLOW", Colors.YELLOW),
            ("BLUE", Colors.BLUE),
            ("MAGENTA", Colors.MAGENTA),
            ("CYAN", Colors.CYAN),
            ("WHITE", Colors.WHITE),
        ]
        
        for name, code in colors:
            print(f"{code}● {name:15s}{Colors.RESET} {code}Texte exemple{Colors.RESET}")
        
        print()
        self.last_exit_code = 0
        return True
    
    def cmd_theme(self, args):
        """Change le thème de couleurs"""
        self.print_info("Thèmes disponibles: default, dark, light")
        self.last_exit_code = 0
        return True
    
    def parse_command(self, cmd_line):
        """Parse et exécute une ligne de commande"""
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
        
        # Commandes intégrées
        result = self.execute_builtin(command, args)
        if result is not None:
            return result
        
        # Commandes système
        return self.execute_system(cmd_line)
    
    def execute_pipe(self, cmd_line):
        """Exécute une commande avec pipes"""
        commands = cmd_line.split('|')
        
        try:
            process = subprocess.Popen(
                commands[0].strip(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
                text=True
            )
            
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
            
            self.last_exit_code = process.returncode
            return process.returncode == 0
        except Exception as e:
            self.print_error(f"Pipe: {e}")
            self.last_exit_code = 1
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
            
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True
            )
            
            with open(filename, mode, encoding='utf-8') as f:
                f.write(result.stdout)
            
            if result.stderr:
                print(result.stderr, end='', file=sys.stderr)
            
            self.last_exit_code = result.returncode
            return result.returncode == 0
        except Exception as e:
            self.print_error(f"Redirection: {e}")
            self.last_exit_code = 1
            return False
    
    def execute_system(self, cmd_line):
        """Exécute une commande système"""
        try:
            result = subprocess.run(
                cmd_line,
                shell=True,
                text=True
            )
            self.last_exit_code = result.returncode
            return result.returncode == 0
        except KeyboardInterrupt:
            print(f"\n{Colors.BRIGHT_RED}^C{Colors.RESET}")
            self.last_exit_code = 130
            return False
        except Exception as e:
            self.print_error(str(e))
            self.last_exit_code = 1
            return False
    
    def print_banner(self):
        """Affiche la bannière de démarrage"""
        banner = f"""
{Colors.BRIGHT_CYAN}╔════════════════════════════════════════════════════════════╗
║                                                            ║
║     {Colors.BOLD}Terminal Python Avancé pour Windows{Colors.RESET}{Colors.BRIGHT_CYAN}                ║
║                                                            ║
║     {Colors.BRIGHT_YELLOW}Version 2.0{Colors.RESET}{Colors.BRIGHT_CYAN} - Avec couleurs et autocomplétion      ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.BRIGHT_GREEN}✓{Colors.RESET} Tapez {Colors.BRIGHT_YELLOW}'help'{Colors.RESET} pour l'aide complète
{Colors.BRIGHT_GREEN}✓{Colors.RESET} Utilisez {Colors.BRIGHT_YELLOW}TAB{Colors.RESET} pour l'autocomplétion
{Colors.BRIGHT_GREEN}✓{Colors.RESET} Tapez {Colors.BRIGHT_YELLOW}'exit'{Colors.RESET} pour quitter

{Colors.BRIGHT_CYAN}{'─'*60}{Colors.RESET}
"""
        print(banner)
    
    def run(self):
        """Boucle principale du terminal"""
        self.print_banner()
        
        while True:
            try:
                cmd_line = input(self.get_prompt()).strip()
                
                if not cmd_line:
                    continue
                
                self.command_history.append(cmd_line)
                
                # Ajouter aux favoris si utilisé souvent
                if self.command_history.count(cmd_line) >= 3 and cmd_line not in self.favorite_commands:
                    self.favorite_commands.append(cmd_line.split()[0])
                
                self.parse_command(cmd_line)
                
            except KeyboardInterrupt:
                print(f"\n{Colors.BRIGHT_YELLOW}^C{Colors.RESET}")
                self.print_info("Tapez 'exit' ou 'quit' pour quitter")
                continue
            except EOFError:
                print(f"\n{Colors.BRIGHT_CYAN}Au revoir! 👋{Colors.RESET}")
                break
            except Exception as e:
                self.print_error(f"Erreur inattendue: {e}")
                continue

def main():
    """Point d'entrée principal"""
    terminal = AdvancedTerminal()
    terminal.run()

if __name__ == "__main__":
    main()