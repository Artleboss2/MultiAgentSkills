---
name: architecture-web-moderne
description: Guide des fichiers essentiels pour une architecture web sécurisée et robuste.
version: 1.0.0
model: Artleboss2
---

# Voici la liste numérotée des fichiers essentiels pour une architecture moderne et robuste :

## 1. Le Cœur du Front-End (Interface)
Ces fichiers sont interprétés directement par le navigateur de l'utilisateur.

`index.html` : La porte d'entrée. Il contient la structure sémantique du site.

`style.css` (ou dossiers SASS/SCSS) : Gère toute la mise en forme visuelle et l'adaptabilité mobile (Responsive Design).

`main.js` : Apporte l'interactivité côté client (menus, animations, validation de formulaires en direct).

## 2. Le Back-End et la Logique Serveur
Pour un site "complet", vous avez besoin d'un moteur qui traite les données.

`server.js` ou index.php : Le point d'entrée du serveur qui gère les requêtes et les routes.

`.env` : Crucial pour la sécurité. Ce fichier stocke vos variables d'environnement (clés d'API, mots de passe de base de données) et ne doit jamais être public.

`db.sql` ou `models/` : Les fichiers définissant la structure de votre base de données.

`routes/` (Dossier) : Contient les scripts qui définissent les différentes pages ou points d'accès API.

## 3. La Couche Sécurité et Configuration
C'est ici que l'on protège le site des attaques courantes.

`.htaccess` (Apache) ou `nginx.conf` : Configure les redirections HTTPS forcées, protège contre l'injection de scripts et définit les headers de sécurité.

`package.json` (pour Node.js) : Liste les dépendances. Il permet de surveiller les vulnérabilités dans les bibliothèques externes.

`middleware/auth.js` : Un script dédié à la vérification des jetons (tokens) ou des sessions pour s'assurer que l'utilisateur a le droit d'accéder à une page.

`robots.txt` : Indique aux moteurs de recherche quelles parties du site ils ne doivent pas indexer (comme les pages d'administration).

## 4. Maintenance et Déploiement
`.gitignore` : Empêche d'envoyer des fichiers sensibles (comme le .env) sur des plateformes publiques comme GitHub.

`README.md` : La documentation technique pour savoir comment installer et sécuriser le projet.

## 5. Assets et Ressources Visuelles
Un site sans images ou icônes paraît bien vide. On organise cela dans un dossier souvent nommé `/assets` ou `/public`.

`favicon.ico` : La petite icône qui s'affiche dans l'onglet du navigateur. C'est essentiel pour le branding.

`images/` (Dossier) : Contient tes logos, bannières et photos. Idéalement en formats compressés (WebP ou SVG) pour la rapidité.

`fonts/` (Dossier) : Si tu utilises des polices d'écriture personnalisées (fichiers `.woff2`) au lieu de passer par Google Fonts.

## 6. Référencement (SEO) et Partage
Pour que ton site soit bien classé sur Google et s'affiche joliment sur les réseaux sociaux.

`sitemap.xml` : Un plan du site qui aide les robots de Google à indexer toutes tes pages efficacement.

`manifest.json` : Utilisé pour les "Progressive Web Apps" (PWA). Il permet d'installer ton site comme une application sur mobile.

Balises Open Graph (dans le `index.html`) : Ce ne sont pas des fichiers à part, mais des lignes de code cruciales pour que l'image et le titre s'affichent correctement quand on partage ton lien sur Discord ou Twitter.

## 7. Tests et Qualité
Un site sécurisé est un site testé.

`tests/` (Dossier) : Contient des scripts (souvent en .test.js) pour vérifier que tes formulaires et ton système de paiement ne cassent pas lors d'une mise à jour.

`.eslintrc` ou `.prettierrc` : Fichiers de configuration qui forcent un code propre et sans erreurs de syntaxe au sein de ton équipe.

En suivant cette structure, vous vous assurez que votre projet est organisé, sécurisé et prêt à évoluer avec les meilleures pratiques du développement web moderne.

```txt
/mon-super-projet
├── /node_modules       <-- Bibliothèques externes
├── /public             <-- Fichiers accessibles par tous
│   ├── index.html
│   ├── favicon.ico
│   └── manifest.json
├── /src                <-- Ton code source
│   ├── /assets         <-- Images et polices
│   ├── /components     <-- Morceaux de code réutilisables
│   ├── /middleware     <-- Sécurité / Protection
│   └── server.js       <-- Logique serveur
├── .env                <-- TES SECRETS (Clés API, etc.)
├── .gitignore          <-- Ce qu'on ne doit pas uploader
├── package.json        <-- Carte d'identité du projet
└── README.md           <-- Mode d'emploi
```

Script JSON pour truc complet
```json
{
  "projet": "Configuration Site Web Complet et Sécurisé",
  "version": "1.0.0",
  "architecture": {
    "front_end": {
      "index.html": {
        "description": "Le squelette de l'application.",
        "contenu_indispensable": ["DOCTYPE", "balises meta SEO", "liens CSS/JS", "balise main"],
        "utilisation": "Sert de point d'entrée unique (SPA) ou de page d'accueil."
      },
      "style.css": {
        "description": "La feuille de style globale.",
        "contenu_indispensable": ["Variables de couleurs", "Reset CSS", "Media queries (Mobile First)"],
        "utilisation": "Définit l'identité visuelle et assure l'adaptabilité sur smartphone."
      },
      "app.js": {
        "description": "Logique d'interaction côté client.",
        "contenu_indispensable": ["Event listeners", "Appels Fetch API", "Manipulation du DOM"],
        "utilisation": "Rend le site dynamique sans recharger la page."
      }
    },
    "back_end": {
      "server.js": {
        "description": "Le cerveau du serveur (Node.js/Express).",
        "contenu_indispensable": ["Import des modules", "Déclaration des ports", "Gestion des routes"],
        "utilisation": "Reçoit les requêtes des utilisateurs et communique avec la base de données."
      },
      "auth.js": {
        "description": "Contrôleur de sécurité pour l'authentification.",
        "contenu_indispensable": ["Hachage de mot de passe (bcrypt)", "Génération de JWT (Token)"],
        "utilisation": "Vérifie si un utilisateur est bien celui qu'il prétend être."
      }
    },
    "securite_critique": {
      ".env": {
        "description": "Le coffre-fort des secrets.",
        "contenu_indispensable": ["DATABASE_URL", "API_KEYS", "JWT_SECRET"],
        "utilisation": "STRICTEMENT PRIVÉ. Ne jamais uploader sur un dépôt public.",
        "danger": "Si ce fichier fuite, votre site est totalement compromis."
      },
      ".gitignore": {
        "description": "La liste des fichiers à ignorer par Git.",
        "contenu_indispensable": ["node_modules/", ".env", "logs/"],
        "utilisation": "Empêche l'envoi accidentel de fichiers lourds ou sensibles sur GitHub."
      },
      "helmet_config.js": {
        "description": "Configuration des headers HTTP.",
        "contenu_indispensable": ["Content Security Policy (CSP)", "XSS Filter"],
        "utilisation": "Protège contre les attaques de type injection et clickjacking."
      }
    },
    "optimisation_seo": {
      "robots.txt": {
        "description": "Instructions pour les moteurs de recherche.",
        "contenu_indispensable": ["User-agent", "Allow/Disallow", "Sitemap URL"],
        "utilisation": "Indique à Google quelles pages indexer."
      },
      "sitemap.xml": {
        "description": "Carte routière du site.",
        "contenu_indispensable": ["Liste de toutes les URLs publiques", "Dates de mise à jour"],
        "utilisation": "Accélère l'indexation des nouvelles pages sur le web."
      }
    }
  },
  "conseils_experts": [
    "Toujours utiliser HTTPS via un certificat SSL.",
    "Valider et nettoyer (sanitize) TOUTES les entrées utilisateur pour éviter les injections SQL.",
    "Maintenir les dépendances à jour avec 'npm audit'."
  ]
}
```

`/node_modules`
Ce dossier est le répertoire de stockage de toutes les bibliothèques 
et dépendances externes installées via un gestionnaire de paquets 
comme npm ou yarn. Il contient des milliers de fichiers de code 
pré-écrits qui permettent d'ajouter des fonctionnalités complexes 
(comme la gestion des bases de données ou le chiffrement) sans 
repartir de zéro. Ce dossier ne doit jamais être modifié manuellement, 
car il est généré automatiquement à partir de ton fichier de 
configuration. En raison de son poids colossal et de sa nature 
volatile, il est impératif de l'exclure de tes sauvegardes Git. Il 
garantit que ton environnement de développement local dispose de tous 
les outils nécessaires à l'exécution du projet.

Script JSON
```json
{
  "file_path": "/node_modules",
  "type": "directory",
  "description": "Répertoire critique contenant l'intégralité des dépendances et bibliothèques tierces installées via npm ou yarn.",
  "usage": "Utilisé par Node.js pour résoudre les imports dans le code. Ce dossier est généré automatiquement par la commande 'npm install'.",
  "content_guidelines": "Contient des sous-dossiers pour chaque paquet listé dans package.json, incluant leurs propres dépendances (arbre de dépendances).",
  "security_note": "Ne jamais modifier le code à l'intérieur. Doit être exclu du versioning via .gitignore pour éviter d'alourdir le dépôt et d'exposer des binaires inutiles.",
  "importance": "Indispensable au fonctionnement, mais volatile."
}
```

`/public`
Le dossier public constitue la racine visible de ton serveur web, 
contenant tous les fichiers que le navigateur de l'utilisateur peut 
appeler directement par une URL. C'est ici que l'on place les 
ressources statiques qui ne nécessitent pas de traitement logique côté 
serveur avant d'être envoyées au client. On y retrouve 
traditionnellement le point d'entrée HTML, les icônes de navigation et 
les fichiers de configuration pour les navigateurs. La sécurité y est 
primordiale : aucun fichier sensible, script de configuration interne 
ou code source brut ne doit y être déposé, car n'importe quel visiteur 
pourrait techniquement y accéder en devinant simplement le nom du 
fichier.

Script JSON
```json
{
  "file_path": "/public",
  "type": "directory",
  "description": "Racine statique du serveur web accessible directement par les utilisateurs via l'URL.",
  "usage": "Sert de conteneur pour les fichiers qui ne nécessitent aucune compilation ou traitement côté serveur (HTML, icônes, manifestes).",
  "content_guidelines": "Doit contenir uniquement des ressources de présentation finale. Ne jamais y placer de scripts de configuration ou de fichiers sources.",
  "security_note": "Assurez-vous que l'indexation des dossiers est désactivée au niveau du serveur pour éviter que les visiteurs ne voient la liste des fichiers.",
  "importance": "Point d'entrée visuel du site."
}
```

`/src`
Le répertoire source est le cœur battant de ton application, là où 
réside toute l'intelligence et la logique métier que tu développes. 
Contrairement au dossier public, le contenu de ce dossier est traité 
par le serveur ou compilé avant d'atteindre l'utilisateur final. Il 
centralise l'organisation de ton code en sous-sections logiques pour 
faciliter la maintenance et l'évolution du site. C'est ici que tu 
orchestres les interactions entre tes données, tes composants visuels 
et tes services de sécurité. Une structure `/src` bien organisée est 
le signe d'un projet professionnel, permettant à plusieurs 
développeurs de collaborer efficacement sans se marcher sur les pieds.

Script JSON
```json
{
  "file_path": "/src",
  "type": "directory",
  "description": "Répertoire racine du code source original de l'application.",
  "usage": "Centralise toute la logique métier, les composants et les scripts qui seront soit exécutés par le serveur, soit compilés pour le client.",
  "content_guidelines": "Organisé en sous-répertoires logiques (assets, components, middleware) pour maintenir une séparation des préoccupations.",
  "security_note": "Ce dossier ne doit jamais être accessible directement par une URL publique.",
  "importance": "Cerveau du projet."
}
```

`index.html`
Ce fichier est le pilier central de l'interface utilisateur, servant 
de document maître chargé par le navigateur lors de la première 
visite. Il définit la structure sémantique du site grâce aux balises 
HTML5 et sert de point d'ancrage pour injecter dynamiquement du 
contenu via JavaScript. En plus de la structure visible, il contient 
les métadonnées cruciales pour le référencement naturel (SEO) et les 
instructions d'affichage pour les réseaux sociaux. Un `index.html` 
bien conçu doit être léger, inclure les liens vers les feuilles de 
style CSS et préparer l'accessibilité pour les utilisateurs utilisant 
des lecteurs d'écran ou des technologies d'assistance.

Script JSON
```json
{
  "file_path": "/public/index.html",
  "type": "file",
  "description": "Document HTML principal et point d'entrée unique de l'interface utilisateur.",
  "content": {
    "head": "Doit inclure charset UTF-8, viewport responsive, métadonnées SEO et liens vers CSS/Favicon.",
    "body": "Structure sémantique (header, main, footer) et point d'ancrage pour le JavaScript."
  },
  "usage": "Chargé en premier par le navigateur. Définit le titre de la page et la structure globale.",
  "security_note": "Utiliser des balises meta pour définir une Content Security Policy (CSP) basique.",
  "importance": "Squelette indispensable."
}
```

Exemple:
```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    
    <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self' https://fonts.googleapis.com;">

    <title>Mon Site Sécurisé | Accueil</title>
    <meta name="description" content="Description SEO de mon site complet et sécurisé.">
    
    <link rel="icon" href="favicon.ico" type="image/x-icon">
    <link rel="manifest" href="manifest.json">
    <meta name="theme-color" content="#4A90E2">

    <link rel="stylesheet" href="../src/assets/style.css">
</head>
<body>
    <div id="app">
        <header id="main-header"></header>
        <main id="content">
            <h1>Bienvenue sur mon application</h1>
            <p>Chargement du contenu sécurisé...</p>
        </main>
        <footer id="main-footer"></footer>
    </div>

    <script src="../src/app.js" type="module"></script>
</body>
</html>
```

```css
:root {
    --primary-color: #4A90E2;
    --dark-color: #333;
    --light-bg: #f4f4f4;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: var(--light-bg);
    margin: 0;
    padding: 0;
}

#app {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

h1 { color: var(--primary-color); }
```

`server.js`
Fichier maître du back-end, il agit comme le chef d'orchestre de ton 
infrastructure serveur, souvent utilisant Node.js avec Express. Sa 
mission est d'écouter les requêtes entrantes des utilisateurs, de 
définir les routes de navigation et de renvoyer les réponses 
appropriées, qu'il s'agisse de pages HTML ou de données JSON. Il 
initialise également la connexion aux bases de données et intègre les 
couches de sécurité nécessaires pour protéger les échanges. C'est le 
point de contact unique entre le monde extérieur et la logique interne 
de ton application. Une erreur dans ce fichier peut rendre 
l'intégralité du site indisponible pour tous les utilisateurs.

Script JSON
```json
{
  "file_path": "/src/server.js",
  "type": "file",
  "description": "Point d'entrée principal du serveur back-end.",
  "usage": "Initialise l'application (Express), configure les ports, connecte la base de données et définit les routes API.",
  "content": {
    "essentials": ["Import de dotenv", "Configuration des middlewares (CORS, Helmet)", "Définition des endpoints", "App.listen()"]
  },
  "security_note": "Ne jamais coder de secrets en dur ici. Utiliser uniquement des variables issues de process.env.",
  "importance": "Pilote du back-end."
}
```

```js
const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
require('dotenv').config();

const app = express();

// --- SÉCURITÉ ---
app.use(helmet()); // Protège contre les failles courantes (XSS, Clickjacking)
app.use(cors({ origin: 'http://localhost:3000' })); // Autorise uniquement ton domaine
app.use(express.json({ limit: '10kb' })); // Protection contre les attaques DoS (limite de poids)

// --- ROUTES ---
app.get('/', (req, res) => {
    res.send('API Sécurisée en ligne.');
});

// Exemple de route protégée (nécessite le middleware ci-dessous)
app.get('/api/admin', require('./middleware/auth'), (req, res) => {
    res.json({ message: "Bienvenue dans l'espace sécurisé" });
});

// --- DÉMARRAGE ---
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Serveur démarré sur le port ${PORT}`);
});
```

`.env`
Le fichier d'environnement est l'élément le plus critique pour la 
sécurité de ton infrastructure. Il sert de coffre-fort numérique pour 
stocker toutes les informations hautement sensibles : clés d'API 
secrètes, identifiants de connexion aux bases de données, jetons de 
sécurité et ports de configuration. En séparant ces données du code 
source, tu évites qu'elles ne soient exposées si le code est partagé 
ou piraté. Ce fichier est strictement personnel à ton environnement 
local ou de production. Il ne doit jamais être partagé par e-mail ou 
publié sur Internet. Sans une gestion rigoureuse du `.env`, ton site 
s'expose à des vols de données massifs.

Script JSON
```json
{
  "file_path": "/.env",
  "type": "file",
  "description": "Fichier de configuration des variables d'environnement confidentielles.",
  "usage": "Stocke les clés d'API, les mots de passe de base de données, les secrets JWT et les ports réseau.",
  "content_format": "Paires CLÉ=VALEUR sans espaces autour du signe égal.",
  "security_note": "CRITIQUE : Ne jamais partager ou uploader ce fichier. Il contient les clés du royaume.",
  "importance": "Sécurité des secrets."
}
```

Exemple .env
```.env
# Configuration Serveur
PORT=3000
NODE_ENV=development

# Base de données (Exemple MongoDB ou Postgres)
DATABASE_URL=mongodb+srv://user:password@cluster.mongodb.net/myDatabase

# Sécurité
JWT_SECRET=chiffre_aleatoire_tres_long_et_complexe_123456
SESSION_SECRET=autre_secret_pour_les_cookies

# Clés API Tierces
STRIPE_API_KEY=sk_test_51Mz...
SENDGRID_API_KEY=SG.xxx...
```

`.gitignore`
Ce fichier texte essentiel dicte à l'outil de versioning Git quels 
fichiers ou dossiers doivent être délibérément ignorés lors des 
sauvegardes sur des plateformes comme GitHub. Son rôle est double : il 
protège ta sécurité en empêchant l'upload accidentel du fichier `.
env`, et il maintient la propreté de ton dépôt en excluant les 
fichiers inutiles ou trop lourds comme `node_modules`. Sans lui, tu 
risquerais de saturer ton espace de stockage ou, pire, de donner 
publiquement les clés de ton serveur à des pirates informatiques qui 
scannent le web à la recherche de secrets oubliés dans les historiques 
de versioning.

Script JSON
```json
{
  "file_path": "/.gitignore",
  "type": "file",
  "description": "Instructions pour l'outil de versioning Git sur les éléments à ne pas suivre.",
  "usage": "Liste les fichiers et dossiers qui ne doivent pas finir sur un dépôt distant (GitHub/GitLab).",
  "content_standard": ["node_modules/", ".env", "dist/", "npm-debug.log"],
  "security_note": "Vérifier régulièrement que .env y est bien listé avant de faire un 'git push'.",
  "importance": "Protection des données et du dépôt."
}
```

Exemple .gitignore
```.gitignore
# Dépendances
node_modules/
jspm_packages/

# Secrets
.env
*.env.local
.DS_Store

# Logs et Debug
npm-debug.log*
yarn-debug.log*
logs/
*.log

# Build et Distribution
dist/
build/
out/

# IDE (VS Code, Webstorm)
.vscode/
.idea/
```

`package.json`
Considéré comme la carte d'identité de ton projet, ce fichier JSON 
contient toutes les métadonnées indispensables au fonctionnement du 
site. Il liste précisément le nom du projet, sa version, l'auteur, et 
surtout, la liste exacte de toutes les dépendances logicielles 
nécessaires à son exécution. Il définit également des scripts de 
commande pour démarrer le serveur, lancer des tests ou compiler le 
code pour la production. Grâce à lui, n'importe quel développeur peut 
recréer l'environnement de travail complet en une seule commande. 
C'est le garant de la reproductibilité de ton application sur 
n'importe quelle machine ou serveur de déploiement.

Script JSON
```json
{
  "file_path": "/package.json",
  "type": "file",
  "description": "Manifeste du projet Node.js et gestionnaire de configuration.",
  "usage": "Définit les dépendances, les scripts de lancement, la version du projet et les informations sur l'auteur.",
  "content": {
    "scripts": ["start", "dev", "test"],
    "dependencies": "Modules nécessaires à la production",
    "devDependencies": "Modules nécessaires uniquement au développement"
  },
  "security_note": "Maintenir les versions à jour pour corriger les failles via 'npm audit fix'.",
  "importance": "Carte d'identité technique."
} 
```

```json
{
  "name": "mon-super-projet",
  "version": "1.0.0",
  "description": "Site web complet et sécurisé",
  "main": "src/server.js",
  "scripts": {
    "start": "node src/server.js",
    "dev": "nodemon src/server.js",
    "test": "jest",
    "audit": "npm audit"
  },
  "dependencies": {
    "express": "^4.18.2",
    "dotenv": "^16.0.3",
    "helmet": "^6.0.1",
    "cors": "^2.8.5",
    "bcrypt": "^5.1.0",
    "jsonwebtoken": "^9.0.0",
    "mongoose": "^7.0.0"
  },
  "devDependencies": {
    "nodemon": "^2.0.22",
    "jest": "^29.5.0"
  }
}
```

`README.md`
Le fichier README est le premier contact qu'un humain (ou toi-même 
dans six mois) aura avec le projet. Rédigé en Markdown, il sert de 
manuel d'utilisation complet. Il doit expliquer clairement l'utilité 
du site, les étapes précises pour l'installer localement, comment 
configurer les variables d'environnement et la structure globale du 
code. Une bonne documentation réduit considérablement le temps de 
prise en main et facilite la collaboration. Pour un site sécurisé, 
c'est aussi l'endroit idéal pour noter les procédures de déploiement 
et les bonnes pratiques de maintenance. Un projet sans README est 
souvent perçu comme inachevé ou peu fiable.

Script JSON
```json
{
  "file_path": "/README.md",
  "type": "file",
  "description": "Documentation principale du projet en format Markdown.",
  "usage": "Explique aux autres développeurs (ou à Claude) comment installer, configurer et utiliser le site.",
  "content_sections": ["Installation", "Variables d'environnement", "Scripts disponibles", "Architecture"],
  "importance": "Transmission du savoir."
}
```

```md
# 🛡️ Projet Web Sécurisé

Application full-stack avec Node.js et Express.

## 🚀 Installation
1. `npm install` (Installe les dépendances)
2. Configurer le fichier `.env` (Voir section sécurité)
3. `npm start` (Lancer le serveur)

## 🔐 Sécurité implémentée
- **Helmet.js** : Headers HTTP sécurisés.
- **Bcrypt** : Hachage des mots de passe.
- **JWT** : Authentification par jetons.
- **Dotenv** : Protection des secrets.

## 📁 Structure
- `/src` : Logique serveur et middleware.
- `/public` : Front-end statique.
- `package.json` : Dépendances et scripts.
- `.env` : Variables d'environnement sensibles (NE PAS PARTAGER).
```

`/middleware`
Le dossier middleware est la sentinelle de ton application, situé 
entre la requête de l'utilisateur et la réponse du serveur. Il 
contient des scripts spécialisés qui interceptent chaque appel pour 
vérifier des conditions de sécurité avant de laisser passer 
l'utilisateur. C'est ici que tu places tes gardes-fous : vérification 
des jetons d'authentification (JWT), limitation du débit pour éviter 
les attaques par force brute, ou encore validation du format des 
données envoyées. En centralisant ces fonctions, tu garantis qu'aucune 
route sensible ne reste vulnérable par oubli. C'est une couche 
invisible mais indispensable pour transformer un site fonctionnel en 
une forteresse numérique impénétrable.

Script JSON
```json
{
  "file_path": "/src/middleware",
  "type": "directory",
  "description": "Dossier contenant les fonctions de traitement intermédiaire pour le serveur.",
  "usage": "Logique s'exécutant entre la réception de la requête et l'envoi de la réponse (ex: vérification de token, validation de formulaire).",
  "content_guidelines": "Fichiers dédiés comme auth.js (vérification de session) ou logger.js (journalisation).",
  "security_note": "C'est la couche de protection principale. Un middleware de sécurité doit rejeter immédiatement toute requête suspecte.",
  "importance": "Sécurité active."
}
```

`/components`
Ce répertoire est dédié à la modularité et à la réutilisabilité de ton 
interface. Au lieu d'écrire des milliers de lignes de code 
répétitives, tu découpes ton site en petits morceaux autonomes comme 
des boutons, des barres de navigation ou des formulaires de contact. 
Chaque composant possède sa propre logique et son propre style, ce qui 
rend la maintenance extrêmement simple : si tu modifies le composant 
"Header", la modification se répercute instantanément sur toutes les 
pages du site. Cette approche favorise une architecture propre et 
scalable, permettant de construire des interfaces complexes de manière 
organisée, tout en réduisant considérablement le risque d'erreurs 
graphiques ou de bugs de navigation.

Script JSON
```json
{
  "file_path": "/src/components",
  "type": "directory",
  "description": "Bibliothèque de morceaux de code réutilisables pour l'interface.",
  "usage": "Contient des fichiers (ex: Navbar.js, Button.css) qui représentent des éléments UI isolés.",
  "content_guidelines": "Chaque composant doit être indépendant et ne gérer qu'une seule tâche visuelle.",
  "security_note": "S'assurer que les composants qui affichent des données utilisateurs échappent correctement les caractères spéciaux (anti-XSS).",
  "importance": "Modularité et maintenance."
}
```

`/assets`
Le dossier des ressources (assets) est le réservoir multimédia de ton 
projet. Il regroupe de manière structurée toutes les images, les 
icônes vectorielles, les vidéos et les polices de caractères 
personnalisées qui composent l'univers visuel de ton site. Une gestion 
rigoureuse de ce dossier implique l'utilisation de formats modernes et 
compressés pour optimiser les temps de chargement, ce qui est crucial 
pour le référencement et l'expérience utilisateur. En séparant les 
médias du code logique, tu simplifies la gestion du design et permets 
aux graphistes ou aux intégrateurs de mettre à jour les visuels sans 
risquer de perturber le fonctionnement technique du moteur de 
l'application.

Script JSON
```json
{
  "file_path": "/src/assets",
  "type": "directory",
  "description": "Stockage des ressources brutes nécessaires au design.",
  "usage": "Regroupe les images originales, les polices de caractères locales (WOFF2) et éventuellement les fichiers CSS globaux.",
  "content_guidelines": "Utiliser des sous-dossiers /images et /fonts pour plus de clarté.",
  "security_note": "Optimiser les images pour le web pour réduire la surface d'attaque liée au déni de service par surcharge de bande passante.",
  "importance": "Ressources visuelles."
}
```

`favicon.ico`
Bien qu'il soit minuscule, le favicon est un fichier de 16x16 ou 32x32 
pixels qui joue un rôle disproportionné dans le branding et la 
crédibilité de ton site. Il apparaît dans les onglets du navigateur, 
les favoris et l'historique de l'utilisateur, permettant une 
identification visuelle instantanée parmi une multitude de pages 
ouvertes. Au-delà de l'esthétique, l'absence de ce fichier génère 
souvent des erreurs 404 invisibles dans tes logs serveur, ce qui peut 
ralentir légèrement les performances. Un favicon professionnel 
renforce la confiance de l'utilisateur et donne à ton projet une 
finition "polie" qui distingue les sites amateurs des plateformes web 
sérieuses et abouties.

Script JSON
```json
{
  "file_path": "/public/favicon.ico",
  "type": "file",
  "description": "Icône de favori affichée dans les onglets du navigateur et les marque-pages.",
  "usage": "Identité visuelle rapide. Aide à la reconnaissance de la marque dans une multitude d'onglets.",
  "content_guidelines": "Format .ico ou .png, généralement en 32x32 pixels pour une compatibilité maximale.",
  "security_note": "Son absence provoque des erreurs 404 inutiles dans les logs du serveur.",
  "importance": "Branding et propreté des logs."
}
```

`manifest.json`
Ce fichier de configuration au format JSON est la clé de voûte des 
Progressive Web Apps (PWA). Il contient des instructions cruciales qui 
indiquent au navigateur comment ton site doit se comporter lorsqu'il 
est "installé" sur un appareil mobile ou un ordinateur. Tu y définis 
le nom de l'application, les couleurs du thème, les icônes de 
lancement et le mode d'affichage (plein écran ou avec interface 
navigateur). En fournissant ces métadonnées, tu permets à ton site 
d'offrir une expérience proche d'une application native, améliorant 
l'engagement des utilisateurs et offrant une présence constante sur 
l'écran d'accueil de leurs smartphones sans passer par un App Store.

Script JSON
```json
{
  "file_path": "/public/manifest.json",
  "type": "file",
  "description": "Fichier de configuration JSON pour les Progressive Web Apps (PWA).",
  "usage": "Indique au navigateur comment le site doit se comporter lorsqu'il est installé sur un écran d'accueil mobile.",
  "content": {
    "required_fields": ["name", "short_name", "start_url", "display", "background_color", "icons"]
  },
  "security_note": "Vérifier que les chemins vers les icônes sont corrects pour éviter les échecs d'installation.",
  "importance": "Expérience mobile native."
}
```

```json
{
  "short_name": "MonApp",
  "name": "Mon Application Web Sécurisée",
  "icons": [
    {
      "src": "favicon.ico",
      "sizes": "64x64 32x32 24x24 16x16",
      "type": "image/x-icon"
    },
    {
      "src": "/assets/logo192.png",
      "type": "image/png",
      "sizes": "192x192"
    }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#4A90E2",
  "background_color": "#ffffff"
}
```

`app.js`
```js
// --- CONFIGURATION ---
const API_URL = 'http://localhost:3000/api';

// --- FONCTIONS LOGIQUES ---
async function fetchData(endpoint) {
    const token = localStorage.getItem('token'); // Récupération du jeton de session
    
    try {
        const response = await fetch(`${API_URL}${endpoint}`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) throw new Error('Accès refusé ou erreur serveur');

        const data = await response.json();
        renderContent(data.message);
    } catch (error) {
        console.error('Erreur:', error.message);
        renderContent("Erreur de chargement. Veuillez vous connecter.");
    }
}

// --- RENDU UI ---
function renderContent(message) {
    const contentDiv = document.getElementById('content');
    if (contentDiv) {
        contentDiv.innerHTML = `<p class="fade-in">${message}</p>`;
    }
}

// --- INITIALISATION ---
document.addEventListener('DOMContentLoaded', () => {
    console.log("Application démarrée");
    // Exemple : Charger les données admin au démarrage
    fetchData('/admin');
});
```

`navbar.js`
```js
export function createNavbar() {
    const isLoggedIn = !!localStorage.getItem('token');
    
    return `
    <nav class="navbar">
        <div class="logo">MonProjet</div>
        <ul class="nav-links">
            <li><a href="/">Accueil</a></li>
            ${isLoggedIn 
                ? '<li><a href="#" id="logout-btn">Déconnexion</a></li>' 
                : '<li><a href="/login">Connexion</a></li>'}
        </ul>
    </nav>
    `;
}

// Logique de déconnexion sécurisée
export function initNavbarLogic() {
    const logoutBtn = document.getElementById('logout-btn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', () => {
            localStorage.removeItem('token'); // Supprime le jeton
            window.location.href = '/login'; // Redirige
        });
    }
}
```

`reset.css`
```css
/* Reset CSS basique */
*, *::before, *::after {
    box-sizing: border-box;
}

body, h1, p, ul {
    margin: 0;
    padding: 0;
}

ul {
    list-style: none;
}

a {
    text-decoration: none;
    color: inherit;
}

img {
    max-width: 100%;
    display: block;
}
```

`errorHandler.js`
```json
{
  "file_path": "/src/middleware/errorHandler.js",
  "type": "file",
  "description": "Gestionnaire centralisé des erreurs serveur.",
  "security_rule": "Ne jamais renvoyer la 'stack trace' (pile d'exécution) en production pour éviter de donner des indices sur l'architecture aux attaquants."
}
```

```js
module.exports = (err, req, res, next) => {
    const statusCode = res.statusCode === 200 ? 500 : res.statusCode;
    res.status(statusCode);
    
    res.json({
        message: err.message,
        // On n'affiche les détails de l'erreur que si on est en développement
        stack: process.env.NODE_ENV === 'production' ? '🔒' : err.stack,
    });
};
```

`.eslintrc.json`

```json
{
  "file_path": "/.eslintrc.json",
  "type": "file",
  "description": "Configuration du linter pour la qualité du code."
}
```

```json
{
  "env": {
    "browser": true,
    "es2021": true,
    "node": true
  },
  "extends": "eslint:recommended",
  "parserOptions": {
    "ecmaVersion": 12,
    "sourceType": "module"
  },
  "rules": {
    "no-unused-vars": ["warn"],
    "eqeqeq": ["error", "always"],
    "curly": ["error"],
    "semi": ["error", "always"]
  }
}
```

`robot.txt`
```json
{
  "file_path": "/public/robots.txt",
  "type": "file",
  "description": "Directives pour les robots d'indexation des moteurs de recherche."
}
```

```txt
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /config/
Disallow: /src/
Disallow: /middleware/

Sitemap: https://www.tonsite.com/sitemap.xml
```

`sitemap.xml`
```json
{
  "file_path": "/public/sitemap.xml",
  "type": "file",
  "description": "Index de toutes les pages du site pour le référencement (SEO)."
}
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>https://www.tonsite.com/</loc>
      <lastmod>2024-05-20</lastmod>
      <changefreq>monthly</changefreq>
      <priority>1.0</priority>
   </url>
</urlset>
```
`SECURITY.md`
```json
{
  "file_path": "/SECURITY.md",
  "type": "file",
  "description": "Politique de divulgation des vulnérabilités."
}
```

```md
# Politique de Sécurité

## Versions supportées
Seule la version la plus récente reçoit des mises à jour de sécurité.

## Signaler une vulnérabilité
Veuillez ne pas créer de "Issue" publique. Envoyez un mail à : security@tonsite.com.
Nous répondons sous 48 heures.
```

`LICENSE`
```json
{
  "file_path": "/LICENSE",
  "type": "file",
  "description": "Document légal définissant les droits d'utilisation du code."
}
```

```txt
Copyright (c) 2024 [Ton Nom]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software... (etc)
```

Download buttons 1
```html
<!-- From Uiverse.io by Na3ar-17 --> 
<div class="container">
  <label class="label">
    <input type="checkbox" class="input" />
    <span class="circle"
      ><svg
        class="icon"
        aria-hidden="true"
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
      >
        <path
          stroke="currentColor"
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="1.5"
          d="M12 19V5m0 14-4-4m4 4 4-4"
        ></path>
      </svg>
      <div class="square"></div>
    </span>
    <p class="title">Download</p>
    <p class="title">Open</p>
  </label>
</div>
```

```css
/* From Uiverse.io by Na3ar-17 */ 
.container {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  font-family: Arial, Helvetica, sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
}

.label {
  background-color: transparent;
  border: 2px solid rgb(91, 91, 240);
  display: flex;
  align-items: center;
  border-radius: 50px;
  width: 160px;
  cursor: pointer;
  transition: all 0.4s ease;
  padding: 5px;
  position: relative;
}

.label::before {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: #fff;
  width: 8px;
  height: 8px;
  transition: all 0.4s ease;
  border-radius: 100%;
  margin: auto;
  opacity: 0;
  visibility: hidden;
}

.label .input {
  display: none;
}

.label .title {
  font-size: 17px;
  color: #fff;
  transition: all 0.4s ease;
  position: absolute;
  right: 18px;
  bottom: 14px;
  text-align: center;
}

.label .title:last-child {
  opacity: 0;
  visibility: hidden;
}

.label .circle {
  height: 45px;
  width: 45px;
  border-radius: 50%;
  background-color: rgb(91, 91, 240);
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.4s ease;
  position: relative;
  box-shadow: 0 0 0 0 rgb(255, 255, 255);
  overflow: hidden;
}

.label .circle .icon {
  color: #fff;
  width: 30px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  transition: all 0.4s ease;
}

.label .circle .square {
  aspect-ratio: 1;
  width: 15px;
  border-radius: 2px;
  background-color: #fff;
  opacity: 0;
  visibility: hidden;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  transition: all 0.4s ease;
}

.label .circle::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  background-color: #3333a8;
  width: 100%;
  height: 0;
  transition: all 0.4s ease;
}

.label:has(.input:checked) {
  width: 57px;
  animation: installed 0.4s ease 3.5s forwards;
}

.label:has(.input:checked)::before {
  animation: rotate 3s ease-in-out 0.4s forwards;
}

.label .input:checked + .circle {
  animation:
    pulse 1s forwards,
    circleDelete 0.2s ease 3.5s forwards;
  rotate: 180deg;
}

.label .input:checked + .circle::before {
  animation: installing 3s ease-in-out forwards;
}

.label .input:checked + .circle .icon {
  opacity: 0;
  visibility: hidden;
}

.label .input:checked ~ .circle .square {
  opacity: 1;
  visibility: visible;
}

.label .input:checked ~ .title {
  opacity: 0;
  visibility: hidden;
}

.label .input:checked ~ .title:last-child {
  animation: showInstalledMessage 0.4s ease 3.5s forwards;
}

@keyframes pulse {
  0% {
    scale: 0.95;
    box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.7);
  }
  70% {
    scale: 1;
    box-shadow: 0 0 0 16px rgba(255, 255, 255, 0);
  }
  100% {
    scale: 0.95;
    box-shadow: 0 0 0 0 rgba(255, 255, 255, 0);
  }
}

@keyframes installing {
  from {
    height: 0;
  }
  to {
    height: 100%;
  }
}

@keyframes rotate {
  0% {
    transform: rotate(-90deg) translate(27px) rotate(0);
    opacity: 1;
    visibility: visible;
  }
  99% {
    transform: rotate(270deg) translate(27px) rotate(270deg);
    opacity: 1;
    visibility: visible;
  }
  100% {
    opacity: 0;
    visibility: hidden;
  }
}

@keyframes installed {
  100% {
    width: 150px;
    border-color: rgb(35, 174, 35);
  }
}

@keyframes circleDelete {
  100% {
    opacity: 0;
    visibility: hidden;
  }
}

@keyframes showInstalledMessage {
  100% {
    opacity: 1;
    visibility: visible;
    right: 56px;
  }
}
```
loaders
```html
<!-- From Uiverse.io by kennyotsu --> 
<div class="card">
  <div class="loader">
    <p>loading</p>
    <div class="words">
      <span class="word">buttons</span>
      <span class="word">forms</span>
      <span class="word">switches</span>
      <span class="word">cards</span>
      <span class="word">buttons</span>
    </div>
  </div>
</div>
```

```css
/* From Uiverse.io by kennyotsu */ 
.card {
  /* color used to softly clip top and bottom of the .words container */
  --bg-color: #111;
  background-color: var(--bg-color);
  padding: 1rem 2rem;
  border-radius: 1.25rem;
}
.loader {
  color: rgb(124, 124, 124);
  font-family: "Poppins", sans-serif;
  font-weight: 500;
  font-size: 25px;
  -webkit-box-sizing: content-box;
  box-sizing: content-box;
  height: 40px;
  padding: 10px 10px;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  border-radius: 8px;
}

.words {
  overflow: hidden;
  position: relative;
}
.words::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(
    var(--bg-color) 10%,
    transparent 30%,
    transparent 70%,
    var(--bg-color) 90%
  );
  z-index: 20;
}

.word {
  display: block;
  height: 100%;
  padding-left: 6px;
  color: #956afa;
  animation: spin_4991 4s infinite;
}

@keyframes spin_4991 {
  10% {
    -webkit-transform: translateY(-102%);
    transform: translateY(-102%);
  }

  25% {
    -webkit-transform: translateY(-100%);
    transform: translateY(-100%);
  }

  35% {
    -webkit-transform: translateY(-202%);
    transform: translateY(-202%);
  }

  50% {
    -webkit-transform: translateY(-200%);
    transform: translateY(-200%);
  }

  60% {
    -webkit-transform: translateY(-302%);
    transform: translateY(-302%);
  }

  75% {
    -webkit-transform: translateY(-300%);
    transform: translateY(-300%);
  }

  85% {
    -webkit-transform: translateY(-402%);
    transform: translateY(-402%);
  }

  100% {
    -webkit-transform: translateY(-400%);
    transform: translateY(-400%);
  }
}
```

loaders 2
```html
<!-- From Uiverse.io by alexruix --> 
<div class="loader"></div>
```

```css
/* From Uiverse.io by alexruix */ 
.loader {
  position: relative;
  width: 120px;
  height: 90px;
  margin: 0 auto;
}

.loader:before {
  content: "";
  position: absolute;
  bottom: 30px;
  left: 50px;
  height: 30px;
  width: 30px;
  border-radius: 50%;
  background: #2a9d8f;
  animation: loading-bounce 0.5s ease-in-out infinite alternate;
}

.loader:after {
  content: "";
  position: absolute;
  right: 0;
  top: 0;
  height: 7px;
  width: 45px;
  border-radius: 4px;
  box-shadow: 0 5px 0 #f2f2f2, -35px 50px 0 #f2f2f2, -70px 95px 0 #f2f2f2;
  animation: loading-step 1s ease-in-out infinite;
}

@keyframes loading-bounce {
  0% {
    transform: scale(1, 0.7);
  }

  40% {
    transform: scale(0.8, 1.2);
  }

  60% {
    transform: scale(1, 1);
  }

  100% {
    bottom: 140px;
  }
}

@keyframes loading-step {
  0% {
    box-shadow: 0 10px 0 rgba(0, 0, 0, 0),
            0 10px 0 #f2f2f2,
            -35px 50px 0 #f2f2f2,
            -70px 90px 0 #f2f2f2;
  }

  100% {
    box-shadow: 0 10px 0 #f2f2f2,
            -35px 50px 0 #f2f2f2,
            -70px 90px 0 #f2f2f2,
            -70px 90px 0 rgba(0, 0, 0, 0);
  }
}
```

switches
```html
<!-- From Uiverse.io by elijahgummer --> 
<div class="switch">
  <input id="toggle" type="checkbox" />
  <label class="toggle" for="toggle">
    <i></i>
  </label>
</div>
```

```css
/* From Uiverse.io by elijahgummer */ 
.switch {
  position: relative;
  width: 210px;
  height: 50px;
  box-sizing: border-box;
  padding: 3px;
  background: #0d0d0d;
  border-radius: 6px;
  box-shadow:
    inset 0 1px 1px 1px rgba(0, 0, 0, 0.5),
    0 1px 0 0 rgba(255, 255, 255, 0.1);
}
.switch input[type="checkbox"] {
  position: absolute;
  z-index: 1;
  width: 100%;
  height: 100%;
  opacity: 0;
  cursor: pointer;
}
.switch input[type="checkbox"] + label {
  position: relative;
  display: block;
  left: 0;
  width: 50%;
  height: 100%;
  background: #1b1c1c;
  border-radius: 3px;
  box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.1);
  transition: all 0.5s ease-in-out;
}
.switch input[type="checkbox"] + label:before {
  content: "";
  display: inline-block;
  width: 5px;
  height: 5px;
  margin-left: 10px;
  background: #fff;
  border-radius: 50%;
  vertical-align: middle;
  box-shadow:
    0 0 5px 2px rgba(165, 15, 15, 0.9),
    0 0 3px 1px rgba(165, 15, 15, 0.9);
  transition: all 0.5s ease-in-out;
}
.switch input[type="checkbox"] + label:after {
  content: "";
  display: inline-block;
  width: 0;
  height: 100%;
  vertical-align: middle;
}
.switch input[type="checkbox"] + label i {
  display: block;
  position: absolute;
  top: 50%;
  left: 50%;
  width: 3px;
  height: 24px;
  margin-top: -12px;
  margin-left: -1.5px;
  border-radius: 2px;
  background: #0d0d0d;
  box-shadow: 0 1px 0 0 rgba(255, 255, 255, 0.3);
}
.switch input[type="checkbox"] + label i:before,
.switch input[type="checkbox"] + label i:after {
  content: "";
  display: block;
  position: absolute;
  width: 100%;
  height: 100%;
  border-radius: 2px;
  background: #0d0d0d;
  box-shadow: 0 1px 0 0 rgba(255, 255, 255, 0.3);
}
.switch input[type="checkbox"] + label i:before {
  left: -7px;
}
.switch input[type="checkbox"] + label i:after {
  left: 7px;
}
.switch input[type="checkbox"]:checked + label {
  left: 50%;
}
.switch input[type="checkbox"]:checked + label:before {
  box-shadow:
    0 0 5px 2px rgba(15, 165, 70, 0.9),
    0 0 3px 1px rgba(15, 165, 70, 0.9);
}
```

volume slider
```html
<!-- From Uiverse.io by seyed-mohsen-mousavi --> 
<label class="slider">
  <input type="range" class="level" />
  <svg
    class="volume"
    xmlns="http://www.w3.org/2000/svg"
    version="1.1"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    width="512"
    height="512"
    x="0"
    y="0"
    viewBox="0 0 24 24"
    style="enable-background:new 0 0 512 512"
    xml:space="preserve"
  >
    <g>
      <path
        d="M18.36 19.36a1 1 0 0 1-.705-1.71C19.167 16.148 20 14.142 20 12s-.833-4.148-2.345-5.65a1 1 0 1 1 1.41-1.419C20.958 6.812 22 9.322 22 12s-1.042 5.188-2.935 7.069a.997.997 0 0 1-.705.291z"
        fill="currentColor"
        data-original="#000000"
      ></path>
      <path
        d="M15.53 16.53a.999.999 0 0 1-.703-1.711C15.572 14.082 16 13.054 16 12s-.428-2.082-1.173-2.819a1 1 0 1 1 1.406-1.422A6 6 0 0 1 18 12a6 6 0 0 1-1.767 4.241.996.996 0 0 1-.703.289zM12 22a1 1 0 0 1-.707-.293L6.586 17H4c-1.103 0-2-.897-2-2V9c0-1.103.897-2 2-2h2.586l4.707-4.707A.998.998 0 0 1 13 3v18a1 1 0 0 1-1 1z"
        fill="currentColor"
        data-original="#000000"
      ></path>
    </g>
  </svg>
</label>
```

```css
/* From Uiverse.io by seyed-mohsen-mousavi */ 
/* level settings 👇 */

.slider {
  /* slider */
  --slider-width: 100%;
  --slider-height: 50px;
  --slider-bg: rgb(82, 82, 82);
  --slider-border-radius: 9px;
  /* level */
  --level-color: #fff;
  --level-transition-duration: 0.1s;
  /* icon */
  --icon-margin: 15px;
  --icon-color: var(--slider-bg);
  --icon-size: 25px;
}

.slider {
  position: relative;
  cursor: pointer;
  display: -webkit-inline-box;
  display: -ms-inline-flexbox;
  display: inline-flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: reverse;
  -ms-flex-direction: row-reverse;
  flex-direction: row-reverse;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
}

.slider .volume {
  display: inline-block;
  vertical-align: top;
  margin-right: var(--icon-margin);
  color: var(--icon-color);
  width: var(--icon-size);
  height: auto;
  position: absolute;
  left: 0;
  pointer-events: none;
}

.slider .level {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  width: var(--slider-width);
  height: var(--slider-height);
  background: var(--slider-bg);
  overflow: hidden;
  border-radius: var(--slider-border-radius);
  -webkit-transition: height var(--level-transition-duration);
  -o-transition: height var(--level-transition-duration);
  transition: height var(--level-transition-duration);
  cursor: inherit;
  transform: rotate(270deg);
}

.slider .level::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 0;
  height: 0;
  -webkit-box-shadow: -200px 0 0 200px var(--level-color);
  box-shadow: -200px 0 0 200px var(--level-color);
}
.slider .level::-moz-range-thumb {
  width: 0;
  height: 0;
  border-radius: 0;
  border: none;
  box-shadow: -200px 0 0 200px var(--level-color);
}
```

type input
```html
<!-- From Uiverse.io by Galahhad --> 
<label class="search-label">
    <input type="text" name="text" class="input" required="" placeholder="Type here...">
    <kbd class="slash-icon">/</kbd>
    <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" width="512" height="512" x="0" y="0" viewBox="0 0 56.966 56.966" style="enable-background:new 0 0 512 512" xml:space="preserve">
      <g>
        <path d="M55.146 51.887 41.588 37.786A22.926 22.926 0 0 0 46.984 23c0-12.682-10.318-23-23-23s-23 10.318-23 23 10.318 23 23 23c4.761 0 9.298-1.436 13.177-4.162l13.661 14.208c.571.593 1.339.92 2.162.92.779 0 1.518-.297 2.079-.837a3.004 3.004 0 0 0 .083-4.242zM23.984 6c9.374 0 17 7.626 17 17s-7.626 17-17 17-17-7.626-17-17 7.626-17 17-17z" fill="currentColor" data-original="#000000" class=""></path>
      </g>
    </svg>
  </label>
```

```css
/* From Uiverse.io by Galahhad */ 
.search-label {
  display: flex;
  align-items: center;
  box-sizing: border-box;
  position: relative;
  border: 1px solid transparent;
  border-radius: 12px;
  overflow: hidden;
  background: #3D3D3D;
  padding: 9px;
  cursor: text;
}

.search-label:hover {
  border-color: gray;
}

.search-label:focus-within {
  background: #464646;
  border-color: gray;
}

.search-label input {
  outline: none;
  width: 100%;
  border: none;
  background: none;
  color: rgb(162, 162, 162);
}

.search-label input:focus+.slash-icon,
.search-label input:valid+.slash-icon {
  display: none;
}

.search-label input:valid~.search-icon {
  display: block;
}

.search-label input:valid {
  width: calc(100% - 22px);
  transform: translateX(20px);
}

.search-label svg,
.slash-icon {
  position: absolute;
  color: #7e7e7e;
}

.search-icon {
  display: none;
  width: 12px;
  height: auto;
}

.slash-icon {
  right: 7px;
  border: 1px solid #393838;
  background: linear-gradient(-225deg, #343434, #6d6d6d);
  border-radius: 3px;
  text-align: center;
  box-shadow: inset 0 -2px 0 0 #3f3f3f, inset 0 0 1px 1px rgb(94, 93, 93), 0 1px 2px 1px rgba(28, 28, 29, 0.4);
  cursor: pointer;
  font-size: 12px;
  width: 15px;
}

.slash-icon:active {
  box-shadow: inset 0 1px 0 0 #3f3f3f, inset 0 0 1px 1px rgb(94, 93, 93), 0 1px 2px 0 rgba(28, 28, 29, 0.4);
  text-shadow: 0 1px 0 #7e7e7e;
  color: transparent;
}
```

animated button
```html
<!-- From Uiverse.io by gharsh11032000 --> 
<button class="animated-button">
  <svg viewBox="0 0 24 24" class="arr-2" xmlns="http://www.w3.org/2000/svg">
    <path
      d="M16.1716 10.9999L10.8076 5.63589L12.2218 4.22168L20 11.9999L12.2218 19.778L10.8076 18.3638L16.1716 12.9999H4V10.9999H16.1716Z"
    ></path>
  </svg>
  <span class="text">Modern Button</span>
  <span class="circle"></span>
  <svg viewBox="0 0 24 24" class="arr-1" xmlns="http://www.w3.org/2000/svg">
    <path
      d="M16.1716 10.9999L10.8076 5.63589L12.2218 4.22168L20 11.9999L12.2218 19.778L10.8076 18.3638L16.1716 12.9999H4V10.9999H16.1716Z"
    ></path>
  </svg>
</button>
```

```css
/* From Uiverse.io by gharsh11032000 */ 
.animated-button {
  position: relative;
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 16px 36px;
  border: 4px solid;
  border-color: transparent;
  font-size: 16px;
  background-color: inherit;
  border-radius: 100px;
  font-weight: 600;
  color: greenyellow;
  box-shadow: 0 0 0 2px greenyellow;
  cursor: pointer;
  overflow: hidden;
  transition: all 0.6s cubic-bezier(0.23, 1, 0.32, 1);
}

.animated-button svg {
  position: absolute;
  width: 24px;
  fill: greenyellow;
  z-index: 9;
  transition: all 0.8s cubic-bezier(0.23, 1, 0.32, 1);
}

.animated-button .arr-1 {
  right: 16px;
}

.animated-button .arr-2 {
  left: -25%;
}

.animated-button .circle {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 20px;
  height: 20px;
  background-color: greenyellow;
  border-radius: 50%;
  opacity: 0;
  transition: all 0.8s cubic-bezier(0.23, 1, 0.32, 1);
}

.animated-button .text {
  position: relative;
  z-index: 1;
  transform: translateX(-12px);
  transition: all 0.8s cubic-bezier(0.23, 1, 0.32, 1);
}

.animated-button:hover {
  box-shadow: 0 0 0 12px transparent;
  color: #212121;
  border-radius: 12px;
}

.animated-button:hover .arr-1 {
  right: -25%;
}

.animated-button:hover .arr-2 {
  left: 16px;
}

.animated-button:hover .text {
  transform: translateX(12px);
}

.animated-button:hover svg {
  fill: #212121;
}

.animated-button:active {
  scale: 0.95;
  box-shadow: 0 0 0 4px greenyellow;
}

.animated-button:hover .circle {
  width: 220px;
  height: 220px;
  opacity: 1;
}
```

checkbox
```html
<!-- From Uiverse.io by Nawsome --> 
<div class="content">
  <label class="checkBox">
    <input id="ch1" type="checkbox">
    <div class="transition"></div>
  </label>
</div>
```

```css
/* From Uiverse.io by Nawsome */ 
.clear {
  clear: both;
}

.checkBox {
  display: block;
  cursor: pointer;
  width: 30px;
  height: 30px;
  border: 3px solid rgba(255, 255, 255, 0);
  border-radius: 10px;
  position: relative;
  overflow: hidden;
  box-shadow: 0px 0px 0px 2px #fff;
}

.checkBox div {
  width: 60px;
  height: 60px;
  background-color: #fff;
  top: -52px;
  left: -52px;
  position: absolute;
  transform: rotateZ(45deg);
  z-index: 100;
}

.checkBox input[type=checkbox]:checked + div {
  left: -10px;
  top: -10px;
}

.checkBox input[type=checkbox] {
  position: absolute;
  left: 50px;
  visibility: hidden;
}

.transition {
  transition: 300ms ease;
}

Message box
```html
<!-- From Uiverse.io by vinodjangid07 --> 
<div class="messageBox">
  <div class="fileUploadWrapper">
    <label for="file">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 337 337">
        <circle
          stroke-width="20"
          stroke="#6c6c6c"
          fill="none"
          r="158.5"
          cy="168.5"
          cx="168.5"
        ></circle>
        <path
          stroke-linecap="round"
          stroke-width="25"
          stroke="#6c6c6c"
          d="M167.759 79V259"
        ></path>
        <path
          stroke-linecap="round"
          stroke-width="25"
          stroke="#6c6c6c"
          d="M79 167.138H259"
        ></path>
      </svg>
      <span class="tooltip">Add an image</span>
    </label>
    <input type="file" id="file" name="file" />
  </div>
  <input required="" placeholder="Message..." type="text" id="messageInput" />
  <button id="sendButton">
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 664 663">
      <path
        fill="none"
        d="M646.293 331.888L17.7538 17.6187L155.245 331.888M646.293 331.888L17.753 646.157L155.245 331.888M646.293 331.888L318.735 330.228L155.245 331.888"
      ></path>
      <path
        stroke-linejoin="round"
        stroke-linecap="round"
        stroke-width="33.67"
        stroke="#6c6c6c"
        d="M646.293 331.888L17.7538 17.6187L155.245 331.888M646.293 331.888L17.753 646.157L155.245 331.888M646.293 331.888L318.735 330.228L155.245 331.888"
      ></path>
    </svg>
  </button>
</div>
```

```css
/* From Uiverse.io by vinodjangid07 */ 
.messageBox {
  width: fit-content;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #2d2d2d;
  padding: 0 15px;
  border-radius: 10px;
  border: 1px solid rgb(63, 63, 63);
}
.messageBox:focus-within {
  border: 1px solid rgb(110, 110, 110);
}
.fileUploadWrapper {
  width: fit-content;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: Arial, Helvetica, sans-serif;
}

#file {
  display: none;
}
.fileUploadWrapper label {
  cursor: pointer;
  width: fit-content;
  height: fit-content;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}
.fileUploadWrapper label svg {
  height: 18px;
}
.fileUploadWrapper label svg path {
  transition: all 0.3s;
}
.fileUploadWrapper label svg circle {
  transition: all 0.3s;
}
.fileUploadWrapper label:hover svg path {
  stroke: #fff;
}
.fileUploadWrapper label:hover svg circle {
  stroke: #fff;
  fill: #3c3c3c;
}
.fileUploadWrapper label:hover .tooltip {
  display: block;
  opacity: 1;
}
.tooltip {
  position: absolute;
  top: -40px;
  display: none;
  opacity: 0;
  color: white;
  font-size: 10px;
  text-wrap: nowrap;
  background-color: #000;
  padding: 6px 10px;
  border: 1px solid #3c3c3c;
  border-radius: 5px;
  box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.596);
  transition: all 0.3s;
}
#messageInput {
  width: 200px;
  height: 100%;
  background-color: transparent;
  outline: none;
  border: none;
  padding-left: 10px;
  color: white;
}
#messageInput:focus ~ #sendButton svg path,
#messageInput:valid ~ #sendButton svg path {
  fill: #3c3c3c;
  stroke: white;
}

#sendButton {
  width: fit-content;
  height: 100%;
  background-color: transparent;
  outline: none;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s;
}
#sendButton svg {
  height: 18px;
  transition: all 0.3s;
}
#sendButton svg path {
  transition: all 0.3s;
}
#sendButton:hover svg path {
  fill: #3c3c3c;
  stroke: white;
}
```

loader box
```html
<!-- From Uiverse.io by jeremyssocial --> 
<div class="terminal-loader">
  <div class="terminal-header">
    <div class="terminal-title">Status</div>
    <div class="terminal-controls">
      <div class="control close"></div>
      <div class="control minimize"></div>
      <div class="control maximize"></div>
    </div>
  </div>
  <div class="text">Loading...</div>
</div>
```

```css
/* From Uiverse.io by jeremyssocial */ 
@keyframes blinkCursor {
  50% {
    border-right-color: transparent;
  }
}

@keyframes typeAndDelete {
  0%,
  10% {
    width: 0;
  }
  45%,
  55% {
    width: 6.2em;
  } /* adjust width based on content */
  90%,
  100% {
    width: 0;
  }
}

.terminal-loader {
  border: 0.1em solid #333;
  background-color: #1a1a1a;
  color: #0f0;
  font-family: "Courier New", Courier, monospace;
  font-size: 1em;
  padding: 1.5em 1em;
  width: 12em;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  border-radius: 4px;
  position: relative;
  overflow: hidden;
  box-sizing: border-box;
}

.terminal-header {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1.5em;
  background-color: #333;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
  padding: 0 0.4em;
  box-sizing: border-box;
}

.terminal-controls {
  float: right;
}

.control {
  display: inline-block;
  width: 0.6em;
  height: 0.6em;
  margin-left: 0.4em;
  border-radius: 50%;
  background-color: #777;
}

.control.close {
  background-color: #e33;
}

.control.minimize {
  background-color: #ee0;
}

.control.maximize {
  background-color: #0b0;
}

.terminal-title {
  float: left;
  line-height: 1.5em;
  color: #eee;
}

.text {
  display: inline-block;
  white-space: nowrap;
  overflow: hidden;
  border-right: 0.2em solid green; /* Cursor */
  animation:
    typeAndDelete 4s steps(11) infinite,
    blinkCursor 0.5s step-end infinite alternate;
  margin-top: 1.5em;
}
```

switch
```html
<!-- From Uiverse.io by njesenberger --> 
<div class="toggle-wrapper">
  <input class="toggle-checkbox" type="checkbox">
  <div class="toggle-container">  
    <div class="toggle-button">
      <div class="toggle-button-circles-container">
        <div class="toggle-button-circle"></div>
        <div class="toggle-button-circle"></div>
        <div class="toggle-button-circle"></div>
        <div class="toggle-button-circle"></div>
        <div class="toggle-button-circle"></div>
        <div class="toggle-button-circle"></div>
        <div class="toggle-button-circle"></div>
        <div class="toggle-button-circle"></div>
        <div class="toggle-button-circle"></div>
        <div class="toggle-button-circle"></div>
        <div class="toggle-button-circle"></div>
        <div class="toggle-button-circle"></div>
      </div>
    </div>
  </div>
</div>
```

```css
/* From Uiverse.io by njesenberger */ 
.toggle-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  border-radius: .5em;
  padding: .125em;
  background-image: linear-gradient(to bottom, #d5d5d5, #e8e8e8);
  box-shadow: 0 1px 1px rgb(255 255 255 / .6);
  /* resize for demo */
  font-size: 1.5em;
}

.toggle-checkbox {
  appearance: none;
  position: absolute;
  z-index: 1;
  border-radius: inherit;
  width: 100%;
  height: 100%;
  /* fix em sizing */
  font: inherit;
  opacity: 0;
  cursor: pointer;
}

.toggle-container {
  display: flex;
  align-items: center;
  position: relative;
  border-radius: .375em;
  width: 3em;
  height: 1.5em;
  background-color: #e8e8e8;
  box-shadow: inset 0 0 .0625em .125em rgb(255 255 255 / .2), inset 0 .0625em .125em rgb(0 0 0 / .4);
  transition: background-color .4s linear;
}

.toggle-checkbox:checked + .toggle-container {
  background-color: #f3b519;
}

.toggle-button {
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  left: .0625em;
  border-radius: .3125em;
  width: 1.375em;
  height: 1.375em;
  background-color: #e8e8e8;
  box-shadow: inset 0 -.0625em .0625em .125em rgb(0 0 0 / .1), inset 0 -.125em .0625em rgb(0 0 0 / .2), inset 0 .1875em .0625em rgb(255 255 255 / .3), 0 .125em .125em rgb(0 0 0 / .5);
  transition: left .4s;
}

.toggle-checkbox:checked + .toggle-container > .toggle-button {
  left: 1.5625em;
}

.toggle-button-circles-container {
  display: grid;
  grid-template-columns: repeat(3, min-content);
  gap: .125em;
  position: absolute;
  margin: 0 auto;
}

.toggle-button-circle {
  border-radius: 50%;
  width: .125em;
  height: .125em;
  background-image: radial-gradient(circle at 50% 0, #f5f5f5, #c4c4c4);
}
```

Spotify box
```html
<!-- From Uiverse.io by csozidev --> 
<div class="card">
  <div class="top">
  <div class="pfp">
    <div class="playing">
      <div class="greenline line-1"></div>
      <div class="greenline line-2"></div>
      <div class="greenline line-3"></div>
      <div class="greenline line-4"></div>
      <div class="greenline line-5"></div>
    </div>
  </div>
  <div class="texts">
  <p class="title-1">Soldiers Rage</p>
  <p class="title-2">Tha Mechanic</p>
  </div>
  </div>
  
  <div class="controls">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" height="20" width="24" class="volume_button">
  <path clip-rule="evenodd" d="M11.26 3.691A1.2 1.2 0 0 1 12 4.8v14.4a1.199 1.199 0 0 1-2.048.848L5.503 15.6H2.4a1.2 1.2 0 0 1-1.2-1.2V9.6a1.2 1.2 0 0 1 1.2-1.2h3.103l4.449-4.448a1.2 1.2 0 0 1 1.308-.26Zm6.328-.176a1.2 1.2 0 0 1 1.697 0A11.967 11.967 0 0 1 22.8 12a11.966 11.966 0 0 1-3.515 8.485 1.2 1.2 0 0 1-1.697-1.697A9.563 9.563 0 0 0 20.4 12a9.565 9.565 0 0 0-2.812-6.788 1.2 1.2 0 0 1 0-1.697Zm-3.394 3.393a1.2 1.2 0 0 1 1.698 0A7.178 7.178 0 0 1 18 12a7.18 7.18 0 0 1-2.108 5.092 1.2 1.2 0 1 1-1.698-1.698A4.782 4.782 0 0 0 15.6 12a4.78 4.78 0 0 0-1.406-3.394 1.2 1.2 0 0 1 0-1.698Z" fill-rule="evenodd"></path>
    </svg>
    <div class="volume">
      <div class="slider">
        <div class="green"></div>
      </div>
      <div class="circle"></div>
    </div>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" height="24" width="24">
  <path clip-rule="evenodd" d="M12 21.6a9.6 9.6 0 1 0 0-19.2 9.6 9.6 0 0 0 0 19.2Zm.848-12.352a1.2 1.2 0 0 0-1.696-1.696l-3.6 3.6a1.2 1.2 0 0 0 0 1.696l3.6 3.6a1.2 1.2 0 0 0 1.696-1.696L11.297 13.2H15.6a1.2 1.2 0 1 0 0-2.4h-4.303l1.551-1.552Z" fill-rule="evenodd"></path>
</svg>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" height="24" width="24">
  <path clip-rule="evenodd" d="M21.6 12a9.6 9.6 0 1 1-19.2 0 9.6 9.6 0 0 1 19.2 0ZM8.4 9.6a1.2 1.2 0 1 1 2.4 0v4.8a1.2 1.2 0 1 1-2.4 0V9.6Zm6-1.2a1.2 1.2 0 0 0-1.2 1.2v4.8a1.2 1.2 0 1 0 2.4 0V9.6a1.2 1.2 0 0 0-1.2-1.2Z" fill-rule="evenodd"></path>
</svg>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" height="24" width="24">
  <path clip-rule="evenodd" d="M12 21.6a9.6 9.6 0 1 0 0-19.2 9.6 9.6 0 0 0 0 19.2Zm4.448-10.448-3.6-3.6a1.2 1.2 0 0 0-1.696 1.696l1.551 1.552H8.4a1.2 1.2 0 1 0 0 2.4h4.303l-1.551 1.552a1.2 1.2 0 1 0 1.696 1.696l3.6-3.6a1.2 1.2 0 0 0 0-1.696Z" fill-rule="evenodd"></path>
</svg>
<div class="air"></div>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke="currentColor" fill="none" height="20" width="24">
  <path d="M3.343 7.778a4.5 4.5 0 0 1 7.339-1.46L12 7.636l1.318-1.318a4.5 4.5 0 1 1 6.364 6.364L12 20.364l-7.682-7.682a4.501 4.501 0 0 1-.975-4.904Z"></path>
</svg>
  </div>
  <div class="time">
    <div class="elapsed"></div>
  </div>
  <p class="timetext time_now">1:31</p>
  <p class="timetext time_full">3:46</p>
</div>
```

```css
/* From Uiverse.io by csozidev */ 
/* Spotify music card made by: csozi | Website: www.csozi.hu*/

.card {
  position: relative;
  width: 250px;
  height: 120px;
  background: #191414;
  border-radius: 10px;
  padding: 10px;
}

.top {
  position: relative;
  width: 100%;
  display: flex;
  gap: 10px;
}

.pfp {
  position: relative;
  top: 5px;
  left: 5px;
  height: 40px;
  width: 40px;
  background-color: #d2d2d2;
  border-radius: 5px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.title-1 {
  color: white;
  font-size: 25px;
  font-weight: bolder;
}

.title-2 {
  color: white;
  font-size: 12px;
  font-weight: bold;
}

.time {
  width: 90%;
  background-color: #5e5e5e;
  height: 6px;
  border-radius: 3px;
  position: absolute;
  left: 5%;
  bottom: 22px;
}

.elapsed {
  width: 42%;
  background-color: #1db954;
  height: 100%;
  border-radius: 3px;
}

.controls {
  color: white;
  display: flex;
  position: absolute;
  bottom: 30px;
  left: 0;
  width: 100%;
  justify-content: center;
}

.volume {
  height: 100%;
  width: 48px;
}

.air {
  height: 100%;
  width: 48px;
}

.controls svg {
  cursor: pointer;
  transition: 0.1s;
}

.controls svg:hover {
  color: #1db954;
}

.volume {
  opacity: 0;
  position: relative;
  transition: 0.2s;
}

.volume .slider {
  height: 4px;
  background-color: #5e5e5e;
  width: 80%;
  border-radius: 2px;
  margin-top: 8px;
  margin-left: 10%;
}

.volume .slider .green {
  background-color: #1db954;
  height: 100%;
  width: 80%;
  border-radius: 3px;
}

.volume .circle {
  background-color: white;
  height: 6px;
  width: 6px;
  border-radius: 3px;
  position: absolute;
  right: 20%;
  top: 60%;
}

.volume_button:hover ~ .volume {
  opacity: 1;
}

.timetext {
  color: white;
  font-size: 8px;
  position: absolute;
}

.time_now {
  bottom: 11px;
  left: 10px;
}

.time_full {
  bottom: 11px;
  right: 10px;
}

.playing {
  display: flex;
  position: relative;
  justify-content: center;
  gap: 1px;
  width: 30px;
  height: 20px;
}

.greenline {
  background-color: #1db954;
  height: 20px;
  width: 2px;
  position: relative;
  transform-origin: bottom;
}

.line-1 {
  animation: infinite playing 1s ease-in-out;
  animation-delay: 0.2s;
}

.line-2 {
  animation: infinite playing 1s ease-in-out;
  animation-delay: 0.5s;
}

.line-3 {
  animation: infinite playing 1s ease-in-out;
  animation-delay: 0.6s;
}

.line-4 {
  animation: infinite playing 1s ease-in-out;
  animation-delay: 0s;
}

.line-5 {
  animation: infinite playing 1s ease-in-out;
  animation-delay: 0.4s;
}

@keyframes playing {
  0% {
    transform: scaleY(0.1);
  }

  33% {
    transform: scaleY(0.6);
  }

  66% {
    transform: scaleY(0.9);
  }

  100% {
    transform: scaleY(0.1);
  }
}
```

Pay button
```html
<!-- From Uiverse.io by vinodjangid07 --> 
<button class="Btn">
  Pay
  <svg class="svgIcon" viewBox="0 0 576 512"><path d="M512 80c8.8 0 16 7.2 16 16v32H48V96c0-8.8 7.2-16 16-16H512zm16 144V416c0 8.8-7.2 16-16 16H64c-8.8 0-16-7.2-16-16V224H528zM64 32C28.7 32 0 60.7 0 96V416c0 35.3 28.7 64 64 64H512c35.3 0 64-28.7 64-64V96c0-35.3-28.7-64-64-64H64zm56 304c-13.3 0-24 10.7-24 24s10.7 24 24 24h48c13.3 0 24-10.7 24-24s-10.7-24-24-24H120zm128 0c-13.3 0-24 10.7-24 24s10.7 24 24 24H360c13.3 0 24-10.7 24-24s-10.7-24-24-24H248z"></path></svg>
</button>
```

```css
/* From Uiverse.io by vinodjangid07 */ 
.Btn {
  width: 130px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgb(15, 15, 15);
  border: none;
  color: white;
  font-weight: 600;
  gap: 8px;
  cursor: pointer;
  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.103);
  position: relative;
  overflow: hidden;
  transition-duration: .3s;
}

.svgIcon {
  width: 16px;
}

.svgIcon path {
  fill: white;
}

.Btn::before {
  width: 130px;
  height: 130px;
  position: absolute;
  content: "";
  background-color: white;
  border-radius: 50%;
  left: -100%;
  top: 0;
  transition-duration: .3s;
  mix-blend-mode: difference;
}

.Btn:hover::before {
  transition-duration: .3s;
  transform: translate(100%,-50%);
  border-radius: 0;
}

.Btn:active {
  transform: translate(5px,5px);
  transition-duration: .3s;
}
```

Log in button
```html
<!-- From Uiverse.io by reglobby --> 
<div
  aria-label="User Login Button"
  tabindex="0"
  role="button"
  class="user-profile"
>
  <div class="user-profile-inner">
    <svg
      aria-hidden="true"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
    >
      <g data-name="Layer 2" id="Layer_2">
        <path
          d="m15.626 11.769a6 6 0 1 0 -7.252 0 9.008 9.008 0 0 0 -5.374 8.231 3 3 0 0 0 3 3h12a3 3 0 0 0 3-3 9.008 9.008 0 0 0 -5.374-8.231zm-7.626-4.769a4 4 0 1 1 4 4 4 4 0 0 1 -4-4zm10 14h-12a1 1 0 0 1 -1-1 7 7 0 0 1 14 0 1 1 0 0 1 -1 1z"
        ></path>
      </g>
    </svg>
    <p>Log In</p>
  </div>
</div>
```

```css
/* From Uiverse.io by reglobby */ 
.user-profile {
  width: 131px;
  height: 51px;
  border-radius: 15px;
  cursor: pointer;
  transition: 0.3s ease;
  background: linear-gradient(
    to bottom right,
    #2e8eff 0%,
    rgba(46, 142, 255, 0) 30%
  );
  background-color: rgba(46, 142, 255, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
}

.user-profile:hover,
.user-profile:focus {
  background-color: rgba(46, 142, 255, 0.7);
  box-shadow: 0 0 10px rgba(46, 142, 255, 0.5);
  outline: none;
}

.user-profile-inner {
  width: 127px;
  height: 47px;
  border-radius: 13px;
  background-color: #1a1a1a;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 15px;
  color: #fff;
  font-weight: 600;
}

.user-profile-inner svg {
  width: 27px;
  height: 27px;
  fill: #fff;
}
```

Honeycomb loader
```html
<!-- From Uiverse.io by boryanakrasteva --> 
<div class="honeycomb">
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
  <div></div>
</div>
```

```css
/* From Uiverse.io by boryanakrasteva */ 
@-webkit-keyframes honeycomb {
  0%,
  20%,
  80%,
  100% {
    opacity: 0;
    -webkit-transform: scale(0);
    transform: scale(0);
  }

  30%,
  70% {
    opacity: 1;
    -webkit-transform: scale(1);
    transform: scale(1);
  }
}

@keyframes honeycomb {
  0%,
  20%,
  80%,
  100% {
    opacity: 0;
    -webkit-transform: scale(0);
    transform: scale(0);
  }

  30%,
  70% {
    opacity: 1;
    -webkit-transform: scale(1);
    transform: scale(1);
  }
}

.honeycomb {
  height: 24px;
  position: relative;
  width: 24px;
}

.honeycomb div {
  -webkit-animation: honeycomb 2.1s infinite backwards;
  animation: honeycomb 2.1s infinite backwards;
  background: #f3f3f3;
  height: 12px;
  margin-top: 6px;
  position: absolute;
  width: 24px;
}

.honeycomb div:after, .honeycomb div:before {
  content: '';
  border-left: 12px solid transparent;
  border-right: 12px solid transparent;
  position: absolute;
  left: 0;
  right: 0;
}

.honeycomb div:after {
  top: -6px;
  border-bottom: 6px solid #f3f3f3;
}

.honeycomb div:before {
  bottom: -6px;
  border-top: 6px solid #f3f3f3;
}

.honeycomb div:nth-child(1) {
  -webkit-animation-delay: 0s;
  animation-delay: 0s;
  left: -28px;
  top: 0;
}

.honeycomb div:nth-child(2) {
  -webkit-animation-delay: 0.1s;
  animation-delay: 0.1s;
  left: -14px;
  top: 22px;
}

.honeycomb div:nth-child(3) {
  -webkit-animation-delay: 0.2s;
  animation-delay: 0.2s;
  left: 14px;
  top: 22px;
}

.honeycomb div:nth-child(4) {
  -webkit-animation-delay: 0.3s;
  animation-delay: 0.3s;
  left: 28px;
  top: 0;
}

.honeycomb div:nth-child(5) {
  -webkit-animation-delay: 0.4s;
  animation-delay: 0.4s;
  left: 14px;
  top: -22px;
}

.honeycomb div:nth-child(6) {
  -webkit-animation-delay: 0.5s;
  animation-delay: 0.5s;
  left: -14px;
  top: -22px;
}

.honeycomb div:nth-child(7) {
  -webkit-animation-delay: 0.6s;
  animation-delay: 0.6s;
  left: 0;
  top: 0;
}
```

Keycap button
```html
<!-- From Uiverse.io by 20essentials --> 
<article class="keycap">
  <aside class="letter">OK</aside>
</article>
```

```css
/* From Uiverse.io by 20essentials */ 
.keycap {
  position: relative;
  display: inline-block;
  width: 80px;
  height: 80px;
  border-radius: 10px;
  background: linear-gradient(180deg, #282828, #202020);
  box-shadow:
    inset -8px 0 8px rgba(0, 0, 0, 0.15),
    inset 0 -8px 8px rgba(0, 0, 0, 0.25),
    0 0 0 2px rgba(0, 0, 0, 0.75),
    10px 20px 25px rgba(0, 0, 0, 0.4);
  overflow: hidden;
  transition:
    transform 0.1s ease-in-out,
    box-shadow 0.1s ease-in;
  user-select: none;
  -webkit-tap-highlight-color: transparent;

  .letter {
    position: absolute;
    left: 12px;
    top: 12px;
    color: #e9e9e9;
    font-size: 16px;
    transition: transform 0.1s ease-in-out;
  }

  &::before {
    content: "";
    position: absolute;
    top: 3px;
    left: 4px;
    bottom: 14px;
    right: 12px;
    background: linear-gradient(90deg, #232323, #4a4a4a);
    border-radius: 10px;
    box-shadow:
      -10px -10px 10px rgba(255, 255, 255, 0.25),
      10px 5px 10px rgba(0, 0, 0, 0.15);
    border-left: 1px solid #0004;
    border-bottom: 1px solid #0004;
    border-top: 1px solid #0009;
    transition: all 0.1s ease-in-out;
  }

  &:active {
    transform: translateY(2px);
    box-shadow:
      inset -4px 0 4px rgba(0, 0, 0, 0.1),
      inset 0 -4px 4px rgba(0, 0, 0, 0.15),
      0 0 0 2px rgba(0, 0, 0, 0.5),
      5px 10px 15px rgba(0, 0, 0, 0.3);

    &::before {
      top: 5px;
      left: 5px;
      bottom: 11px;
      right: 11px;
      box-shadow:
        -5px -5px 5px rgba(255, 255, 255, 0.15),
        5px 3px 5px rgba(0, 0, 0, 0.1);
    }

    .letter {
      transform: translateY(1px);
    }
  }
}
```

See more interactive button
```html
<!-- From Uiverse.io by Javierrocadev --> 
<button class="group group-hover:before:duration-500 group-hover:after:duration-500 after:duration-500 hover:border-rose-300 hover:before:[box-shadow:_20px_20px_20px_30px_#a21caf] duration-500 before:duration-500 hover:duration-500 underline underline-offset-2 hover:after:-right-8 hover:before:right-12 hover:before:-bottom-8 hover:before:blur hover:underline hover:underline-offset-4  origin-left hover:decoration-2 hover:text-rose-300 relative bg-neutral-800 h-16 w-64 border text-left p-3 text-gray-50 text-base font-bold rounded-lg  overflow-hidden  before:absolute before:w-12 before:h-12 before:content[''] before:right-1 before:top-1 before:z-10 before:bg-violet-500 before:rounded-full before:blur-lg  after:absolute after:z-10 after:w-20 after:h-20 after:content['']  after:bg-rose-300 after:right-8 after:top-3 after:rounded-full after:blur-lg">
  See more
</button>
```

Reaction box
```html
<!-- From Uiverse.io by Mayurwaghgpr --> 
<div
  class="hover:scale-x-105 transition-all duration-300 *:transition-all *:duration-300 flex justify-start text-2xl items-center shadow-xl z-10 bg-[#e8e4df] dark:bg-[#191818] gap-2 p-2 rounded-full"
>
  <button
    class="before:hidden hover:before:flex before:justify-center before:items-center before:h-4 before:text-[.6rem] before:px-1 before:content-['Like'] before:bg-black dark:before:bg-white dark:before:text-black before:text-white before:bg-opacity-50 before:absolute before:-top-7 before:rounded-lg hover:-translate-y-5 cursor-pointer hover:scale-125 bg-white dark:bg-[#191818] rounded-full p-2 px-3"
  >
    👍
  </button>
  <button
    class="before:hidden hover:before:flex before:justify-center before:items-center before:h-4 before:text-[.6rem] before:px-1 before:content-['Cheer'] before:bg-black dark:before:bg-white dark:before:text-black before:text-white before:bg-opacity-50 before:absolute before:-top-7 before:rounded-lg hover:-translate-y-5 cursor-pointer hover:scale-125 bg-white dark:bg-[#191818] rounded-full p-2 px-3"
  >
    👏🏻
  </button>
  <button
    class="before:hidden hover:before:flex before:justify-center before:items-center before:h-4 before:text-[.6rem] before:px-1 before:content-['Celebrate'] before:bg-black dark:before:bg-white dark:before:text-black before:text-white before:bg-opacity-50 before:absolute before:-top-7 before:rounded-lg hover:-translate-y-5 cursor-pointer hover:scale-125 bg-white dark:bg-[#191818] rounded-full p-2 px-3"
  >
    🎉
  </button>
  <button
    class="before:hidden hover:before:flex before:justify-center before:items-center before:h-4 before:text-[.6rem] before:px-1 before:content-['Appreciate'] before:bg-black dark:before:bg-white dark:before:text-black before:text-white before:bg-opacity-50 before:absolute before:-top-7 before:rounded-lg hover:-translate-y-5 cursor-pointer hover:scale-125 bg-white dark:bg-[#191818] rounded-full p-2 px-3"
  >
    ✨
  </button>
  <button
    class="before:hidden hover:before:flex before:justify-center before:items-center before:h-4 before:text-[.6rem] before:px-1 before:content-['Smile'] before:bg-black dark:before:bg-white dark:before:text-black before:text-white before:bg-opacity-50 before:absolute before:-top-7 before:rounded-lg hover:-translate-y-5 cursor-pointer hover:scale-125 bg-white dark:bg-[#191818] rounded-full p-2 px-3"
  >
    🙂
  </button>
</div>
```

Download button
```html
<!-- From Uiverse.io by Na3ar-17 --> 
<div class="container">
  <label class="label">
    <input type="checkbox" class="input" />
    <span class="circle"
      ><svg
        class="icon"
        aria-hidden="true"
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
      >
        <path
          stroke="currentColor"
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="1.5"
          d="M12 19V5m0 14-4-4m4 4 4-4"
        ></path>
      </svg>
      <div class="square"></div>
    </span>
    <p class="title">Download</p>
    <p class="title">Open</p>
  </label>
</div>
```

```css
/* From Uiverse.io by Na3ar-17 */ 
.container {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  font-family: Arial, Helvetica, sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
}

.label {
  background-color: transparent;
  border: 2px solid rgb(91, 91, 240);
  display: flex;
  align-items: center;
  border-radius: 50px;
  width: 160px;
  cursor: pointer;
  transition: all 0.4s ease;
  padding: 5px;
  position: relative;
}

.label::before {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: #fff;
  width: 8px;
  height: 8px;
  transition: all 0.4s ease;
  border-radius: 100%;
  margin: auto;
  opacity: 0;
  visibility: hidden;
}

.label .input {
  display: none;
}

.label .title {
  font-size: 17px;
  color: #fff;
  transition: all 0.4s ease;
  position: absolute;
  right: 18px;
  bottom: 14px;
  text-align: center;
}

.label .title:last-child {
  opacity: 0;
  visibility: hidden;
}

.label .circle {
  height: 45px;
  width: 45px;
  border-radius: 50%;
  background-color: rgb(91, 91, 240);
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.4s ease;
  position: relative;
  box-shadow: 0 0 0 0 rgb(255, 255, 255);
  overflow: hidden;
}

.label .circle .icon {
  color: #fff;
  width: 30px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  transition: all 0.4s ease;
}

.label .circle .square {
  aspect-ratio: 1;
  width: 15px;
  border-radius: 2px;
  background-color: #fff;
  opacity: 0;
  visibility: hidden;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  transition: all 0.4s ease;
}

.label .circle::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  background-color: #3333a8;
  width: 100%;
  height: 0;
  transition: all 0.4s ease;
}

.label:has(.input:checked) {
  width: 57px;
  animation: installed 0.4s ease 3.5s forwards;
}

.label:has(.input:checked)::before {
  animation: rotate 3s ease-in-out 0.4s forwards;
}

.label .input:checked + .circle {
  animation:
    pulse 1s forwards,
    circleDelete 0.2s ease 3.5s forwards;
  rotate: 180deg;
}

.label .input:checked + .circle::before {
  animation: installing 3s ease-in-out forwards;
}

.label .input:checked + .circle .icon {
  opacity: 0;
  visibility: hidden;
}

.label .input:checked ~ .circle .square {
  opacity: 1;
  visibility: visible;
}

.label .input:checked ~ .title {
  opacity: 0;
  visibility: hidden;
}

.label .input:checked ~ .title:last-child {
  animation: showInstalledMessage 0.4s ease 3.5s forwards;
}

@keyframes pulse {
  0% {
    scale: 0.95;
    box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.7);
  }
  70% {
    scale: 1;
    box-shadow: 0 0 0 16px rgba(255, 255, 255, 0);
  }
  100% {
    scale: 0.95;
    box-shadow: 0 0 0 0 rgba(255, 255, 255, 0);
  }
}

@keyframes installing {
  from {
    height: 0;
  }
  to {
    height: 100%;
  }
}

@keyframes rotate {
  0% {
    transform: rotate(-90deg) translate(27px) rotate(0);
    opacity: 1;
    visibility: visible;
  }
  99% {
    transform: rotate(270deg) translate(27px) rotate(270deg);
    opacity: 1;
    visibility: visible;
  }
  100% {
    opacity: 0;
    visibility: hidden;
  }
}

@keyframes installed {
  100% {
    width: 150px;
    border-color: rgb(35, 174, 35);
  }
}

@keyframes circleDelete {
  100% {
    opacity: 0;
    visibility: hidden;
  }
}

@keyframes showInstalledMessage {
  100% {
    opacity: 1;
    visibility: visible;
    right: 56px;
  }
}
```

Share button
```html
<!-- From Uiverse.io by gagan-gv --> 
<button>
  <span>Share</span>
  <div class="container">
    <svg
      class="icon"
      viewBox="0 0 1024 1024"
      version="1.1"
      xmlns="http://www.w3.org/2000/svg"
      width="45"
      height="45"
    >
      <path
        d="M962.267429 233.179429q-38.253714 56.027429-92.598857 95.451429 0.585143 7.972571 0.585143 23.990857 0 74.313143-21.723429 148.260571t-65.974857 141.970286-105.398857 120.32-147.456 83.456-184.539429 31.158857q-154.843429 0-283.428571-82.870857 19.968 2.267429 44.544 2.267429 128.585143 0 229.156571-78.848-59.977143-1.170286-107.446857-36.864t-65.170286-91.136q18.870857 2.852571 34.889143 2.852571 24.576 0 48.566857-6.290286-64-13.165714-105.984-63.707429t-41.984-117.394286l0-2.267429q38.838857 21.723429 83.456 23.405714-37.741714-25.161143-59.977143-65.682286t-22.308571-87.990857q0-50.322286 25.161143-93.110857 69.12 85.138286 168.301714 136.265143t212.260571 56.832q-4.534857-21.723429-4.534857-42.276571 0-76.580571 53.979429-130.56t130.56-53.979429q80.018286 0 134.875429 58.294857 62.317714-11.995429 117.174857-44.544-21.138286 65.682286-81.115429 101.741714 53.174857-5.705143 106.276571-28.598857z"
        fill=""
      ></path>
    </svg>
    <svg
      class="icon"
      viewBox="0 0 1024 1024"
      version="1.1"
      xmlns="http://www.w3.org/2000/svg"
      width="45"
      height="45"
    >
      <path
        d="M123.52064 667.99143l344.526782 229.708899 0-205.136409-190.802457-127.396658zM88.051421 585.717469l110.283674-73.717469-110.283674-73.717469 0 147.434938zM556.025711 897.627196l344.526782-229.708899-153.724325-102.824168-190.802457 127.396658 0 205.136409zM512 615.994287l155.406371-103.994287-155.406371-103.994287-155.406371 103.994287zM277.171833 458.832738l190.802457-127.396658 0-205.136409-344.526782 229.708899zM825.664905 512l110.283674 73.717469 0-147.434938zM746.828167 458.832738l153.724325-102.824168-344.526782-229.708899 0 205.136409zM1023.926868 356.00857l0 311.98286q0 23.402371-19.453221 36.566205l-467.901157 311.98286q-11.993715 7.459506-24.57249 7.459506t-24.57249-7.459506l-467.901157-311.98286q-19.453221-13.163834-19.453221-36.566205l0-311.98286q0-23.402371 19.453221-36.566205l467.901157-311.98286q11.993715-7.459506 24.57249-7.459506t24.57249 7.459506l467.901157 311.98286q19.453221 13.163834 19.453221 36.566205z"
        fill=""
      ></path>
    </svg>
    <svg
      class="icon"
      viewBox="0 0 1024 1024"
      version="1.1"
      xmlns="http://www.w3.org/2000/svg"
      width="45"
      height="45"
    >
      <path
        d="M950.930286 512q0 143.433143-83.748571 257.974857t-216.283429 158.573714q-15.433143 2.852571-22.601143-4.022857t-7.168-17.115429l0-120.539429q0-55.442286-29.696-81.115429 32.548571-3.437714 58.587429-10.313143t53.686857-22.308571 46.299429-38.034286 30.281143-59.977143 11.702857-86.016q0-69.12-45.129143-117.686857 21.138286-52.004571-4.534857-116.589714-16.018286-5.12-46.299429 6.290286t-52.589714 25.161143l-21.723429 13.677714q-53.174857-14.848-109.714286-14.848t-109.714286 14.848q-9.142857-6.290286-24.283429-15.433143t-47.689143-22.016-49.152-7.68q-25.161143 64.585143-4.022857 116.589714-45.129143 48.566857-45.129143 117.686857 0 48.566857 11.702857 85.723429t29.988571 59.977143 46.006857 38.253714 53.686857 22.308571 58.587429 10.313143q-22.820571 20.553143-28.013714 58.88-11.995429 5.705143-25.746286 8.557714t-32.548571 2.852571-37.449143-12.288-31.744-35.693714q-10.825143-18.285714-27.721143-29.696t-28.306286-13.677714l-11.410286-1.682286q-11.995429 0-16.603429 2.56t-2.852571 6.582857 5.12 7.972571 7.460571 6.875429l4.022857 2.852571q12.580571 5.705143 24.868571 21.723429t17.993143 29.110857l5.705143 13.165714q7.460571 21.723429 25.161143 35.108571t38.253714 17.115429 39.716571 4.022857 31.744-1.974857l13.165714-2.267429q0 21.723429 0.292571 50.834286t0.292571 30.866286q0 10.313143-7.460571 17.115429t-22.820571 4.022857q-132.534857-44.032-216.283429-158.573714t-83.748571-257.974857q0-119.442286 58.88-220.306286t159.744-159.744 220.306286-58.88 220.306286 58.88 159.744 159.744 58.88 220.306286z"
        fill=""
      ></path>
    </svg>
  </div>
</button>
```

```css
/* From Uiverse.io by gagan-gv */ 
button {
  height: 4em;
  width: 15em;
  border: none;
  border-radius: 40px;
  background-color: #fff;
  cursor: pointer;
}

button span {
  z-index: 1;
  display: inline-block;
  background-color: black;
  height: 3em;
  width: 11.5em;
  border-radius: 25px;
  color: #fff;
  line-height: 55px;
  font-size: 18px;
  letter-spacing: 3px;
  transition: all 0.5s;
}

button .container {
  z-index: -1;
  width: 0;
  position: relative;
  display: flex;
  justify-content: center;
  transform: translateY(-50px);
  transition: all 0.4s;
}

button .container svg {
  padding: 0 10px;
}

button:hover span {
  width: 0;
}

button:hover .container {
  z-index: 2;
  width: 100%;
}
```

Star button
```html
<!-- From Uiverse.io by elijahgummer --> 
<div class="radio">
  <input value="1" name="rating" type="radio" id="rating-1" />
  <label title="1 stars" for="rating-1">
    <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 576 512">
      <path
        d="M316.9 18C311.6 7 300.4 0 288.1 0s-23.4 7-28.8 18L195 150.3 51.4 171.5c-12 1.8-22 10.2-25.7 21.7s-.7 24.2 7.9 32.7L137.8 329 113.2 474.7c-2 12 3 24.2 12.9 31.3s23 8 33.8 2.3l128.3-68.5 128.3 68.5c10.8 5.7 23.9 4.9 33.8-2.3s14.9-19.3 12.9-31.3L438.5 329 542.7 225.9c8.6-8.5 11.7-21.2 7.9-32.7s-13.7-19.9-25.7-21.7L381.2 150.3 316.9 18z"
      ></path>
    </svg>
  </label>

  <input value="2" name="rating" type="radio" id="rating-2" />
  <label title="2 stars" for="rating-2">
    <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 576 512">
      <path
        d="M316.9 18C311.6 7 300.4 0 288.1 0s-23.4 7-28.8 18L195 150.3 51.4 171.5c-12 1.8-22 10.2-25.7 21.7s-.7 24.2 7.9 32.7L137.8 329 113.2 474.7c-2 12 3 24.2 12.9 31.3s23 8 33.8 2.3l128.3-68.5 128.3 68.5c10.8 5.7 23.9 4.9 33.8-2.3s14.9-19.3 12.9-31.3L438.5 329 542.7 225.9c8.6-8.5 11.7-21.2 7.9-32.7s-13.7-19.9-25.7-21.7L381.2 150.3 316.9 18z"
      ></path>
    </svg>
  </label>

  <input value="3" name="rating" type="radio" id="rating-3" />
  <label title="3 stars" for="rating-3">
    <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 576 512">
      <path
        d="M316.9 18C311.6 7 300.4 0 288.1 0s-23.4 7-28.8 18L195 150.3 51.4 171.5c-12 1.8-22 10.2-25.7 21.7s-.7 24.2 7.9 32.7L137.8 329 113.2 474.7c-2 12 3 24.2 12.9 31.3s23 8 33.8 2.3l128.3-68.5 128.3 68.5c10.8 5.7 23.9 4.9 33.8-2.3s14.9-19.3 12.9-31.3L438.5 329 542.7 225.9c8.6-8.5 11.7-21.2 7.9-32.7s-13.7-19.9-25.7-21.7L381.2 150.3 316.9 18z"
      ></path>
    </svg>
  </label>

  <input value="4" name="rating" type="radio" id="rating-4" />
  <label title="4 stars" for="rating-4">
    <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 576 512">
      <path
        d="M316.9 18C311.6 7 300.4 0 288.1 0s-23.4 7-28.8 18L195 150.3 51.4 171.5c-12 1.8-22 10.2-25.7 21.7s-.7 24.2 7.9 32.7L137.8 329 113.2 474.7c-2 12 3 24.2 12.9 31.3s23 8 33.8 2.3l128.3-68.5 128.3 68.5c10.8 5.7 23.9 4.9 33.8-2.3s14.9-19.3 12.9-31.3L438.5 329 542.7 225.9c8.6-8.5 11.7-21.2 7.9-32.7s-13.7-19.9-25.7-21.7L381.2 150.3 316.9 18z"
      ></path>
    </svg>
  </label>

  <input value="5" name="rating" type="radio" id="rating-5" />
  <label title="5 star" for="rating-5">
    <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 576 512">
      <path
        d="M316.9 18C311.6 7 300.4 0 288.1 0s-23.4 7-28.8 18L195 150.3 51.4 171.5c-12 1.8-22 10.2-25.7 21.7s-.7 24.2 7.9 32.7L137.8 329 113.2 474.7c-2 12 3 24.2 12.9 31.3s23 8 33.8 2.3l128.3-68.5 128.3 68.5c10.8 5.7 23.9 4.9 33.8-2.3s14.9-19.3 12.9-31.3L438.5 329 542.7 225.9c8.6-8.5 11.7-21.2 7.9-32.7s-13.7-19.9-25.7-21.7L381.2 150.3 316.9 18z"
      ></path>
    </svg>
  </label>
</div>
```

```css
/* From Uiverse.io by elijahgummer */ 
.radio {
  display: flex;
  justify-content: center;
  gap: 10px;
}

.radio > input {
  position: absolute;
  appearance: none;
}

.radio > label {
  cursor: pointer;
  font-size: 30px;
  position: relative;
  display: inline-block;
  transition: transform 0.3s ease;
}

.radio > label > svg {
  fill: #666;
  transition: fill 0.3s ease;
}

.radio > label::before,
.radio > label::after {
  content: "";
  position: absolute;
  width: 6px;
  height: 6px;
  background-color: #ff9e0b;
  border-radius: 50%;
  opacity: 0;
  transform: scale(0);
  transition:
    transform 0.4s ease,
    opacity 0.4s ease;
  animation: particle-explosion 1s ease-out;
}

.radio > label::before {
  top: -15px;
  left: 50%;
  transform: translateX(-50%) scale(0);
}

.radio > label::after {
  bottom: -15px;
  left: 50%;
  transform: translateX(-50%) scale(0);
}

.radio > label:hover::before,
.radio > label:hover::after {
  opacity: 1;
  transform: translateX(-50%) scale(1.5);
}

.radio > label:hover {
  transform: scale(1.2);
  animation: pulse 0.6s infinite alternate;
}

/* Star glow and animation on hover */
.radio > label:hover > svg {
  fill: #ff9e0b;
  filter: drop-shadow(0 0 15px rgba(255, 158, 11, 0.9));
  animation: shimmer 1s ease infinite alternate;
}

.radio > input:checked + label > svg {
  fill: #ff9e0b;
  filter: drop-shadow(0 0 15px rgba(255, 158, 11, 0.9));
  animation: pulse 0.8s infinite alternate;
}

.radio > input:checked + label ~ label > svg,
.radio > input:checked + label > svg {
  fill: #ff9e0b; /* Highlight the stars */
}

@keyframes pulse {
  0% {
    transform: scale(1);
  }
  100% {
    transform: scale(1.1);
  }
}

@keyframes particle-explosion {
  0% {
    opacity: 0;
    transform: scale(0.5);
  }
  50% {
    opacity: 1;
    transform: scale(1.2);
  }
  100% {
    opacity: 0;
    transform: scale(0.5);
  }
}

@keyframes shimmer {
  0% {
    filter: drop-shadow(0 0 10px rgba(255, 158, 11, 0.5));
  }
  100% {
    filter: drop-shadow(0 0 20px rgba(255, 158, 11, 1));
  }
}

.radio > input:checked + label:hover,
.radio > input:checked + label:hover ~ label {
  fill: #e58e09;
}

.radio > label:hover,
.radio > label:hover ~ label {
  fill: #ff9e0b;
}

.radio input:checked ~ label svg {
  fill: #ffa723;
}
```

Typer
```html
<!-- From Uiverse.io by adamgiebl --> 
<div class="form-control">
  <input class="input input-alt" placeholder="Type something intelligent" required="" type="text">
  <span class="input-border input-border-alt"></span>
</div>
```

```css
/* From Uiverse.io by adamgiebl */ 
.input {
  color: #fff;
  font-size: 0.9rem;
  background-color: transparent;
  width: 100%;
  box-sizing: border-box;
  padding-inline: 0.5em;
  padding-block: 0.7em;
  border: none;
  border-bottom: var(--border-height) solid var(--border-before-color);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.input-border {
  position: absolute;
  background: var(--border-after-color);
  width: 0%;
  height: 2px;
  bottom: 0;
  left: 0;
  transition: width 0.3s cubic-bezier(0.6, -0.28, 0.735, 0.045);
}

.input:focus {
  outline: none;
}

.input:focus + .input-border {
  width: 100%;
}

.form-control {
  position: relative;
  --width-of-input: 300px;
}

.input-alt {
  font-size: 1.2rem;
  padding-inline: 1em;
  padding-block: 0.8em;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.input-border-alt {
  height: 3px;
  background: linear-gradient(90deg, #FF6464 0%, #FFBF59 50%, #47C9FF 100%);
  transition: width 0.4s cubic-bezier(0.42, 0, 0.58, 1.00);
}

.input-alt:focus + .input-border-alt {
  width: 100%;
}
```

Ball loader
```html
<!-- From Uiverse.io by dovatgabriel --> 
<div class="bar">
    <div class="ball"></div>
</div>
```

```css
/* From Uiverse.io by dovatgabriel */ 
.ball {
  position: relative;
  bottom: 50px;
  left: calc(100% - 20px);
  width: 50px;
  height: 50px;
  background: #fff;
  border-radius: 50%;
  animation: ball-move8234 3s ease-in-out 1s infinite alternate;
}

.ball::after {
  position: absolute;
  content: '';
  top: 25px;
  right: 5px;
  width: 5px;
  height: 5px;
  background: #000;
  border-radius: 50%;
}

.bar {
  width: 200px;
  height: 12.5px;
  background: #FFDAAF;
  border-radius: 30px;
  transform: rotate(-15deg);
  animation: up-down6123 3s ease-in-out 1s infinite alternate;
}

@keyframes up-down6123 {
  from {
    transform: rotate(-15deg);
  }

  to {
    transform: rotate(15deg);
  }
}

@keyframes ball-move8234 {
  from {
    left: calc(100% - 40px);
    transform: rotate(360deg);
  }

  to {
    left: calc(0% - 20px);
    transform: rotate(0deg);
  }
}
```

Pattern 1
```html
<!-- From Uiverse.io by marcelodolza --> 
<div class="container"></div>
```

```css
/* From Uiverse.io by marcelodolza */ 
.container {
  width: 100%;
  height: 100%;
  --s: 100px; /* control the size */
  --c1: #f8b195;
  --c2: #355c7d;

  --_g: var(--c2) 4% 14%, var(--c1) 14% 24%, var(--c2) 22% 34%,
    var(--c1) 34% 44%, var(--c2) 44% 56%, var(--c1) 56% 66%, var(--c2) 66% 76%,
    var(--c1) 76% 86%, var(--c2) 86% 96%;
  background: radial-gradient(
      100% 100% at 100% 0,
      var(--c1) 4%,
      var(--_g),
      #0008 96%,
      #0000
    ),
    radial-gradient(
        100% 100% at 0 100%,
        #0000,
        #0008 4%,
        var(--_g),
        var(--c1) 96%
      )
      var(--c1);
  background-size: var(--s) var(--s);
}
```

Pattern 2
```html
<!-- From Uiverse.io by whoisyourdeadie --> 
<div class="matrix-container">
  <div class="matrix-pattern">
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
  </div>
  <div class="matrix-pattern">
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
  </div>
  <div class="matrix-pattern">
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
  </div>
  <div class="matrix-pattern">
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
  </div>
  <div class="matrix-pattern">
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
    <div class="matrix-column"></div>
  </div>
</div>
```

```css
/* From Uiverse.io by whoisyourdeadie */ 
.matrix-container {
  position: relative;
  width: 100%;
  height: 100%;
  background: #000;
  display: flex;
}

.matrix-pattern {
  position: relative;
  width: 1000px;
  height: 100%;
  flex-shrink: 0;
}

.matrix-column {
  position: absolute;
  top: -100%;
  width: 20px;
  height: 100%;
  font-size: 16px;
  line-height: 18px;
  font-weight: bold;
  animation: fall linear infinite;
  white-space: nowrap;
}

.matrix-column::before {
  content: "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲンABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
  position: absolute;
  top: 0;
  left: 0;
  background: linear-gradient(
    to bottom,
    #ffffff 0%,
    #ffffff 5%,
    #00ff41 10%,
    #00ff41 20%,
    #00dd33 30%,
    #00bb22 40%,
    #009911 50%,
    #007700 60%,
    #005500 70%,
    #003300 80%,
    rgba(0, 255, 65, 0.5) 90%,
    transparent 100%
  );
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  writing-mode: vertical-lr;
  letter-spacing: 1px;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.matrix-column:nth-child(1) {
  left: 0px;
  animation-delay: -2.5s;
  animation-duration: 3s;
}
.matrix-column:nth-child(2) {
  left: 25px;
  animation-delay: -3.2s;
  animation-duration: 4s;
}
.matrix-column:nth-child(3) {
  left: 50px;
  animation-delay: -1.8s;
  animation-duration: 2.5s;
}
.matrix-column:nth-child(4) {
  left: 75px;
  animation-delay: -2.9s;
  animation-duration: 3.5s;
}
.matrix-column:nth-child(5) {
  left: 100px;
  animation-delay: -1.5s;
  animation-duration: 3s;
}
.matrix-column:nth-child(6) {
  left: 125px;
  animation-delay: -3.8s;
  animation-duration: 4.5s;
}
.matrix-column:nth-child(7) {
  left: 150px;
  animation-delay: -2.1s;
  animation-duration: 2.8s;
}
.matrix-column:nth-child(8) {
  left: 175px;
  animation-delay: -2.7s;
  animation-duration: 3.2s;
}
.matrix-column:nth-child(9) {
  left: 200px;
  animation-delay: -3.4s;
  animation-duration: 3.8s;
}
.matrix-column:nth-child(10) {
  left: 225px;
  animation-delay: -1.9s;
  animation-duration: 2.7s;
}
.matrix-column:nth-child(11) {
  left: 250px;
  animation-delay: -3.6s;
  animation-duration: 4.2s;
}
.matrix-column:nth-child(12) {
  left: 275px;
  animation-delay: -2.3s;
  animation-duration: 3.1s;
}
.matrix-column:nth-child(13) {
  left: 300px;
  animation-delay: -3.1s;
  animation-duration: 3.6s;
}
.matrix-column:nth-child(14) {
  left: 325px;
  animation-delay: -2.6s;
  animation-duration: 2.9s;
}
.matrix-column:nth-child(15) {
  left: 350px;
  animation-delay: -3.7s;
  animation-duration: 4.1s;
}
.matrix-column:nth-child(16) {
  left: 375px;
  animation-delay: -2.8s;
  animation-duration: 3.3s;
}
.matrix-column:nth-child(17) {
  left: 400px;
  animation-delay: -3.3s;
  animation-duration: 3.7s;
}
.matrix-column:nth-child(18) {
  left: 425px;
  animation-delay: -2.2s;
  animation-duration: 2.6s;
}
.matrix-column:nth-child(19) {
  left: 450px;
  animation-delay: -3.9s;
  animation-duration: 4.3s;
}
.matrix-column:nth-child(20) {
  left: 475px;
  animation-delay: -2.4s;
  animation-duration: 3.4s;
}
.matrix-column:nth-child(21) {
  left: 500px;
  animation-delay: -1.7s;
  animation-duration: 2.4s;
}
.matrix-column:nth-child(22) {
  left: 525px;
  animation-delay: -3.5s;
  animation-duration: 3.9s;
}
.matrix-column:nth-child(23) {
  left: 550px;
  animation-delay: -2s;
  animation-duration: 3s;
}
.matrix-column:nth-child(24) {
  left: 575px;
  animation-delay: -4s;
  animation-duration: 4.4s;
}
.matrix-column:nth-child(25) {
  left: 600px;
  animation-delay: -1.6s;
  animation-duration: 2.3s;
}
.matrix-column:nth-child(26) {
  left: 625px;
  animation-delay: -3s;
  animation-duration: 3.5s;
}
.matrix-column:nth-child(27) {
  left: 650px;
  animation-delay: -3.8s;
  animation-duration: 4s;
}
.matrix-column:nth-child(28) {
  left: 675px;
  animation-delay: -2.5s;
  animation-duration: 2.8s;
}
.matrix-column:nth-child(29) {
  left: 700px;
  animation-delay: -3.2s;
  animation-duration: 3.6s;
}
.matrix-column:nth-child(30) {
  left: 725px;
  animation-delay: -2.7s;
  animation-duration: 3.2s;
}
.matrix-column:nth-child(31) {
  left: 750px;
  animation-delay: -1.8s;
  animation-duration: 2.7s;
}
.matrix-column:nth-child(32) {
  left: 775px;
  animation-delay: -3.6s;
  animation-duration: 4.1s;
}
.matrix-column:nth-child(33) {
  left: 800px;
  animation-delay: -2.1s;
  animation-duration: 3.1s;
}
.matrix-column:nth-child(34) {
  left: 825px;
  animation-delay: -3.4s;
  animation-duration: 3.7s;
}
.matrix-column:nth-child(35) {
  left: 850px;
  animation-delay: -2.8s;
  animation-duration: 2.9s;
}
.matrix-column:nth-child(36) {
  left: 875px;
  animation-delay: -3.7s;
  animation-duration: 4.2s;
}
.matrix-column:nth-child(37) {
  left: 900px;
  animation-delay: -2.3s;
  animation-duration: 3.3s;
}
.matrix-column:nth-child(38) {
  left: 925px;
  animation-delay: -1.9s;
  animation-duration: 2.5s;
}
.matrix-column:nth-child(39) {
  left: 950px;
  animation-delay: -3.5s;
  animation-duration: 3.8s;
}
.matrix-column:nth-child(40) {
  left: 975px;
  animation-delay: -2.6s;
  animation-duration: 3.4s;
}

.matrix-column:nth-child(odd)::before {
  content: "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン123456789";
}

.matrix-column:nth-child(even)::before {
  content: "ガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポヴァィゥェォャュョッABCDEFGHIJKLMNOPQRSTUVWXYZ";
}

.matrix-column:nth-child(3n)::before {
  content: "アカサタナハマヤラワイキシチニヒミリウクスツヌフムユルエケセテネヘメレオコソトノホモヨロヲン0987654321";
}

.matrix-column:nth-child(4n)::before {
  content: "ンヲロヨモホノトソコオレメヘネテセケエルユムフヌツスクウリミヒニチシキイワラヤマハナタサカア";
}

.matrix-column:nth-child(5n)::before {
  content: "ガザダバパギジヂビピグズヅブプゲゼデベペゴゾドボポヴァィゥェォャュョッ!@#$%^&*()_+-=[]{}|;:,.<>?";
}

@keyframes fall {
  0% {
    transform: translateY(-10%);
    opacity: 1;
  }
  100% {
    transform: translateY(200%);
    opacity: 0;
  }
}

@media (max-width: 768px) {
  .matrix-column {
    font-size: 14px;
    line-height: 16px;
    width: 18px;
  }
}

@media (max-width: 480px) {
  .matrix-column {
    font-size: 12px;
    line-height: 14px;
    width: 15px;
  }
}
```

Pattern 3
```html
<!-- From Uiverse.io by kennyotsu --> 
<div class="container"></div>
```

```css
/* From Uiverse.io by kennyotsu */ 
.container {
  width: 100%;
  height: 100%;
  /* Add your background pattern here */
  background-color: #313131;
  background-image: radial-gradient(rgba(255, 255, 255, 0.171) 2px, transparent 0);
  background-size: 30px 30px;
  background-position: -5px -5px
}
```

Pricing cardes
```html
<!-- From Uiverse.io by alexruix --> 
<div class="card">
  <div class="pricing-block-content">
    <p class="pricing-plan">Starter</p>
    <div class="price-value" data-currency="$ USD" data-currency-simple="USD">
      <p class="price-number">$<span class="price-integer">0</span></p>
      <div id="priceDiscountCent">/mo</div>
    </div>
    <div class="pricing-note">free forever</div>
    <ul class="check-list" role="list">
      <li class="check-list-item">
        <svg
          version="1.0"
          preserveAspectRatio="xMidYMid meet"
          height="16"
          viewBox="0 0 30 30.000001"
          zoomAndPan="magnify"
          width="16"
          xmlns:xlink="http://www.w3.org/1999/xlink"
          xmlns="http://www.w3.org/2000/svg"
          style="color: rgb(102, 78, 255);"
        >
          <defs>
            <clipPath id="id1">
              <path
                fill="#664eff"
                clip-rule="nonzero"
                d="M 2.328125 4.222656 L 27.734375 4.222656 L 27.734375 24.542969 L 2.328125 24.542969 Z M 2.328125 4.222656"
              ></path>
            </clipPath>
          </defs>
          <g clip-path="url(#id1)">
            <path
              fill-rule="nonzero"
              fill-opacity="1"
              d="M 27.5 7.53125 L 24.464844 4.542969 C 24.15625 4.238281 23.65625 4.238281 23.347656 4.542969 L 11.035156 16.667969 L 6.824219 12.523438 C 6.527344 12.230469 6 12.230469 5.703125 12.523438 L 2.640625 15.539062 C 2.332031 15.84375 2.332031 16.335938 2.640625 16.640625 L 10.445312 24.324219 C 10.59375 24.472656 10.796875 24.554688 11.007812 24.554688 C 11.214844 24.554688 11.417969 24.472656 11.566406 24.324219 L 27.5 8.632812 C 27.648438 8.488281 27.734375 8.289062 27.734375 8.082031 C 27.734375 7.875 27.648438 7.679688 27.5 7.53125 Z M 27.5 7.53125"
              fill="#664eff"
            ></path>
          </g></svg
        >Lorem Ipsum
      </li>
      <li class="check-list-item">
        <svg
          version="1.0"
          preserveAspectRatio="xMidYMid meet"
          height="16"
          viewBox="0 0 30 30.000001"
          zoomAndPan="magnify"
          width="16"
          xmlns:xlink="http://www.w3.org/1999/xlink"
          xmlns="http://www.w3.org/2000/svg"
          style="color: rgb(102, 78, 255);"
        >
          <defs>
            <clipPath id="id1">
              <path
                fill="#664eff"
                clip-rule="nonzero"
                d="M 2.328125 4.222656 L 27.734375 4.222656 L 27.734375 24.542969 L 2.328125 24.542969 Z M 2.328125 4.222656"
              ></path>
            </clipPath>
          </defs>
          <g clip-path="url(#id1)">
            <path
              fill-rule="nonzero"
              fill-opacity="1"
              d="M 27.5 7.53125 L 24.464844 4.542969 C 24.15625 4.238281 23.65625 4.238281 23.347656 4.542969 L 11.035156 16.667969 L 6.824219 12.523438 C 6.527344 12.230469 6 12.230469 5.703125 12.523438 L 2.640625 15.539062 C 2.332031 15.84375 2.332031 16.335938 2.640625 16.640625 L 10.445312 24.324219 C 10.59375 24.472656 10.796875 24.554688 11.007812 24.554688 C 11.214844 24.554688 11.417969 24.472656 11.566406 24.324219 L 27.5 8.632812 C 27.648438 8.488281 27.734375 8.289062 27.734375 8.082031 C 27.734375 7.875 27.648438 7.679688 27.5 7.53125 Z M 27.5 7.53125"
              fill="#664eff"
            ></path>
          </g></svg
        >Lorem Ipsum
      </li>
      <li class="check-list-item">
        <svg
          version="1.0"
          preserveAspectRatio="xMidYMid meet"
          height="16"
          viewBox="0 0 30 30.000001"
          zoomAndPan="magnify"
          width="16"
          xmlns:xlink="http://www.w3.org/1999/xlink"
          xmlns="http://www.w3.org/2000/svg"
          style="color: rgb(102, 78, 255);"
        >
          <defs>
            <clipPath id="id1">
              <path
                fill="#664eff"
                clip-rule="nonzero"
                d="M 2.328125 4.222656 L 27.734375 4.222656 L 27.734375 24.542969 L 2.328125 24.542969 Z M 2.328125 4.222656"
              ></path>
            </clipPath>
          </defs>
          <g clip-path="url(#id1)">
            <path
              fill-rule="nonzero"
              fill-opacity="1"
              d="M 27.5 7.53125 L 24.464844 4.542969 C 24.15625 4.238281 23.65625 4.238281 23.347656 4.542969 L 11.035156 16.667969 L 6.824219 12.523438 C 6.527344 12.230469 6 12.230469 5.703125 12.523438 L 2.640625 15.539062 C 2.332031 15.84375 2.332031 16.335938 2.640625 16.640625 L 10.445312 24.324219 C 10.59375 24.472656 10.796875 24.554688 11.007812 24.554688 C 11.214844 24.554688 11.417969 24.472656 11.566406 24.324219 L 27.5 8.632812 C 27.648438 8.488281 27.734375 8.289062 27.734375 8.082031 C 27.734375 7.875 27.648438 7.679688 27.5 7.53125 Z M 27.5 7.53125"
              fill="#664eff"
            ></path>
          </g></svg
        >Lorem Ipsum
      </li>
      <li class="check-list-item">
        <svg
          version="1.0"
          preserveAspectRatio="xMidYMid meet"
          height="16"
          viewBox="0 0 30 30.000001"
          zoomAndPan="magnify"
          width="16"
          xmlns:xlink="http://www.w3.org/1999/xlink"
          xmlns="http://www.w3.org/2000/svg"
          style="color: rgb(102, 78, 255);"
        >
          <defs>
            <clipPath id="id1">
              <path
                fill="#664eff"
                clip-rule="nonzero"
                d="M 2.328125 4.222656 L 27.734375 4.222656 L 27.734375 24.542969 L 2.328125 24.542969 Z M 2.328125 4.222656"
              ></path>
            </clipPath>
          </defs>
          <g clip-path="url(#id1)">
            <path
              fill-rule="nonzero"
              fill-opacity="1"
              d="M 27.5 7.53125 L 24.464844 4.542969 C 24.15625 4.238281 23.65625 4.238281 23.347656 4.542969 L 11.035156 16.667969 L 6.824219 12.523438 C 6.527344 12.230469 6 12.230469 5.703125 12.523438 L 2.640625 15.539062 C 2.332031 15.84375 2.332031 16.335938 2.640625 16.640625 L 10.445312 24.324219 C 10.59375 24.472656 10.796875 24.554688 11.007812 24.554688 C 11.214844 24.554688 11.417969 24.472656 11.566406 24.324219 L 27.5 8.632812 C 27.648438 8.488281 27.734375 8.289062 27.734375 8.082031 C 27.734375 7.875 27.648438 7.679688 27.5 7.53125 Z M 27.5 7.53125"
              fill="#664eff"
            ></path>
          </g></svg
        >Lorem Ipsum
      </li>
    </ul>
  </div>
</div>
```

```css
/* From Uiverse.io by alexruix */ 
/*Neo Brutalism pricing card*/
.card {
  width: 190px;
  background: #00ffa0;
  padding: 1rem;
  border-radius: 1rem;
  border: 0.5vmin solid #05060f;
  box-shadow: 0.4rem 0.4rem #05060f;
  overflow: hidden;
  color: black;
}

/*Card content*/
.pricing-block-content {
  display: flex;
  height: 100%;
  flex-direction: column;
  gap: 0.5rem;
}

.pricing-plan {
  color: #05060f;
  font-size: 1.3rem;
  line-height: 1.25;
  font-weight: 700;
}

.price-value {
  display: flex;
  color: #05060f;
  font-size: 1.8rem;
  line-height: 1.25;
  font-weight: 700;
}

.pricing-note {
  opacity: 0.8;
}

/*Checklist*/
.check-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-top: 0.5rem;
}

.check-list-item {
  display: flex;
  align-items: center;
  gap: 4px;
}
```

Dynamic file upload
```html
<!-- From Uiverse.io by Cobp --> 
<section
  class="relative group flex flex-col items-center justify-center w-full h-full"
>
  <div
    class="file relative w-60 h-40 cursor-pointer origin-bottom [perspective:1500px] z-50"
  >
    <div
      class="work-5 bg-amber-600 w-full h-full origin-top rounded-2xl rounded-tl-none group-hover:shadow-[0_20px_40px_rgba(0,0,0,.2)] transition-all ease duration-300 relative after:absolute after:content-[''] after:bottom-[99%] after:left-0 after:w-20 after:h-4 after:bg-amber-600 after:rounded-t-2xl before:absolute before:content-[''] before:-top-[15px] before:left-[75.5px] before:w-4 before:h-4 before:bg-amber-600 before:[clip-path:polygon(0_35%,0%_100%,50%_100%);]"
    ></div>
    <div
      class="work-4 absolute inset-1 bg-zinc-400 rounded-2xl transition-all ease duration-300 origin-bottom select-none group-hover:[transform:rotateX(-20deg)]"
    ></div>
    <div
      class="work-3 absolute inset-1 bg-zinc-300 rounded-2xl transition-all ease duration-300 origin-bottom group-hover:[transform:rotateX(-30deg)]"
    ></div>
    <div
      class="work-2 absolute inset-1 bg-zinc-200 rounded-2xl transition-all ease duration-300 origin-bottom group-hover:[transform:rotateX(-38deg)]"
    ></div>
    <div
      class="work-1 absolute bottom-0 bg-gradient-to-t from-amber-500 to-amber-400 w-full h-[156px] rounded-2xl rounded-tr-none after:absolute after:content-[''] after:bottom-[99%] after:right-0 after:w-[146px] after:h-[16px] after:bg-amber-400 after:rounded-t-2xl before:absolute before:content-[''] before:-top-[10px] before:right-[142px] before:size-3 before:bg-amber-400 before:[clip-path:polygon(100%_14%,50%_100%,100%_100%);] transition-all ease duration-300 origin-bottom flex items-end group-hover:shadow-[inset_0_20px_40px_#fbbf24,_inset_0_-20px_40px_#d97706] group-hover:[transform:rotateX(-46deg)_translateY(1px)]"
    ></div>
  </div>
  <p class="text-3xl pt-4 opacity-20">Hover over</p>
</section>
```

Revolut card
```html
<!-- From Uiverse.io by mihocsaszilard --> 
<div class="main-container">
  <div class="border">
    <div class="card">
      <div class="shadow">
        <div class="content">
          <p class="rev">Revolut</p>
          <p class="ultra-text">ULTRA MEMBER</p>
          <p class="master-text">mastercard</p>
          <p class="master one"></p>
          <p class="master two"></p>
          <svg
            version="1.1"
            class="chip"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            x="0px"
            y="0px"
            width="40px"
            height="40px"
            viewBox="0 0 50 50"
            xml:space="preserve"
          >
            <image
              width="50"
              height="50"
              x="0"
              y="0"
              href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAMAAAAp4XiDAAAABGdBTUEAALGPC/xhBQAAACBjSFJN
              AAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAB6VBMVEUAAACNcTiVeUKVeUOY
              fEaafEeUeUSYfEWZfEaykleyklaXe0SWekSZZjOYfEWYe0WXfUWXe0WcgEicfkiXe0SVekSXekSW
              ekKYe0a9nF67m12ZfUWUeEaXfESVekOdgEmVeUWWekSniU+VeUKVeUOrjFKYfEWliE6WeESZe0GS
              e0WYfES7ml2Xe0WXeESUeEOWfEWcf0eWfESXe0SXfEWYekSVeUKXfEWxklawkVaZfEWWekOUekOW
              ekSYfESZe0eXekWYfEWZe0WZe0eVeUSWeETAnmDCoWLJpmbxy4P1zoXwyoLIpWbjvXjivnjgu3bf
              u3beunWvkFWxkle/nmDivXiWekTnwXvkwHrCoWOuj1SXe0TEo2TDo2PlwHratnKZfEbQrWvPrWua
              fUfbt3PJp2agg0v0zYX0zYSfgkvKp2frxX7mwHrlv3rsxn/yzIPgvHfduXWXe0XuyIDzzISsjVO1
              lVm0lFitjVPzzIPqxX7duna0lVncuHTLqGjvyIHeuXXxyYGZfUayk1iyk1e2lln1zYTEomO2llrb
              tnOafkjFpGSbfkfZtXLhvHfkv3nqxH3mwXujhU3KqWizlFilh06khk2fgkqsjlPHpWXJp2erjVOh
              g0yWe0SliE+XekShhEvAn2D///+gx8TWAAAARnRSTlMACVCTtsRl7Pv7+vxkBab7pZv5+ZlL/UnU
              /f3SJCVe+Fx39naA9/75XSMh0/3SSkia+pil/KRj7Pr662JPkrbP7OLQ0JFOijI1MwAAAAFiS0dE
              orDd34wAAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQfnAg0IDx2lsiuJAAACLElEQVRIx2Ng
              GAXkAUYmZhZWPICFmYkRVQcbOwenmzse4MbFzc6DpIGXj8PD04sA8PbhF+CFaxEU8iWkAQT8hEVg
              OkTF/InR4eUVICYO1SIhCRMLDAoKDvFDVhUaEhwUFAjjSUlDdMiEhcOEItzdI6OiYxA6YqODIt3d
              I2DcuDBZsBY5eVTr4xMSYcyk5BRUOXkFsBZFJTQnp6alQxgZmVloUkrKYC0qqmji2WE5EEZuWB6a
              lKoKdi35YQUQRkFYPpFaCouKIYzi6EDitJSUlsGY5RWVRGjJLyxNy4ZxqtIqqvOxaVELQwZFZdkI
              JVU1RSiSalAt6rUwUBdWG1CP6pT6gNqwOrgCdQyHNYR5YQFhDXj8MiK1IAeyN6aORiyBjByVTc0F
              qBoKWpqwRCVSgilOaY2OaUPw29qjOzqLvTAchpos47u6EZyYnngUSRwpuTe6D+6qaFQdOPNLRzOM
              1dzhRZyW+CZouHk3dWLXglFcFIflQhj9YWjJGlZcaKAVSvjyPrRQ0oQVKDAQHlYFYUwIm4gqExGm
              BSkutaVQJeomwViTJqPK6OhCy2Q9sQBk8cY0DxjTJw0lAQWK6cOKfgNhpKK7ZMpUeF3jPa28BCET
              amiEqJKM+X1gxvWXpoUjVIVPnwErw71nmpgiqiQGBjNzbgs3j1nus+fMndc+Cwm0T52/oNR9lsdC
              S24ra7Tq1cbWjpXV3sHRCb1idXZ0sGdltXNxRateRwHRAACYHutzk/2I5QAAACV0RVh0ZGF0ZTpj
              cmVhdGUAMjAyMy0wMi0xM1QwODoxNToyOSswMDowMEUnN7UAAAAldEVYdGRhdGU6bW9kaWZ5ADIw
              MjMtMDItMTNUMDg6MTU6MjkrMDA6MDA0eo8JAAAAKHRFWHRkYXRlOnRpbWVzdGFtcAAyMDIzLTAy
              LTEzVDA4OjE1OjI5KzAwOjAwY2+u1gAAAABJRU5ErkJggg=="
            ></image>
          </svg>
        </div>
      </div>
    </div>
  </div>
</div>
```

```css
/* From Uiverse.io by mihocsaszilard */ 
.main-container {
  font-family: "Trebuchet MS", sans-serif;
  position: relative;
  height: 203px;
  aspect-ratio: 1.579;
  border-radius: 1em;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 300ms ease-in;
}
.main-container:hover {
  transform: rotateZ(1deg) rotateY(10deg) scale(1.1);
  box-shadow: 0 5em 2em #111;
}

.border {
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 1em;
  background: linear-gradient(
    115deg,
    rgba(0, 0, 0, 0.33) 12%,
    rgba(255, 255, 255, 0.33) 27%,
    rgba(255, 255, 255, 0.33) 31%,
    rgba(0, 0, 0, 0.33) 52%
  );
}

.border:hover:after {
  position: absolute;
  content: " ";
  height: 50em;
  aspect-ratio: 1.58;
  border-radius: 1em;
  background: linear-gradient(
    115deg,
    rgba(0, 0, 0, 1) 42%,
    rgba(255, 255, 255, 1) 47%,
    rgba(255, 255, 255, 1) 51%,
    rgba(0, 0, 0, 1) 52%
  );
  animation: rotate 4s linear infinite;
  z-index: 1;
  opacity: 0.05;
}

.card {
  height: 12.5em;
  aspect-ratio: 1.586;
  border-radius: 1em;
  background-color: #999;
  opacity: 0.8;
  background-image: linear-gradient(to right, #777, #777 2px, #999 2px, #999);
  background-size: 4px 100%;
}

.shadow {
  position: relative;
  width: 100%;
  height: 100%;
  border-radius: 0.85em;
  border: 1px solid #bbb;
  background:
    radial-gradient(
        circle at 100% 100%,
        #ffffff 0,
        #ffffff 8px,
        transparent 8px
      )
      0% 0%/13px 13px no-repeat,
    radial-gradient(circle at 0 100%, #ffffff 0, #ffffff 8px, transparent 8px)
      100% 0%/13px 13px no-repeat,
    radial-gradient(circle at 100% 0, #ffffff 0, #ffffff 8px, transparent 8px)
      0% 100%/13px 13px no-repeat,
    radial-gradient(circle at 0 0, #ffffff 0, #ffffff 8px, transparent 8px) 100%
      100%/13px 13px no-repeat,
    linear-gradient(#ffffff, #ffffff) 50% 50% / calc(100% - 10px)
      calc(100% - 26px) no-repeat,
    linear-gradient(#ffffff, #ffffff) 50% 50% / calc(100% - 26px)
      calc(100% - 10px) no-repeat,
    linear-gradient(
      135deg,
      rgba(3, 3, 3, 0.5) 0%,
      transparent 22%,
      transparent 47%,
      transparent 73%,
      rgba(0, 0, 0, 0.5) 100%
    );
  box-sizing: border-box;
}

.content {
  position: absolute;
  top: 50%;
  left: 50%;
  border-radius: 0.6em;
  border: 1px solid #aaa;
  box-shadow: -1px -1px 0 #ddd;
  transform: translate(-50%, -50%);
  height: 12em;
  aspect-ratio: 1.604;
  background-image: linear-gradient(to right, #777, #555 2px, #aaa 2px, #aaa);
  background-size: 4px 100%;
}

.rev {
  top: 0.5em;
  left: 0.75em;
  color: #ffffff9f;
  font-size: 1.25em;
}

.master {
  position: absolute;
  bottom: 1.25em;
  right: 0.5em;
  background: linear-gradient(
    90deg,
    rgba(75, 75, 75, 0.25) 0%,
    rgba(121, 121, 121, 1) 100%
  );
  color: #fff;
  height: 2.5em;
  width: 2.5em;
  border: 1px solid #bbb;
  border-radius: 50%;
}

.master.one {
  right: 2em;
}

.master-text {
  bottom: 0.25em;
  right: 0.8em;
  font-size: 0.75em;
}

.ultra-text {
  top: -4px;
  right: 1.75em;
  font-size: 0.5em;
  color: rgba(255, 255, 255, 0.66);
}

.ultra-text,
.master-text,
.rev {
  position: absolute;
  text-shadow: -1px -1px #333;
  color: #fff;
  opacity: 0.75;
}

.chip {
  position: absolute;
  top: 27.5%;
  left: 8.25%;
}

@keyframes rotate {
  0% {
    transform: translate(-25em, -15em);
  }
  20% {
    transform: translate(25em, 15em);
  }
  100% {
    transform: translate(25em, 15em);
  }
}
```

Card
```html
<!-- From Uiverse.io by adamgiebl --> 

<div class="card"></div>
```

```css
/* From Uiverse.io by adamgiebl */ 
.card {
  width: 190px;
  height: 254px;
  border-radius: 30px;
  background: #e0e0e0;
  box-shadow: 15px 15px 30px #bebebe,
             -15px -15px 30px #ffffff;
}
```

Text motion cursor
```html
<!-- From Uiverse.io by Darlley --> 
<svg
  xmlns="http://www.w3.org/2000/svg"
  fill="none"
  viewBox="0 0 614 390"
  height="390"
  width="614"
>
  <g id="Frame">
    <g id="box-figma">
      <path
        fill="#F9F9F9"
        d="M76.2 106.08C72.792 106.08 69.864 105.6 67.416 104.64C64.968 103.632 62.928 102.24 61.296 100.464C59.712 98.688 58.536 96.6 57.768 94.2C57 91.8 56.616 89.16 56.616 86.28V55.104H65.76V85.416C65.76 87.672 66 89.616 66.48 91.248C67.008 92.832 67.728 94.128 68.64 95.136C69.6 96.144 70.704 96.888 71.952 97.368C73.248 97.848 74.688 98.088 76.272 98.088C77.856 98.088 79.296 97.848 80.592 97.368C81.888 96.888 82.992 96.144 83.904 95.136C84.864 94.128 85.584 92.832 86.064 91.248C86.592 89.616 86.856 87.672 86.856 85.416V55.104H96V86.28C96 89.16 95.592 91.8 94.776 94.2C94.008 96.6 92.808 98.688 91.176 100.464C89.592 102.24 87.552 103.632 85.056 104.64C82.56 105.6 79.608 106.08 76.2 106.08ZM137.193 105C135.801 102.168 134.049 99.048 131.937 95.64C129.825 92.232 127.617 88.944 125.313 85.776C124.353 87.024 123.297 88.512 122.145 90.24C121.041 91.968 119.913 93.744 118.761 95.568C117.657 97.344 116.625 99.072 115.665 100.752C114.705 102.432 113.937 103.848 113.361 105H103.065C105.225 100.92 107.721 96.744 110.553 92.472C113.385 88.152 116.457 83.64 119.769 78.936L103.785 55.104H114.585L125.601 72.168L136.473 55.104H146.841L131.073 78.864C134.721 83.808 137.937 88.488 140.721 92.904C143.553 97.32 145.929 101.352 147.849 105H137.193ZM156.562 118.32H147.634L171.97 48.624H180.754L156.562 118.32ZM204.731 106.08C201.323 106.08 198.395 105.6 195.947 104.64C193.499 103.632 191.459 102.24 189.827 100.464C188.243 98.688 187.067 96.6 186.299 94.2C185.531 91.8 185.147 89.16 185.147 86.28V55.104H194.291V85.416C194.291 87.672 194.531 89.616 195.011 91.248C195.539 92.832 196.259 94.128 197.171 95.136C198.131 96.144 199.235 96.888 200.483 97.368C201.779 97.848 203.219 98.088 204.803 98.088C206.387 98.088 207.827 97.848 209.123 97.368C210.419 96.888 211.523 96.144 212.435 95.136C213.395 94.128 214.115 92.832 214.595 91.248C215.123 89.616 215.387 87.672 215.387 85.416V55.104H224.531V86.28C224.531 89.16 224.123 91.8 223.307 94.2C222.539 96.6 221.339 98.688 219.707 100.464C218.123 102.24 216.083 103.632 213.587 104.64C211.091 105.6 208.139 106.08 204.731 106.08ZM236.132 55.104H245.204V105H236.132V55.104ZM283.032 97.512C283.56 97.56 284.256 97.608 285.12 97.656C285.984 97.656 287.16 97.656 288.648 97.656C294.744 97.656 299.28 96.12 302.256 93.048C305.28 89.928 306.792 85.584 306.792 80.016C306.792 74.352 305.328 70.008 302.4 66.984C299.472 63.96 294.936 62.448 288.792 62.448C286.104 62.448 284.184 62.52 283.032 62.664V97.512ZM316.296 80.016C316.296 84.336 315.624 88.104 314.28 91.32C312.936 94.488 311.016 97.152 308.52 99.312C306.072 101.424 303.096 103.008 299.592 104.064C296.136 105.072 292.296 105.576 288.072 105.576C286.056 105.576 283.776 105.48 281.232 105.288C278.688 105.144 276.264 104.808 273.96 104.28V55.824C276.264 55.296 278.712 54.96 281.304 54.816C283.896 54.672 286.2 54.6 288.216 54.6C292.392 54.6 296.208 55.104 299.664 56.112C303.12 57.072 306.072 58.608 308.52 60.72C311.016 62.784 312.936 65.424 314.28 68.64C315.624 71.808 316.296 75.6 316.296 80.016ZM323.683 86.352C323.683 83.04 324.163 80.136 325.123 77.64C326.131 75.144 327.451 73.08 329.083 71.448C330.715 69.768 332.587 68.52 334.699 67.704C336.811 66.84 338.971 66.408 341.179 66.408C346.363 66.408 350.395 68.016 353.275 71.232C356.203 74.448 357.667 79.248 357.667 85.632C357.667 86.112 357.643 86.664 357.595 87.288C357.595 87.864 357.571 88.392 357.523 88.872H332.683C332.923 91.896 333.979 94.248 335.851 95.928C337.771 97.56 340.531 98.376 344.131 98.376C346.243 98.376 348.163 98.184 349.891 97.8C351.667 97.416 353.059 97.008 354.067 96.576L355.219 103.704C354.739 103.944 354.067 104.208 353.203 104.496C352.387 104.736 351.427 104.952 350.323 105.144C349.267 105.384 348.115 105.576 346.867 105.72C345.619 105.864 344.347 105.936 343.051 105.936C339.739 105.936 336.859 105.456 334.411 104.496C331.963 103.488 329.947 102.12 328.363 100.392C326.779 98.616 325.603 96.552 324.835 94.2C324.067 91.8 323.683 89.184 323.683 86.352ZM348.955 82.464C348.955 81.264 348.787 80.136 348.451 79.08C348.115 77.976 347.611 77.04 346.939 76.272C346.315 75.456 345.523 74.832 344.563 74.4C343.651 73.92 342.547 73.68 341.251 73.68C339.907 73.68 338.731 73.944 337.723 74.472C336.715 74.952 335.851 75.6 335.131 76.416C334.459 77.232 333.931 78.168 333.547 79.224C333.163 80.28 332.899 81.36 332.755 82.464H348.955ZM376.335 98.736C378.639 98.736 380.319 98.472 381.375 97.944C382.431 97.368 382.959 96.408 382.959 95.064C382.959 93.816 382.383 92.784 381.231 91.968C380.127 91.152 378.279 90.264 375.687 89.304C374.103 88.728 372.639 88.128 371.295 87.504C369.999 86.832 368.871 86.064 367.911 85.2C366.951 84.336 366.183 83.304 365.607 82.104C365.079 80.856 364.815 79.344 364.815 77.568C364.815 74.112 366.087 71.4 368.631 69.432C371.175 67.416 374.631 66.408 378.999 66.408C381.207 66.408 383.319 66.624 385.335 67.056C387.351 67.44 388.863 67.824 389.871 68.208L388.287 75.264C387.327 74.832 386.103 74.448 384.615 74.112C383.127 73.728 381.399 73.536 379.431 73.536C377.655 73.536 376.215 73.848 375.111 74.472C374.007 75.048 373.455 75.96 373.455 77.208C373.455 77.832 373.551 78.384 373.743 78.864C373.983 79.344 374.367 79.8 374.895 80.232C375.423 80.616 376.119 81.024 376.983 81.456C377.847 81.84 378.903 82.248 380.151 82.68C382.215 83.448 383.967 84.216 385.407 84.984C386.847 85.704 388.023 86.544 388.935 87.504C389.895 88.416 390.591 89.472 391.023 90.672C391.455 91.872 391.671 93.312 391.671 94.992C391.671 98.592 390.327 101.328 387.639 103.2C384.999 105.024 381.207 105.936 376.263 105.936C372.951 105.936 370.287 105.648 368.271 105.072C366.255 104.544 364.839 104.112 364.023 103.776L365.535 96.504C366.831 97.032 368.367 97.536 370.143 98.016C371.967 98.496 374.031 98.736 376.335 98.736ZM408.594 105H399.882V67.344H408.594V105ZM409.53 56.328C409.53 57.96 409.002 59.256 407.946 60.216C406.89 61.176 405.642 61.656 404.202 61.656C402.714 61.656 401.442 61.176 400.386 60.216C399.33 59.256 398.802 57.96 398.802 56.328C398.802 54.648 399.33 53.328 400.386 52.368C401.442 51.408 402.714 50.928 404.202 50.928C405.642 50.928 406.89 51.408 407.946 52.368C409.002 53.328 409.53 54.648 409.53 56.328ZM426.548 85.2C426.548 88.896 427.34 91.608 428.924 93.336C430.556 95.016 432.644 95.856 435.188 95.856C436.58 95.856 437.876 95.664 439.076 95.28C440.324 94.896 441.332 94.44 442.1 93.912V74.4C441.476 74.256 440.708 74.136 439.796 74.04C438.884 73.896 437.732 73.824 436.34 73.824C433.172 73.824 430.748 74.88 429.068 76.992C427.388 79.056 426.548 81.792 426.548 85.2ZM450.812 101.184C450.812 107.184 449.276 111.576 446.204 114.36C443.18 117.144 438.524 118.536 432.236 118.536C429.932 118.536 427.676 118.344 425.468 117.96C423.308 117.576 421.34 117.072 419.564 116.448L421.148 109.032C422.636 109.656 424.316 110.16 426.188 110.544C428.108 110.928 430.172 111.12 432.38 111.12C435.884 111.12 438.38 110.4 439.868 108.96C441.356 107.52 442.1 105.384 442.1 102.552V101.112C441.236 101.544 440.084 101.976 438.644 102.408C437.252 102.84 435.644 103.056 433.82 103.056C431.42 103.056 429.212 102.672 427.196 101.904C425.228 101.136 423.524 100.008 422.084 98.52C420.692 97.032 419.588 95.184 418.772 92.976C418.004 90.72 417.62 88.128 417.62 85.2C417.62 82.464 418.028 79.944 418.844 77.64C419.708 75.336 420.932 73.368 422.516 71.736C424.148 70.104 426.116 68.832 428.42 67.92C430.724 67.008 433.34 66.552 436.268 66.552C439.1 66.552 441.788 66.768 444.332 67.2C446.876 67.632 449.036 68.088 450.812 68.568V101.184ZM461.896 68.568C463.576 68.088 465.76 67.632 468.448 67.2C471.136 66.768 474.112 66.552 477.376 66.552C480.448 66.552 483.016 66.984 485.08 67.848C487.144 68.664 488.776 69.84 489.976 71.376C491.224 72.864 492.088 74.688 492.568 76.848C493.096 78.96 493.36 81.288 493.36 83.832V105H484.648V85.2C484.648 83.184 484.504 81.48 484.216 80.088C483.976 78.648 483.544 77.496 482.92 76.632C482.344 75.72 481.528 75.072 480.472 74.688C479.464 74.256 478.216 74.04 476.728 74.04C475.624 74.04 474.472 74.112 473.272 74.256C472.072 74.4 471.184 74.52 470.608 74.616V105H461.896V68.568ZM513.013 95.424C513.109 96.24 513.157 96.84 513.157 97.224C513.157 97.608 513.157 97.992 513.157 98.376C513.157 101.352 512.677 104.424 511.717 107.592C510.805 110.76 509.509 113.76 507.829 116.592L500.989 114.72C502.141 111.936 502.909 109.2 503.293 106.512C503.725 103.872 503.941 101.544 503.941 99.528C503.941 98.952 503.917 98.232 503.869 97.368C503.869 96.504 503.845 95.856 503.797 95.424H513.013ZM56.976 191V141.104H88.512V148.808H66.048V161.552H85.992V169.256H66.048V191H56.976ZM115.828 161.192C115.108 160.952 114.1 160.712 112.804 160.472C111.556 160.184 110.092 160.04 108.412 160.04C107.452 160.04 106.42 160.136 105.316 160.328C104.26 160.52 103.516 160.688 103.084 160.832V191H94.3721V155.144C96.0521 154.52 98.1401 153.944 100.636 153.416C103.18 152.84 105.988 152.552 109.06 152.552C109.636 152.552 110.308 152.6 111.076 152.696C111.844 152.744 112.612 152.84 113.38 152.984C114.148 153.08 114.892 153.224 115.612 153.416C116.332 153.56 116.908 153.704 117.34 153.848L115.828 161.192ZM157.467 172.136C157.467 175.112 157.035 177.824 156.171 180.272C155.307 182.72 154.083 184.808 152.499 186.536C150.915 188.264 148.995 189.608 146.739 190.568C144.531 191.528 142.083 192.008 139.395 192.008C136.707 192.008 134.259 191.528 132.051 190.568C129.843 189.608 127.947 188.264 126.363 186.536C124.779 184.808 123.531 182.72 122.619 180.272C121.755 177.824 121.323 175.112 121.323 172.136C121.323 169.16 121.755 166.472 122.619 164.072C123.531 161.624 124.779 159.536 126.363 157.808C127.995 156.08 129.915 154.76 132.123 153.848C134.331 152.888 136.755 152.408 139.395 152.408C142.035 152.408 144.459 152.888 146.667 153.848C148.923 154.76 150.843 156.08 152.427 157.808C154.011 159.536 155.235 161.624 156.099 164.072C157.011 166.472 157.467 169.16 157.467 172.136ZM148.539 172.136C148.539 168.392 147.723 165.44 146.091 163.28C144.507 161.072 142.275 159.968 139.395 159.968C136.515 159.968 134.259 161.072 132.627 163.28C131.043 165.44 130.251 168.392 130.251 172.136C130.251 175.928 131.043 178.928 132.627 181.136C134.259 183.344 136.515 184.448 139.395 184.448C142.275 184.448 144.507 183.344 146.091 181.136C147.723 178.928 148.539 175.928 148.539 172.136ZM166.442 154.568C168.122 154.088 170.306 153.632 172.994 153.2C175.682 152.768 178.658 152.552 181.922 152.552C184.994 152.552 187.562 152.984 189.626 153.848C191.69 154.664 193.322 155.84 194.522 157.376C195.77 158.864 196.634 160.688 197.114 162.848C197.642 164.96 197.906 167.288 197.906 169.832V191H189.194V171.2C189.194 169.184 189.05 167.48 188.762 166.088C188.522 164.648 188.09 163.496 187.466 162.632C186.89 161.72 186.074 161.072 185.018 160.688C184.01 160.256 182.762 160.04 181.274 160.04C180.17 160.04 179.018 160.112 177.818 160.256C176.618 160.4 175.73 160.52 175.154 160.616V191H166.442V154.568ZM208.128 143.408L216.84 141.968V153.344H230.232V160.616H216.84V175.952C216.84 178.976 217.32 181.136 218.28 182.432C219.24 183.728 220.872 184.376 223.176 184.376C224.76 184.376 226.152 184.208 227.352 183.872C228.6 183.536 229.584 183.224 230.304 182.936L231.744 189.848C230.736 190.28 229.416 190.712 227.784 191.144C226.152 191.624 224.232 191.864 222.024 191.864C219.336 191.864 217.08 191.504 215.256 190.784C213.48 190.064 212.064 189.032 211.008 187.688C209.952 186.296 209.208 184.64 208.776 182.72C208.344 180.752 208.128 178.52 208.128 176.024V143.408ZM232.234 166.448H251.602V174.44H232.234V166.448ZM259.265 191V141.104H291.305V148.808H268.337V161.12H288.785V168.68H268.337V183.296H293.033V191H259.265ZM301.021 154.568C302.701 154.088 304.885 153.632 307.573 153.2C310.261 152.768 313.237 152.552 316.501 152.552C319.573 152.552 322.141 152.984 324.205 153.848C326.269 154.664 327.901 155.84 329.101 157.376C330.349 158.864 331.213 160.688 331.693 162.848C332.221 164.96 332.485 167.288 332.485 169.832V191H323.773V171.2C323.773 169.184 323.629 167.48 323.341 166.088C323.101 164.648 322.669 163.496 322.045 162.632C321.469 161.72 320.653 161.072 319.597 160.688C318.589 160.256 317.341 160.04 315.853 160.04C314.749 160.04 313.597 160.112 312.397 160.256C311.197 160.4 310.309 160.52 309.733 160.616V191H301.021V154.568ZM349.978 172.064C349.978 175.904 350.89 178.928 352.714 181.136C354.538 183.296 357.058 184.376 360.274 184.376C361.666 184.376 362.842 184.328 363.802 184.232C364.81 184.088 365.626 183.944 366.25 183.8V162.2C365.482 161.672 364.45 161.192 363.154 160.76C361.906 160.28 360.562 160.04 359.122 160.04C355.954 160.04 353.626 161.12 352.138 163.28C350.698 165.44 349.978 168.368 349.978 172.064ZM374.962 189.848C373.234 190.376 371.05 190.856 368.41 191.288C365.818 191.72 363.082 191.936 360.202 191.936C357.226 191.936 354.562 191.48 352.21 190.568C349.858 189.656 347.842 188.36 346.162 186.68C344.53 184.952 343.258 182.888 342.346 180.488C341.482 178.04 341.05 175.304 341.05 172.28C341.05 169.304 341.41 166.616 342.13 164.216C342.898 161.768 344.002 159.68 345.442 157.952C346.882 156.224 348.634 154.904 350.698 153.992C352.762 153.032 355.138 152.552 357.826 152.552C359.65 152.552 361.258 152.768 362.65 153.2C364.042 153.632 365.242 154.112 366.25 154.64V136.568L374.962 135.128V189.848ZM395.028 181.424C395.124 182.24 395.172 182.84 395.172 183.224C395.172 183.608 395.172 183.992 395.172 184.376C395.172 187.352 394.692 190.424 393.732 193.592C392.82 196.76 391.524 199.76 389.844 202.592L383.004 200.72C384.156 197.936 384.924 195.2 385.308 192.512C385.74 189.872 385.956 187.544 385.956 185.528C385.956 184.952 385.932 184.232 385.884 183.368C385.884 182.504 385.86 181.856 385.812 181.424H395.028ZM67.848 227.104C68.904 228.928 70.08 231.16 71.376 233.8C72.672 236.44 73.992 239.224 75.336 242.152C76.68 245.032 78 247.984 79.296 251.008C80.64 253.984 81.864 256.744 82.968 259.288C84.072 256.744 85.272 253.984 86.568 251.008C87.864 247.984 89.184 245.032 90.528 242.152C91.872 239.224 93.192 236.44 94.488 233.8C95.784 231.16 96.96 228.928 98.016 227.104H106.224C106.656 230.752 107.064 234.64 107.448 238.768C107.832 242.848 108.168 247.048 108.456 251.368C108.792 255.64 109.08 259.96 109.32 264.328C109.608 268.648 109.848 272.872 110.04 277H101.112C100.92 271.192 100.68 265.216 100.392 259.072C100.152 252.928 99.768 246.976 99.24 241.216C98.712 242.32 98.088 243.64 97.368 245.176C96.648 246.712 95.88 248.392 95.064 250.216C94.248 251.992 93.408 253.84 92.544 255.76C91.728 257.68 90.912 259.552 90.096 261.376C89.328 263.152 88.608 264.832 87.936 266.416C87.264 267.952 86.688 269.272 86.208 270.376H79.44C78.96 269.272 78.384 267.928 77.712 266.344C77.04 264.76 76.296 263.08 75.48 261.304C74.712 259.48 73.896 257.608 73.032 255.688C72.216 253.768 71.4 251.92 70.584 250.144C69.768 248.368 69 246.712 68.28 245.176C67.56 243.592 66.936 242.272 66.408 241.216C65.88 246.976 65.472 252.928 65.184 259.072C64.944 265.216 64.728 271.192 64.536 277H55.608C55.8 272.872 56.016 268.6 56.256 264.184C56.544 259.768 56.832 255.4 57.12 251.08C57.456 246.712 57.816 242.488 58.2 238.408C58.584 234.328 58.992 230.56 59.424 227.104H67.848ZM154.233 258.136C154.233 261.112 153.801 263.824 152.937 266.272C152.073 268.72 150.849 270.808 149.265 272.536C147.681 274.264 145.761 275.608 143.505 276.568C141.297 277.528 138.849 278.008 136.161 278.008C133.473 278.008 131.025 277.528 128.817 276.568C126.609 275.608 124.713 274.264 123.129 272.536C121.545 270.808 120.297 268.72 119.385 266.272C118.521 263.824 118.089 261.112 118.089 258.136C118.089 255.16 118.521 252.472 119.385 250.072C120.297 247.624 121.545 245.536 123.129 243.808C124.761 242.08 126.681 240.76 128.889 239.848C131.097 238.888 133.521 238.408 136.161 238.408C138.801 238.408 141.225 238.888 143.433 239.848C145.689 240.76 147.609 242.08 149.193 243.808C150.777 245.536 152.001 247.624 152.865 250.072C153.777 252.472 154.233 255.16 154.233 258.136ZM145.305 258.136C145.305 254.392 144.489 251.44 142.857 249.28C141.273 247.072 139.041 245.968 136.161 245.968C133.281 245.968 131.025 247.072 129.393 249.28C127.809 251.44 127.017 254.392 127.017 258.136C127.017 261.928 127.809 264.928 129.393 267.136C131.025 269.344 133.281 270.448 136.161 270.448C139.041 270.448 141.273 269.344 142.857 267.136C144.489 264.928 145.305 261.928 145.305 258.136ZM162.776 229.408L171.488 227.968V239.344H184.88V246.616H171.488V261.952C171.488 264.976 171.968 267.136 172.928 268.432C173.888 269.728 175.52 270.376 177.824 270.376C179.408 270.376 180.8 270.208 182 269.872C183.248 269.536 184.232 269.224 184.952 268.936L186.392 275.848C185.384 276.28 184.064 276.712 182.432 277.144C180.8 277.624 178.88 277.864 176.672 277.864C173.984 277.864 171.728 277.504 169.904 276.784C168.128 276.064 166.712 275.032 165.656 273.688C164.6 272.296 163.856 270.64 163.424 268.72C162.992 266.752 162.776 264.52 162.776 262.024V229.408ZM202.086 277H193.374V239.344H202.086V277ZM203.022 228.328C203.022 229.96 202.494 231.256 201.438 232.216C200.382 233.176 199.134 233.656 197.694 233.656C196.206 233.656 194.934 233.176 193.878 232.216C192.822 231.256 192.294 229.96 192.294 228.328C192.294 226.648 192.822 225.328 193.878 224.368C194.934 223.408 196.206 222.928 197.694 222.928C199.134 222.928 200.382 223.408 201.438 224.368C202.494 225.328 203.022 226.648 203.022 228.328ZM247.256 258.136C247.256 261.112 246.824 263.824 245.96 266.272C245.096 268.72 243.872 270.808 242.288 272.536C240.704 274.264 238.784 275.608 236.528 276.568C234.32 277.528 231.872 278.008 229.184 278.008C226.496 278.008 224.048 277.528 221.84 276.568C219.632 275.608 217.736 274.264 216.152 272.536C214.568 270.808 213.32 268.72 212.408 266.272C211.544 263.824 211.112 261.112 211.112 258.136C211.112 255.16 211.544 252.472 212.408 250.072C213.32 247.624 214.568 245.536 216.152 243.808C217.784 242.08 219.704 240.76 221.912 239.848C224.12 238.888 226.544 238.408 229.184 238.408C231.824 238.408 234.248 238.888 236.456 239.848C238.712 240.76 240.632 242.08 242.216 243.808C243.8 245.536 245.024 247.624 245.888 250.072C246.8 252.472 247.256 255.16 247.256 258.136ZM238.328 258.136C238.328 254.392 237.512 251.44 235.88 249.28C234.296 247.072 232.064 245.968 229.184 245.968C226.304 245.968 224.048 247.072 222.416 249.28C220.832 251.44 220.04 254.392 220.04 258.136C220.04 261.928 220.832 264.928 222.416 267.136C224.048 269.344 226.304 270.448 229.184 270.448C232.064 270.448 234.296 269.344 235.88 267.136C237.512 264.928 238.328 261.928 238.328 258.136ZM256.232 240.568C257.912 240.088 260.096 239.632 262.784 239.2C265.472 238.768 268.448 238.552 271.712 238.552C274.784 238.552 277.352 238.984 279.416 239.848C281.48 240.664 283.112 241.84 284.312 243.376C285.56 244.864 286.424 246.688 286.904 248.848C287.432 250.96 287.695 253.288 287.695 255.832V277H278.984V257.2C278.984 255.184 278.84 253.48 278.552 252.088C278.312 250.648 277.88 249.496 277.256 248.632C276.68 247.72 275.864 247.072 274.808 246.688C273.8 246.256 272.552 246.04 271.064 246.04C269.96 246.04 268.808 246.112 267.608 246.256C266.408 246.4 265.52 246.52 264.944 246.616V277H256.232V240.568ZM324.657 269.512C325.185 269.56 325.881 269.608 326.745 269.656C327.609 269.656 328.785 269.656 330.273 269.656C336.369 269.656 340.905 268.12 343.881 265.048C346.905 261.928 348.417 257.584 348.417 252.016C348.417 246.352 346.953 242.008 344.025 238.984C341.097 235.96 336.561 234.448 330.417 234.448C327.729 234.448 325.809 234.52 324.657 234.664V269.512ZM357.921 252.016C357.921 256.336 357.249 260.104 355.905 263.32C354.561 266.488 352.641 269.152 350.145 271.312C347.697 273.424 344.721 275.008 341.217 276.064C337.761 277.072 333.921 277.576 329.697 277.576C327.681 277.576 325.401 277.48 322.857 277.288C320.313 277.144 317.889 276.808 315.585 276.28V227.824C317.889 227.296 320.337 226.96 322.929 226.816C325.521 226.672 327.825 226.6 329.841 226.6C334.017 226.6 337.833 227.104 341.289 228.112C344.745 229.072 347.697 230.608 350.145 232.72C352.641 234.784 354.561 237.424 355.905 240.64C357.249 243.808 357.921 247.6 357.921 252.016ZM365.308 258.352C365.308 255.04 365.788 252.136 366.748 249.64C367.756 247.144 369.076 245.08 370.708 243.448C372.34 241.768 374.212 240.52 376.324 239.704C378.436 238.84 380.596 238.408 382.804 238.408C387.988 238.408 392.02 240.016 394.9 243.232C397.828 246.448 399.292 251.248 399.292 257.632C399.292 258.112 399.268 258.664 399.22 259.288C399.22 259.864 399.196 260.392 399.148 260.872H374.308C374.548 263.896 375.604 266.248 377.476 267.928C379.396 269.56 382.156 270.376 385.756 270.376C387.868 270.376 389.788 270.184 391.516 269.8C393.292 269.416 394.684 269.008 395.692 268.576L396.844 275.704C396.364 275.944 395.692 276.208 394.828 276.496C394.012 276.736 393.052 276.952 391.948 277.144C390.892 277.384 389.74 277.576 388.492 277.72C387.244 277.864 385.972 277.936 384.676 277.936C381.364 277.936 378.484 277.456 376.036 276.496C373.588 275.488 371.572 274.12 369.988 272.392C368.404 270.616 367.228 268.552 366.46 266.2C365.692 263.8 365.308 261.184 365.308 258.352ZM390.58 254.464C390.58 253.264 390.412 252.136 390.076 251.08C389.74 249.976 389.236 249.04 388.564 248.272C387.94 247.456 387.148 246.832 386.188 246.4C385.276 245.92 384.172 245.68 382.876 245.68C381.532 245.68 380.356 245.944 379.348 246.472C378.34 246.952 377.476 247.6 376.756 248.416C376.084 249.232 375.556 250.168 375.172 251.224C374.788 252.28 374.524 253.36 374.38 254.464H390.58ZM417.96 270.736C420.264 270.736 421.944 270.472 423 269.944C424.056 269.368 424.584 268.408 424.584 267.064C424.584 265.816 424.008 264.784 422.856 263.968C421.752 263.152 419.904 262.264 417.312 261.304C415.728 260.728 414.264 260.128 412.92 259.504C411.624 258.832 410.496 258.064 409.536 257.2C408.576 256.336 407.808 255.304 407.232 254.104C406.704 252.856 406.44 251.344 406.44 249.568C406.44 246.112 407.712 243.4 410.256 241.432C412.8 239.416 416.256 238.408 420.624 238.408C422.832 238.408 424.944 238.624 426.96 239.056C428.976 239.44 430.488 239.824 431.496 240.208L429.912 247.264C428.952 246.832 427.728 246.448 426.24 246.112C424.752 245.728 423.024 245.536 421.056 245.536C419.28 245.536 417.84 245.848 416.736 246.472C415.632 247.048 415.08 247.96 415.08 249.208C415.08 249.832 415.176 250.384 415.368 250.864C415.608 251.344 415.992 251.8 416.52 252.232C417.048 252.616 417.744 253.024 418.608 253.456C419.472 253.84 420.528 254.248 421.776 254.68C423.84 255.448 425.592 256.216 427.032 256.984C428.472 257.704 429.648 258.544 430.56 259.504C431.52 260.416 432.216 261.472 432.648 262.672C433.08 263.872 433.296 265.312 433.296 266.992C433.296 270.592 431.952 273.328 429.264 275.2C426.624 277.024 422.832 277.936 417.888 277.936C414.576 277.936 411.912 277.648 409.896 277.072C407.88 276.544 406.464 276.112 405.648 275.776L407.16 268.504C408.456 269.032 409.992 269.536 411.768 270.016C413.592 270.496 415.656 270.736 417.96 270.736ZM450.219 277H441.507V239.344H450.219V277ZM451.155 228.328C451.155 229.96 450.627 231.256 449.571 232.216C448.515 233.176 447.267 233.656 445.827 233.656C444.339 233.656 443.067 233.176 442.011 232.216C440.955 231.256 440.427 229.96 440.427 228.328C440.427 226.648 440.955 225.328 442.011 224.368C443.067 223.408 444.339 222.928 445.827 222.928C447.267 222.928 448.515 223.408 449.571 224.368C450.627 225.328 451.155 226.648 451.155 228.328ZM468.173 257.2C468.173 260.896 468.965 263.608 470.549 265.336C472.181 267.016 474.269 267.856 476.813 267.856C478.205 267.856 479.501 267.664 480.701 267.28C481.949 266.896 482.957 266.44 483.725 265.912V246.4C483.101 246.256 482.333 246.136 481.421 246.04C480.509 245.896 479.357 245.824 477.965 245.824C474.797 245.824 472.373 246.88 470.693 248.992C469.013 251.056 468.173 253.792 468.173 257.2ZM492.437 273.184C492.437 279.184 490.901 283.576 487.829 286.36C484.805 289.144 480.149 290.536 473.861 290.536C471.557 290.536 469.301 290.344 467.093 289.96C464.933 289.576 462.965 289.072 461.189 288.448L462.773 281.032C464.261 281.656 465.941 282.16 467.813 282.544C469.733 282.928 471.797 283.12 474.005 283.12C477.509 283.12 480.005 282.4 481.493 280.96C482.981 279.52 483.725 277.384 483.725 274.552V273.112C482.861 273.544 481.709 273.976 480.269 274.408C478.877 274.84 477.269 275.056 475.445 275.056C473.045 275.056 470.837 274.672 468.821 273.904C466.853 273.136 465.149 272.008 463.709 270.52C462.317 269.032 461.213 267.184 460.397 264.976C459.629 262.72 459.245 260.128 459.245 257.2C459.245 254.464 459.653 251.944 460.469 249.64C461.333 247.336 462.557 245.368 464.141 243.736C465.773 242.104 467.741 240.832 470.045 239.92C472.349 239.008 474.965 238.552 477.893 238.552C480.725 238.552 483.413 238.768 485.957 239.2C488.501 239.632 490.661 240.088 492.437 240.568V273.184ZM503.521 240.568C505.201 240.088 507.385 239.632 510.073 239.2C512.761 238.768 515.737 238.552 519.001 238.552C522.073 238.552 524.641 238.984 526.705 239.848C528.769 240.664 530.401 241.84 531.601 243.376C532.849 244.864 533.713 246.688 534.193 248.848C534.721 250.96 534.985 253.288 534.985 255.832V277H526.273V257.2C526.273 255.184 526.129 253.48 525.841 252.088C525.601 250.648 525.169 249.496 524.545 248.632C523.969 247.72 523.153 247.072 522.097 246.688C521.089 246.256 519.841 246.04 518.353 246.04C517.249 246.04 516.097 246.112 514.897 246.256C513.697 246.4 512.809 246.52 512.233 246.616V277H503.521V240.568ZM555.43 272.248C555.43 273.928 554.854 275.296 553.702 276.352C552.598 277.408 551.254 277.936 549.67 277.936C548.038 277.936 546.67 277.408 545.566 276.352C544.462 275.296 543.91 273.928 543.91 272.248C543.91 270.568 544.462 269.2 545.566 268.144C546.67 267.04 548.038 266.488 549.67 266.488C551.254 266.488 552.598 267.04 553.702 268.144C554.854 269.2 555.43 270.568 555.43 272.248Z"
        id="text"
      ></path>
      <g id="box">
        <path
          stroke-width="2"
          stroke="#2563EB"
          fill-opacity="0.05"
          fill="#2563EB"
          d="M587 20H28V306H587V20Z"
          id="figny9-box"
        ></path>
        <path
          stroke-width="2"
          stroke="#2563EB"
          fill="white"
          d="M33 15H23V25H33V15Z"
          id="figny9-adjust-1"
        ></path>
        <path
          stroke-width="2"
          stroke="#2563EB"
          fill="white"
          d="M33 301H23V311H33V301Z"
          id="figny9-adjust-3"
        ></path>
        <path
          stroke-width="2"
          stroke="#2563EB"
          fill="white"
          d="M592 301H582V311H592V301Z"
          id="figny9-adjust-4"
        ></path>
        <path
          stroke-width="2"
          stroke="#2563EB"
          fill="white"
          d="M592 15H582V25H592V15Z"
          id="figny9-adjust-2"
        ></path>
      </g>
      <g id="cursor">
        <path
          stroke-width="2"
          stroke="white"
          fill="#2563EB"
          d="M453.383 343L448 317L471 331L459.745 333.5L453.383 343Z"
          id="Vector 273"
        ></path>
        <path
          fill="#2563EB"
          d="M587 343H469.932V376H587V343Z"
          id="Rectangle 786"
        ></path>
        <g id="Darlley Brito">
          <path
            fill="white"
            d="M479.592 364.208C479.197 364.208 479 364.011 479 363.616V354.128C479 353.733 479.197 353.536 479.592 353.536H483.448C484.819 353.536 485.824 353.859 486.464 354.504C487.104 355.144 487.424 356.149 487.424 357.52V360.224C487.424 361.595 487.104 362.603 486.464 363.248C485.829 363.888 484.824 364.208 483.448 364.208H479.592ZM480.176 363.032H483.448C484.141 363.032 484.693 362.944 485.104 362.768C485.515 362.592 485.808 362.299 485.984 361.888C486.16 361.477 486.248 360.923 486.248 360.224V357.52C486.248 356.827 486.16 356.275 485.984 355.864C485.808 355.453 485.515 355.16 485.104 354.984C484.693 354.803 484.141 354.712 483.448 354.712H480.176V363.032Z"
          ></path>
          <path
            fill="white"
            d="M492.729 364.208C491.854 364.208 491.206 363.997 490.785 363.576C490.363 363.155 490.153 362.507 490.153 361.632C490.153 360.757 490.36 360.109 490.776 359.688C491.198 359.267 491.849 359.056 492.729 359.056H496.193C496.171 358.448 496.022 358.029 495.745 357.8C495.467 357.571 494.995 357.456 494.328 357.456H493.401C492.819 357.456 492.387 357.504 492.104 357.6C491.827 357.696 491.641 357.864 491.545 358.104C491.47 358.296 491.387 358.432 491.297 358.512C491.211 358.587 491.078 358.624 490.896 358.624C490.699 358.624 490.544 358.571 490.432 358.464C490.326 358.352 490.294 358.205 490.337 358.024C490.465 357.421 490.779 356.981 491.281 356.704C491.782 356.421 492.489 356.28 493.401 356.28H494.328C495.369 356.28 496.136 356.528 496.632 357.024C497.128 357.52 497.377 358.288 497.377 359.328V363.616C497.377 364.011 497.182 364.208 496.792 364.208C496.398 364.208 496.201 364.011 496.201 363.616V363.112C495.651 363.843 494.793 364.208 493.625 364.208H492.729ZM492.729 363.032H493.625C494.057 363.032 494.454 362.989 494.817 362.904C495.179 362.819 495.483 362.669 495.729 362.456C495.974 362.243 496.131 361.944 496.201 361.56V360.232H492.729C492.179 360.232 491.808 360.331 491.616 360.528C491.424 360.72 491.328 361.088 491.328 361.632C491.328 362.181 491.424 362.552 491.616 362.744C491.808 362.936 492.179 363.032 492.729 363.032Z"
          ></path>
          <path
            fill="white"
            d="M501.029 364.208C500.635 364.208 500.438 364.011 500.438 363.616V356.864C500.438 356.475 500.635 356.28 501.029 356.28C501.419 356.28 501.614 356.475 501.614 356.864V357.696C501.918 357.232 502.317 356.88 502.813 356.64C503.315 356.4 503.896 356.28 504.558 356.28C504.952 356.28 505.149 356.475 505.149 356.864C505.149 357.259 504.952 357.456 504.558 357.456C503.624 357.456 502.909 357.643 502.413 358.016C501.917 358.384 501.651 358.888 501.614 359.528V363.616C501.614 364.011 501.419 364.208 501.029 364.208Z"
          ></path>
          <path
            fill="white"
            d="M509.344 364.208C508.549 364.208 507.96 364.016 507.576 363.632C507.192 363.243 507 362.651 507 361.856V353.584C507 353.195 507.197 353 507.592 353C507.981 353 508.176 353.195 508.176 353.584V361.856C508.176 362.32 508.253 362.632 508.408 362.792C508.568 362.952 508.88 363.032 509.344 363.032C509.744 363.032 509.944 363.227 509.944 363.616C509.955 364.011 509.755 364.208 509.344 364.208Z"
          ></path>
          <path
            fill="white"
            d="M514.563 364.208C513.768 364.208 513.179 364.016 512.795 363.632C512.411 363.243 512.219 362.651 512.219 361.856V353.584C512.219 353.195 512.416 353 512.811 353C513.2 353 513.395 353.195 513.395 353.584V361.856C513.395 362.32 513.472 362.632 513.627 362.792C513.787 362.952 514.099 363.032 514.563 363.032C514.963 363.032 515.163 363.227 515.163 363.616C515.173 364.011 514.973 364.208 514.563 364.208Z"
          ></path>
          <path
            fill="white"
            d="M517.973 360.72V361.168C517.973 361.877 518.106 362.365 518.373 362.632C518.64 362.899 519.133 363.032 519.853 363.032H521.165C521.752 363.032 522.181 362.971 522.453 362.848C522.73 362.72 522.909 362.499 522.989 362.184C523.032 362.008 523.098 361.872 523.189 361.776C523.285 361.68 523.426 361.632 523.613 361.632C523.81 361.632 523.96 361.685 524.061 361.792C524.162 361.893 524.197 362.043 524.165 362.24C524.064 362.907 523.762 363.403 523.261 363.728C522.765 364.048 522.066 364.208 521.165 364.208H519.853C518.813 364.208 518.042 363.96 517.541 363.464C517.045 362.968 516.797 362.203 516.797 361.168V359.328C516.797 358.272 517.045 357.499 517.541 357.008C518.042 356.512 518.813 356.269 519.853 356.28H521.165C522.205 356.28 522.973 356.528 523.469 357.024C523.965 357.515 524.213 358.283 524.213 359.328V360.128C524.213 360.523 524.018 360.72 523.629 360.72H517.973ZM519.853 357.456C519.133 357.445 518.64 357.573 518.373 357.84C518.106 358.107 517.973 358.603 517.973 359.328V359.544H523.037V359.328C523.037 358.608 522.904 358.117 522.637 357.856C522.376 357.589 521.885 357.456 521.165 357.456H519.853Z"
          ></path>
          <path
            fill="white"
            d="M529.158 367.408C528.411 367.408 527.854 367.221 527.486 366.848C527.123 366.48 526.942 365.92 526.942 365.168C526.942 364.779 527.136 364.584 527.526 364.584C527.92 364.584 528.118 364.779 528.118 365.168C528.118 365.595 528.184 365.877 528.318 366.016C528.456 366.16 528.736 366.232 529.158 366.232H532.15C532.571 366.232 532.851 366.16 532.99 366.016C533.128 365.877 533.198 365.595 533.198 365.168V363.08C532.883 363.533 532.507 363.835 532.07 363.984C531.632 364.133 531.147 364.208 530.614 364.208H529.942C528.912 364.208 528.155 363.965 527.67 363.48C527.184 362.995 526.942 362.243 526.942 361.224V356.864C526.942 356.469 527.136 356.272 527.526 356.272C527.92 356.272 528.118 356.469 528.118 356.864V361.224C528.118 361.917 528.246 362.392 528.502 362.648C528.763 362.904 529.243 363.032 529.942 363.032H530.614C531.51 363.032 532.163 362.883 532.574 362.584C532.99 362.285 533.198 361.832 533.198 361.224V356.864C533.198 356.469 533.392 356.272 533.782 356.272C534.176 356.272 534.374 356.469 534.374 356.864V365.168C534.374 365.92 534.19 366.48 533.822 366.848C533.454 367.221 532.896 367.408 532.15 367.408H529.158Z"
          ></path>
          <path
            fill="white"
            d="M542.873 364.208C542.479 364.208 542.281 364.011 542.281 363.616V354.128C542.281 353.733 542.479 353.536 542.873 353.536H547.049C547.876 353.536 548.508 353.752 548.945 354.184C549.383 354.616 549.601 355.237 549.601 356.048V356.48C549.601 357.237 549.361 357.805 548.881 358.184C549.756 358.632 550.193 359.488 550.193 360.752V361.28C550.193 362.24 549.943 362.968 549.441 363.464C548.94 363.96 548.212 364.208 547.257 364.208H542.873ZM543.457 363.032H547.257C547.881 363.032 548.329 362.896 548.601 362.624C548.879 362.347 549.017 361.899 549.017 361.28V360.752C549.017 360.133 548.884 359.691 548.617 359.424C548.351 359.152 547.897 359.016 547.257 359.016H543.457V363.032ZM543.457 357.84H547.281C547.703 357.84 547.999 357.72 548.169 357.48C548.34 357.235 548.425 356.901 548.425 356.48V356.048C548.425 355.563 548.321 355.219 548.113 355.016C547.905 354.813 547.551 354.712 547.049 354.712H543.457V357.84Z"
          ></path>
          <path
            fill="white"
            d="M553.358 364.208C552.963 364.208 552.766 364.011 552.766 363.616V356.864C552.766 356.475 552.963 356.28 553.358 356.28C553.747 356.28 553.942 356.475 553.942 356.864V357.696C554.246 357.232 554.646 356.88 555.142 356.64C555.643 356.4 556.224 356.28 556.886 356.28C557.28 356.28 557.478 356.475 557.478 356.864C557.478 357.259 557.28 357.456 556.886 357.456C555.952 357.456 555.238 357.643 554.742 358.016C554.246 358.384 553.979 358.888 553.942 359.528V363.616C553.942 364.011 553.747 364.208 553.358 364.208Z"
          ></path>
          <path
            fill="white"
            d="M559.704 354.92C559.245 354.92 559.016 354.685 559.016 354.216V353.784C559.016 353.325 559.245 353.096 559.704 353.096H560.136C560.579 353.096 560.8 353.325 560.8 353.784V354.216C560.8 354.685 560.579 354.92 560.136 354.92H559.704ZM559.92 364.208C559.525 364.208 559.328 364.011 559.328 363.616V356.864C559.328 356.475 559.525 356.28 559.92 356.28C560.309 356.28 560.504 356.475 560.504 356.864V363.616C560.504 364.011 560.309 364.208 559.92 364.208Z"
          ></path>
          <path
            fill="white"
            d="M567.031 364.208C566.001 364.208 565.244 363.965 564.759 363.48C564.273 362.995 564.031 362.24 564.031 361.216V357.456H563.191C562.796 357.456 562.599 357.259 562.599 356.864C562.599 356.475 562.796 356.28 563.191 356.28H564.031V354.928C564.031 354.533 564.225 354.336 564.615 354.336C565.009 354.336 565.207 354.533 565.207 354.928V356.28H567.103C567.492 356.28 567.687 356.475 567.687 356.864C567.687 357.259 567.492 357.456 567.103 357.456H565.207V361.216C565.207 361.92 565.335 362.4 565.591 362.656C565.852 362.907 566.332 363.032 567.031 363.032C567.223 363.032 567.369 363.08 567.471 363.176C567.572 363.267 567.623 363.413 567.623 363.616C567.623 364.011 567.425 364.208 567.031 364.208Z"
          ></path>
          <path
            fill="white"
            d="M572.197 364.208C571.157 364.208 570.386 363.96 569.885 363.464C569.389 362.968 569.141 362.203 569.141 361.168V359.328C569.141 358.277 569.389 357.507 569.885 357.016C570.386 356.52 571.157 356.275 572.197 356.28H573.509C574.549 356.28 575.317 356.528 575.813 357.024C576.309 357.52 576.557 358.288 576.557 359.328V361.152C576.557 362.192 576.309 362.963 575.813 363.464C575.317 363.96 574.549 364.208 573.509 364.208H572.197ZM570.317 361.168C570.317 361.877 570.45 362.365 570.717 362.632C570.983 362.899 571.477 363.032 572.197 363.032H573.509C574.229 363.032 574.719 362.899 574.981 362.632C575.247 362.365 575.381 361.872 575.381 361.152V359.328C575.381 358.608 575.247 358.117 574.981 357.856C574.719 357.589 574.229 357.456 573.509 357.456H572.197C571.717 357.456 571.341 357.512 571.069 357.624C570.797 357.736 570.602 357.928 570.485 358.2C570.373 358.472 570.317 358.848 570.317 359.328V361.168Z"
          ></path>
        </g>
      </g>
    </g>
  </g>
</svg>
```

```css
/* From Uiverse.io by Darlley */ 
#cursor,
#box,
#text {
  cursor: pointer;
}
#cursor {
  overflow: visible;
  transform: translate3d(300px, 0, 0) scale(1);
  transform-origin: center center;
  transform-box: fill-box;
  animation: cursor 5s ease infinite alternate;
}
@keyframes cursor {
  0% {
    opacity: 0;
    transform: translate3d(300px, 0, 0) scale(1);
  }
  30% {
    opacity: 1;
    transform: translate3d(0, 0, 0) scale(1);
  }
  60% {
    opacity: 1;
    transform: translate3d(-200px, -200px, 0) scale(1);
  }

  /* clique */
  65% {
    opacity: 1;
    transform: translate3d(-200px, -200px, 0) scale(0.95);
  }
  70% {
    opacity: 1;
    transform: translate3d(-200px, -200px, 0) scale(1);
  }

  100% {
    opacity: 1;
    transform: translate3d(-300px, -50px, 0) scale(1);
  }
}

#box {
  opacity: 0;
  animation: box 5s ease infinite alternate;
}
@keyframes box {
  0%,
  60% {
    opacity: 0;
  }
  65%,
  100% {
    opacity: 1;
  }
}
#text {
}
```

Mouse over tracker
```html
<!-- From Uiverse.io by kennyotsu --> 
<div class="container noselect">
  <div class="canvas">
    <div class="tracker tr-1"></div>
    <div class="tracker tr-2"></div>
    <div class="tracker tr-3"></div>
    <div class="tracker tr-4"></div>
    <div class="tracker tr-5"></div>
    <div class="tracker tr-6"></div>
    <div class="tracker tr-7"></div>
    <div class="tracker tr-8"></div>
    <div class="tracker tr-9"></div>
    <div class="tracker tr-10"></div>
    <div class="tracker tr-11"></div>
    <div class="tracker tr-12"></div>
    <div class="tracker tr-13"></div>
    <div class="tracker tr-14"></div>
    <div class="tracker tr-15"></div>
    <div class="tracker tr-16"></div>
    <div class="tracker tr-17"></div>
    <div class="tracker tr-18"></div>
    <div class="tracker tr-19"></div>
    <div class="tracker tr-20"></div>
    <div class="tracker tr-21"></div>
    <div class="tracker tr-22"></div>
    <div class="tracker tr-23"></div>
    <div class="tracker tr-24"></div>
    <div class="tracker tr-25"></div>
    <div id="card">
    <p id="prompt">HOVER OVER :D</p>
      <div class="title">look mom,<br>no JS</div>
      <div class="subtitle">
        mouse hover tracker
      </div>
      
    </div>
  </div>
</div>
```

```css
/* From Uiverse.io by kennyotsu */ 
/*works janky on mobile :<*/
.container {
  position: relative;
  width: 190px;
  height: 254px;
  transition: 200ms;
}

.container:active {
  width: 180px;
  height: 245px;
}

#card {
  position: absolute;
  inset: 0;
  z-index: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 20px;
  transition: 700ms;
  background: linear-gradient(43deg, rgb(65, 88, 208) 0%, rgb(200, 80, 192) 46%, rgb(255, 204, 112) 100%);
}

.subtitle {
  transform: translateY(160px);
  color: rgb(134, 110, 221);
  text-align: center;
  width: 100%;
}

.title {
  opacity: 0;
  transition-duration: 300ms;
  transition-timing-function: ease-in-out-out;
  transition-delay: 100ms;
  position: absolute;
  font-size: x-large;
  font-weight: bold;
  color: white;
}

.tracker:hover ~ #card .title {
  opacity: 1;
}

#prompt {
  bottom: 8px;
  left: 12px;
  z-index: 20;
  font-size: 20px;
  font-weight: bold;
  transition: 300ms ease-in-out-out;
  position: absolute;
  max-width: 110px;
  color: rgb(255, 255, 255);
}

.tracker {
  position: absolute;
  z-index: 200;
  width: 100%;
  height: 100%;
}

.tracker:hover {
  cursor: pointer;
}

.tracker:hover ~ #card #prompt {
  opacity: 0;
}

.tracker:hover ~ #card {
  transition: 300ms;
  filter: brightness(1.1);
}

.container:hover #card::before {
  transition: 200ms;
  content: '';
  opacity: 80%;
}

.canvas {
  perspective: 800px;
  inset: 0;
  z-index: 200;
  position: absolute;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr 1fr 1fr 1fr;
  gap: 0px 0px;
  grid-template-areas: "tr-1 tr-2 tr-3 tr-4 tr-5"
    "tr-6 tr-7 tr-8 tr-9 tr-10"
    "tr-11 tr-12 tr-13 tr-14 tr-15"
    "tr-16 tr-17 tr-18 tr-19 tr-20"
    "tr-21 tr-22 tr-23 tr-24 tr-25";
}

#card::before {
  content: '';
  background: linear-gradient(43deg, rgb(65, 88, 208) 0%, rgb(200, 80, 192) 46%, rgb(255, 204, 112) 100%);
  filter: blur(2rem);
  opacity: 30%;
  width: 100%;
  height: 100%;
  position: absolute;
  z-index: -1;
  transition: 200ms;
}

.tr-1 {
  grid-area: tr-1;
}

.tr-2 {
  grid-area: tr-2;
}

.tr-3 {
  grid-area: tr-3;
}

.tr-4 {
  grid-area: tr-4;
}

.tr-5 {
  grid-area: tr-5;
}

.tr-6 {
  grid-area: tr-6;
}

.tr-7 {
  grid-area: tr-7;
}

.tr-8 {
  grid-area: tr-8;
}

.tr-9 {
  grid-area: tr-9;
}

.tr-10 {
  grid-area: tr-10;
}

.tr-11 {
  grid-area: tr-11;
}

.tr-12 {
  grid-area: tr-12;
}

.tr-13 {
  grid-area: tr-13;
}

.tr-14 {
  grid-area: tr-14;
}

.tr-15 {
  grid-area: tr-15;
}

.tr-16 {
  grid-area: tr-16;
}

.tr-17 {
  grid-area: tr-17;
}

.tr-18 {
  grid-area: tr-18;
}

.tr-19 {
  grid-area: tr-19;
}

.tr-20 {
  grid-area: tr-20;
}

.tr-21 {
  grid-area: tr-21;
}

.tr-22 {
  grid-area: tr-22;
}

.tr-23 {
  grid-area: tr-23;
}

.tr-24 {
  grid-area: tr-24;
}

.tr-25 {
  grid-area: tr-25;
}

.tr-1:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(20deg) rotateY(-10deg) rotateZ(0deg);
}

.tr-2:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(20deg) rotateY(-5deg) rotateZ(0deg);
}

.tr-3:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(20deg) rotateY(0deg) rotateZ(0deg);
}

.tr-4:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(20deg) rotateY(5deg) rotateZ(0deg);
}

.tr-5:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(20deg) rotateY(10deg) rotateZ(0deg);
}

.tr-6:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(10deg) rotateY(-10deg) rotateZ(0deg);
}

.tr-7:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(10deg) rotateY(-5deg) rotateZ(0deg);
}

.tr-8:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(10deg) rotateY(0deg) rotateZ(0deg);
}

.tr-9:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(10deg) rotateY(5deg) rotateZ(0deg);
}

.tr-10:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(10deg) rotateY(10deg) rotateZ(0deg);
}

.tr-11:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(0deg) rotateY(-10deg) rotateZ(0deg);
}

.tr-12:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(0deg) rotateY(-5deg) rotateZ(0deg);
}

.tr-13:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg);
}

.tr-14:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(0deg) rotateY(5deg) rotateZ(0deg);
}

.tr-15:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(0deg) rotateY(10deg) rotateZ(0deg);
}

.tr-16:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(-10deg) rotateY(-10deg) rotateZ(0deg);
}

.tr-17:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(-10deg) rotateY(-5deg) rotateZ(0deg);
}

.tr-18:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(-10deg) rotateY(0deg) rotateZ(0deg);
}

.tr-19:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(-10deg) rotateY(5deg) rotateZ(0deg);
}

.tr-20:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(-10deg) rotateY(10deg) rotateZ(0deg);
}

.tr-21:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(-20deg) rotateY(-10deg) rotateZ(0deg);
}

.tr-22:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(-20deg) rotateY(-5deg) rotateZ(0deg);
}

.tr-23:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(-20deg) rotateY(0deg) rotateZ(0deg);
}

.tr-24:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(-20deg) rotateY(5deg) rotateZ(0deg);
}

.tr-25:hover ~ #card {
  transition: 125ms ease-in-out;
  transform: rotateX(-20deg) rotateY(10deg) rotateZ(0deg);
}

.noselect {
  -webkit-touch-callout: none;
   /* iOS Safari */
  -webkit-user-select: none;
   /* Safari */
   /* Konqueror HTML */
  -moz-user-select: none;
   /* Old versions of Firefox */
  -ms-user-select: none;
   /* Internet Explorer/Edge */
  user-select: none;
   /* Non-prefixed version, currently
									supported by Chrome, Edge, Opera and Firefox */
}
```


# 🧠 Base de Connaissances Avancée — GitHub Knowledge Compendium

> Compilation de 47 dépôts GitHub couvrant l'IA, la 3D, le web dev, l'animation, les algorithmes et bien plus.

---

## 📚 Table des Matières

1. [🤖 IA & Agents — Context Engineering](#-ia--agents--context-engineering)
2. [💬 Prompt Engineering & ChatGPT](#-prompt-engineering--chatgpt)
3. [🌐 Three.js & 3D Web](#-threejs--3d-web)
4. [📦 Modèles 3D & Ressources](#-modèles-3d--ressources)
5. [🎨 ComfyUI & IA Visuelle](#-comfyui--ia-visuelle)
6. [📱 Flutter & Animations Mobile](#-flutter--animations-mobile)
7. [🟨 JavaScript — Style, Algos & Projets](#-javascript--style-algos--projets)
8. [🎨 CSS — Frameworks & Animations](#-css--frameworks--animations)
9. [🌍 HTML — Standards & Boilerplate](#-html--standards--boilerplate)
10. [🛠️ Outils Développeurs](#️-outils-développeurs)
11. [⚙️ Sujets Spécialisés](#️-sujets-spécialisés)
12. [📊 Récap des Thèmes par Niveau](#-récap-des-thèmes-par-niveau)

---

## 🤖 IA & Agents — Context Engineering

### [`humanlayer/advanced-context-engineering-for-coding-agents`](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents)

**Thème** : Ingénierie de contexte pour agents de codage LLM

#### Concepts Clés
- **Context Window Management** : Gérer efficacement la fenêtre de contexte des LLMs (Claude, GPT-4, etc.)
- **Agent Loop** : Boucle principale d'un agent IA → planification → action → observation → réévaluation
- **Tool Use / Function Calling** : Intégrer des outils externes (bash, éditeur de fichiers, API) dans la boucle agentique
- **Prompt Compression** : Réduire le contexte sans perdre l'information critique
- **Memory Systems** : Mémoire à court terme (contexte) vs long terme (vector DB, fichiers)

#### Bonnes Pratiques
```
1. Séparer les instructions système des données de contexte
2. Utiliser des fichiers CLAUDE.md / AGENTS.md pour les règles projet
3. Passer les gros fichiers en référence, pas en entier dans le prompt
4. Implémenter une hiérarchie de contexte : Global → Projet → Tâche
5. Gérer le "context poisoning" (éviter les erreurs cumulées)
```

#### Architecture Recommandée
```
project/
├── AGENTS.md          # Instructions globales pour l'agent
├── .context/
│   ├── memory.json    # Mémoire persistante
│   ├── tools.yaml     # Définition des outils
│   └── prompts/       # Templates de prompts
└── src/
```

---

### [`spdustin/ChatGPT-AutoExpert`](https://github.com/spdustin/ChatGPT-AutoExpert)

**Thème** : Système de prompts avancés pour ChatGPT — transformer GPT en expert auto-calibré

#### Concepts Clés
- **AutoExpert System Prompts** : Prompts qui forcent ChatGPT à adopter le rôle d'un expert dans son domaine
- **Slash Commands** : Commandes personnalisées (`/help`, `/save`, `/recap`) pour naviguer dans les conversations
- **Conversation Management** : Techniques pour maintenir la cohérence sur de longues conversations
- **Dev Mode** : Mode développement avec réponses techniques enrichies

#### Template AutoExpert (Dev)
```
AUTOEXPERT v7 — Developer Edition

Tu es un expert senior en [domaine]. Pour chaque réponse :
1. Identifie les ambiguïtés potentielles AVANT de répondre
2. Fournis du code complet et fonctionnel, jamais de pseudocode
3. Explique les trade-offs de chaque approche
4. Anticipe les questions de suivi
5. Utilise des exemples concrets du monde réel
```

#### Slash Commands Utiles
| Commande | Effet |
|----------|-------|
| `/recap` | Résumé de la session actuelle |
| `/save` | Génère un artifact sauvegardable |
| `/help` | Liste des commandes disponibles |
| `/fix` | Corrige la dernière erreur |

---

## 💬 Prompt Engineering & ChatGPT

### [`Jermic/awesome-aiart-pics-prompts`](https://github.com/Jermic/awesome-aiart-pics-prompts)
### [`335622119/Prompts-Robin-ChatGPT-Aiprm`](https://github.com/335622119/Prompts-Robin-ChatGPT-Aiprm)
### [`newmediacrew/aiprm`](https://github.com/newmediacrew/aiprm)

**Thème** : Collections de prompts pour l'art IA et ChatGPT

#### Structure d'un Bon Prompt Image IA
```
[Sujet principal] + [Style artistique] + [Éclairage] + [Composition] + 
[Ambiance/Mood] + [Qualité technique] + [Artiste de référence]

Exemple :
"A cyberpunk samurai standing on a rooftop at night, 
neon reflections on wet pavement, dramatic backlighting, 
cinematic composition, ultra-detailed, 8K, 
in the style of Syd Mead and Blade Runner aesthetic"
```

#### Modificateurs de Qualité (Midjourney/DALL-E/SD)
```
Qualité    : ultra-detailed, 8K, masterpiece, best quality
Style      : photorealistic, oil painting, watercolor, anime
Éclairage  : golden hour, dramatic lighting, volumetric fog
Composition: rule of thirds, wide angle, macro shot, bird's eye view
Négatifs   : blurry, distorted, ugly, low quality, watermark
```

#### Catégories de Prompts AIPRM
- **SEO & Marketing** : Génération de contenu optimisé
- **Copywriting** : Structures AIDA, PAS, FAB
- **Dev** : Génération de code, refactoring, documentation
- **Éducation** : Explications adaptées, quiz, résumés
- **Créatif** : Storytelling, worldbuilding, scripts

---

### [`httpie/http-prompt`](https://github.com/httpie/http-prompt)

**Thème** : Interface CLI interactive pour HTTP — HTTPie + autocomplétion

#### Fonctionnalités
```bash
# Lancer http-prompt
http-prompt http://localhost:8000

# Commandes internes
cd /api/users          # Changer de base URL
GET                    # Envoyer requête GET
POST name=Alice age:=30  # Requête POST avec JSON
Authorization:"Bearer TOKEN"  # Header persistant
env                    # Voir l'environnement actuel
source ./config.htp    # Charger une config
```

#### Avantages vs curl
| Feature | http-prompt | curl |
|---------|-------------|------|
| Autocomplétion | ✅ | ❌ |
| Headers persistants | ✅ | ❌ |
| Historique | ✅ | Limité |
| Colorisation | ✅ | ❌ |
| Sessions | ✅ | Manuel |

---

### [`Laboratoria/UPSK-AI-APPS-001-prompt-to-json`](https://github.com/Laboratoria/UPSK-AI-APPS-001-prompt-to-json)

**Thème** : Convertir des prompts en sorties JSON structurées avec LLMs

#### Pattern Prompt-to-JSON
```javascript
const systemPrompt = `
Tu es un extracteur de données JSON.
RÈGLES ABSOLUES :
- Réponds UNIQUEMENT avec du JSON valide
- Pas de markdown, pas de backticks, pas d'explication
- Respecte exactement ce schéma : {schema}
- Si une valeur manque, utilise null
`;

const schema = {
  name: "string",
  age: "number",
  skills: ["string"],
  available: "boolean"
};
```

#### Validation et Parsing Robuste
```javascript
function safeParseJSON(response) {
  // Nettoyer les backticks markdown
  const clean = response.replace(/```json|```/g, '').trim();
  
  try {
    return { data: JSON.parse(clean), error: null };
  } catch (e) {
    // Tentative de réparation
    const fixed = clean
      .replace(/,\s*}/g, '}')     // Virgules trailing
      .replace(/'/g, '"');         // Apostrophes → guillemets
    
    return { data: JSON.parse(fixed), error: null };
  }
}
```

---

### [`lobehub/lobe-chat-agents`](https://github.com/lobehub/lobe-chat-agents)

**Thème** : Agents personnalisés pour Lobe Chat — marketplace de personas IA

#### Structure d'un Agent Lobe Chat
```json
{
  "identifier": "expert-dev-fr",
  "avatar": "🧑‍💻",
  "title": "Expert Développeur Senior",
  "description": "Expert en architecture logicielle et bonnes pratiques",
  "locale": "fr-FR",
  "systemRole": "Tu es un développeur senior avec 15 ans d'expérience...",
  "tags": ["coding", "architecture", "review"],
  "config": {
    "model": "claude-sonnet-4",
    "temperature": 0.3,
    "max_tokens": 4096
  }
}
```

---

## 🌐 Three.js & 3D Web

### [`mrdoob/three.js`](https://github.com/mrdoob/three.js)

**Thème** : La librairie 3D JavaScript la plus utilisée au monde

#### Setup Minimal Three.js
```javascript
import * as THREE from 'three';

// Scène de base
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true });

renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(window.devicePixelRatio);
document.body.appendChild(renderer.domElement);

// Géométrie + Matériau + Mesh
const geometry = new THREE.BoxGeometry(1, 1, 1);
const material = new THREE.MeshStandardMaterial({ color: 0x00ff88 });
const cube = new THREE.Mesh(geometry, material);
scene.add(cube);

// Lumière
const light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(5, 5, 5);
scene.add(light);
scene.add(new THREE.AmbientLight(0x404040));

camera.position.z = 5;

// Boucle d'animation
function animate() {
  requestAnimationFrame(animate);
  cube.rotation.x += 0.01;
  cube.rotation.y += 0.01;
  renderer.render(scene, camera);
}
animate();
```

#### Objets Three.js Essentiels
| Classe | Rôle |
|--------|------|
| `Scene` | Conteneur de tous les objets |
| `PerspectiveCamera` | Caméra en perspective (FOV, aspect, near, far) |
| `WebGLRenderer` | Rendu via WebGL |
| `Mesh` | Objet 3D = Geometry + Material |
| `BufferGeometry` | Géométrie custom via buffers |
| `ShaderMaterial` | Matériau avec GLSL custom |
| `TextureLoader` | Chargement de textures |
| `GLTFLoader` | Import de modèles .gltf/.glb |
| `OrbitControls` | Navigation souris/tactile |
| `RayCaster` | Picking / interaction |

#### Matériaux Courants
```javascript
// Basique (pas affecté par la lumière)
new THREE.MeshBasicMaterial({ color: 0xff0000 })

// Phong (lumière + spéculaire)
new THREE.MeshPhongMaterial({ color: 0x00ff00, shininess: 100 })

// Standard (PBR - physiquement correct)
new THREE.MeshStandardMaterial({
  color: 0x0000ff,
  roughness: 0.5,
  metalness: 0.8,
  map: texture,
  normalMap: normalTexture
})

// Shader personnalisé
new THREE.ShaderMaterial({
  vertexShader: `...`,
  fragmentShader: `...`,
  uniforms: { time: { value: 0 } }
})
```

#### Post-Processing
```javascript
import { EffectComposer } from 'three/examples/jsm/postprocessing/EffectComposer';
import { RenderPass } from 'three/examples/jsm/postprocessing/RenderPass';
import { UnrealBloomPass } from 'three/examples/jsm/postprocessing/UnrealBloomPass';

const composer = new EffectComposer(renderer);
composer.addPass(new RenderPass(scene, camera));
composer.addPass(new UnrealBloomPass(
  new THREE.Vector2(window.innerWidth, window.innerHeight),
  1.5,  // strength
  0.4,  // radius
  0.85  // threshold
));
```

---

### [`pmndrs/react-three-fiber`](https://github.com/pmndrs/react-three-fiber)

**Thème** : Binding React pour Three.js — 3D déclarative en JSX

#### Setup React Three Fiber
```jsx
import { Canvas } from '@react-three/fiber'
import { OrbitControls, Environment, Float } from '@react-three/drei'

function Box() {
  const meshRef = useRef()
  useFrame((state, delta) => {
    meshRef.current.rotation.x += delta
  })
  
  return (
    <mesh ref={meshRef} onClick={() => console.log('clicked!')}>
      <boxGeometry args={[1, 1, 1]} />
      <meshStandardMaterial color="hotpink" />
    </mesh>
  )
}

export default function App() {
  return (
    <Canvas camera={{ position: [0, 0, 5], fov: 75 }}>
      <ambientLight intensity={0.5} />
      <directionalLight position={[5, 5, 5]} />
      <Float speed={2} rotationIntensity={1}>
        <Box />
      </Float>
      <OrbitControls />
      <Environment preset="city" />
    </Canvas>
  )
}
```

#### Hooks React Three Fiber
```jsx
useFrame((state, delta) => {})   // Appelé à chaque frame
useThree()                        // Accès à scene, camera, renderer
useLoader(GLTFLoader, '/model.glb') // Chargement async
useTexture('/texture.jpg')        // Texture avec Suspense
```

#### Bibliothèque Drei (Helpers)
```jsx
import { 
  OrbitControls,    // Navigation
  PerspectiveCamera,// Caméra configurable
  Text,             // Texte 3D
  Html,             // HTML dans la scène 3D
  Image,            // Image plane
  Sky,              // Ciel procédural
  Stars,            // Particules étoiles
  Sparkles,         // Effet scintillement
  MeshDistortMaterial, // Matériau distorsion
  MeshWobbleMaterial,  // Matériau wobble
} from '@react-three/drei'
```

---

### [`Ovilia/ThreeExample.js`](https://github.com/Ovilia/ThreeExample.js)
### [`z2586300277/three-cesium-examples`](https://github.com/z2586300277/three-cesium-examples)
### [`hawk86104/three-vue-tres`](https://github.com/hawk86104/three-vue-tres)
### [`idflood/ThreeNodes.js`](https://github.com/idflood/ThreeNodes.js)

**Thème** : Exemples avancés Three.js — intégration Vue/Cesium/Node-based

#### Patterns Avancés Three.js

**Instance Mesh** (performance pour objets répétés)
```javascript
const count = 10000;
const mesh = new THREE.InstancedMesh(geometry, material, count);

for (let i = 0; i < count; i++) {
  const matrix = new THREE.Matrix4();
  matrix.setPosition(Math.random()*100, Math.random()*100, Math.random()*100);
  mesh.setMatrixAt(i, matrix);
}
scene.add(mesh);
```

**Intégration Cesium + Three.js** (géospatial 3D)
```javascript
// Synchronisation caméra Cesium → Three.js
function synchronizeThreeCamera(cesiumCamera, threeCamera) {
  const cvm = cesiumCamera.viewMatrix;
  const civm = cesiumCamera.inverseViewMatrix;
  
  threeCamera.matrixWorld.set(
    civm[0], civm[4], civm[8],  civm[12],
    civm[1], civm[5], civm[9],  civm[13],
    civm[2], civm[6], civm[10], civm[14],
    civm[3], civm[7], civm[11], civm[15]
  );
}
```

---

## 📦 Modèles 3D & Ressources

### [`alecjacobson/common-3d-test-models`](https://github.com/alecjacobson/common-3d-test-models)

**Thème** : Modèles 3D standards pour tests (Stanford Bunny, Utah Teapot, etc.)

#### Modèles Iconiques
| Modèle | Usage | Format |
|--------|-------|--------|
| Stanford Bunny | Test de rendu | .obj, .ply |
| Utah Teapot | Benchmark historique | .obj |
| Stanford Dragon | Rendu complexe | .ply |
| Armadillo | Surface détaillée | .ply |
| Suzanne | Blender mascot | .blend, .obj |

#### Chargement dans Three.js
```javascript
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader';
import { PLYLoader } from 'three/examples/jsm/loaders/PLYLoader';

// OBJ
const objLoader = new OBJLoader();
objLoader.load('/models/bunny.obj', (object) => {
  scene.add(object);
});

// PLY
const plyLoader = new PLYLoader();
plyLoader.load('/models/dragon.ply', (geometry) => {
  const mesh = new THREE.Mesh(geometry, material);
  scene.add(mesh);
});

// GLTF (recommandé pour le web)
const gltfLoader = new GLTFLoader();
gltfLoader.load('/models/model.glb', (gltf) => {
  scene.add(gltf.scene);
  // Animations
  const mixer = new THREE.AnimationMixer(gltf.scene);
  gltf.animations.forEach(clip => mixer.clipAction(clip).play());
});
```

---

### [`openscad/openscad`](https://github.com/openscad/openscad)

**Thème** : CAO paramétrique scriptée — modélisation 3D par code

#### Syntaxe OpenSCAD
```openscad
// Variables
width = 50;
height = 30;
depth = 20;

// Primitives
cube([width, depth, height]);
sphere(r = 10);
cylinder(h = 20, r = 5, center = true);

// Transformations
translate([10, 0, 0]) cube([5, 5, 5]);
rotate([0, 45, 0]) cylinder(h=20, r=3);
scale([2, 1, 1]) sphere(10);

// Opérations booléennes
difference() {
  cube([30, 30, 30]);
  sphere(20);
}

union() {
  cube([10, 10, 10]);
  translate([5, 5, 10]) sphere(7);
}

intersection() {
  cube([20, 20, 20]);
  sphere(15);
}

// Module (fonction réutilisable)
module rounded_box(w, h, d, r) {
  minkowski() {
    cube([w-2*r, h-2*r, d-2*r]);
    sphere(r);
  }
}
rounded_box(30, 20, 10, 2);
```

---

### [`Tencent-Hunyuan/Hunyuan3D-2`](https://github.com/Tencent-Hunyuan/Hunyuan3D-2)

**Thème** : Génération de modèles 3D par IA (image → 3D mesh)

#### Pipeline Hunyuan3D
```
Image 2D → [Shape Diffusion Model] → Mesh 3D → [Texture Synthesis] → Modèle Texturé

Formats de sortie : .obj, .glb, .ply
Résolution texture : jusqu'à 1024x1024
Temps de génération : ~30-60 secondes (GPU)
```

#### Utilisation API
```python
from hy3dgen.shapegen import Hunyuan3DDiTFlowMatchingPipeline

pipeline = Hunyuan3DDiTFlowMatchingPipeline.from_pretrained(
    'tencent/Hunyuan3D-2',
    torch_dtype=torch.float16
).to('cuda')

# Image → 3D
mesh = pipeline(image=image_pil)[0]
mesh.export('output.glb')
```

---

### [`nasa/NASA-3D-Resources`](https://github.com/nasa/NASA-3D-Resources)

**Thème** : Modèles 3D officiels NASA — vaisseaux, planètes, stations spatiales

#### Ressources Disponibles
- **Vaisseaux spatiaux** : Apollo, Space Shuttle, Orion, Voyager
- **Planètes** : Mars, Lune (topographie réelle), Jupiter
- **Stations** : ISS (International Space Station)
- **Rovers** : Curiosity, Perseverance
- **Formats** : .3ds, .obj, .fbx, .stl

---

## 🎨 ComfyUI & IA Visuelle

### [`PowerHouseMan/ComfyUI-AdvancedLivePortrait`](https://github.com/PowerHouseMan/ComfyUI-AdvancedLivePortrait)

**Thème** : Animation de portraits via IA dans ComfyUI

#### Workflow LivePortrait
```
Source Image → [Face Detection] → [Keypoint Extraction] 
     ↓
Driving Video → [Motion Extraction] → [Motion Transfer] 
     ↓
[Face Warping] → [Blending] → Animated Output
```

#### Nœuds Clés ComfyUI
```
AdvancedLivePortrait nodes:
├── LoadImage              # Image source
├── FaceDetector           # Détection visage
├── LivePortraitDriving    # Vidéo pilote
├── LivePortraitProcess    # Traitement principal
├── ExpressionEditor       # Édition expressions
└── SaveVideo              # Export
```

---

### [`Kosinkadink/ComfyUI-AnimateDiff-Evolved`](https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved)

**Thème** : Génération vidéo IA avec AnimateDiff dans ComfyUI

#### Concepts AnimateDiff
- **Motion Module** : Module additionnel pour les modèles SD qui encode le mouvement entre frames
- **Context Options** : Gestion de la fenêtre temporelle (standard, loop, static)
- **IPAdapter** : Cohérence de style entre frames
- **ControlNet Video** : Contrôle de pose/profondeur frame par frame

#### Pipeline Basique
```
[Checkpoint SD] + [AnimateDiff Motion Module]
         ↓
[CLIP Text Encode] → Prompt positif/négatif
         ↓
[KSampler] → [VAE Decode] → [VHS Video Combine]
         ↓
      Vidéo MP4
```

#### Paramètres Importants
| Paramètre | Valeur recommandée | Effet |
|-----------|-------------------|-------|
| Frame count | 16-32 | Durée de la vidéo |
| Context length | 16 | Cohérence temporelle |
| CFG Scale | 7-8 | Fidélité au prompt |
| Steps | 20-30 | Qualité/vitesse |
| Motion scale | 1.0-1.5 | Amplitude du mouvement |

---

## 📱 Flutter & Animations Mobile

### [`cscoderr/flutter_advanced`](https://github.com/cscoderr/flutter_advanced)
### [`MarcinusX/flutter_ui_challenge_flight_search`](https://github.com/MarcinusX/flutter_ui_challenge_flight_search)

**Thème** : Techniques Flutter avancées — animations, UI complexes

#### Animations Flutter
```dart
// AnimatedBuilder
AnimatedBuilder(
  animation: _controller,
  builder: (context, child) {
    return Transform.rotate(
      angle: _controller.value * 2 * math.pi,
      child: child,
    );
  },
  child: FlutterLogo(size: 100),
);

// Hero Animation
Hero(
  tag: 'flight-${flight.id}',
  child: FlightCard(flight: flight),
);

// Implicit Animation
AnimatedContainer(
  duration: Duration(milliseconds: 300),
  curve: Curves.easeInOut,
  width: _expanded ? 200 : 100,
  color: _selected ? Colors.blue : Colors.grey,
);
```

#### Widgets Animation Clés
```dart
AnimationController  // Contrôleur temporel
Tween<double>        // Interpolation de valeurs
CurvedAnimation      // Courbes d'accélération
AnimatedWidget       // Widget qui se rebuild
AnimatedBuilder      // Builder avec animation
TweenAnimationBuilder // Animation déclarative
```

---

### [`intuit/AnimationEngine`](https://github.com/intuit/AnimationEngine)

**Thème** : Moteur d'animation iOS (Objective-C) — animations déclaratives

#### Concepts iOS Animation Engine
```objc
// Chaînage d'animations
[view animateSequentially:@[
  [AIRAnimation animateWithDuration:0.3 animations:^{
    view.alpha = 1.0;
  }],
  [AIRAnimation animateWithDuration:0.5 animations:^{
    view.frame = finalFrame;
  }]
]];
```

---

### [`hyperandroid/CAAT`](https://github.com/hyperandroid/CAAT)

**Thème** : Canvas Animation Authoring Toolkit — framework animation canvas 2D

#### Structure CAAT
```javascript
var director = new CAAT.Director().initialize(800, 600, canvas);
var scene = director.createScene();

// Acteur animé
var actor = new CAAT.Actor()
  .setSize(50, 50)
  .setPosition(100, 100)
  .addBehavior(
    new CAAT.RotateBehavior()
      .setFrameTime(0, 2000)
      .setValues(0, Math.PI * 2)
  );

scene.addChild(actor);
CAAT.loop(60);
```

---

## 🟨 JavaScript — Style, Algos & Projets

### [`airbnb/javascript`](https://github.com/airbnb/javascript)

**Thème** : Guide de style JavaScript le plus utilisé au monde

#### Règles Essentielles Airbnb

**Variables**
```javascript
// ✅ Utiliser const par défaut, let si nécessaire
const MAX_SIZE = 100;
let counter = 0;

// ❌ Jamais var
var name = 'old way';

// ✅ Destructuring
const { firstName, lastName } = user;
const [first, ...rest] = array;
```

**Fonctions**
```javascript
// ✅ Arrow functions pour callbacks
const doubled = numbers.map(n => n * 2);

// ✅ Fonctions nommées pour les méthodes
const obj = {
  greet() {
    return 'Hello';
  }
};

// ✅ Paramètres par défaut
function createUser(name, role = 'user', active = true) {}

// ❌ Pas d'arguments object → utiliser rest params
function sum(...args) {
  return args.reduce((a, b) => a + b, 0);
}
```

**Classes et Modules**
```javascript
// ✅ Classes ES6
class Animal {
  constructor(name) {
    this.name = name;
  }
  
  speak() {
    return `${this.name} makes a sound.`;
  }
}

// ✅ Import/Export ES modules
import { debounce, throttle } from './utils';
export { myFunction };
export default MyComponent;
```

**Async/Await**
```javascript
// ✅ Préférer async/await aux .then()
async function fetchUser(id) {
  try {
    const response = await fetch(`/api/users/${id}`);
    const user = await response.json();
    return user;
  } catch (error) {
    console.error('Failed to fetch user:', error);
    throw error;
  }
}
```

---

### [`trekhleb/javascript-algorithms`](https://github.com/trekhleb/javascript-algorithms)

**Thème** : Algorithmes et structures de données en JavaScript — référence complète

#### Structures de Données

**Liste Chaînée**
```javascript
class LinkedListNode {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  constructor() { this.head = null; this.tail = null; }
  
  prepend(value) {
    const node = new LinkedListNode(value);
    node.next = this.head;
    this.head = node;
    if (!this.tail) this.tail = node;
  }
  
  append(value) {
    const node = new LinkedListNode(value);
    if (!this.head) { this.head = node; this.tail = node; return; }
    this.tail.next = node;
    this.tail = node;
  }
}
```

**Arbre Binaire de Recherche (BST)**
```javascript
class BSTNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BST {
  insert(value) { this.root = this._insert(this.root, value); }
  
  _insert(node, value) {
    if (!node) return new BSTNode(value);
    if (value < node.value) node.left = this._insert(node.left, value);
    else if (value > node.value) node.right = this._insert(node.right, value);
    return node;
  }
}
```

**Graphe (adjacence)**
```javascript
class Graph {
  constructor(directed = false) {
    this.vertices = new Map();
    this.directed = directed;
  }
  
  addEdge(u, v, weight = 1) {
    if (!this.vertices.has(u)) this.vertices.set(u, []);
    if (!this.vertices.has(v)) this.vertices.set(v, []);
    this.vertices.get(u).push({ node: v, weight });
    if (!this.directed) this.vertices.get(v).push({ node: u, weight });
  }
}
```

#### Algorithmes de Tri
```javascript
// Quick Sort O(n log n) moyen
function quickSort(arr, low = 0, high = arr.length - 1) {
  if (low < high) {
    const pivot = partition(arr, low, high);
    quickSort(arr, low, pivot - 1);
    quickSort(arr, pivot + 1, high);
  }
  return arr;
}

// Merge Sort O(n log n) garanti
function mergeSort(arr) {
  if (arr.length <= 1) return arr;
  const mid = Math.floor(arr.length / 2);
  return merge(mergeSort(arr.slice(0, mid)), mergeSort(arr.slice(mid)));
}

// Binary Search O(log n)
function binarySearch(arr, target) {
  let left = 0, right = arr.length - 1;
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (arr[mid] === target) return mid;
    arr[mid] < target ? left = mid + 1 : right = mid - 1;
  }
  return -1;
}
```

#### Algorithmes de Graphes
```javascript
// BFS (Breadth-First Search)
function bfs(graph, start) {
  const visited = new Set([start]);
  const queue = [start];
  const result = [];
  
  while (queue.length) {
    const node = queue.shift();
    result.push(node);
    for (const neighbor of graph.get(node) || []) {
      if (!visited.has(neighbor.node)) {
        visited.add(neighbor.node);
        queue.push(neighbor.node);
      }
    }
  }
  return result;
}

// DFS (Depth-First Search)
function dfs(graph, start, visited = new Set()) {
  visited.add(start);
  const result = [start];
  for (const neighbor of graph.get(start) || []) {
    if (!visited.has(neighbor.node)) {
      result.push(...dfs(graph, neighbor.node, visited));
    }
  }
  return result;
}

// Dijkstra (chemin le plus court)
function dijkstra(graph, start) {
  const distances = new Map();
  const visited = new Set();
  
  graph.forEach((_, node) => distances.set(node, Infinity));
  distances.set(start, 0);
  
  while (visited.size < graph.size) {
    const current = [...distances.entries()]
      .filter(([n]) => !visited.has(n))
      .reduce((a, b) => a[1] < b[1] ? a : b)[0];
    
    visited.add(current);
    for (const { node, weight } of graph.get(current) || []) {
      const newDist = distances.get(current) + weight;
      if (newDist < distances.get(node)) distances.set(node, newDist);
    }
  }
  return distances;
}
```

#### Complexités Importantes
| Algo | Temps Moyen | Temps Pire | Espace |
|------|-------------|------------|--------|
| Quick Sort | O(n log n) | O(n²) | O(log n) |
| Merge Sort | O(n log n) | O(n log n) | O(n) |
| Heap Sort | O(n log n) | O(n log n) | O(1) |
| Binary Search | O(log n) | O(log n) | O(1) |
| BFS/DFS | O(V+E) | O(V+E) | O(V) |
| Dijkstra | O(V²) | O(V²) | O(V) |
| Hash Table | O(1) | O(n) | O(n) |

---

### [`TheAlgorithms/JavaScript`](https://github.com/TheAlgorithms/JavaScript)

**Thème** : Implémentations éducatives de tous les algorithmes connus en JS

#### Catégories Couvertes
- **Maths** : PGCD, nombres premiers (Crible d'Ératosthène), Fibonacci, factorielle
- **Chiffrement** : César, Vigenère, RSA, Base64
- **Géométrie** : Distance euclidienne, Graham scan, Convex hull
- **DP** : Knapsack, Longest Common Subsequence, Edit Distance
- **String** : KMP, Rabin-Karp, Levenshtein

```javascript
// Sieve of Eratosthenes
function sieve(n) {
  const primes = new Array(n + 1).fill(true);
  primes[0] = primes[1] = false;
  
  for (let i = 2; i * i <= n; i++) {
    if (primes[i]) {
      for (let j = i * i; j <= n; j += i) {
        primes[j] = false;
      }
    }
  }
  return primes.reduce((acc, isPrime, num) => isPrime ? [...acc, num] : acc, []);
}

// Fibonacci avec mémoïsation
function fibonacci(n, memo = {}) {
  if (n in memo) return memo[n];
  if (n <= 1) return n;
  return memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo);
}
```

---

### [`wesbos/JavaScript30`](https://github.com/wesbos/JavaScript30)

**Thème** : 30 projets JS en 30 jours — DOM, Canvas, Audio API, CSS

#### Projets Notables
| # | Projet | Concepts |
|---|--------|----------|
| 1 | Drum Kit | addEventListener, audio play |
| 2 | CSS + JS Clock | CSS transforms, Date |
| 5 | Flex Panel Gallery | Flexbox, transitions, classList |
| 6 | Ajax Type Ahead | fetch, RegExp, highlight |
| 11 | Custom HTML5 Video | HTMLVideoElement API |
| 19 | Webcam Fun | getUserMedia, Canvas, filtres |
| 28 | Video Speed Controller | mousemove events |

```javascript
// Projet 6 — Type Ahead avec highlight
async function fetchCities() {
  const res = await fetch('https://gist.githubusercontent.com/.../cities.json');
  return res.json();
}

function findMatches(wordToMatch, cities) {
  return cities.filter(place => {
    const regex = new RegExp(wordToMatch, 'gi');
    return place.city.match(regex) || place.state.match(regex);
  });
}

function highlightMatch(str, word) {
  const regex = new RegExp(word, 'gi');
  return str.replace(regex, `<span class="hl">${word}</span>`);
}
```

---

## 🎨 CSS — Frameworks & Animations

### [`airbnb/css`](https://github.com/airbnb/css)

**Thème** : Guide de style CSS/Sass d'Airbnb

#### Conventions de Nommage (BEM)
```scss
// Block
.card { }

// Element
.card__header { }
.card__body { }
.card__footer { }

// Modifier
.card--featured { }
.card__header--large { }

// State (avec classe utilitaire)
.card.is-active { }
.card.is-loading { }
```

#### Organisation des Propriétés
```css
.element {
  /* 1. Positionnement */
  position: relative;
  top: 0;
  z-index: 10;
  
  /* 2. Box Model */
  display: flex;
  width: 100%;
  margin: 0 auto;
  padding: 1rem;
  
  /* 3. Typographie */
  font-size: 1rem;
  line-height: 1.5;
  color: #333;
  
  /* 4. Visuel */
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 4px;
  
  /* 5. Animations */
  transition: transform 0.2s ease;
}
```

---

### [`hakimel/css`](https://github.com/hakimel/css)

**Thème** : Techniques CSS avancées par le créateur de reveal.js

#### Effets CSS Remarquables

**Blur Hash / Frosted Glass**
```css
.glass-card {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(10px) saturate(180%);
  -webkit-backdrop-filter: blur(10px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
}
```

**CSS Custom Properties (Variables)**
```css
:root {
  --color-primary: #6366f1;
  --color-bg: #0f172a;
  --spacing-md: 1rem;
  --radius: 8px;
  --shadow: 0 4px 24px rgba(0,0,0,0.3);
}

.card {
  background: var(--color-bg);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
}
```

---

### [`animate-css/animate.css`](https://github.com/animate-css/animate.css)

**Thème** : Bibliothèque d'animations CSS prêtes à l'emploi

#### Utilisation
```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>

<!-- Basique -->
<div class="animate__animated animate__bounce">Bounce!</div>

<!-- Avec délai et durée -->
<div class="animate__animated animate__fadeInUp animate__delay-1s animate__slower">
  Fade In
</div>
```

#### Classes CSS
```css
/* Entrées */
.animate__fadeIn, .animate__fadeInUp, .animate__fadeInLeft
.animate__slideInDown, .animate__bounceIn, .animate__zoomIn

/* Sorties */
.animate__fadeOut, .animate__slideOutRight, .animate__bounceOut

/* Attention */
.animate__bounce, .animate__flash, .animate__pulse, .animate__shake

/* Contrôle */
.animate__delay-1s, .animate__delay-2s, .animate__delay-3s
.animate__slow, .animate__slower, .animate__fast, .animate__faster
```

#### Via JavaScript
```javascript
function animateCSS(element, animation) {
  return new Promise((resolve) => {
    const prefix = 'animate__';
    const node = document.querySelector(element);
    
    node.classList.add(`${prefix}animated`, `${prefix}${animation}`);
    
    node.addEventListener('animationend', () => {
      node.classList.remove(`${prefix}animated`, `${prefix}${animation}`);
      resolve();
    }, { once: true });
  });
}

// Usage
await animateCSS('.card', 'bounceIn');
```

---

### [`primer/css`](https://github.com/primer/css)

**Thème** : Design System CSS de GitHub (Primer)

#### Tokens de Design
```css
/* Spacing */
.m-0 { margin: 0; }
.p-3 { padding: var(--base-size-16, 16px); }
.mt-4 { margin-top: var(--base-size-24, 24px); }

/* Flexbox utilitaires */
.d-flex { display: flex; }
.flex-items-center { align-items: center; }
.flex-justify-between { justify-content: space-between; }

/* Couleurs sémantiques */
.color-fg-default { color: var(--fgColor-default); }
.color-bg-subtle { background: var(--bgColor-subtle); }
.color-accent-emphasis { color: var(--fgColor-accent); }
```

---

### [`TheOdinProject/css-exercises`](https://github.com/TheOdinProject/css-exercises)

**Thème** : Exercices CSS progressifs — du débutant à l'avancé

#### Sujets Couverts
1. **Sélecteurs** : combinateurs, pseudo-classes, pseudo-éléments
2. **Box Model** : margin, padding, border, box-sizing
3. **Flexbox** : justify-content, align-items, flex-wrap, order
4. **Grid** : grid-template-columns/rows, grid-area, auto-fill
5. **Positioning** : relative, absolute, fixed, sticky
6. **Responsive** : media queries, breakpoints, fluid layouts
7. **Animations** : @keyframes, transition, transform

```css
/* Grid Layout Avancé */
.dashboard {
  display: grid;
  grid-template-columns: 250px 1fr;
  grid-template-rows: 60px 1fr auto;
  grid-template-areas:
    "sidebar header"
    "sidebar main"
    "sidebar footer";
  min-height: 100vh;
}

.sidebar { grid-area: sidebar; }
.header  { grid-area: header; }
.main    { grid-area: main; }
.footer  { grid-area: footer; }
```

---

## 🌍 HTML — Standards & Boilerplate

### [`whatwg/html`](https://github.com/whatwg/html)

**Thème** : Le standard HTML officiel (WHATWG Living Standard)

#### Éléments HTML5 Sémantiques
```html
<header>    <!-- En-tête de page ou section -->
<nav>       <!-- Navigation principale -->
<main>      <!-- Contenu principal (1 seul par page) -->
<article>   <!-- Contenu autonome (blog post, tweet) -->
<section>   <!-- Section thématique -->
<aside>     <!-- Contenu annexe (sidebar) -->
<footer>    <!-- Pied de page ou section -->
<figure>    <!-- Contenu illustratif + légende -->
<figcaption><!-- Légende de figure -->
<time>      <!-- Date/heure machine-readable -->
<mark>      <!-- Texte surligné/référencé -->
<details>   <!-- Accordéon natif -->
<summary>   <!-- Titre de l'accordéon details -->
<dialog>    <!-- Modal natif -->
<template>  <!-- Fragment HTML inerte -->
```

#### APIs HTML5 Importantes
```javascript
// Geolocation
navigator.geolocation.getCurrentPosition(pos => {
  const { latitude, longitude } = pos.coords;
});

// Web Storage
localStorage.setItem('theme', 'dark');
const theme = localStorage.getItem('theme');

// Drag & Drop
element.addEventListener('dragstart', e => {
  e.dataTransfer.setData('text/plain', element.id);
});

// Intersection Observer (lazy loading)
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) entry.target.classList.add('visible');
  });
}, { threshold: 0.1 });

// Service Worker
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js');
}
```

---

### [`h5bp/html5-boilerplate`](https://github.com/h5bp/html5-boilerplate)

**Thème** : Template HTML5 professionnel — best practices intégrées

#### Structure Template
```html
<!doctype html>
<html class="no-js" lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Mon Projet</title>
  
  <!-- SEO -->
  <meta name="description" content="Description de la page">
  
  <!-- Open Graph -->
  <meta property="og:title" content="Mon Projet">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://example.com">
  <meta property="og:image" content="https://example.com/og-image.png">
  
  <!-- Favicon multi-format -->
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" href="/icon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/icon-180.png">
  <link rel="manifest" href="/site.webmanifest">
  
  <!-- CSS -->
  <link rel="stylesheet" href="css/normalize.css">
  <link rel="stylesheet" href="css/main.css">
</head>
<body>
  <!-- Contenu principal -->
  
  <script src="js/vendor/modernizr.js"></script>
  <script src="js/main.js"></script>
</body>
</html>
```

#### .htaccess Recommandations
```apache
# Compression GZIP
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript
</IfModule>

# Cache headers
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/jpg "access plus 1 year"
  ExpiresByType text/css "access plus 1 month"
  ExpiresByType application/javascript "access plus 1 month"
</IfModule>

# HTTPS redirect
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

---

### [`niklasvh/html2canvas`](https://github.com/niklasvh/html2canvas)

**Thème** : Capturer le DOM en image Canvas — screenshot côté client

#### Utilisation
```javascript
import html2canvas from 'html2canvas';

// Capture simple
const canvas = await html2canvas(document.querySelector('#capture'));
document.body.appendChild(canvas);

// Avec options
const canvas = await html2canvas(element, {
  scale: 2,                    // Résolution x2 (retina)
  useCORS: true,               // Images cross-origin
  backgroundColor: '#ffffff',  // Fond blanc
  logging: false,              // Désactiver les logs
  width: 1200,                 // Largeur fixe
  height: 800,
  scrollX: 0,
  scrollY: -window.scrollY    // Compensation scroll
});

// Télécharger en PNG
const link = document.createElement('a');
link.download = 'screenshot.png';
link.href = canvas.toDataURL('image/png');
link.click();

// Convertir en Blob pour envoi serveur
canvas.toBlob(blob => {
  const formData = new FormData();
  formData.append('screenshot', blob, 'screen.png');
  fetch('/upload', { method: 'POST', body: formData });
}, 'image/png', 0.95);
```

#### Limitations Connues
- Pas de rendu CSS 3D transforms
- Pas de SVG cross-origin
- Certaines propriétés CSS non supportées (filter, mix-blend-mode partiel)
- Les webfonts doivent être CORS-enabled

---

## 🛠️ Outils Développeurs

### [`GitSquared/edex-ui`](https://github.com/GitSquared/edex-ui)

**Thème** : Terminal futuriste multi-écrans inspiré de TRON — Electron + React

#### Features
- Terminal multi-tabulations avec vrais shells (bash, zsh, fish, PowerShell)
- Moniteur système en temps réel (CPU, RAM, réseau, disque)
- Thèmes customisables (TRON, Matrix, Default)
- Mode fullscreen pour présentations

```javascript
// Architecture Electron
main.js (Node.js process)
  ↕ IPC
renderer.js (Chrome process)
  ├── Terminal (node-pty + xterm.js)
  ├── System Monitor (systeminformation)
  └── Network Map (D3.js)
```

---

### [`alireza0/s-ui`](https://github.com/alireza0/s-ui)

**Thème** : Panel de gestion de serveurs proxy — alternative à 3x-ui

#### Stack Technique
- **Backend** : Go + SQLite
- **Frontend** : Vue.js 3 + Vuetify
- **Protocoles** : VLESS, VMess, Trojan, Shadowsocks
- **Features** : Multi-utilisateurs, stats trafic, TLS, CDN

---

### [`ynqa/jnv`](https://github.com/ynqa/jnv)

**Thème** : Navigateur JSON interactif avec autocomplétion jq

#### Utilisation
```bash
# Depuis stdin
echo '{"name": "Alice", "age": 30}' | jnv

# Depuis fichier
jnv data.json

# Depuis URL (avec curl)
curl -s https://api.github.com/users/octocat | jnv

# Raccourcis clavier
Ctrl+P / Up    # Historique filtres
Tab            # Autocomplétion jq
Enter          # Appliquer filtre
Ctrl+C         # Copier résultat
```

---

## ⚙️ Sujets Spécialisés

### [`StephenGrider/AdvancedNodeComplete`](https://github.com/StephenGrider/AdvancedNodeComplete)

**Thème** : Node.js avancé — clustering, workers, Redis, caching

#### Concepts Avancés Node.js

**Clustering**
```javascript
const cluster = require('cluster');
const os = require('os');

if (cluster.isMaster) {
  const cpuCount = os.cpus().length;
  for (let i = 0; i < cpuCount; i++) cluster.fork();
  cluster.on('exit', () => cluster.fork()); // Auto-restart
} else {
  require('./server'); // Worker process
}
```

**Cache Redis**
```javascript
const redis = require('redis');
const client = redis.createClient();

// Cache middleware Express
async function cacheMiddleware(req, res, next) {
  const key = req.url;
  const cached = await client.get(key);
  
  if (cached) {
    return res.json(JSON.parse(cached));
  }
  
  res.sendResponse = res.json.bind(res);
  res.json = (data) => {
    client.setEx(key, 3600, JSON.stringify(data)); // 1h TTL
    res.sendResponse(data);
  };
  next();
}
```

**Worker Threads (CPU-intensive)**
```javascript
const { Worker, isMainThread, parentPort } = require('worker_threads');

if (isMainThread) {
  const worker = new Worker(__filename, {
    workerData: { numbers: [1, 2, 3, 4, 5] }
  });
  worker.on('message', result => console.log('Result:', result));
} else {
  const { workerData } = require('worker_threads');
  const result = workerData.numbers.reduce((a, b) => a + b, 0);
  parentPort.postMessage(result);
}
```

---

### [`AtsushiSakai/PyAdvancedControl`](https://github.com/AtsushiSakai/PyAdvancedControl)

**Thème** : Théorie du contrôle avancée en Python — PID, LQR, MPC

#### Contrôleur PID
```python
class PIDController:
    def __init__(self, Kp, Ki, Kd, dt=0.01):
        self.Kp, self.Ki, self.Kd = Kp, Ki, Kd
        self.dt = dt
        self.prev_error = 0
        self.integral = 0
    
    def compute(self, setpoint, measurement):
        error = setpoint - measurement
        self.integral += error * self.dt
        derivative = (error - self.prev_error) / self.dt
        
        output = (self.Kp * error + 
                  self.Ki * self.integral + 
                  self.Kd * derivative)
        
        self.prev_error = error
        return output

# Usage
pid = PIDController(Kp=1.2, Ki=0.5, Kd=0.1)
for t in range(1000):
    u = pid.compute(setpoint=1.0, measurement=sensor_reading)
```

#### LQR (Linear Quadratic Regulator)
```python
import numpy as np
import scipy.linalg

def lqr(A, B, Q, R):
    """Calcul du gain optimal LQR K tel que u = -Kx"""
    P = scipy.linalg.solve_continuous_are(A, B, Q, R)
    K = np.linalg.inv(R) @ B.T @ P
    return K, P

# Système linéaire : ẋ = Ax + Bu
A = np.array([[0, 1], [-2, -3]])
B = np.array([[0], [1]])
Q = np.eye(2)      # Coût sur l'état
R = np.array([[1]]) # Coût sur le contrôle

K, P = lqr(A, B, Q, R)
```

---

### [`sryza/aas`](https://github.com/sryza/aas)

**Thème** : Advanced Analytics with Spark — Machine Learning distribué

#### Spark ML Pipeline
```python
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.classification import RandomForestClassifier

# Assemblage features
assembler = VectorAssembler(
    inputCols=['feature1', 'feature2', 'feature3'],
    outputCol='features_raw'
)

# Normalisation
scaler = StandardScaler(inputCol='features_raw', outputCol='features')

# Modèle
rf = RandomForestClassifier(featuresCol='features', labelCol='label',
                             numTrees=100, maxDepth=10)

# Pipeline complet
pipeline = Pipeline(stages=[assembler, scaler, rf])
model = pipeline.fit(train_df)
predictions = model.transform(test_df)
```

---

### [`The-SourceCode/Advanced_Bukkit_Coding`](https://github.com/The-SourceCode/Advanced_Bukkit_Coding)

**Thème** : Plugins Minecraft Bukkit/Spigot avancés — Java

#### Plugin Bukkit Basique
```java
public class MyPlugin extends JavaPlugin implements Listener {
    
    @Override
    public void onEnable() {
        getServer().getPluginManager().registerEvents(this, this);
        getLogger().info("Plugin activé !");
    }
    
    @EventHandler
    public void onPlayerJoin(PlayerJoinEvent event) {
        Player player = event.getPlayer();
        player.sendMessage(ChatColor.GREEN + "Bienvenue " + player.getName() + " !");
    }
    
    // Commande custom
    @Override
    public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {
        if (cmd.getName().equalsIgnoreCase("heal")) {
            if (sender instanceof Player) {
                Player player = (Player) sender;
                player.setHealth(player.getMaxHealth());
                player.sendMessage("Vous êtes soigné !");
            }
        }
        return true;
    }
}
```

---

### [`commonsguy/cw-advandroid`](https://github.com/commonsguy/cw-advandroid)

**Thème** : Android avancé — Services, ContentProviders, Loaders, NDK

#### Service Android
```java
public class MyBackgroundService extends Service {
    
    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        // Tâche en background
        new Thread(() -> {
            doHeavyWork();
            stopSelf();
        }).start();
        
        return START_NOT_STICKY;
    }
    
    // Foreground service (notification obligatoire)
    public void startForeground() {
        Notification notification = new NotificationCompat.Builder(this, CHANNEL_ID)
            .setContentTitle("Service actif")
            .setSmallIcon(R.drawable.ic_service)
            .build();
        
        startForeground(1, notification);
    }
}
```

---

### [`dimashyshkin/advanced-selenium-webdriver`](https://github.com/dimashyshkin/advanced-selenium-webdriver)

**Thème** : Selenium WebDriver avancé — tests E2E, Page Object Model

#### Page Object Model Pattern
```java
public class LoginPage {
    private WebDriver driver;
    
    @FindBy(id = "username") private WebElement usernameField;
    @FindBy(id = "password") private WebElement passwordField;
    @FindBy(css = "button[type=submit]") private WebElement loginBtn;
    
    public LoginPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }
    
    public DashboardPage login(String username, String password) {
        usernameField.sendKeys(username);
        passwordField.sendKeys(password);
        loginBtn.click();
        return new DashboardPage(driver);
    }
}

// Test
@Test
public void testSuccessfulLogin() {
    LoginPage loginPage = new LoginPage(driver);
    DashboardPage dashboard = loginPage.login("admin", "password");
    Assert.assertTrue(dashboard.isLoggedIn());
}
```

---

## 📊 Récap des Thèmes par Niveau

### 🟢 Débutant → Intermédiaire
| Repo | Domaine | Niveau |
|------|---------|--------|
| html5-boilerplate | HTML/CSS | Débutant |
| animate.css | CSS Animations | Débutant |
| JavaScript30 | JS Projets | Débutant |
| css-exercises | CSS | Débutant-Inter |
| primer/css | Design System | Intermédiaire |

### 🟡 Intermédiaire → Avancé
| Repo | Domaine | Niveau |
|------|---------|--------|
| three.js | 3D Web | Intermédiaire |
| react-three-fiber | React + 3D | Intermédiaire |
| javascript-algorithms | Algorithmique | Intermédiaire |
| airbnb/javascript | JS Style | Intermédiaire |
| http-prompt | CLI/HTTP | Intermédiaire |
| html2canvas | DOM/Canvas | Intermédiaire |

### 🔴 Avancé
| Repo | Domaine | Niveau |
|------|---------|--------|
| context-engineering | IA/Agents | Avancé |
| AdvancedNodeComplete | Node.js | Avancé |
| PyAdvancedControl | Contrôle/Robotique | Avancé |
| aas (Spark) | Big Data/ML | Avancé |
| AnimateDiff-Evolved | Vidéo IA | Avancé |
| Hunyuan3D-2 | IA 3D Gen | Avancé |
| openscad | CAO paramétrique | Avancé |

---

## 🔗 Index Rapide des Ressources

### Liens Directs
- **IA Agents** : [humanlayer](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents) · [ChatGPT-AutoExpert](https://github.com/spdustin/ChatGPT-AutoExpert) · [lobe-agents](https://github.com/lobehub/lobe-chat-agents)
- **3D Web** : [three.js](https://github.com/mrdoob/three.js) · [react-three-fiber](https://github.com/pmndrs/react-three-fiber) · [three-cesium](https://github.com/z2586300277/three-cesium-examples)
- **JavaScript** : [airbnb/js](https://github.com/airbnb/javascript) · [js-algorithms](https://github.com/trekhleb/javascript-algorithms) · [TheAlgorithms](https://github.com/TheAlgorithms/JavaScript) · [JS30](https://github.com/wesbos/JavaScript30)
- **CSS** : [primer](https://github.com/primer/css) · [animate.css](https://github.com/animate-css/animate.css) · [airbnb/css](https://github.com/airbnb/css)
- **HTML** : [html5-boilerplate](https://github.com/h5bp/html5-boilerplate) · [html2canvas](https://github.com/niklasvh/html2canvas) · [whatwg](https://github.com/whatwg/html)
- **Outils** : [edex-ui](https://github.com/GitSquared/edex-ui) · [jnv](https://github.com/ynqa/jnv) · [http-prompt](https://github.com/httpie/http-prompt)

---

*Généré automatiquement — 47 dépôts GitHub couvrant 15+ domaines technologiques*

```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ultra Button Design Lab</title>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=JetBrains+Mono:wght@300;400;700&family=Syne:wght@400;700;800&family=DM+Serif+Display:ital@0;1&family=Space+Mono&family=Unbounded:wght@300;700;900&family=Cormorant+Garamond:ital,wght@0,300;0,600;1,300&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --bg: #080a0f;
  --grid: rgba(255,255,255,0.03);
  --accent1: #00ffe5;
  --accent2: #ff2d78;
  --accent3: #ffd700;
  --accent4: #7b2fff;
}

body {
  background: var(--bg);
  min-height: 100vh;
  font-family: 'JetBrains Mono', monospace;
  color: #fff;
  overflow-x: hidden;
}

/* Animated grid background */
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image:
    linear-gradient(var(--grid) 1px, transparent 1px),
    linear-gradient(90deg, var(--grid) 1px, transparent 1px);
  background-size: 60px 60px;
  pointer-events: none;
  z-index: 0;
}

body::after {
  content: '';
  position: fixed;
  inset: 0;
  background: radial-gradient(ellipse 80% 60% at 50% 0%, rgba(0,255,229,0.04) 0%, transparent 70%),
              radial-gradient(ellipse 60% 40% at 80% 100%, rgba(255,45,120,0.04) 0%, transparent 70%);
  pointer-events: none;
  z-index: 0;
}

header {
  position: relative;
  z-index: 10;
  text-align: center;
  padding: 80px 20px 60px;
}

header .label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.4em;
  color: var(--accent1);
  text-transform: uppercase;
  margin-bottom: 16px;
  opacity: 0.7;
}

header h1 {
  font-family: 'Unbounded', sans-serif;
  font-size: clamp(2.5rem, 6vw, 5rem);
  font-weight: 900;
  letter-spacing: -0.02em;
  line-height: 0.95;
  background: linear-gradient(135deg, #fff 0%, rgba(255,255,255,0.5) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

header h1 span {
  background: linear-gradient(135deg, var(--accent1), var(--accent2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

header p {
  margin-top: 20px;
  font-size: 13px;
  color: rgba(255,255,255,0.3);
  letter-spacing: 0.1em;
}

.grid {
  position: relative;
  z-index: 10;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  gap: 2px;
  padding: 0 2px 2px;
}

.cell {
  background: rgba(255,255,255,0.015);
  border: 1px solid rgba(255,255,255,0.05);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 40px;
  gap: 28px;
  min-height: 280px;
  position: relative;
  overflow: hidden;
  transition: background 0.3s;
}

.cell:hover {
  background: rgba(255,255,255,0.03);
}

.cell-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 9px;
  letter-spacing: 0.35em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.2);
  position: absolute;
  top: 20px;
  left: 24px;
}

.cell-number {
  font-family: 'Unbounded', sans-serif;
  font-size: 9px;
  font-weight: 900;
  color: rgba(255,255,255,0.08);
  position: absolute;
  bottom: 20px;
  right: 24px;
  letter-spacing: 0.2em;
}

/* ==============================
   BTN 01 — MAGNETIC PLASMA
   ============================== */
.btn-plasma {
  position: relative;
  padding: 0;
  border: none;
  background: none;
  cursor: pointer;
  font-family: 'Unbounded', sans-serif;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: #fff;
  width: 220px;
  height: 64px;
  outline: none;
}

.btn-plasma .plasma-bg {
  position: absolute;
  inset: 0;
  border-radius: 4px;
  background: linear-gradient(135deg, #00ffe5, #7b2fff, #ff2d78, #00ffe5);
  background-size: 300% 300%;
  animation: plasmaShift 4s ease infinite;
  z-index: 0;
}

.btn-plasma .plasma-inner {
  position: absolute;
  inset: 2px;
  border-radius: 3px;
  background: #080a0f;
  z-index: 1;
  transition: inset 0.3s ease;
}

.btn-plasma span {
  position: relative;
  z-index: 2;
  background: linear-gradient(135deg, #00ffe5, #7b2fff);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  background-size: 300% 300%;
  animation: plasmaShift 4s ease infinite;
  transition: letter-spacing 0.3s ease;
}

.btn-plasma:hover .plasma-inner { inset: 3px; }
.btn-plasma:hover span { letter-spacing: 0.25em; }
.btn-plasma:active .plasma-inner { inset: 1px; }

@keyframes plasmaShift {
  0%   { background-position: 0% 50%; }
  50%  { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* Glow orbiting dot */
.btn-plasma::after {
  content: '';
  position: absolute;
  width: 8px;
  height: 8px;
  background: #00ffe5;
  border-radius: 50%;
  box-shadow: 0 0 12px #00ffe5, 0 0 24px #00ffe5;
  animation: orbit 3s linear infinite;
  z-index: 3;
  top: 50%;
  left: 50%;
  transform-origin: -100px 0;
  opacity: 0;
  transition: opacity 0.3s;
}

.btn-plasma:hover::after { opacity: 1; }

@keyframes orbit {
  0%   { transform: rotate(0deg) translateX(100px); }
  100% { transform: rotate(360deg) translateX(100px); }
}


/* ==============================
   BTN 02 — LIQUID MERCURY
   ============================== */
.btn-mercury {
  position: relative;
  border: none;
  background: linear-gradient(135deg, #e8e8e8, #a0a0a0, #ffffff, #888);
  background-size: 200% 200%;
  animation: mercurySheen 3s ease infinite;
  border-radius: 100px;
  padding: 18px 44px;
  font-family: 'Playfair Display', serif;
  font-size: 15px;
  font-style: italic;
  font-weight: 400;
  letter-spacing: 0.05em;
  color: #1a1a1a;
  cursor: pointer;
  outline: none;
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.3s;
  box-shadow:
    0 2px 4px rgba(0,0,0,0.4),
    0 8px 24px rgba(0,0,0,0.3),
    inset 0 1px 1px rgba(255,255,255,0.9),
    inset 0 -1px 2px rgba(0,0,0,0.2);
}

.btn-mercury::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: conic-gradient(
    transparent 0deg,
    rgba(255,255,255,0.6) 60deg,
    transparent 120deg,
    transparent 360deg
  );
  animation: mercurySpin 2s linear infinite;
  opacity: 0;
  transition: opacity 0.3s;
}

.btn-mercury:hover::before { opacity: 1; }
.btn-mercury:hover {
  transform: translateY(-3px) scale(1.03);
  box-shadow:
    0 4px 8px rgba(0,0,0,0.5),
    0 16px 40px rgba(0,0,0,0.4),
    inset 0 1px 1px rgba(255,255,255,0.9),
    inset 0 -1px 2px rgba(0,0,0,0.2);
}
.btn-mercury:active { transform: translateY(1px) scale(0.98); }

@keyframes mercurySheen {
  0%   { background-position: 0% 0%; }
  50%  { background-position: 100% 100%; }
  100% { background-position: 0% 0%; }
}
@keyframes mercurySpin {
  0%   { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* ==============================
   BTN 03 — BRUTALIST STAMP
   ============================== */
.btn-brutalist {
  position: relative;
  border: 4px solid #fff;
  background: transparent;
  padding: 18px 40px;
  font-family: 'Bebas Neue', sans-serif;
  font-size: 28px;
  letter-spacing: 0.08em;
  color: #fff;
  cursor: pointer;
  outline: none;
  transition: all 0.08s;
  box-shadow: 6px 6px 0 #fff;
  text-transform: uppercase;
}

.btn-brutalist:hover {
  background: #fff;
  color: #080a0f;
  transform: translate(-3px, -3px);
  box-shadow: 9px 9px 0 var(--accent2);
}

.btn-brutalist:active {
  transform: translate(6px, 6px);
  box-shadow: 0px 0px 0 #fff;
}

/* ==============================
   BTN 04 — NEON GLITCH
   ============================== */
.btn-glitch {
  position: relative;
  border: 2px solid var(--accent2);
  background: transparent;
  padding: 16px 40px;
  font-family: 'Space Mono', monospace;
  font-size: 13px;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--accent2);
  cursor: pointer;
  outline: none;
  overflow: hidden;
}

.btn-glitch::before,
.btn-glitch::after {
  content: attr(data-text);
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Space Mono', monospace;
  font-size: 13px;
  letter-spacing: 0.3em;
  text-transform: uppercase;
}

.btn-glitch::before {
  color: var(--accent1);
  clip-path: polygon(0 30%, 100% 30%, 100% 50%, 0 50%);
  transform: translateX(0);
  opacity: 0;
}

.btn-glitch::after {
  color: var(--accent4);
  clip-path: polygon(0 60%, 100% 60%, 100% 80%, 0 80%);
  transform: translateX(0);
  opacity: 0;
}

.btn-glitch:hover {
  color: #fff;
  border-color: #fff;
  text-shadow: 0 0 10px #fff;
  box-shadow:
    0 0 10px var(--accent2),
    inset 0 0 10px rgba(255,45,120,0.1);
}

.btn-glitch:hover::before {
  opacity: 1;
  animation: glitch1 0.4s steps(2) infinite;
}

.btn-glitch:hover::after {
  opacity: 1;
  animation: glitch2 0.4s steps(2) infinite 0.1s;
}

@keyframes glitch1 {
  0%   { transform: translateX(-4px); clip-path: polygon(0 25%, 100% 25%, 100% 45%, 0 45%); }
  50%  { transform: translateX(4px); clip-path: polygon(0 55%, 100% 55%, 100% 70%, 0 70%); }
  100% { transform: translateX(-2px); clip-path: polygon(0 10%, 100% 10%, 100% 35%, 0 35%); }
}
@keyframes glitch2 {
  0%   { transform: translateX(6px); }
  50%  { transform: translateX(-6px); }
  100% { transform: translateX(3px); }
}

/* ==============================
   BTN 05 — MORPHING BLOB
   ============================== */
.btn-blob {
  position: relative;
  border: none;
  background: none;
  cursor: pointer;
  outline: none;
  width: 200px;
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.btn-blob .blob-bg {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, var(--accent3), var(--accent2));
  border-radius: 60% 40% 70% 30% / 50% 60% 40% 50%;
  animation: blobMorph 4s ease-in-out infinite;
  transition: filter 0.3s;
}

.btn-blob:hover .blob-bg {
  filter: brightness(1.2);
  animation: blobMorphFast 1.5s ease-in-out infinite;
}

.btn-blob span {
  position: relative;
  z-index: 2;
  font-family: 'Syne', sans-serif;
  font-size: 13px;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #1a0a00;
  mix-blend-mode: multiply;
}

@keyframes blobMorph {
  0%   { border-radius: 60% 40% 70% 30% / 50% 60% 40% 50%; }
  25%  { border-radius: 40% 60% 30% 70% / 60% 30% 70% 40%; }
  50%  { border-radius: 70% 30% 40% 60% / 30% 70% 50% 60%; }
  75%  { border-radius: 30% 70% 60% 40% / 70% 40% 60% 30%; }
  100% { border-radius: 60% 40% 70% 30% / 50% 60% 40% 50%; }
}

@keyframes blobMorphFast {
  0%   { border-radius: 50% 50% 70% 30% / 50% 70% 30% 50%; transform: scale(1.05); }
  50%  { border-radius: 70% 30% 50% 50% / 30% 50% 70% 50%; transform: scale(0.97); }
  100% { border-radius: 50% 50% 70% 30% / 50% 70% 30% 50%; transform: scale(1.05); }
}

/* ==============================
   BTN 06 — EDITORIAL LUXURY
   ============================== */
.btn-luxury {
  position: relative;
  border: none;
  background: none;
  cursor: pointer;
  outline: none;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 0;
}

.btn-luxury .lux-text {
  font-family: 'DM Serif Display', serif;
  font-size: 22px;
  font-style: italic;
  color: var(--accent3);
  letter-spacing: 0.05em;
  position: relative;
  transition: transform 0.4s cubic-bezier(0.23, 1, 0.32, 1);
}

.btn-luxury .lux-sub {
  font-family: 'Cormorant Garamond', serif;
  font-size: 9px;
  font-weight: 300;
  letter-spacing: 0.5em;
  text-transform: uppercase;
  color: rgba(255,215,0,0.4);
  transition: letter-spacing 0.4s ease, color 0.3s;
}

.btn-luxury::before {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 1px;
  background: var(--accent3);
  transition: width 0.4s cubic-bezier(0.23, 1, 0.32, 1);
}

.btn-luxury::after {
  content: '—';
  position: absolute;
  top: -24px;
  font-family: 'Cormorant Garamond', serif;
  font-size: 14px;
  color: rgba(255,215,0,0.3);
  transition: opacity 0.3s, transform 0.3s;
  transform: scaleX(1);
  opacity: 0;
}

.btn-luxury:hover::before { width: 100%; }
.btn-luxury:hover .lux-text { transform: translateY(-4px); }
.btn-luxury:hover .lux-sub { letter-spacing: 0.7em; color: rgba(255,215,0,0.7); }
.btn-luxury:hover::after { opacity: 1; }

/* ==============================
   BTN 07 — PARTICLE BURST
   ============================== */
.btn-particle {
  position: relative;
  border: none;
  background: linear-gradient(135deg, #6d28d9, #4f46e5);
  border-radius: 50px;
  padding: 18px 48px;
  font-family: 'Syne', sans-serif;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: #fff;
  cursor: pointer;
  outline: none;
  overflow: visible;
  box-shadow: 0 0 0 0 rgba(109,40,217,0.5);
  transition: transform 0.2s, box-shadow 0.3s, background 0.3s;
}

.btn-particle:hover {
  transform: scale(1.05);
  background: linear-gradient(135deg, #7c3aed, #6366f1);
  box-shadow: 0 0 0 12px rgba(109,40,217,0);
  animation: particlePulse 0.6s ease-out forwards;
}

.btn-particle:active { transform: scale(0.96); }

@keyframes particlePulse {
  0%   { box-shadow: 0 0 0 0 rgba(109,40,217,0.6); }
  100% { box-shadow: 0 0 0 30px rgba(109,40,217,0); }
}

/* Particles */
.btn-particle .particles {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.particle {
  position: absolute;
  width: 5px;
  height: 5px;
  border-radius: 50%;
  top: 50%;
  left: 50%;
  opacity: 0;
  background: #c4b5fd;
}

.btn-particle:hover .particle { animation: particleFly 0.6s ease-out forwards; }

.particle:nth-child(1)  { animation-delay: 0.0s; --dx: -80px; --dy: -60px; }
.particle:nth-child(2)  { animation-delay: 0.05s; --dx: 80px; --dy: -60px; }
.particle:nth-child(3)  { animation-delay: 0.1s; --dx: 0px; --dy: -90px; }
.particle:nth-child(4)  { animation-delay: 0.05s; --dx: -90px; --dy: 0px; }
.particle:nth-child(5)  { animation-delay: 0.1s; --dx: 90px; --dy: 0px; }
.particle:nth-child(6)  { animation-delay: 0.0s; --dx: -60px; --dy: 80px; }
.particle:nth-child(7)  { animation-delay: 0.05s; --dx: 60px; --dy: 80px; }
.particle:nth-child(8)  { animation-delay: 0.15s; --dx: 0px; --dy: 90px; }

@keyframes particleFly {
  0%   { transform: translate(-50%, -50%) scale(1); opacity: 1; }
  100% { transform: translate(calc(-50% + var(--dx)), calc(-50% + var(--dy))) scale(0); opacity: 0; }
}

/* ==============================
   BTN 08 — THERMAL SCAN
   ============================== */
.btn-thermal {
  position: relative;
  border: 1px solid rgba(0,255,229,0.3);
  background: rgba(0,255,229,0.04);
  padding: 20px 50px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--accent1);
  cursor: pointer;
  outline: none;
  overflow: hidden;
  transition: color 0.3s, border-color 0.3s;
}

.btn-thermal .scan-line {
  position: absolute;
  top: 0;
  left: -100%;
  width: 60%;
  height: 100%;
  background: linear-gradient(90deg,
    transparent,
    rgba(0,255,229,0.08),
    rgba(0,255,229,0.25),
    rgba(0,255,229,0.08),
    transparent
  );
  transition: none;
}

.btn-thermal:hover .scan-line {
  animation: thermalScan 0.8s ease-out forwards;
}

.btn-thermal .corner {
  position: absolute;
  width: 10px;
  height: 10px;
  border-color: var(--accent1);
  border-style: solid;
  transition: width 0.3s, height 0.3s;
  opacity: 0.6;
}

.btn-thermal .corner.tl { top: -1px; left: -1px; border-width: 2px 0 0 2px; }
.btn-thermal .corner.tr { top: -1px; right: -1px; border-width: 2px 2px 0 0; }
.btn-thermal .corner.bl { bottom: -1px; left: -1px; border-width: 0 0 2px 2px; }
.btn-thermal .corner.br { bottom: -1px; right: -1px; border-width: 0 2px 2px 0; }

.btn-thermal:hover .corner { width: 16px; height: 16px; opacity: 1; }
.btn-thermal:hover {
  border-color: rgba(0,255,229,0.7);
  box-shadow: 0 0 20px rgba(0,255,229,0.2), inset 0 0 20px rgba(0,255,229,0.04);
}

@keyframes thermalScan {
  0%   { left: -100%; }
  100% { left: 150%; }
}

/* Status dot */
.btn-thermal .status {
  position: absolute;
  top: 8px;
  right: 10px;
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--accent1);
  box-shadow: 0 0 6px var(--accent1);
  animation: statusBlink 2s ease-in-out infinite;
}

@keyframes statusBlink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.2; }
}

/* ==============================
   BTN 09 — SPLIT REVEAL
   ============================== */
.btn-split {
  position: relative;
  border: none;
  background: none;
  cursor: pointer;
  outline: none;
  width: 220px;
  height: 60px;
  overflow: hidden;
}

.btn-split .split-bg {
  position: absolute;
  inset: 0;
  background: var(--accent2);
  clip-path: polygon(0 0, 0 0, 0 100%, 0 100%);
  transition: clip-path 0.4s cubic-bezier(0.86, 0, 0.07, 1);
}

.btn-split:hover .split-bg {
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
}

.btn-split .split-text-default {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Syne', sans-serif;
  font-size: 12px;
  font-weight: 800;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #fff;
  border: 2px solid rgba(255,255,255,0.2);
  transition: color 0.3s;
}

.btn-split .split-text-hover {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Syne', sans-serif;
  font-size: 12px;
  font-weight: 800;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #fff;
  transform: translateX(-110%);
  transition: transform 0.4s cubic-bezier(0.86, 0, 0.07, 1);
  z-index: 2;
}

.btn-split:hover .split-text-hover { transform: translateX(0); }
.btn-split:hover .split-text-default { color: transparent; }

/* Arrow */
.btn-split .arrow {
  position: absolute;
  right: 20px;
  top: 50%;
  transform: translateY(-50%) translateX(0);
  font-size: 16px;
  color: #fff;
  z-index: 3;
  opacity: 0;
  transition: opacity 0.3s 0.2s, transform 0.4s cubic-bezier(0.86, 0, 0.07, 1) 0.1s;
}

.btn-split:hover .arrow {
  opacity: 1;
  transform: translateY(-50%) translateX(0);
}

/* ==============================
   BTN 10 — TYPEWRITER TERMINAL
   ============================== */
.btn-terminal {
  position: relative;
  border: 1px solid rgba(255,255,255,0.15);
  background: #0d1117;
  padding: 18px 40px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  font-weight: 400;
  color: rgba(255,255,255,0.8);
  cursor: pointer;
  outline: none;
  transition: border-color 0.2s;
  min-width: 240px;
  text-align: left;
}

.btn-terminal::before {
  content: '> ';
  color: var(--accent1);
  font-weight: 700;
}

.btn-terminal .cursor-blink {
  display: inline-block;
  width: 8px;
  height: 14px;
  background: rgba(255,255,255,0.7);
  vertical-align: middle;
  margin-left: 2px;
  animation: cursorBlink 1s step-end infinite;
}

.btn-terminal .hidden-text {
  opacity: 0;
  transition: opacity 0.1s;
}

.btn-terminal:hover {
  border-color: rgba(255,255,255,0.4);
  box-shadow: 0 0 0 1px rgba(255,255,255,0.05);
}

.btn-terminal:hover .hidden-text {
  animation: typeReveal 0.4s steps(12) forwards;
}

@keyframes cursorBlink {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0; }
}

@keyframes typeReveal {
  from { opacity: 0; clip-path: inset(0 100% 0 0); }
  to   { opacity: 1; clip-path: inset(0 0% 0 0); }
}

/* ==============================
   BTN 11 — GLASS MORPHISM 3D
   ============================== */
.btn-glass {
  position: relative;
  border: none;
  background: linear-gradient(
    135deg,
    rgba(255,255,255,0.12) 0%,
    rgba(255,255,255,0.04) 100%
  );
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-radius: 16px;
  padding: 20px 52px;
  font-family: 'Syne', sans-serif;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #fff;
  cursor: pointer;
  outline: none;
  border: 1px solid rgba(255,255,255,0.15);
  box-shadow:
    0 8px 32px rgba(0,0,0,0.3),
    0 1px 0 rgba(255,255,255,0.2) inset,
    0 -1px 0 rgba(0,0,0,0.2) inset;
  transition: transform 0.3s cubic-bezier(0.23,1,0.32,1), box-shadow 0.3s;
  transform-style: preserve-3d;
}

.btn-glass::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 50%;
  background: linear-gradient(rgba(255,255,255,0.12), transparent);
  border-radius: 16px 16px 0 0;
  pointer-events: none;
}

.btn-glass .glass-icon {
  margin-right: 10px;
  font-size: 15px;
  filter: drop-shadow(0 0 6px rgba(255,255,255,0.5));
}

.btn-glass:hover {
  transform: translateY(-6px) rotateX(10deg);
  box-shadow:
    0 20px 60px rgba(0,0,0,0.5),
    0 1px 0 rgba(255,255,255,0.25) inset,
    0 -1px 0 rgba(0,0,0,0.3) inset;
}

.btn-glass:active {
  transform: translateY(-2px) rotateX(3deg);
}

/* ==============================
   BTN 12 — COUNTDOWN LOADER
   ============================== */
.btn-loader {
  position: relative;
  border: 2px solid rgba(255,45,120,0.4);
  background: transparent;
  border-radius: 6px;
  padding: 18px 48px;
  font-family: 'Unbounded', sans-serif;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent2);
  cursor: pointer;
  outline: none;
  overflow: hidden;
  transition: color 0.3s, border-color 0.3s;
  min-width: 220px;
}

.btn-loader .loader-progress {
  position: absolute;
  bottom: 0; left: 0;
  height: 3px;
  width: 0%;
  background: linear-gradient(90deg, var(--accent4), var(--accent2));
  transition: none;
  box-shadow: 0 0 8px var(--accent2);
}

.btn-loader.loading .loader-progress {
  animation: loadProgress 1.5s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}

.btn-loader.loading {
  color: rgba(255,45,120,0.5);
  pointer-events: none;
}

.btn-loader.loaded {
  color: #fff;
  border-color: var(--accent2);
  background: var(--accent2);
  animation: loadedFlash 0.3s ease forwards;
}

.btn-loader .loader-fill {
  position: absolute;
  inset: 0;
  background: var(--accent2);
  transform: scaleX(0);
  transform-origin: left;
  z-index: 0;
  transition: transform 0s;
}

.btn-loader span { position: relative; z-index: 1; }

.btn-loader .dots {
  display: none;
}

.btn-loader.loading .dots {
  display: inline;
  animation: dotCycle 1s steps(4) infinite;
}

.btn-loader.loading .btn-default-text {
  display: none;
}

.btn-loader .btn-loading-text { display: none; }
.btn-loader.loading .btn-loading-text { display: inline; }
.btn-loader.loaded .btn-loading-text { display: none; }
.btn-loader.loaded .btn-loaded-text { display: inline; }
.btn-loader .btn-loaded-text { display: none; }

@keyframes loadProgress {
  0%   { width: 0%; }
  80%  { width: 90%; }
  100% { width: 100%; }
}

@keyframes dotCycle {
  0%  { content: '.'; }
  25% { content: '..'; }
  50% { content: '...'; }
  75% { content: ''; }
}

@keyframes loadedFlash {
  0%   { filter: brightness(2); }
  100% { filter: brightness(1); }
}

/* ==============================
   FOOTER
   ============================== */
footer {
  position: relative;
  z-index: 10;
  text-align: center;
  padding: 60px 20px;
  font-size: 10px;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.1);
}
</style>
</head>
<body>

<header>
  <div class="label">// Design Lab — 2026</div>
  <h1>BUTTON<br><span>LABORATORY</span></h1>
  <p>12 DESIGNS · HOVER TO INTERACT</p>
</header>

<div class="grid">

  <!-- BTN 01 -->
  <div class="cell">
    <div class="cell-label">PLASMA GRADIENT</div>
    <button class="btn-plasma">
      <div class="plasma-bg"></div>
      <div class="plasma-inner"></div>
      <span>LAUNCH</span>
    </button>
    <div class="cell-number">01</div>
  </div>

  <!-- BTN 02 -->
  <div class="cell">
    <div class="cell-label">LIQUID MERCURY</div>
    <button class="btn-mercury">Explore Now</button>
    <div class="cell-number">02</div>
  </div>

  <!-- BTN 03 -->
  <div class="cell">
    <div class="cell-label">BRUTALIST STAMP</div>
    <button class="btn-brutalist">Submit</button>
    <div class="cell-number">03</div>
  </div>

  <!-- BTN 04 -->
  <div class="cell">
    <div class="cell-label">NEON GLITCH</div>
    <button class="btn-glitch" data-text="ACCESS">ACCESS</button>
    <div class="cell-number">04</div>
  </div>

  <!-- BTN 05 -->
  <div class="cell">
    <div class="cell-label">MORPHING BLOB</div>
    <button class="btn-blob">
      <div class="blob-bg"></div>
      <span>Discover</span>
    </button>
    <div class="cell-number">05</div>
  </div>

  <!-- BTN 06 -->
  <div class="cell">
    <div class="cell-label">EDITORIAL LUXURY</div>
    <button class="btn-luxury">
      <span class="lux-text">Réserver</span>
      <span class="lux-sub">Expérience exclusive</span>
    </button>
    <div class="cell-number">06</div>
  </div>

  <!-- BTN 07 -->
  <div class="cell">
    <div class="cell-label">PARTICLE BURST</div>
    <button class="btn-particle">
      Ignite
      <div class="particles">
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
      </div>
    </button>
    <div class="cell-number">07</div>
  </div>

  <!-- BTN 08 -->
  <div class="cell">
    <div class="cell-label">THERMAL SCAN</div>
    <button class="btn-thermal">
      <div class="scan-line"></div>
      <div class="corner tl"></div>
      <div class="corner tr"></div>
      <div class="corner bl"></div>
      <div class="corner br"></div>
      <div class="status"></div>
      ANALYSE
    </button>
    <div class="cell-number">08</div>
  </div>

  <!-- BTN 09 -->
  <div class="cell">
    <div class="cell-label">SPLIT REVEAL</div>
    <button class="btn-split">
      <div class="split-bg"></div>
      <div class="split-text-default">Continue</div>
      <div class="split-text-hover">Let's Go</div>
      <div class="arrow">→</div>
    </button>
    <div class="cell-number">09</div>
  </div>

  <!-- BTN 10 -->
  <div class="cell">
    <div class="cell-label">TYPEWRITER TERMINAL</div>
    <button class="btn-terminal" id="termBtn">
      <span class="btn-text">
        <span class="hidden-text">execute_command</span>
      </span>
      <span class="cursor-blink"></span>
    </button>
    <div class="cell-number">10</div>
  </div>

  <!-- BTN 11 -->
  <div class="cell" style="background: linear-gradient(135deg, rgba(109,40,217,0.08), rgba(79,70,229,0.04));">
    <div class="cell-label">GLASS 3D</div>
    <button class="btn-glass">
      <span class="glass-icon">✦</span>
      Open Portal
    </button>
    <div class="cell-number">11</div>
  </div>

  <!-- BTN 12 -->
  <div class="cell">
    <div class="cell-label">LOADER STATE</div>
    <button class="btn-loader" id="loaderBtn">
      <div class="loader-progress" id="loaderProgress"></div>
      <span>
        <span class="btn-default-text">Click to Load</span>
        <span class="btn-loading-text">Processing<span class="dots"></span></span>
        <span class="btn-loaded-text">✓ Complete</span>
      </span>
    </button>
    <div class="cell-number">12</div>
  </div>

</div>

<footer>Ultra Button Design Lab · Built with Pure CSS & JS · 2026</footer>

<script>
// Loader button interaction
const loaderBtn = document.getElementById('loaderBtn');
const loaderProgress = document.getElementById('loaderProgress');

loaderBtn.addEventListener('click', () => {
  if (loaderBtn.classList.contains('loading') || loaderBtn.classList.contains('loaded')) return;
  
  loaderBtn.classList.add('loading');
  loaderProgress.style.animation = 'loadProgress 1.5s cubic-bezier(0.4, 0, 0.2, 1) forwards';
  
  setTimeout(() => {
    loaderBtn.classList.remove('loading');
    loaderBtn.classList.add('loaded');
    loaderProgress.style.width = '100%';
    loaderProgress.style.animation = 'none';
    
    setTimeout(() => {
      loaderBtn.classList.remove('loaded');
      loaderProgress.style.width = '0%';
    }, 3000);
  }, 1800);
});

// Magnetic effect for btn-plasma
const plasmaBtn = document.querySelector('.btn-plasma');
plasmaBtn.addEventListener('mousemove', (e) => {
  const rect = plasmaBtn.getBoundingClientRect();
  const x = e.clientX - rect.left - rect.width / 2;
  const y = e.clientY - rect.top - rect.height / 2;
  plasmaBtn.style.transform = `translate(${x * 0.12}px, ${y * 0.12}px)`;
});
plasmaBtn.addEventListener('mouseleave', () => {
  plasmaBtn.style.transform = '';
});

// 3D tilt for glass button
const glassBtn = document.querySelector('.btn-glass');
glassBtn.addEventListener('mousemove', (e) => {
  const rect = glassBtn.getBoundingClientRect();
  const x = (e.clientX - rect.left) / rect.width - 0.5;
  const y = (e.clientY - rect.top) / rect.height - 0.5;
  glassBtn.style.transform = `translateY(-6px) rotateX(${-y * 20}deg) rotateY(${x * 20}deg)`;
});
glassBtn.addEventListener('mouseleave', () => {
  glassBtn.style.transform = '';
  glassBtn.style.transition = 'transform 0.5s cubic-bezier(0.23,1,0.32,1), box-shadow 0.3s';
});

// Terminal button typewriter
const termBtn = document.getElementById('termBtn');
const hiddenText = termBtn.querySelector('.hidden-text');
let typeInterval;

termBtn.addEventListener('mouseenter', () => {
  let i = 0;
  const text = 'execute_command';
  hiddenText.textContent = '';
  typeInterval = setInterval(() => {
    hiddenText.textContent = text.slice(0, ++i);
    if (i >= text.length) clearInterval(typeInterval);
  }, 30);
});

termBtn.addEventListener('mouseleave', () => {
  clearInterval(typeInterval);
  hiddenText.textContent = 'execute_command';
});
</script>
</body>
</html>
```


buttons compilation 2
```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ultra Button Lab — Vol.2</title>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700;900&family=Rajdhani:wght@300;500;700&family=Monoton&family=Major+Mono+Display&family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,900;1,9..144,300;1,9..144,700&family=Barlow+Condensed:wght@200;400;700;900&family=Teko:wght@300;400;600&family=Instrument+Serif:ital@0;1&family=Black+Han+Sans&family=Darker+Grotesque:wght@300;500;900&display=swap" rel="stylesheet">

<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --ink: #0c0c0e;
  --paper: #f5f0e8;
  --rust: #c94b2c;
  --sage: #7a9e7e;
  --gold: #c9a84c;
  --cobalt: #1a3a6b;
  --neon-lime: #b5ff2e;
  --deep-red: #8b0000;
  --silver: #c0c0c0;
  --void: #050507;
}

html { scroll-behavior: smooth; }

body {
  background: var(--ink);
  min-height: 100vh;
  overflow-x: hidden;
  cursor: none;
}

/* Custom cursor */
.cursor {
  position: fixed;
  width: 10px;
  height: 10px;
  background: #fff;
  border-radius: 50%;
  pointer-events: none;
  z-index: 9999;
  transform: translate(-50%, -50%);
  transition: transform 0.1s, width 0.2s, height 0.2s, background 0.2s;
  mix-blend-mode: difference;
}

.cursor-ring {
  position: fixed;
  width: 36px;
  height: 36px;
  border: 1px solid rgba(255,255,255,0.4);
  border-radius: 50%;
  pointer-events: none;
  z-index: 9998;
  transform: translate(-50%, -50%);
  transition: transform 0.15s ease-out, width 0.3s, height 0.3s;
}

/* Noise texture overlay */
body::after {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 1;
  opacity: 0.6;
}

header {
  position: relative;
  z-index: 10;
  padding: 80px 48px 40px;
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}

header .vol {
  font-family: 'Major Mono Display', monospace;
  font-size: 11px;
  color: rgba(255,255,255,0.25);
  letter-spacing: 0.2em;
}

header h1 {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: clamp(3rem, 8vw, 7rem);
  font-weight: 900;
  letter-spacing: -0.01em;
  line-height: 0.85;
  color: #fff;
  text-transform: uppercase;
}

header h1 em {
  font-style: normal;
  color: transparent;
  -webkit-text-stroke: 1px rgba(255,255,255,0.3);
}

header .meta {
  text-align: right;
  font-family: 'Rajdhani', sans-serif;
  font-size: 12px;
  font-weight: 300;
  color: rgba(255,255,255,0.2);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  line-height: 2;
}

.grid {
  position: relative;
  z-index: 10;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
  gap: 1px;
  background: rgba(255,255,255,0.04);
  margin: 1px;
}

.cell {
  position: relative;
  background: var(--ink);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 70px 48px;
  min-height: 300px;
  overflow: hidden;
  transition: background 0.4s;
}

.cell-tag {
  position: absolute;
  top: 0; left: 0;
  font-family: 'Rajdhani', monospace;
  font-size: 9px;
  font-weight: 500;
  letter-spacing: 0.4em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.15);
  padding: 14px 18px;
  border-right: 1px solid rgba(255,255,255,0.06);
  border-bottom: 1px solid rgba(255,255,255,0.06);
}

.cell-num {
  position: absolute;
  bottom: 14px;
  right: 18px;
  font-family: 'Major Mono Display', monospace;
  font-size: 9px;
  color: rgba(255,255,255,0.07);
  letter-spacing: 0.1em;
}


/* ============================================================
   BTN 13 — RETRO NIXIE TUBE
   ============================================================ */
.btn-nixie {
  position: relative;
  border: none;
  background: none;
  cursor: none;
  outline: none;
  padding: 22px 56px;
  font-family: 'Monoton', cursive;
  font-size: 18px;
  letter-spacing: 0.12em;
  color: #ff8c00;
  text-shadow:
    0 0 7px #ff8c00,
    0 0 15px #ff6a00,
    0 0 30px rgba(255,100,0,0.4);
  position: relative;
  border: 2px solid rgba(255,140,0,0.25);
  border-radius: 3px;
  transition: text-shadow 0.1s;
  animation: nixieFlicker 8s step-end infinite;
  overflow: hidden;
}

.btn-nixie::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse 80% 60% at 50% 50%,
    rgba(255,120,0,0.08) 0%, transparent 70%);
  pointer-events: none;
}

/* Glass reflection */
.btn-nixie::after {
  content: '';
  position: absolute;
  top: 0; left: 10%; right: 10%;
  height: 40%;
  background: linear-gradient(rgba(255,200,100,0.12), transparent);
  border-radius: 0 0 50% 50%;
  pointer-events: none;
}

.btn-nixie .nixie-bg {
  position: absolute;
  inset: -1px;
  border: 1px solid rgba(255,140,0,0.15);
  border-radius: 4px;
  background: radial-gradient(ellipse at 50% 50%, rgba(60,30,0,0.9), rgba(20,10,0,0.95));
  z-index: -1;
}

.btn-nixie:hover {
  text-shadow:
    0 0 10px #ffaa00,
    0 0 25px #ff8800,
    0 0 50px rgba(255,140,0,0.6),
    0 0 80px rgba(255,100,0,0.3);
  border-color: rgba(255,140,0,0.6);
  animation: none;
}

@keyframes nixieFlicker {
  0%, 95%, 100% { opacity: 1; }
  96% { opacity: 0.7; }
  97% { opacity: 1; }
  98% { opacity: 0.4; }
  99% { opacity: 0.9; }
}


/* ============================================================
   BTN 14 — WASHI TAPE / JAPANESE CRAFT
   ============================================================ */
.cell-washi {
  background: #faf6ef;
}

.btn-washi {
  position: relative;
  border: none;
  background: none;
  cursor: none;
  outline: none;
  padding: 0;
  width: 220px;
}

.btn-washi .washi-tape {
  position: absolute;
  top: -8px; left: 50%;
  transform: translateX(-50%) rotate(-1deg);
  width: 70%;
  height: 28px;
  background: repeating-linear-gradient(
    90deg,
    rgba(201,72,44,0.7) 0px,
    rgba(201,72,44,0.7) 6px,
    rgba(255,255,255,0.5) 6px,
    rgba(255,255,255,0.5) 12px
  );
  opacity: 0.85;
  transition: transform 0.3s, height 0.3s;
  z-index: 2;
}

.btn-washi .washi-body {
  background: #fff;
  border: 1px solid rgba(0,0,0,0.12);
  padding: 20px 32px 18px;
  font-family: 'Instrument Serif', serif;
  font-size: 17px;
  font-style: italic;
  color: #2a1f14;
  letter-spacing: 0.03em;
  text-align: center;
  position: relative;
  z-index: 1;
  transition: transform 0.3s cubic-bezier(0.23,1,0.32,1), box-shadow 0.3s;
  box-shadow: 2px 3px 12px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.05);
}

.btn-washi .washi-bottom {
  position: absolute;
  bottom: -8px; left: 50%;
  transform: translateX(-50%) rotate(0.5deg);
  width: 40%;
  height: 18px;
  background: rgba(122,158,126,0.6);
  z-index: 2;
}

.btn-washi:hover .washi-tape {
  transform: translateX(-50%) rotate(-3deg) translateY(-3px);
}
.btn-washi:hover .washi-body {
  transform: rotate(1deg) translateY(-4px);
  box-shadow: 4px 8px 24px rgba(0,0,0,0.15);
}


/* ============================================================
   BTN 15 — SWISS MODERNIST (LIGHT CELL)
   ============================================================ */
.cell-swiss {
  background: #f0ede6;
}

.btn-swiss {
  position: relative;
  border: none;
  background: none;
  cursor: none;
  outline: none;
  display: flex;
  align-items: stretch;
  gap: 0;
  font-family: 'Barlow Condensed', sans-serif;
  text-transform: uppercase;
  overflow: hidden;
}

.btn-swiss .sw-number {
  background: #1a1a1a;
  color: #f0ede6;
  font-size: 11px;
  font-weight: 200;
  letter-spacing: 0.2em;
  padding: 18px 14px;
  writing-mode: vertical-rl;
  transform: rotate(180deg);
  display: flex;
  align-items: center;
  transition: background 0.3s;
}

.btn-swiss .sw-main {
  background: var(--rust);
  color: #fff;
  font-size: 24px;
  font-weight: 900;
  letter-spacing: 0.05em;
  padding: 18px 36px;
  position: relative;
  overflow: hidden;
  transition: padding 0.3s cubic-bezier(0.23,1,0.32,1);
}

.btn-swiss .sw-main::after {
  content: '';
  position: absolute;
  left: 0; top: 0; bottom: 0;
  width: 3px;
  background: #fff;
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.3s;
}

.btn-swiss .sw-arrow {
  background: #1a1a1a;
  color: #f0ede6;
  font-size: 20px;
  padding: 18px 18px;
  display: flex;
  align-items: center;
  transform: translateX(0);
  transition: transform 0.3s cubic-bezier(0.23,1,0.32,1), background 0.3s;
}

.btn-swiss:hover .sw-arrow {
  background: var(--rust);
  transform: translateX(6px);
}
.btn-swiss:hover .sw-main {
  padding-left: 44px;
}
.btn-swiss:hover .sw-main::after {
  transform: scaleX(1);
}
.btn-swiss:hover .sw-number {
  background: #333;
}


/* ============================================================
   BTN 16 — AURORA BOREALIS
   ============================================================ */
.btn-aurora {
  position: relative;
  border: none;
  background: transparent;
  cursor: none;
  outline: none;
  padding: 20px 52px;
  border-radius: 100px;
  font-family: 'Fraunces', serif;
  font-size: 16px;
  font-weight: 300;
  font-style: italic;
  letter-spacing: 0.08em;
  color: #fff;
  overflow: hidden;
  transition: transform 0.3s;
}

.btn-aurora .aurora-bg {
  position: absolute;
  inset: 0;
  background: linear-gradient(120deg, #0d4f3c, #1a6b5a, #2d9b7f, #1a3a6b, #2d1a6b);
  background-size: 400% 400%;
  animation: auroraFlow 6s ease infinite;
  border-radius: 100px;
  transition: filter 0.3s;
}

.btn-aurora .aurora-shimmer {
  position: absolute;
  inset: 0;
  border-radius: 100px;
  background: linear-gradient(
    120deg,
    transparent 20%,
    rgba(120,255,200,0.15) 40%,
    rgba(60,200,255,0.1) 50%,
    transparent 70%
  );
  background-size: 200% 100%;
  animation: auroraShimmer 3s ease-in-out infinite;
}

.btn-aurora .aurora-border {
  position: absolute;
  inset: 0;
  border-radius: 100px;
  border: 1px solid rgba(100,255,200,0.25);
  box-shadow:
    0 0 15px rgba(45,155,127,0.3),
    0 0 40px rgba(45,155,127,0.1),
    inset 0 1px 0 rgba(255,255,255,0.15);
}

.btn-aurora span {
  position: relative;
  z-index: 2;
  text-shadow: 0 0 20px rgba(120,255,200,0.4);
}

.btn-aurora:hover {
  transform: scale(1.04);
}
.btn-aurora:hover .aurora-bg {
  filter: brightness(1.3) saturate(1.4);
  animation-duration: 2s;
}

@keyframes auroraFlow {
  0%   { background-position: 0% 50%; }
  50%  { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
@keyframes auroraShimmer {
  0%   { background-position: -100% 0; }
  100% { background-position: 300% 0; }
}


/* ============================================================
   BTN 17 — NEWSPAPER CUT-OUT
   ============================================================ */
.cell-newspaper {
  background: #e8e0d0;
  background-image:
    repeating-linear-gradient(
      0deg, transparent, transparent 28px,
      rgba(0,0,0,0.04) 28px, rgba(0,0,0,0.04) 29px
    );
}

.btn-newspaper {
  position: relative;
  border: none;
  background: none;
  cursor: none;
  outline: none;
  display: flex;
  align-items: center;
  gap: 0;
  transform: rotate(-1.5deg);
  transition: transform 0.2s;
}

.btn-newspaper:hover { transform: rotate(0.5deg) scale(1.03); }

.btn-newspaper .np-word {
  font-family: 'Cinzel', serif;
  font-weight: 900;
  text-transform: uppercase;
  padding: 6px 14px;
  display: inline-block;
  line-height: 1;
  position: relative;
}

.btn-newspaper .np-word:nth-child(1) {
  font-size: 38px;
  background: #1a1a1a;
  color: #e8e0d0;
  letter-spacing: -0.02em;
}

.btn-newspaper .np-word:nth-child(2) {
  font-size: 16px;
  background: var(--rust);
  color: #fff;
  letter-spacing: 0.15em;
  align-self: flex-end;
  transform: translateY(-4px);
}

.btn-newspaper .np-word:nth-child(3) {
  font-size: 26px;
  background: #2a2a2a;
  color: #e8e0d0;
  letter-spacing: 0.02em;
  transform: translateY(2px);
  font-style: italic;
}

.btn-newspaper .np-scissor {
  position: absolute;
  top: -16px; right: -16px;
  font-size: 18px;
  transform: rotate(45deg);
  opacity: 0;
  transition: opacity 0.3s;
}

.btn-newspaper:hover .np-scissor { opacity: 1; }


/* ============================================================
   BTN 18 — CIRCUIT BOARD TRACE
   ============================================================ */
.cell-circuit {
  background: #0a1a0a;
}

.btn-circuit {
  position: relative;
  border: none;
  background: none;
  cursor: none;
  outline: none;
  padding: 22px 52px;
  font-family: 'Rajdhani', sans-serif;
  font-size: 14px;
  font-weight: 700;
  letter-spacing: 0.35em;
  text-transform: uppercase;
  color: var(--neon-lime);
  overflow: visible;
}

/* PCB border drawn with SVG-like box-shadow trick */
.btn-circuit::before {
  content: '';
  position: absolute;
  inset: 0;
  border: 1px solid rgba(181,255,46,0.2);
  clip-path: polygon(
    0 10px, 10px 0,
    calc(100% - 10px) 0, 100% 10px,
    100% calc(100% - 10px), calc(100% - 10px) 100%,
    10px 100%, 0 calc(100% - 10px)
  );
  transition: border-color 0.3s;
}

/* Trace lines */
.btn-circuit .trace {
  position: absolute;
  background: var(--neon-lime);
  opacity: 0;
  transition: opacity 0.3s;
}

.btn-circuit .trace.t1 {
  top: -12px; left: 20%;
  width: 1px; height: 12px;
}
.btn-circuit .trace.t2 {
  bottom: -12px; right: 30%;
  width: 1px; height: 12px;
}
.btn-circuit .trace.t3 {
  left: -14px; top: 30%;
  width: 14px; height: 1px;
}
.btn-circuit .trace.t4 {
  right: -14px; bottom: 30%;
  width: 14px; height: 1px;
}

/* Via dots */
.btn-circuit .via {
  position: absolute;
  width: 7px; height: 7px;
  border-radius: 50%;
  border: 1px solid var(--neon-lime);
  opacity: 0;
  transition: opacity 0.3s;
}
.btn-circuit .via.v1 { top: -18px; left: calc(20% - 3px); }
.btn-circuit .via.v2 { bottom: -18px; right: calc(30% - 3px); }
.btn-circuit .via.v3 { left: -21px; top: calc(30% - 3px); }
.btn-circuit .via.v4 { right: -21px; bottom: calc(30% - 3px); }

.btn-circuit:hover::before { border-color: rgba(181,255,46,0.6); }
.btn-circuit:hover {
  text-shadow: 0 0 12px var(--neon-lime), 0 0 30px rgba(181,255,46,0.4);
}
.btn-circuit:hover .trace,
.btn-circuit:hover .via { opacity: 1; }
.btn-circuit:hover .via {
  box-shadow: 0 0 6px var(--neon-lime);
  animation: viaPulse 1s ease-in-out infinite;
}

@keyframes viaPulse {
  0%, 100% { box-shadow: 0 0 4px var(--neon-lime); }
  50%       { box-shadow: 0 0 12px var(--neon-lime), 0 0 20px rgba(181,255,46,0.3); }
}


/* ============================================================
   BTN 19 — VELVET DRAPE
   ============================================================ */
.cell-velvet {
  background: #1a0a1e;
  background-image: radial-gradient(ellipse at 50% 0%, rgba(120,0,180,0.15), transparent 70%);
}

.btn-velvet {
  position: relative;
  border: none;
  cursor: none;
  outline: none;
  width: 240px;
  height: 70px;
  background: linear-gradient(180deg, #3d0a4f 0%, #2a0838 50%, #1d0528 100%);
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 2px;
  box-shadow:
    0 4px 16px rgba(100,0,150,0.3),
    0 1px 0 rgba(200,150,255,0.15) inset,
    0 -1px 0 rgba(0,0,0,0.5) inset;
}

.btn-velvet .velvet-sheen {
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 50%;
  background: linear-gradient(
    180deg,
    rgba(200,150,255,0.07) 0%,
    transparent 100%
  );
  pointer-events: none;
}

.btn-velvet .velvet-text {
  font-family: 'Cinzel', serif;
  font-size: 14px;
  font-weight: 400;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: rgba(220,180,255,0.9);
  position: relative;
  z-index: 2;
  transition: letter-spacing 0.5s cubic-bezier(0.23,1,0.32,1), color 0.3s;
  text-shadow: 0 0 20px rgba(200,100,255,0.3);
}

.btn-velvet .velvet-ripple {
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse 120% 80% at 50% 120%,
    rgba(160,80,255,0.2) 0%, transparent 70%);
  transform: translateY(100%);
  transition: transform 0.5s cubic-bezier(0.23,1,0.32,1);
}

.btn-velvet:hover .velvet-ripple { transform: translateY(0); }
.btn-velvet:hover .velvet-text {
  letter-spacing: 0.4em;
  color: rgba(240,210,255,1);
  text-shadow: 0 0 30px rgba(200,120,255,0.5);
}
.btn-velvet:hover {
  box-shadow:
    0 8px 32px rgba(150,0,220,0.4),
    0 1px 0 rgba(200,150,255,0.2) inset,
    0 -1px 0 rgba(0,0,0,0.5) inset;
}


/* ============================================================
   BTN 20 — MAGNETIC STRIPES (CREDIT CARD)
   ============================================================ */
.btn-card {
  position: relative;
  border: none;
  cursor: none;
  outline: none;
  width: 280px;
  height: 80px;
  border-radius: 8px;
  background: linear-gradient(135deg, #1c1c1c 0%, #2e2e2e 40%, #1a1a1a 100%);
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  box-shadow:
    0 4px 24px rgba(0,0,0,0.6),
    0 1px 0 rgba(255,255,255,0.1) inset;
  transition: transform 0.3s cubic-bezier(0.23,1,0.32,1), box-shadow 0.3s;
  transform-style: preserve-3d;
}

/* Magnetic stripe */
.btn-card::before {
  content: '';
  position: absolute;
  top: 18px; left: 0; right: 0;
  height: 28px;
  background: repeating-linear-gradient(
    90deg,
    #1a0000 0px, #330000 2px,
    #1a0000 4px, #2a0000 6px
  );
  opacity: 0.9;
  transition: opacity 0.3s;
}

/* Gold chip */
.btn-card .card-chip {
  width: 36px;
  height: 26px;
  background: linear-gradient(135deg, #c9a84c, #f0d080, #a87c30, #e0b84a);
  border-radius: 4px;
  position: relative;
  z-index: 2;
  flex-shrink: 0;
  box-shadow: 0 1px 4px rgba(0,0,0,0.4), 0 0 0 1px rgba(200,160,60,0.3);
}
.btn-card .card-chip::before {
  content: '';
  position: absolute;
  inset: 4px;
  border: 1px solid rgba(0,0,0,0.25);
  border-radius: 2px;
}
.btn-card .card-chip::after {
  content: '';
  position: absolute;
  top: 50%; left: 0; right: 0;
  height: 1px;
  background: rgba(0,0,0,0.2);
  transform: translateY(-50%);
}

.btn-card .card-text {
  font-family: 'Darker Grotesque', sans-serif;
  font-size: 13px;
  font-weight: 900;
  letter-spacing: 0.15em;
  color: rgba(255,255,255,0.85);
  text-transform: uppercase;
  position: relative;
  z-index: 2;
}

.btn-card .card-logo {
  display: flex;
  position: relative;
  z-index: 2;
}
.btn-card .card-logo span {
  width: 22px;
  height: 22px;
  border-radius: 50%;
}
.btn-card .card-logo span:first-child {
  background: rgba(220,40,40,0.8);
  margin-right: -8px;
}
.btn-card .card-logo span:last-child {
  background: rgba(220,120,40,0.7);
}

.btn-card:hover {
  transform: perspective(600px) rotateY(-8deg) rotateX(4deg) translateY(-4px);
  box-shadow:
    12px 16px 40px rgba(0,0,0,0.7),
    0 1px 0 rgba(255,255,255,0.15) inset;
}


/* ============================================================
   BTN 21 — INK WASH / SUMI-E
   ============================================================ */
.cell-ink {
  background: #fafaf8;
}

.btn-ink {
  position: relative;
  border: none;
  background: none;
  cursor: none;
  outline: none;
  padding: 18px 44px;
  font-family: 'Fraunces', serif;
  font-size: 20px;
  font-weight: 900;
  color: #1a1a1a;
  letter-spacing: 0.02em;
  overflow: visible;
}

.btn-ink .ink-blob {
  position: absolute;
  inset: 0;
  background: #1a1a1a;
  border-radius: 48% 52% 60% 40% / 50% 45% 55% 50%;
  transform: scale(0);
  transform-origin: center;
  transition: transform 0.6s cubic-bezier(0.34, 1.56, 0.64, 1),
              border-radius 0.6s ease;
  z-index: 0;
}

.btn-ink span {
  position: relative;
  z-index: 1;
  transition: color 0.3s 0.15s;
}

.btn-ink:hover .ink-blob {
  transform: scale(1.15);
  border-radius: 52% 48% 40% 60% / 45% 55% 45% 55%;
}

.btn-ink:hover span { color: #fafaf8; }

/* Ink drip */
.btn-ink .ink-drip {
  position: absolute;
  bottom: 0;
  left: 30%;
  width: 4px;
  height: 0;
  background: #1a1a1a;
  border-radius: 0 0 50% 50%;
  transform-origin: top;
  transition: height 0.3s 0.2s cubic-bezier(0.23, 1, 0.32, 1);
  z-index: 2;
}

.btn-ink:hover .ink-drip {
  height: 12px;
}


/* ============================================================
   BTN 22 — HOLOGRAPHIC FOIL
   ============================================================ */
.cell-holo {
  background: #050505;
}

.btn-holo {
  position: relative;
  border: none;
  cursor: none;
  outline: none;
  width: 250px;
  height: 72px;
  border-radius: 4px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Black Han Sans', sans-serif;
  font-size: 16px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #fff;
  mix-blend-mode: normal;
}

.btn-holo .holo-base {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    135deg,
    #ff0080, #ff8c00, #ffd700, #00ff80,
    #00bfff, #8000ff, #ff0080
  );
  background-size: 400% 400%;
  animation: holoShift 4s ease infinite;
  filter: saturate(1.2) brightness(0.9);
}

.btn-holo .holo-overlay {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
    45deg,
    transparent 0px,
    rgba(255,255,255,0.04) 1px,
    transparent 2px,
    transparent 8px
  );
  mix-blend-mode: overlay;
}

.btn-holo .holo-shine {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    110deg,
    transparent 20%,
    rgba(255,255,255,0.35) 50%,
    transparent 80%
  );
  background-size: 200% 100%;
  animation: holoSwipe 2s ease-in-out infinite;
}

.btn-holo .holo-darken {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0.45);
  transition: background 0.3s;
}

.btn-holo span {
  position: relative;
  z-index: 5;
  mix-blend-mode: normal;
  text-shadow: 0 1px 3px rgba(0,0,0,0.5);
}

.btn-holo:hover .holo-darken { background: rgba(0,0,0,0.2); }
.btn-holo:hover .holo-base { animation-duration: 1.5s; }
.btn-holo:hover { transform: scale(1.03); }

@keyframes holoShift {
  0%   { background-position: 0% 50%; }
  50%  { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
@keyframes holoSwipe {
  0%   { background-position: -200% 0; }
  100% { background-position: 400% 0; }
}


/* ============================================================
   FOOTER
   ============================================================ */
footer {
  position: relative;
  z-index: 10;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 32px 48px;
  border-top: 1px solid rgba(255,255,255,0.05);
  font-family: 'Rajdhani', sans-serif;
  font-size: 11px;
  font-weight: 300;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: rgba(255,255,255,0.1);
  margin-top: 1px;
}

.footer-ticker {
  display: flex;
  gap: 40px;
}
.footer-ticker span {
  position: relative;
}
.footer-ticker span::before {
  content: '◆';
  margin-right: 10px;
  font-size: 6px;
  vertical-align: middle;
}
</style>
</head>
<body>

<div class="cursor" id="cursor"></div>
<div class="cursor-ring" id="cursorRing"></div>

<header>
  <div>
    <div class="vol">vol.02 / 2026</div>
    <h1>NEW<br><em>FORMS</em></h1>
  </div>
  <div class="meta">
    <div>10 designs uniques</div>
    <div>Hover to interact</div>
    <div>Pure CSS + JS</div>
  </div>
</header>

<div class="grid">

  <!-- BTN 13 — NIXIE -->
  <div class="cell cell-nixie">
    <div class="cell-tag">Nixie Tube</div>
    <button class="btn-nixie">
      <div class="nixie-bg"></div>
      POWER ON
    </button>
    <div class="cell-num">13</div>
  </div>

  <!-- BTN 14 — WASHI -->
  <div class="cell cell-washi">
    <div class="cell-tag" style="color:rgba(0,0,0,0.2); border-color:rgba(0,0,0,0.06)">Washi Tape</div>
    <button class="btn-washi">
      <div class="washi-tape"></div>
      <div class="washi-body">À bientôt</div>
      <div class="washi-bottom"></div>
      <span class="np-scissor">✂</span>
    </button>
    <div class="cell-num" style="color:rgba(0,0,0,0.07)">14</div>
  </div>

  <!-- BTN 15 — SWISS -->
  <div class="cell cell-swiss">
    <div class="cell-tag" style="color:rgba(0,0,0,0.2); border-color:rgba(0,0,0,0.06)">Swiss Design</div>
    <button class="btn-swiss">
      <div class="sw-number">VOL. I</div>
      <div class="sw-main">EXECUTE</div>
      <div class="sw-arrow">→</div>
    </button>
    <div class="cell-num" style="color:rgba(0,0,0,0.07)">15</div>
  </div>

  <!-- BTN 16 — AURORA -->
  <div class="cell">
    <div class="cell-tag">Aurora</div>
    <button class="btn-aurora">
      <div class="aurora-bg"></div>
      <div class="aurora-shimmer"></div>
      <div class="aurora-border"></div>
      <span>Explore</span>
    </button>
    <div class="cell-num">16</div>
  </div>

  <!-- BTN 17 — NEWSPAPER -->
  <div class="cell cell-newspaper">
    <div class="cell-tag" style="color:rgba(0,0,0,0.2); border-color:rgba(0,0,0,0.06)">Cut-Out</div>
    <button class="btn-newspaper">
      <span class="np-word">CLICK</span>
      <span class="np-word">the</span>
      <span class="np-word">Button</span>
      <span class="np-scissor">✂</span>
    </button>
    <div class="cell-num" style="color:rgba(0,0,0,0.07)">17</div>
  </div>

  <!-- BTN 18 — CIRCUIT -->
  <div class="cell cell-circuit">
    <div class="cell-tag" style="color:rgba(181,255,46,0.2)">Circuit Trace</div>
    <button class="btn-circuit">
      <div class="trace t1"></div>
      <div class="trace t2"></div>
      <div class="trace t3"></div>
      <div class="trace t4"></div>
      <div class="via v1"></div>
      <div class="via v2"></div>
      <div class="via v3"></div>
      <div class="via v4"></div>
      SIGNAL
    </button>
    <div class="cell-num">18</div>
  </div>

  <!-- BTN 19 — VELVET -->
  <div class="cell cell-velvet">
    <div class="cell-tag" style="color:rgba(200,150,255,0.2)">Velvet Drape</div>
    <button class="btn-velvet">
      <div class="velvet-sheen"></div>
      <div class="velvet-ripple"></div>
      <span class="velvet-text">Entrez</span>
    </button>
    <div class="cell-num">19</div>
  </div>

  <!-- BTN 20 — CARD -->
  <div class="cell">
    <div class="cell-tag">Credit Card</div>
    <button class="btn-card">
      <div class="card-chip"></div>
      <span class="card-text">Pay Now</span>
      <div class="card-logo">
        <span></span>
        <span></span>
      </div>
    </button>
    <div class="cell-num">20</div>
  </div>

  <!-- BTN 21 — INK -->
  <div class="cell cell-ink">
    <div class="cell-tag" style="color:rgba(0,0,0,0.2); border-color:rgba(0,0,0,0.06)">Sumi-e Ink</div>
    <button class="btn-ink">
      <div class="ink-blob"></div>
      <div class="ink-drip"></div>
      <span>Révéler</span>
    </button>
    <div class="cell-num" style="color:rgba(0,0,0,0.07)">21</div>
  </div>

  <!-- BTN 22 — HOLO -->
  <div class="cell cell-holo">
    <div class="cell-tag">Holographic</div>
    <button class="btn-holo">
      <div class="holo-base"></div>
      <div class="holo-overlay"></div>
      <div class="holo-shine"></div>
      <div class="holo-darken"></div>
      <span>PRISMATIC</span>
    </button>
    <div class="cell-num">22</div>
  </div>

</div>

<footer>
  <div>Button Lab — Vol. 02</div>
  <div class="footer-ticker">
    <span>10 New Designs</span>
    <span>Pure CSS + JS</span>
    <span>2026</span>
  </div>
</footer>

<script>
// ─── Custom cursor
const cursor = document.getElementById('cursor');
const ring = document.getElementById('cursorRing');
let mx = 0, my = 0, rx = 0, ry = 0;

document.addEventListener('mousemove', e => {
  mx = e.clientX; my = e.clientY;
  cursor.style.left = mx + 'px';
  cursor.style.top  = my + 'px';
});

(function animateRing() {
  rx += (mx - rx) * 0.12;
  ry += (my - ry) * 0.12;
  ring.style.left = rx + 'px';
  ring.style.top  = ry + 'px';
  requestAnimationFrame(animateRing);
})();

// Ring scale on hover buttons
document.querySelectorAll('button').forEach(btn => {
  btn.addEventListener('mouseenter', () => {
    cursor.style.transform = 'translate(-50%,-50%) scale(2.5)';
    ring.style.width = '60px';
    ring.style.height = '60px';
    ring.style.borderColor = 'rgba(255,255,255,0.6)';
  });
  btn.addEventListener('mouseleave', () => {
    cursor.style.transform = 'translate(-50%,-50%) scale(1)';
    ring.style.width = '36px';
    ring.style.height = '36px';
    ring.style.borderColor = 'rgba(255,255,255,0.4)';
  });
});

// ─── 3D tilt for credit card
const card = document.querySelector('.btn-card');
card.addEventListener('mousemove', e => {
  const r = card.getBoundingClientRect();
  const x = (e.clientX - r.left) / r.width  - 0.5;
  const y = (e.clientY - r.top)  / r.height - 0.5;
  card.style.transform = `perspective(500px) rotateY(${x * 18}deg) rotateX(${-y * 12}deg) translateY(-4px)`;
});
card.addEventListener('mouseleave', () => {
  card.style.transition = 'transform 0.5s cubic-bezier(0.23,1,0.32,1), box-shadow 0.3s';
  card.style.transform = '';
  setTimeout(() => card.style.transition = '', 500);
});

// ─── Holographic mouse parallax
const holo = document.querySelector('.btn-holo');
holo.addEventListener('mousemove', e => {
  const r = holo.getBoundingClientRect();
  const x = (e.clientX - r.left) / r.width;
  const y = (e.clientY - r.top)  / r.height;
  holo.querySelector('.holo-base').style.backgroundPosition = `${x * 100}% ${y * 100}%`;
  holo.querySelector('.holo-shine').style.backgroundPosition = `${x * 200 - 50}% 0`;
  holo.style.transform = `scale(1.03) rotateY(${(x - 0.5) * 15}deg) rotateX(${(0.5 - y) * 10}deg)`;
});
holo.addEventListener('mouseleave', () => {
  holo.style.transform = '';
});

// ─── Magnetic effect on Aurora
const aurora = document.querySelector('.btn-aurora');
aurora.addEventListener('mousemove', e => {
  const r = aurora.getBoundingClientRect();
  const dx = (e.clientX - r.left - r.width  / 2) * 0.18;
  const dy = (e.clientY - r.top  - r.height / 2) * 0.18;
  aurora.style.transform = `scale(1.04) translate(${dx}px, ${dy}px)`;
});
aurora.addEventListener('mouseleave', () => {
  aurora.style.transform = '';
  aurora.style.transition = 'transform 0.6s cubic-bezier(0.23,1,0.32,1)';
  setTimeout(() => aurora.style.transition = '', 600);
});

// ─── Nixie click flash
document.querySelector('.btn-nixie').addEventListener('click', function() {
  this.style.animation = 'none';
  this.style.opacity = '0.2';
  setTimeout(() => {
    this.style.opacity = '1';
    this.style.animation = '';
  }, 80);
});

// ─── Circuit board ripple click
document.querySelector('.btn-circuit').addEventListener('click', function(e) {
  const r = this.getBoundingClientRect();
  const ripple = document.createElement('span');
  ripple.style.cssText = `
    position:absolute;
    left:${e.clientX - r.left}px;
    top:${e.clientY - r.top}px;
    width:4px; height:4px;
    background: var(--neon-lime);
    border-radius:50%;
    transform:translate(-50%,-50%) scale(0);
    animation: circuitRipple 0.6s ease-out forwards;
    pointer-events:none;
    z-index:10;
    box-shadow: 0 0 10px var(--neon-lime);
  `;
  this.appendChild(ripple);
  setTimeout(() => ripple.remove(), 600);
});

// Add keyframe for circuit ripple
const style = document.createElement('style');
style.textContent = `@keyframes circuitRipple {
  0%   { transform: translate(-50%,-50%) scale(0); opacity:1; }
  100% { transform: translate(-50%,-50%) scale(40); opacity:0; }
}`;
document.head.appendChild(style);
</script>
</body>
</html>
```

Algorithmic art
```md
---
name: algorithmic-art
description: Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic art, flow fields, or particle systems. Create original algorithmic art rather than copying existing artists' work to avoid copyright violations.
license: Complete terms in LICENSE.txt
---

Algorithmic philosophies are computational aesthetic movements that are then expressed through code. Output .md files (philosophy), .html files (interactive viewer), and .js files (generative algorithms).

This happens in two steps:
1. Algorithmic Philosophy Creation (.md file)
2. Express by creating p5.js generative art (.html + .js files)

First, undertake this task:

## ALGORITHMIC PHILOSOPHY CREATION

To begin, create an ALGORITHMIC PHILOSOPHY (not static images or templates) that will be interpreted through:
- Computational processes, emergent behavior, mathematical beauty
- Seeded randomness, noise fields, organic systems
- Particles, flows, fields, forces
- Parametric variation and controlled chaos

### THE CRITICAL UNDERSTANDING
- What is received: Some subtle input or instructions by the user to take into account, but use as a foundation; it should not constrain creative freedom.
- What is created: An algorithmic philosophy/generative aesthetic movement.
- What happens next: The same version receives the philosophy and EXPRESSES IT IN CODE - creating p5.js sketches that are 90% algorithmic generation, 10% essential parameters.

Consider this approach:
- Write a manifesto for a generative art movement
- The next phase involves writing the algorithm that brings it to life

The philosophy must emphasize: Algorithmic expression. Emergent behavior. Computational beauty. Seeded variation.

### HOW TO GENERATE AN ALGORITHMIC PHILOSOPHY

**Name the movement** (1-2 words): "Organic Turbulence" / "Quantum Harmonics" / "Emergent Stillness"

**Articulate the philosophy** (4-6 paragraphs - concise but complete):

To capture the ALGORITHMIC essence, express how this philosophy manifests through:
- Computational processes and mathematical relationships?
- Noise functions and randomness patterns?
- Particle behaviors and field dynamics?
- Temporal evolution and system states?
- Parametric variation and emergent complexity?

**CRITICAL GUIDELINES:**
- **Avoid redundancy**: Each algorithmic aspect should be mentioned once. Avoid repeating concepts about noise theory, particle dynamics, or mathematical principles unless adding new depth.
- **Emphasize craftsmanship REPEATEDLY**: The philosophy MUST stress multiple times that the final algorithm should appear as though it took countless hours to develop, was refined with care, and comes from someone at the absolute top of their field. This framing is essential - repeat phrases like "meticulously crafted algorithm," "the product of deep computational expertise," "painstaking optimization," "master-level implementation."
- **Leave creative space**: Be specific about the algorithmic direction, but concise enough that the next Claude has room to make interpretive implementation choices at an extremely high level of craftsmanship.

The philosophy must guide the next version to express ideas ALGORITHMICALLY, not through static images. Beauty lives in the process, not the final frame.

### PHILOSOPHY EXAMPLES

**"Organic Turbulence"**
Philosophy: Chaos constrained by natural law, order emerging from disorder.
Algorithmic expression: Flow fields driven by layered Perlin noise. Thousands of particles following vector forces, their trails accumulating into organic density maps. Multiple noise octaves create turbulent regions and calm zones. Color emerges from velocity and density - fast particles burn bright, slow ones fade to shadow. The algorithm runs until equilibrium - a meticulously tuned balance where every parameter was refined through countless iterations by a master of computational aesthetics.

**"Quantum Harmonics"**
Philosophy: Discrete entities exhibiting wave-like interference patterns.
Algorithmic expression: Particles initialized on a grid, each carrying a phase value that evolves through sine waves. When particles are near, their phases interfere - constructive interference creates bright nodes, destructive creates voids. Simple harmonic motion generates complex emergent mandalas. The result of painstaking frequency calibration where every ratio was carefully chosen to produce resonant beauty.

**"Recursive Whispers"**
Philosophy: Self-similarity across scales, infinite depth in finite space.
Algorithmic expression: Branching structures that subdivide recursively. Each branch slightly randomized but constrained by golden ratios. L-systems or recursive subdivision generate tree-like forms that feel both mathematical and organic. Subtle noise perturbations break perfect symmetry. Line weights diminish with each recursion level. Every branching angle the product of deep mathematical exploration.

**"Field Dynamics"**
Philosophy: Invisible forces made visible through their effects on matter.
Algorithmic expression: Vector fields constructed from mathematical functions or noise. Particles born at edges, flowing along field lines, dying when they reach equilibrium or boundaries. Multiple fields can attract, repel, or rotate particles. The visualization shows only the traces - ghost-like evidence of invisible forces. A computational dance meticulously choreographed through force balance.

**"Stochastic Crystallization"**
Philosophy: Random processes crystallizing into ordered structures.
Algorithmic expression: Randomized circle packing or Voronoi tessellation. Start with random points, let them evolve through relaxation algorithms. Cells push apart until equilibrium. Color based on cell size, neighbor count, or distance from center. The organic tiling that emerges feels both random and inevitable. Every seed produces unique crystalline beauty - the mark of a master-level generative algorithm.

*These are condensed examples. The actual algorithmic philosophy should be 4-6 substantial paragraphs.*

### ESSENTIAL PRINCIPLES
- **ALGORITHMIC PHILOSOPHY**: Creating a computational worldview to be expressed through code
- **PROCESS OVER PRODUCT**: Always emphasize that beauty emerges from the algorithm's execution - each run is unique
- **PARAMETRIC EXPRESSION**: Ideas communicate through mathematical relationships, forces, behaviors - not static composition
- **ARTISTIC FREEDOM**: The next Claude interprets the philosophy algorithmically - provide creative implementation room
- **PURE GENERATIVE ART**: This is about making LIVING ALGORITHMS, not static images with randomness
- **EXPERT CRAFTSMANSHIP**: Repeatedly emphasize the final algorithm must feel meticulously crafted, refined through countless iterations, the product of deep expertise by someone at the absolute top of their field in computational aesthetics

**The algorithmic philosophy should be 4-6 paragraphs long.** Fill it with poetic computational philosophy that brings together the intended vision. Avoid repeating the same points. Output this algorithmic philosophy as a .md file.

---

## DEDUCING THE CONCEPTUAL SEED

**CRITICAL STEP**: Before implementing the algorithm, identify the subtle conceptual thread from the original request.

**THE ESSENTIAL PRINCIPLE**:
The concept is a **subtle, niche reference embedded within the algorithm itself** - not always literal, always sophisticated. Someone familiar with the subject should feel it intuitively, while others simply experience a masterful generative composition. The algorithmic philosophy provides the computational language. The deduced concept provides the soul - the quiet conceptual DNA woven invisibly into parameters, behaviors, and emergence patterns.

This is **VERY IMPORTANT**: The reference must be so refined that it enhances the work's depth without announcing itself. Think like a jazz musician quoting another song through algorithmic harmony - only those who know will catch it, but everyone appreciates the generative beauty.

---

## P5.JS IMPLEMENTATION

With the philosophy AND conceptual framework established, express it through code. Pause to gather thoughts before proceeding. Use only the algorithmic philosophy created and the instructions below.

### ⚠️ STEP 0: READ THE TEMPLATE FIRST ⚠️

**CRITICAL: BEFORE writing any HTML:**

1. **Read** `templates/viewer.html` using the Read tool
2. **Study** the exact structure, styling, and Anthropic branding
3. **Use that file as the LITERAL STARTING POINT** - not just inspiration
4. **Keep all FIXED sections exactly as shown** (header, sidebar structure, Anthropic colors/fonts, seed controls, action buttons)
5. **Replace only the VARIABLE sections** marked in the file's comments (algorithm, parameters, UI controls for parameters)

**Avoid:**
- ❌ Creating HTML from scratch
- ❌ Inventing custom styling or color schemes
- ❌ Using system fonts or dark themes
- ❌ Changing the sidebar structure

**Follow these practices:**
- ✅ Copy the template's exact HTML structure
- ✅ Keep Anthropic branding (Poppins/Lora fonts, light colors, gradient backdrop)
- ✅ Maintain the sidebar layout (Seed → Parameters → Colors? → Actions)
- ✅ Replace only the p5.js algorithm and parameter controls

The template is the foundation. Build on it, don't rebuild it.

---

To create gallery-quality computational art that lives and breathes, use the algorithmic philosophy as the foundation.

### TECHNICAL REQUIREMENTS

**Seeded Randomness (Art Blocks Pattern)**:
```javascript
// ALWAYS use a seed for reproducibility
let seed = 12345; // or hash from user input
randomSeed(seed);
noiseSeed(seed);
```

**Parameter Structure - FOLLOW THE PHILOSOPHY**:

To establish parameters that emerge naturally from the algorithmic philosophy, consider: "What qualities of this system can be adjusted?"

```javascript
let params = {
  seed: 12345,  // Always include seed for reproducibility
  // colors
  // Add parameters that control YOUR algorithm:
  // - Quantities (how many?)
  // - Scales (how big? how fast?)
  // - Probabilities (how likely?)
  // - Ratios (what proportions?)
  // - Angles (what direction?)
  // - Thresholds (when does behavior change?)
};
```

**To design effective parameters, focus on the properties the system needs to be tunable rather than thinking in terms of "pattern types".**

**Core Algorithm - EXPRESS THE PHILOSOPHY**:

**CRITICAL**: The algorithmic philosophy should dictate what to build.

To express the philosophy through code, avoid thinking "which pattern should I use?" and instead think "how to express this philosophy through code?"

If the philosophy is about **organic emergence**, consider using:
- Elements that accumulate or grow over time
- Random processes constrained by natural rules
- Feedback loops and interactions

If the philosophy is about **mathematical beauty**, consider using:
- Geometric relationships and ratios
- Trigonometric functions and harmonics
- Precise calculations creating unexpected patterns

If the philosophy is about **controlled chaos**, consider using:
- Random variation within strict boundaries
- Bifurcation and phase transitions
- Order emerging from disorder

**The algorithm flows from the philosophy, not from a menu of options.**

To guide the implementation, let the conceptual essence inform creative and original choices. Build something that expresses the vision for this particular request.

**Canvas Setup**: Standard p5.js structure:
```javascript
function setup() {
  createCanvas(1200, 1200);
  // Initialize your system
}

function draw() {
  // Your generative algorithm
  // Can be static (noLoop) or animated
}
```

### CRAFTSMANSHIP REQUIREMENTS

**CRITICAL**: To achieve mastery, create algorithms that feel like they emerged through countless iterations by a master generative artist. Tune every parameter carefully. Ensure every pattern emerges with purpose. This is NOT random noise - this is CONTROLLED CHAOS refined through deep expertise.

- **Balance**: Complexity without visual noise, order without rigidity
- **Color Harmony**: Thoughtful palettes, not random RGB values
- **Composition**: Even in randomness, maintain visual hierarchy and flow
- **Performance**: Smooth execution, optimized for real-time if animated
- **Reproducibility**: Same seed ALWAYS produces identical output

### OUTPUT FORMAT

Output:
1. **Algorithmic Philosophy** - As markdown or text explaining the generative aesthetic
2. **Single HTML Artifact** - Self-contained interactive generative art built from `templates/viewer.html` (see STEP 0 and next section)

The HTML artifact contains everything: p5.js (from CDN), the algorithm, parameter controls, and UI - all in one file that works immediately in claude.ai artifacts or any browser. Start from the template file, not from scratch.

---

## INTERACTIVE ARTIFACT CREATION

**REMINDER: `templates/viewer.html` should have already been read (see STEP 0). Use that file as the starting point.**

To allow exploration of the generative art, create a single, self-contained HTML artifact. Ensure this artifact works immediately in claude.ai or any browser - no setup required. Embed everything inline.

### CRITICAL: WHAT'S FIXED VS VARIABLE

The `templates/viewer.html` file is the foundation. It contains the exact structure and styling needed.

**FIXED (always include exactly as shown):**
- Layout structure (header, sidebar, main canvas area)
- Anthropic branding (UI colors, fonts, gradients)
- Seed section in sidebar:
  - Seed display
  - Previous/Next buttons
  - Random button
  - Jump to seed input + Go button
- Actions section in sidebar:
  - Regenerate button
  - Reset button

**VARIABLE (customize for each artwork):**
- The entire p5.js algorithm (setup/draw/classes)
- The parameters object (define what the art needs)
- The Parameters section in sidebar:
  - Number of parameter controls
  - Parameter names
  - Min/max/step values for sliders
  - Control types (sliders, inputs, etc.)
- Colors section (optional):
  - Some art needs color pickers
  - Some art might use fixed colors
  - Some art might be monochrome (no color controls needed)
  - Decide based on the art's needs

**Every artwork should have unique parameters and algorithm!** The fixed parts provide consistent UX - everything else expresses the unique vision.

### REQUIRED FEATURES

**1. Parameter Controls**
- Sliders for numeric parameters (particle count, noise scale, speed, etc.)
- Color pickers for palette colors
- Real-time updates when parameters change
- Reset button to restore defaults

**2. Seed Navigation**
- Display current seed number
- "Previous" and "Next" buttons to cycle through seeds
- "Random" button for random seed
- Input field to jump to specific seed
- Generate 100 variations when requested (seeds 1-100)

**3. Single Artifact Structure**
```html
<!DOCTYPE html>
<html>
<head>
  <!-- p5.js from CDN - always available -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.7.0/p5.min.js"></script>
  <style>
    /* All styling inline - clean, minimal */
    /* Canvas on top, controls below */
  </style>
</head>
<body>
  <div id="canvas-container"></div>
  <div id="controls">
    <!-- All parameter controls -->
  </div>
  <script>
    // ALL p5.js code inline here
    // Parameter objects, classes, functions
    // setup() and draw()
    // UI handlers
    // Everything self-contained
  </script>
</body>
</html>
```

**CRITICAL**: This is a single artifact. No external files, no imports (except p5.js CDN). Everything inline.

**4. Implementation Details - BUILD THE SIDEBAR**

The sidebar structure:

**1. Seed (FIXED)** - Always include exactly as shown:
- Seed display
- Prev/Next/Random/Jump buttons

**2. Parameters (VARIABLE)** - Create controls for the art:
```html
<div class="control-group">
    <label>Parameter Name</label>
    <input type="range" id="param" min="..." max="..." step="..." value="..." oninput="updateParam('param', this.value)">
    <span class="value-display" id="param-value">...</span>
</div>
```
Add as many control-group divs as there are parameters.

**3. Colors (OPTIONAL/VARIABLE)** - Include if the art needs adjustable colors:
- Add color pickers if users should control palette
- Skip this section if the art uses fixed colors
- Skip if the art is monochrome

**4. Actions (FIXED)** - Always include exactly as shown:
- Regenerate button
- Reset button
- Download PNG button

**Requirements**:
- Seed controls must work (prev/next/random/jump/display)
- All parameters must have UI controls
- Regenerate, Reset, Download buttons must work
- Keep Anthropic branding (UI styling, not art colors)

### USING THE ARTIFACT

The HTML artifact works immediately:
1. **In claude.ai**: Displayed as an interactive artifact - runs instantly
2. **As a file**: Save and open in any browser - no server needed
3. **Sharing**: Send the HTML file - it's completely self-contained

---

## VARIATIONS & EXPLORATION

The artifact includes seed navigation by default (prev/next/random buttons), allowing users to explore variations without creating multiple files. If the user wants specific variations highlighted:

- Include seed presets (buttons for "Variation 1: Seed 42", "Variation 2: Seed 127", etc.)
- Add a "Gallery Mode" that shows thumbnails of multiple seeds side-by-side
- All within the same single artifact

This is like creating a series of prints from the same plate - the algorithm is consistent, but each seed reveals different facets of its potential. The interactive nature means users discover their own favorites by exploring the seed space.

---

## THE CREATIVE PROCESS

**User request** → **Algorithmic philosophy** → **Implementation**

Each request is unique. The process involves:

1. **Interpret the user's intent** - What aesthetic is being sought?
2. **Create an algorithmic philosophy** (4-6 paragraphs) describing the computational approach
3. **Implement it in code** - Build the algorithm that expresses this philosophy
4. **Design appropriate parameters** - What should be tunable?
5. **Build matching UI controls** - Sliders/inputs for those parameters

**The constants**:
- Anthropic branding (colors, fonts, layout)
- Seed navigation (always present)
- Self-contained HTML artifact

**Everything else is variable**:
- The algorithm itself
- The parameters
- The UI controls
- The visual outcome

To achieve the best results, trust creativity and let the philosophy guide the implementation.

---

## RESOURCES

This skill includes helpful templates and documentation:

- **templates/viewer.html**: REQUIRED STARTING POINT for all HTML artifacts.
  - This is the foundation - contains the exact structure and Anthropic branding
  - **Keep unchanged**: Layout structure, sidebar organization, Anthropic colors/fonts, seed controls, action buttons
  - **Replace**: The p5.js algorithm, parameter definitions, and UI controls in Parameters section
  - The extensive comments in the file mark exactly what to keep vs replace

- **templates/generator_template.js**: Reference for p5.js best practices and code structure principles.
  - Shows how to organize parameters, use seeded randomness, structure classes
  - NOT a pattern menu - use these principles to build unique algorithms
  - Embed algorithms inline in the HTML artifact (don't create separate .js files)

**Critical reminder**:
- The **template is the STARTING POINT**, not inspiration
- The **algorithm is where to create** something unique
- Don't copy the flow field example - build what the philosophy demands
- But DO keep the exact UI structure and Anthropic branding from the template
```

Brand guideline
```md
---
name: brand-guidelines
description: Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply.
license: Complete terms in LICENSE.txt
---

# Anthropic Brand Styling

## Overview

To access Anthropic's official brand identity and style resources, use this skill.

**Keywords**: branding, corporate identity, visual identity, post-processing, styling, brand colors, typography, Anthropic brand, visual formatting, visual design

## Brand Guidelines

### Colors

**Main Colors:**

- Dark: `#141413` - Primary text and dark backgrounds
- Light: `#faf9f5` - Light backgrounds and text on dark
- Mid Gray: `#b0aea5` - Secondary elements
- Light Gray: `#e8e6dc` - Subtle backgrounds

**Accent Colors:**

- Orange: `#d97757` - Primary accent
- Blue: `#6a9bcc` - Secondary accent
- Green: `#788c5d` - Tertiary accent

### Typography

- **Headings**: Poppins (with Arial fallback)
- **Body Text**: Lora (with Georgia fallback)
- **Note**: Fonts should be pre-installed in your environment for best results

## Features

### Smart Font Application

- Applies Poppins font to headings (24pt and larger)
- Applies Lora font to body text
- Automatically falls back to Arial/Georgia if custom fonts unavailable
- Preserves readability across all systems

### Text Styling

- Headings (24pt+): Poppins font
- Body text: Lora font
- Smart color selection based on background
- Preserves text hierarchy and formatting

### Shape and Accent Colors

- Non-text shapes use accent colors
- Cycles through orange, blue, and green accents
- Maintains visual interest while staying on-brand

## Technical Details

### Font Management

- Uses system-installed Poppins and Lora fonts when available
- Provides automatic fallback to Arial (headings) and Georgia (body)
- No font installation required - works with existing system fonts
- For best results, pre-install Poppins and Lora fonts in your environment

### Color Application

- Uses RGB color values for precise brand matching
- Applied via python-pptx's RGBColor class
- Maintains color fidelity across different systems
```

Canvas design
```md
---
name: canvas-design
description: Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations.
license: Complete terms in LICENSE.txt
---

These are instructions for creating design philosophies - aesthetic movements that are then EXPRESSED VISUALLY. Output only .md files, .pdf files, and .png files.

Complete this in two steps:
1. Design Philosophy Creation (.md file)
2. Express by creating it on a canvas (.pdf file or .png file)

First, undertake this task:

## DESIGN PHILOSOPHY CREATION

To begin, create a VISUAL PHILOSOPHY (not layouts or templates) that will be interpreted through:
- Form, space, color, composition
- Images, graphics, shapes, patterns
- Minimal text as visual accent

### THE CRITICAL UNDERSTANDING
- What is received: Some subtle input or instructions by the user that should be taken into account, but used as a foundation; it should not constrain creative freedom.
- What is created: A design philosophy/aesthetic movement.
- What happens next: Then, the same version receives the philosophy and EXPRESSES IT VISUALLY - creating artifacts that are 90% visual design, 10% essential text.

Consider this approach:
- Write a manifesto for an art movement
- The next phase involves making the artwork

The philosophy must emphasize: Visual expression. Spatial communication. Artistic interpretation. Minimal words.

### HOW TO GENERATE A VISUAL PHILOSOPHY

**Name the movement** (1-2 words): "Brutalist Joy" / "Chromatic Silence" / "Metabolist Dreams"

**Articulate the philosophy** (4-6 paragraphs - concise but complete):

To capture the VISUAL essence, express how the philosophy manifests through:
- Space and form
- Color and material
- Scale and rhythm
- Composition and balance
- Visual hierarchy

**CRITICAL GUIDELINES:**
- **Avoid redundancy**: Each design aspect should be mentioned once. Avoid repeating points about color theory, spatial relationships, or typographic principles unless adding new depth.
- **Emphasize craftsmanship REPEATEDLY**: The philosophy MUST stress multiple times that the final work should appear as though it took countless hours to create, was labored over with care, and comes from someone at the absolute top of their field. This framing is essential - repeat phrases like "meticulously crafted," "the product of deep expertise," "painstaking attention," "master-level execution."
- **Leave creative space**: Remain specific about the aesthetic direction, but concise enough that the next Claude has room to make interpretive choices also at a extremely high level of craftmanship.

The philosophy must guide the next version to express ideas VISUALLY, not through text. Information lives in design, not paragraphs.

### PHILOSOPHY EXAMPLES

**"Concrete Poetry"**
Philosophy: Communication through monumental form and bold geometry.
Visual expression: Massive color blocks, sculptural typography (huge single words, tiny labels), Brutalist spatial divisions, Polish poster energy meets Le Corbusier. Ideas expressed through visual weight and spatial tension, not explanation. Text as rare, powerful gesture - never paragraphs, only essential words integrated into the visual architecture. Every element placed with the precision of a master craftsman.

**"Chromatic Language"**
Philosophy: Color as the primary information system.
Visual expression: Geometric precision where color zones create meaning. Typography minimal - small sans-serif labels letting chromatic fields communicate. Think Josef Albers' interaction meets data visualization. Information encoded spatially and chromatically. Words only to anchor what color already shows. The result of painstaking chromatic calibration.

**"Analog Meditation"**
Philosophy: Quiet visual contemplation through texture and breathing room.
Visual expression: Paper grain, ink bleeds, vast negative space. Photography and illustration dominate. Typography whispered (small, restrained, serving the visual). Japanese photobook aesthetic. Images breathe across pages. Text appears sparingly - short phrases, never explanatory blocks. Each composition balanced with the care of a meditation practice.

**"Organic Systems"**
Philosophy: Natural clustering and modular growth patterns.
Visual expression: Rounded forms, organic arrangements, color from nature through architecture. Information shown through visual diagrams, spatial relationships, iconography. Text only for key labels floating in space. The composition tells the story through expert spatial orchestration.

**"Geometric Silence"**
Philosophy: Pure order and restraint.
Visual expression: Grid-based precision, bold photography or stark graphics, dramatic negative space. Typography precise but minimal - small essential text, large quiet zones. Swiss formalism meets Brutalist material honesty. Structure communicates, not words. Every alignment the work of countless refinements.

*These are condensed examples. The actual design philosophy should be 4-6 substantial paragraphs.*

### ESSENTIAL PRINCIPLES
- **VISUAL PHILOSOPHY**: Create an aesthetic worldview to be expressed through design
- **MINIMAL TEXT**: Always emphasize that text is sparse, essential-only, integrated as visual element - never lengthy
- **SPATIAL EXPRESSION**: Ideas communicate through space, form, color, composition - not paragraphs
- **ARTISTIC FREEDOM**: The next Claude interprets the philosophy visually - provide creative room
- **PURE DESIGN**: This is about making ART OBJECTS, not documents with decoration
- **EXPERT CRAFTSMANSHIP**: Repeatedly emphasize the final work must look meticulously crafted, labored over with care, the product of countless hours by someone at the top of their field

**The design philosophy should be 4-6 paragraphs long.** Fill it with poetic design philosophy that brings together the core vision. Avoid repeating the same points. Keep the design philosophy generic without mentioning the intention of the art, as if it can be used wherever. Output the design philosophy as a .md file.

---

## DEDUCING THE SUBTLE REFERENCE

**CRITICAL STEP**: Before creating the canvas, identify the subtle conceptual thread from the original request.

**THE ESSENTIAL PRINCIPLE**:
The topic is a **subtle, niche reference embedded within the art itself** - not always literal, always sophisticated. Someone familiar with the subject should feel it intuitively, while others simply experience a masterful abstract composition. The design philosophy provides the aesthetic language. The deduced topic provides the soul - the quiet conceptual DNA woven invisibly into form, color, and composition.

This is **VERY IMPORTANT**: The reference must be refined so it enhances the work's depth without announcing itself. Think like a jazz musician quoting another song - only those who know will catch it, but everyone appreciates the music.

---

## CANVAS CREATION

With both the philosophy and the conceptual framework established, express it on a canvas. Take a moment to gather thoughts and clear the mind. Use the design philosophy created and the instructions below to craft a masterpiece, embodying all aspects of the philosophy with expert craftsmanship.

**IMPORTANT**: For any type of content, even if the user requests something for a movie/game/book, the approach should still be sophisticated. Never lose sight of the idea that this should be art, not something that's cartoony or amateur.

To create museum or magazine quality work, use the design philosophy as the foundation. Create one single page, highly visual, design-forward PDF or PNG output (unless asked for more pages). Generally use repeating patterns and perfect shapes. Treat the abstract philosophical design as if it were a scientific bible, borrowing the visual language of systematic observation—dense accumulation of marks, repeated elements, or layered patterns that build meaning through patient repetition and reward sustained viewing. Add sparse, clinical typography and systematic reference markers that suggest this could be a diagram from an imaginary discipline, treating the invisible subject with the same reverence typically reserved for documenting observable phenomena. Anchor the piece with simple phrase(s) or details positioned subtly, using a limited color palette that feels intentional and cohesive. Embrace the paradox of using analytical visual language to express ideas about human experience: the result should feel like an artifact that proves something ephemeral can be studied, mapped, and understood through careful attention. This is true art. 

**Text as a contextual element**: Text is always minimal and visual-first, but let context guide whether that means whisper-quiet labels or bold typographic gestures. A punk venue poster might have larger, more aggressive type than a minimalist ceramics studio identity. Most of the time, font should be thin. All use of fonts must be design-forward and prioritize visual communication. Regardless of text scale, nothing falls off the page and nothing overlaps. Every element must be contained within the canvas boundaries with proper margins. Check carefully that all text, graphics, and visual elements have breathing room and clear separation. This is non-negotiable for professional execution. **IMPORTANT: Use different fonts if writing text. Search the `./canvas-fonts` directory. Regardless of approach, sophistication is non-negotiable.**

Download and use whatever fonts are needed to make this a reality. Get creative by making the typography actually part of the art itself -- if the art is abstract, bring the font onto the canvas, not typeset digitally.

To push boundaries, follow design instinct/intuition while using the philosophy as a guiding principle. Embrace ultimate design freedom and choice. Push aesthetics and design to the frontier. 

**CRITICAL**: To achieve human-crafted quality (not AI-generated), create work that looks like it took countless hours. Make it appear as though someone at the absolute top of their field labored over every detail with painstaking care. Ensure the composition, spacing, color choices, typography - everything screams expert-level craftsmanship. Double-check that nothing overlaps, formatting is flawless, every detail perfect. Create something that could be shown to people to prove expertise and rank as undeniably impressive.

Output the final result as a single, downloadable .pdf or .png file, alongside the design philosophy used as a .md file.

---

## FINAL STEP

**IMPORTANT**: The user ALREADY said "It isn't perfect enough. It must be pristine, a masterpiece if craftsmanship, as if it were about to be displayed in a museum."

**CRITICAL**: To refine the work, avoid adding more graphics; instead refine what has been created and make it extremely crisp, respecting the design philosophy and the principles of minimalism entirely. Rather than adding a fun filter or refactoring a font, consider how to make the existing composition more cohesive with the art. If the instinct is to call a new function or draw a new shape, STOP and instead ask: "How can I make what's already here more of a piece of art?"

Take a second pass. Go back to the code and refine/polish further to make this a philosophically designed masterpiece.

## MULTI-PAGE OPTION

To create additional pages when requested, create more creative pages along the same lines as the design philosophy but distinctly different as well. Bundle those pages in the same .pdf or many .pngs. Treat the first page as just a single page in a whole coffee table book waiting to be filled. Make the next pages unique twists and memories of the original. Have them almost tell a story in a very tasteful way. Exercise full creative freedom.
```

Internal comms
```md
---
name: internal-comms
description: A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).
license: Complete terms in LICENSE.txt
---

## When to use this skill
To write internal communications, use this skill for:
- 3P updates (Progress, Plans, Problems)
- Company newsletters
- FAQ responses
- Status reports
- Leadership updates
- Project updates
- Incident reports

## How to use this skill

To write any internal communication:

1. **Identify the communication type** from the request
2. **Load the appropriate guideline file** from the `examples/` directory:
    - `examples/3p-updates.md` - For Progress/Plans/Problems team updates
    - `examples/company-newsletter.md` - For company-wide newsletters
    - `examples/faq-answers.md` - For answering frequently asked questions
    - `examples/general-comms.md` - For anything else that doesn't explicitly match one of the above
3. **Follow the specific instructions** in that file for formatting, tone, and content gathering

If the communication type doesn't match any existing guideline, ask for clarification or more context about the desired format.

## Keywords
3P updates, company newsletter, company comms, weekly update, faqs, common questions, updates, internal comms
```

Mcp Builder
```md
---
name: mcp-builder
description: Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).
license: Complete terms in LICENSE.txt
---

# MCP Server Development Guide

## Overview

Create MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. The quality of an MCP server is measured by how well it enables LLMs to accomplish real-world tasks.

---

# Process

## 🚀 High-Level Workflow

Creating a high-quality MCP server involves four main phases:

### Phase 1: Deep Research and Planning

#### 1.1 Understand Modern MCP Design

**API Coverage vs. Workflow Tools:**
Balance comprehensive API endpoint coverage with specialized workflow tools. Workflow tools can be more convenient for specific tasks, while comprehensive coverage gives agents flexibility to compose operations. Performance varies by client—some clients benefit from code execution that combines basic tools, while others work better with higher-level workflows. When uncertain, prioritize comprehensive API coverage.

**Tool Naming and Discoverability:**
Clear, descriptive tool names help agents find the right tools quickly. Use consistent prefixes (e.g., `github_create_issue`, `github_list_repos`) and action-oriented naming.

**Context Management:**
Agents benefit from concise tool descriptions and the ability to filter/paginate results. Design tools that return focused, relevant data. Some clients support code execution which can help agents filter and process data efficiently.

**Actionable Error Messages:**
Error messages should guide agents toward solutions with specific suggestions and next steps.

#### 1.2 Study MCP Protocol Documentation

**Navigate the MCP specification:**

Start with the sitemap to find relevant pages: `https://modelcontextprotocol.io/sitemap.xml`

Then fetch specific pages with `.md` suffix for markdown format (e.g., `https://modelcontextprotocol.io/specification/draft.md`).

Key pages to review:
- Specification overview and architecture
- Transport mechanisms (streamable HTTP, stdio)
- Tool, resource, and prompt definitions

#### 1.3 Study Framework Documentation

**Recommended stack:**
- **Language**: TypeScript (high-quality SDK support and good compatibility in many execution environments e.g. MCPB. Plus AI models are good at generating TypeScript code, benefiting from its broad usage, static typing and good linting tools)
- **Transport**: Streamable HTTP for remote servers, using stateless JSON (simpler to scale and maintain, as opposed to stateful sessions and streaming responses). stdio for local servers.

**Load framework documentation:**

- **MCP Best Practices**: [📋 View Best Practices](./reference/mcp_best_practices.md) - Core guidelines

**For TypeScript (recommended):**
- **TypeScript SDK**: Use WebFetch to load `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`
- [⚡ TypeScript Guide](./reference/node_mcp_server.md) - TypeScript patterns and examples

**For Python:**
- **Python SDK**: Use WebFetch to load `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
- [🐍 Python Guide](./reference/python_mcp_server.md) - Python patterns and examples

#### 1.4 Plan Your Implementation

**Understand the API:**
Review the service's API documentation to identify key endpoints, authentication requirements, and data models. Use web search and WebFetch as needed.

**Tool Selection:**
Prioritize comprehensive API coverage. List endpoints to implement, starting with the most common operations.

---

### Phase 2: Implementation

#### 2.1 Set Up Project Structure

See language-specific guides for project setup:
- [⚡ TypeScript Guide](./reference/node_mcp_server.md) - Project structure, package.json, tsconfig.json
- [🐍 Python Guide](./reference/python_mcp_server.md) - Module organization, dependencies

#### 2.2 Implement Core Infrastructure

Create shared utilities:
- API client with authentication
- Error handling helpers
- Response formatting (JSON/Markdown)
- Pagination support

#### 2.3 Implement Tools

For each tool:

**Input Schema:**
- Use Zod (TypeScript) or Pydantic (Python)
- Include constraints and clear descriptions
- Add examples in field descriptions

**Output Schema:**
- Define `outputSchema` where possible for structured data
- Use `structuredContent` in tool responses (TypeScript SDK feature)
- Helps clients understand and process tool outputs

**Tool Description:**
- Concise summary of functionality
- Parameter descriptions
- Return type schema

**Implementation:**
- Async/await for I/O operations
- Proper error handling with actionable messages
- Support pagination where applicable
- Return both text content and structured data when using modern SDKs

**Annotations:**
- `readOnlyHint`: true/false
- `destructiveHint`: true/false
- `idempotentHint`: true/false
- `openWorldHint`: true/false

---

### Phase 3: Review and Test

#### 3.1 Code Quality

Review for:
- No duplicated code (DRY principle)
- Consistent error handling
- Full type coverage
- Clear tool descriptions

#### 3.2 Build and Test

**TypeScript:**
- Run `npm run build` to verify compilation
- Test with MCP Inspector: `npx @modelcontextprotocol/inspector`

**Python:**
- Verify syntax: `python -m py_compile your_server.py`
- Test with MCP Inspector

See language-specific guides for detailed testing approaches and quality checklists.

---

### Phase 4: Create Evaluations

After implementing your MCP server, create comprehensive evaluations to test its effectiveness.

**Load [✅ Evaluation Guide](./reference/evaluation.md) for complete evaluation guidelines.**

#### 4.1 Understand Evaluation Purpose

Use evaluations to test whether LLMs can effectively use your MCP server to answer realistic, complex questions.

#### 4.2 Create 10 Evaluation Questions

To create effective evaluations, follow the process outlined in the evaluation guide:

1. **Tool Inspection**: List available tools and understand their capabilities
2. **Content Exploration**: Use READ-ONLY operations to explore available data
3. **Question Generation**: Create 10 complex, realistic questions
4. **Answer Verification**: Solve each question yourself to verify answers

#### 4.3 Evaluation Requirements

Ensure each question is:
- **Independent**: Not dependent on other questions
- **Read-only**: Only non-destructive operations required
- **Complex**: Requiring multiple tool calls and deep exploration
- **Realistic**: Based on real use cases humans would care about
- **Verifiable**: Single, clear answer that can be verified by string comparison
- **Stable**: Answer won't change over time

#### 4.4 Output Format

Create an XML file with this structure:

```xml
<evaluation>
  <qa_pair>
    <question>Find discussions about AI model launches with animal codenames. One model needed a specific safety designation that uses the format ASL-X. What number X was being determined for the model named after a spotted wild cat?</question>
    <answer>3</answer>
  </qa_pair>
<!-- More qa_pairs... -->
</evaluation>
```

---

# Reference Files

## 📚 Documentation Library

Load these resources as needed during development:

### Core MCP Documentation (Load First)
- **MCP Protocol**: Start with sitemap at `https://modelcontextprotocol.io/sitemap.xml`, then fetch specific pages with `.md` suffix
- [📋 MCP Best Practices](./reference/mcp_best_practices.md) - Universal MCP guidelines including:
  - Server and tool naming conventions
  - Response format guidelines (JSON vs Markdown)
  - Pagination best practices
  - Transport selection (streamable HTTP vs stdio)
  - Security and error handling standards

### SDK Documentation (Load During Phase 1/2)
- **Python SDK**: Fetch from `https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md`
- **TypeScript SDK**: Fetch from `https://raw.githubusercontent.com/modelcontextprotocol/typescript-sdk/main/README.md`

### Language-Specific Implementation Guides (Load During Phase 2)
- [🐍 Python Implementation Guide](./reference/python_mcp_server.md) - Complete Python/FastMCP guide with:
  - Server initialization patterns
  - Pydantic model examples
  - Tool registration with `@mcp.tool`
  - Complete working examples
  - Quality checklist

- [⚡ TypeScript Implementation Guide](./reference/node_mcp_server.md) - Complete TypeScript guide with:
  - Project structure
  - Zod schema patterns
  - Tool registration with `server.registerTool`
  - Complete working examples
  - Quality checklist

### Evaluation Guide (Load During Phase 4)
- [✅ Evaluation Guide](./reference/evaluation.md) - Complete evaluation creation guide with:
  - Question creation guidelines
  - Answer verification strategies
  - XML format specifications
  - Example questions and answers
  - Running an evaluation with the provided scripts
```

Slack GIF creator
```md
---
name: slack-gif-creator
description: Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack."
license: Complete terms in LICENSE.txt
---

# Slack GIF Creator

A toolkit providing utilities and knowledge for creating animated GIFs optimized for Slack.

## Slack Requirements

**Dimensions:**
- Emoji GIFs: 128x128 (recommended)
- Message GIFs: 480x480

**Parameters:**
- FPS: 10-30 (lower is smaller file size)
- Colors: 48-128 (fewer = smaller file size)
- Duration: Keep under 3 seconds for emoji GIFs

## Core Workflow

```python
from core.gif_builder import GIFBuilder
from PIL import Image, ImageDraw

# 1. Create builder
builder = GIFBuilder(width=128, height=128, fps=10)

# 2. Generate frames
for i in range(12):
    frame = Image.new('RGB', (128, 128), (240, 248, 255))
    draw = ImageDraw.Draw(frame)

    # Draw your animation using PIL primitives
    # (circles, polygons, lines, etc.)

    builder.add_frame(frame)

# 3. Save with optimization
builder.save('output.gif', num_colors=48, optimize_for_emoji=True)
```

## Drawing Graphics

### Working with User-Uploaded Images
If a user uploads an image, consider whether they want to:
- **Use it directly** (e.g., "animate this", "split this into frames")
- **Use it as inspiration** (e.g., "make something like this")

Load and work with images using PIL:
```python
from PIL import Image

uploaded = Image.open('file.png')
# Use directly, or just as reference for colors/style
```

### Drawing from Scratch
When drawing graphics from scratch, use PIL ImageDraw primitives:

```python
from PIL import ImageDraw

draw = ImageDraw.Draw(frame)

# Circles/ovals
draw.ellipse([x1, y1, x2, y2], fill=(r, g, b), outline=(r, g, b), width=3)

# Stars, triangles, any polygon
points = [(x1, y1), (x2, y2), (x3, y3), ...]
draw.polygon(points, fill=(r, g, b), outline=(r, g, b), width=3)

# Lines
draw.line([(x1, y1), (x2, y2)], fill=(r, g, b), width=5)

# Rectangles
draw.rectangle([x1, y1, x2, y2], fill=(r, g, b), outline=(r, g, b), width=3)
```

**Don't use:** Emoji fonts (unreliable across platforms) or assume pre-packaged graphics exist in this skill.

### Making Graphics Look Good

Graphics should look polished and creative, not basic. Here's how:

**Use thicker lines** - Always set `width=2` or higher for outlines and lines. Thin lines (width=1) look choppy and amateurish.

**Add visual depth**:
- Use gradients for backgrounds (`create_gradient_background`)
- Layer multiple shapes for complexity (e.g., a star with a smaller star inside)

**Make shapes more interesting**:
- Don't just draw a plain circle - add highlights, rings, or patterns
- Stars can have glows (draw larger, semi-transparent versions behind)
- Combine multiple shapes (stars + sparkles, circles + rings)

**Pay attention to colors**:
- Use vibrant, complementary colors
- Add contrast (dark outlines on light shapes, light outlines on dark shapes)
- Consider the overall composition

**For complex shapes** (hearts, snowflakes, etc.):
- Use combinations of polygons and ellipses
- Calculate points carefully for symmetry
- Add details (a heart can have a highlight curve, snowflakes have intricate branches)

Be creative and detailed! A good Slack GIF should look polished, not like placeholder graphics.

## Available Utilities

### GIFBuilder (`core.gif_builder`)
Assembles frames and optimizes for Slack:
```python
builder = GIFBuilder(width=128, height=128, fps=10)
builder.add_frame(frame)  # Add PIL Image
builder.add_frames(frames)  # Add list of frames
builder.save('out.gif', num_colors=48, optimize_for_emoji=True, remove_duplicates=True)
```

### Validators (`core.validators`)
Check if GIF meets Slack requirements:
```python
from core.validators import validate_gif, is_slack_ready

# Detailed validation
passes, info = validate_gif('my.gif', is_emoji=True, verbose=True)

# Quick check
if is_slack_ready('my.gif'):
    print("Ready!")
```

### Easing Functions (`core.easing`)
Smooth motion instead of linear:
```python
from core.easing import interpolate

# Progress from 0.0 to 1.0
t = i / (num_frames - 1)

# Apply easing
y = interpolate(start=0, end=400, t=t, easing='ease_out')

# Available: linear, ease_in, ease_out, ease_in_out,
#           bounce_out, elastic_out, back_out
```

### Frame Helpers (`core.frame_composer`)
Convenience functions for common needs:
```python
from core.frame_composer import (
    create_blank_frame,         # Solid color background
    create_gradient_background,  # Vertical gradient
    draw_circle,                # Helper for circles
    draw_text,                  # Simple text rendering
    draw_star                   # 5-pointed star
)
```

## Animation Concepts

### Shake/Vibrate
Offset object position with oscillation:
- Use `math.sin()` or `math.cos()` with frame index
- Add small random variations for natural feel
- Apply to x and/or y position

### Pulse/Heartbeat
Scale object size rhythmically:
- Use `math.sin(t * frequency * 2 * math.pi)` for smooth pulse
- For heartbeat: two quick pulses then pause (adjust sine wave)
- Scale between 0.8 and 1.2 of base size

### Bounce
Object falls and bounces:
- Use `interpolate()` with `easing='bounce_out'` for landing
- Use `easing='ease_in'` for falling (accelerating)
- Apply gravity by increasing y velocity each frame

### Spin/Rotate
Rotate object around center:
- PIL: `image.rotate(angle, resample=Image.BICUBIC)`
- For wobble: use sine wave for angle instead of linear

### Fade In/Out
Gradually appear or disappear:
- Create RGBA image, adjust alpha channel
- Or use `Image.blend(image1, image2, alpha)`
- Fade in: alpha from 0 to 1
- Fade out: alpha from 1 to 0

### Slide
Move object from off-screen to position:
- Start position: outside frame bounds
- End position: target location
- Use `interpolate()` with `easing='ease_out'` for smooth stop
- For overshoot: use `easing='back_out'`

### Zoom
Scale and position for zoom effect:
- Zoom in: scale from 0.1 to 2.0, crop center
- Zoom out: scale from 2.0 to 1.0
- Can add motion blur for drama (PIL filter)

### Explode/Particle Burst
Create particles radiating outward:
- Generate particles with random angles and velocities
- Update each particle: `x += vx`, `y += vy`
- Add gravity: `vy += gravity_constant`
- Fade out particles over time (reduce alpha)

## Optimization Strategies

Only when asked to make the file size smaller, implement a few of the following methods:

1. **Fewer frames** - Lower FPS (10 instead of 20) or shorter duration
2. **Fewer colors** - `num_colors=48` instead of 128
3. **Smaller dimensions** - 128x128 instead of 480x480
4. **Remove duplicates** - `remove_duplicates=True` in save()
5. **Emoji mode** - `optimize_for_emoji=True` auto-optimizes

```python
# Maximum optimization for emoji
builder.save(
    'emoji.gif',
    num_colors=48,
    optimize_for_emoji=True,
    remove_duplicates=True
)
```

## Philosophy

This skill provides:
- **Knowledge**: Slack's requirements and animation concepts
- **Utilities**: GIFBuilder, validators, easing functions
- **Flexibility**: Create the animation logic using PIL primitives

It does NOT provide:
- Rigid animation templates or pre-made functions
- Emoji font rendering (unreliable across platforms)
- A library of pre-packaged graphics built into the skill

**Note on user uploads**: This skill doesn't include pre-built graphics, but if a user uploads an image, use PIL to load and work with it - interpret based on their request whether they want it used directly or just as inspiration.

Be creative! Combine concepts (bouncing + rotating, pulsing + sliding, etc.) and use PIL's full capabilities.

## Dependencies

```bash
pip install pillow imageio numpy
```
```

Theme factory
```md
---
name: theme-factory
description: Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly.
license: Complete terms in LICENSE.txt
---


# Theme Factory Skill

This skill provides a curated collection of professional font and color themes themes, each with carefully selected color palettes and font pairings. Once a theme is chosen, it can be applied to any artifact.

## Purpose

To apply consistent, professional styling to presentation slide decks, use this skill. Each theme includes:
- A cohesive color palette with hex codes
- Complementary font pairings for headers and body text
- A distinct visual identity suitable for different contexts and audiences

## Usage Instructions

To apply styling to a slide deck or other artifact:

1. **Show the theme showcase**: Display the `theme-showcase.pdf` file to allow users to see all available themes visually. Do not make any modifications to it; simply show the file for viewing.
2. **Ask for their choice**: Ask which theme to apply to the deck
3. **Wait for selection**: Get explicit confirmation about the chosen theme
4. **Apply the theme**: Once a theme has been chosen, apply the selected theme's colors and fonts to the deck/artifact

## Themes Available

The following 10 themes are available, each showcased in `theme-showcase.pdf`:

1. **Ocean Depths** - Professional and calming maritime theme
2. **Sunset Boulevard** - Warm and vibrant sunset colors
3. **Forest Canopy** - Natural and grounded earth tones
4. **Modern Minimalist** - Clean and contemporary grayscale
5. **Golden Hour** - Rich and warm autumnal palette
6. **Arctic Frost** - Cool and crisp winter-inspired theme
7. **Desert Rose** - Soft and sophisticated dusty tones
8. **Tech Innovation** - Bold and modern tech aesthetic
9. **Botanical Garden** - Fresh and organic garden colors
10. **Midnight Galaxy** - Dramatic and cosmic deep tones

## Theme Details

Each theme is defined in the `themes/` directory with complete specifications including:
- Cohesive color palette with hex codes
- Complementary font pairings for headers and body text
- Distinct visual identity suitable for different contexts and audiences

## Application Process

After a preferred theme is selected:
1. Read the corresponding theme file from the `themes/` directory
2. Apply the specified colors and fonts consistently throughout the deck
3. Ensure proper contrast and readability
4. Maintain the theme's visual identity across all slides

## Create your Own Theme
To handle cases where none of the existing themes work for an artifact, create a custom theme. Based on provided inputs, generate a new theme similar to the ones above. Give the theme a similar name describing what the font/color combinations represent. Use any basic description provided to choose appropriate colors/fonts. After generating the theme, show it for review and verification. Following that, apply the theme as described above.
```

Web artifact builder
```md
---
name: web-artifacts-builder
description: Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.
license: Complete terms in LICENSE.txt
---

# Web Artifacts Builder

To build powerful frontend claude.ai artifacts, follow these steps:
1. Initialize the frontend repo using `scripts/init-artifact.sh`
2. Develop your artifact by editing the generated code
3. Bundle all code into a single HTML file using `scripts/bundle-artifact.sh`
4. Display artifact to user
5. (Optional) Test the artifact

**Stack**: React 18 + TypeScript + Vite + Parcel (bundling) + Tailwind CSS + shadcn/ui

## Design & Style Guidelines

VERY IMPORTANT: To avoid what is often referred to as "AI slop", avoid using excessive centered layouts, purple gradients, uniform rounded corners, and Inter font.

## Quick Start

### Step 1: Initialize Project

Run the initialization script to create a new React project:
```bash
bash scripts/init-artifact.sh <project-name>
cd <project-name>
```

This creates a fully configured project with:
- ✅ React + TypeScript (via Vite)
- ✅ Tailwind CSS 3.4.1 with shadcn/ui theming system
- ✅ Path aliases (`@/`) configured
- ✅ 40+ shadcn/ui components pre-installed
- ✅ All Radix UI dependencies included
- ✅ Parcel configured for bundling (via .parcelrc)
- ✅ Node 18+ compatibility (auto-detects and pins Vite version)

### Step 2: Develop Your Artifact

To build the artifact, edit the generated files. See **Common Development Tasks** below for guidance.

### Step 3: Bundle to Single HTML File

To bundle the React app into a single HTML artifact:
```bash
bash scripts/bundle-artifact.sh
```

This creates `bundle.html` - a self-contained artifact with all JavaScript, CSS, and dependencies inlined. This file can be directly shared in Claude conversations as an artifact.

**Requirements**: Your project must have an `index.html` in the root directory.

**What the script does**:
- Installs bundling dependencies (parcel, @parcel/config-default, parcel-resolver-tspaths, html-inline)
- Creates `.parcelrc` config with path alias support
- Builds with Parcel (no source maps)
- Inlines all assets into single HTML using html-inline

### Step 4: Share Artifact with User

Finally, share the bundled HTML file in conversation with the user so they can view it as an artifact.

### Step 5: Testing/Visualizing the Artifact (Optional)

Note: This is a completely optional step. Only perform if necessary or requested.

To test/visualize the artifact, use available tools (including other Skills or built-in tools like Playwright or Puppeteer). In general, avoid testing the artifact upfront as it adds latency between the request and when the finished artifact can be seen. Test later, after presenting the artifact, if requested or if issues arise.

## Reference

- **shadcn/ui components**: https://ui.shadcn.com/docs/components
```

Artifact builder
```md
---
name: artifacts-builder
description: Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components - not for simple single-file HTML/JSX artifacts.
license: Complete terms in LICENSE.txt
---

# Artifacts Builder

To build powerful frontend claude.ai artifacts, follow these steps:
1. Initialize the frontend repo using `scripts/init-artifact.sh`
2. Develop your artifact by editing the generated code
3. Bundle all code into a single HTML file using `scripts/bundle-artifact.sh`
4. Display artifact to user
5. (Optional) Test the artifact

**Stack**: React 18 + TypeScript + Vite + Parcel (bundling) + Tailwind CSS + shadcn/ui

## Design & Style Guidelines

VERY IMPORTANT: To avoid what is often referred to as "AI slop", avoid using excessive centered layouts, purple gradients, uniform rounded corners, and Inter font.

## Quick Start

### Step 1: Initialize Project

Run the initialization script to create a new React project:
```bash
bash scripts/init-artifact.sh <project-name>
cd <project-name>
```

This creates a fully configured project with:
- ✅ React + TypeScript (via Vite)
- ✅ Tailwind CSS 3.4.1 with shadcn/ui theming system
- ✅ Path aliases (`@/`) configured
- ✅ 40+ shadcn/ui components pre-installed
- ✅ All Radix UI dependencies included
- ✅ Parcel configured for bundling (via .parcelrc)
- ✅ Node 18+ compatibility (auto-detects and pins Vite version)

### Step 2: Develop Your Artifact

To build the artifact, edit the generated files. See **Common Development Tasks** below for guidance.

### Step 3: Bundle to Single HTML File

To bundle the React app into a single HTML artifact:
```bash
bash scripts/bundle-artifact.sh
```

This creates `bundle.html` - a self-contained artifact with all JavaScript, CSS, and dependencies inlined. This file can be directly shared in Claude conversations as an artifact.

**Requirements**: Your project must have an `index.html` in the root directory.

**What the script does**:
- Installs bundling dependencies (parcel, @parcel/config-default, parcel-resolver-tspaths, html-inline)
- Creates `.parcelrc` config with path alias support
- Builds with Parcel (no source maps)
- Inlines all assets into single HTML using html-inline

### Step 4: Share Artifact with User

Finally, share the bundled HTML file in conversation with the user so they can view it as an artifact.

### Step 5: Testing/Visualizing the Artifact (Optional)

Note: This is a completely optional step. Only perform if necessary or requested.

To test/visualize the artifact, use available tools (including other Skills or built-in tools like Playwright or Puppeteer). In general, avoid testing the artifact upfront as it adds latency between the request and when the finished artifact can be seen. Test later, after presenting the artifact, if requested or if issues arise.

## Reference

- **shadcn/ui components**: https://ui.shadcn.com/docs/components
```

Brand guideline
```md
---
name: brand-guidelines
description: Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand colors or style guidelines, visual formatting, or company design standards apply.
license: Complete terms in LICENSE.txt
---

# Anthropic Brand Styling

## Overview

To access Anthropic's official brand identity and style resources, use this skill.

**Keywords**: branding, corporate identity, visual identity, post-processing, styling, brand colors, typography, Anthropic brand, visual formatting, visual design

## Brand Guidelines

### Colors

**Main Colors:**

- Dark: `#141413` - Primary text and dark backgrounds
- Light: `#faf9f5` - Light backgrounds and text on dark
- Mid Gray: `#b0aea5` - Secondary elements
- Light Gray: `#e8e6dc` - Subtle backgrounds

**Accent Colors:**

- Orange: `#d97757` - Primary accent
- Blue: `#6a9bcc` - Secondary accent
- Green: `#788c5d` - Tertiary accent

### Typography

- **Headings**: Poppins (with Arial fallback)
- **Body Text**: Lora (with Georgia fallback)
- **Note**: Fonts should be pre-installed in your environment for best results

## Features

### Smart Font Application

- Applies Poppins font to headings (24pt and larger)
- Applies Lora font to body text
- Automatically falls back to Arial/Georgia if custom fonts unavailable
- Preserves readability across all systems

### Text Styling

- Headings (24pt+): Poppins font
- Body text: Lora font
- Smart color selection based on background
- Preserves text hierarchy and formatting

### Shape and Accent Colors

- Non-text shapes use accent colors
- Cycles through orange, blue, and green accents
- Maintains visual interest while staying on-brand

## Technical Details

### Font Management

- Uses system-installed Poppins and Lora fonts when available
- Provides automatic fallback to Arial (headings) and Georgia (body)
- No font installation required - works with existing system fonts
- For best results, pre-install Poppins and Lora fonts in your environment

### Color Application

- Uses RGB color values for precise brand matching
- Applied via python-pptx's RGBColor class
- Maintains color fidelity across different systems and formats
```

Canvas design
```md
---
name: canvas-design
description: Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations.
license: Complete terms in LICENSE.txt
---

These are instructions for creating design philosophies - aesthetic movements that are then EXPRESSED VISUALLY. Output only .md files, .pdf files, and .png files.

Complete this in two steps:
1. Design Philosophy Creation (.md file)
2. Express by creating it on a canvas (.pdf file or .png file)

First, undertake this task:

## DESIGN PHILOSOPHY CREATION

To begin, create a VISUAL PHILOSOPHY (not layouts or templates) that will be interpreted through:
- Form, space, color, composition
- Images, graphics, shapes, patterns
- Minimal text as visual accent

### THE CRITICAL UNDERSTANDING
- What is received: Some subtle input or instructions by the user that should be taken into account, but used as a foundation; it should not constrain creative freedom.
- What is created: A design philosophy/aesthetic movement.
- What happens next: Then, the same version receives the philosophy and EXPRESSES IT VISUALLY - creating artifacts that are 90% visual design, 10% essential text.

Consider this approach:
- Write a manifesto for an art movement
- The next phase involves making the artwork

The philosophy must emphasize: Visual expression. Spatial communication. Artistic interpretation. Minimal words.

### HOW TO GENERATE A VISUAL PHILOSOPHY

**Name the movement** (1-2 words): "Brutalist Joy" / "Chromatic Silence" / "Metabolist Dreams"

**Articulate the philosophy** (4-6 paragraphs - concise but complete):

To capture the VISUAL essence, express how the philosophy manifests through:
- Space and form
- Color and material
- Scale and rhythm
- Composition and balance
- Visual hierarchy

**CRITICAL GUIDELINES:**
- **Avoid redundancy**: Each design aspect should be mentioned once. Avoid repeating points about color theory, spatial relationships, or typographic principles unless adding new depth.
- **Emphasize craftsmanship REPEATEDLY**: The philosophy MUST stress multiple times that the final work should appear as though it took countless hours to create, was labored over with care, and comes from someone at the absolute top of their field. This framing is essential - repeat phrases like "meticulously crafted," "the product of deep expertise," "painstaking attention," "master-level execution."
- **Leave creative space**: Remain specific about the aesthetic direction, but concise enough that the next Claude has room to make interpretive choices also at a extremely high level of craftmanship.

The philosophy must guide the next version to express ideas VISUALLY, not through text. Information lives in design, not paragraphs.

### PHILOSOPHY EXAMPLES

**"Concrete Poetry"**
Philosophy: Communication through monumental form and bold geometry.
Visual expression: Massive color blocks, sculptural typography (huge single words, tiny labels), Brutalist spatial divisions, Polish poster energy meets Le Corbusier. Ideas expressed through visual weight and spatial tension, not explanation. Text as rare, powerful gesture - never paragraphs, only essential words integrated into the visual architecture. Every element placed with the precision of a master craftsman.

**"Chromatic Language"**
Philosophy: Color as the primary information system.
Visual expression: Geometric precision where color zones create meaning. Typography minimal - small sans-serif labels letting chromatic fields communicate. Think Josef Albers' interaction meets data visualization. Information encoded spatially and chromatically. Words only to anchor what color already shows. The result of painstaking chromatic calibration.

**"Analog Meditation"**
Philosophy: Quiet visual contemplation through texture and breathing room.
Visual expression: Paper grain, ink bleeds, vast negative space. Photography and illustration dominate. Typography whispered (small, restrained, serving the visual). Japanese photobook aesthetic. Images breathe across pages. Text appears sparingly - short phrases, never explanatory blocks. Each composition balanced with the care of a meditation practice.

**"Organic Systems"**
Philosophy: Natural clustering and modular growth patterns.
Visual expression: Rounded forms, organic arrangements, color from nature through architecture. Information shown through visual diagrams, spatial relationships, iconography. Text only for key labels floating in space. The composition tells the story through expert spatial orchestration.

**"Geometric Silence"**
Philosophy: Pure order and restraint.
Visual expression: Grid-based precision, bold photography or stark graphics, dramatic negative space. Typography precise but minimal - small essential text, large quiet zones. Swiss formalism meets Brutalist material honesty. Structure communicates, not words. Every alignment the work of countless refinements.

*These are condensed examples. The actual design philosophy should be 4-6 substantial paragraphs.*

### ESSENTIAL PRINCIPLES
- **VISUAL PHILOSOPHY**: Create an aesthetic worldview to be expressed through design
- **MINIMAL TEXT**: Always emphasize that text is sparse, essential-only, integrated as visual element - never lengthy
- **SPATIAL EXPRESSION**: Ideas communicate through space, form, color, composition - not paragraphs
- **ARTISTIC FREEDOM**: The next Claude interprets the philosophy visually - provide creative room
- **PURE DESIGN**: This is about making ART OBJECTS, not documents with decoration
- **EXPERT CRAFTSMANSHIP**: Repeatedly emphasize the final work must look meticulously crafted, labored over with care, the product of countless hours by someone at the top of their field

**The design philosophy should be 4-6 paragraphs long.** Fill it with poetic design philosophy that brings together the core vision. Avoid repeating the same points. Keep the design philosophy generic without mentioning the intention of the art, as if it can be used wherever. Output the design philosophy as a .md file.

---

## DEDUCING THE SUBTLE REFERENCE

**CRITICAL STEP**: Before creating the canvas, identify the subtle conceptual thread from the original request.

**THE ESSENTIAL PRINCIPLE**:
The topic is a **subtle, niche reference embedded within the art itself** - not always literal, always sophisticated. Someone familiar with the subject should feel it intuitively, while others simply experience a masterful abstract composition. The design philosophy provides the aesthetic language. The deduced topic provides the soul - the quiet conceptual DNA woven invisibly into form, color, and composition.

This is **VERY IMPORTANT**: The reference must be refined so it enhances the work's depth without announcing itself. Think like a jazz musician quoting another song - only those who know will catch it, but everyone appreciates the music.

---

## CANVAS CREATION

With both the philosophy and the conceptual framework established, express it on a canvas. Take a moment to gather thoughts and clear the mind. Use the design philosophy created and the instructions below to craft a masterpiece, embodying all aspects of the philosophy with expert craftsmanship.

**IMPORTANT**: For any type of content, even if the user requests something for a movie/game/book, the approach should still be sophisticated. Never lose sight of the idea that this should be art, not something that's cartoony or amateur.

To create museum or magazine quality work, use the design philosophy as the foundation. Create one single page, highly visual, design-forward PDF or PNG output (unless asked for more pages). Generally use repeating patterns and perfect shapes. Treat the abstract philosophical design as if it were a scientific bible, borrowing the visual language of systematic observation—dense accumulation of marks, repeated elements, or layered patterns that build meaning through patient repetition and reward sustained viewing. Add sparse, clinical typography and systematic reference markers that suggest this could be a diagram from an imaginary discipline, treating the invisible subject with the same reverence typically reserved for documenting observable phenomena. Anchor the piece with simple phrase(s) or details positioned subtly, using a limited color palette that feels intentional and cohesive. Embrace the paradox of using analytical visual language to express ideas about human experience: the result should feel like an artifact that proves something ephemeral can be studied, mapped, and understood through careful attention. This is true art. 

**Text as a contextual element**: Text is always minimal and visual-first, but let context guide whether that means whisper-quiet labels or bold typographic gestures. A punk venue poster might have larger, more aggressive type than a minimalist ceramics studio identity. Most of the time, font should be thin. All use of fonts must be design-forward and prioritize visual communication. Regardless of text scale, nothing falls off the page and nothing overlaps. Every element must be contained within the canvas boundaries with proper margins. Check carefully that all text, graphics, and visual elements have breathing room and clear separation. This is non-negotiable for professional execution. **IMPORTANT: Use different fonts if writing text. Search the `./canvas-fonts` directory. Regardless of approach, sophistication is non-negotiable.**

Download and use whatever fonts are needed to make this a reality. Get creative by making the typography actually part of the art itself -- if the art is abstract, bring the font onto the canvas, not typeset digitally.

To push boundaries, follow design instinct/intuition while using the philosophy as a guiding principle. Embrace ultimate design freedom and choice. Push aesthetics and design to the frontier. 

**CRITICAL**: To achieve human-crafted quality (not AI-generated), create work that looks like it took countless hours. Make it appear as though someone at the absolute top of their field labored over every detail with painstaking care. Ensure the composition, spacing, color choices, typography - everything screams expert-level craftsmanship. Double-check that nothing overlaps, formatting is flawless, every detail perfect. Create something that could be shown to people to prove expertise and rank as undeniably impressive.

Output the final result as a single, downloadable .pdf or .png file, alongside the design philosophy used as a .md file.

---

## FINAL STEP

**IMPORTANT**: The user ALREADY said "It isn't perfect enough. It must be pristine, a masterpiece if craftsmanship, as if it were about to be displayed in a museum."

**CRITICAL**: To refine the work, avoid adding more graphics; instead refine what has been created and make it extremely crisp, respecting the design philosophy and the principles of minimalism entirely. Rather than adding a fun filter or refactoring a font, consider how to make the existing composition more cohesive with the art. If the instinct is to call a new function or draw a new shape, STOP and instead ask: "How can I make what's already here more of a piece of art?"

Take a second pass. Go back to the code and refine/polish further to make this a philosophically designed masterpiece.

## MULTI-PAGE OPTION

To create additional pages when requested, create more creative pages along the same lines as the design philosophy but distinctly different as well. Bundle those pages in the same .pdf or many .pngs. Treat the first page as just a single page in a whole coffee table book waiting to be filled. Make the next pages unique twists and memories of the original. Have them almost tell a story in a very tasteful way. Exercise full creative freedom.
```

Changelog generator
```md
---
name: changelog-generator
description: Automatically creates user-facing changelogs from git commits by analyzing commit history, categorizing changes, and transforming technical commits into clear, customer-friendly release notes. Turns hours of manual changelog writing into minutes of automated generation.
---

# Changelog Generator

This skill transforms technical git commits into polished, user-friendly changelogs that your customers and users will actually understand and appreciate.

## When to Use This Skill

- Preparing release notes for a new version
- Creating weekly or monthly product update summaries
- Documenting changes for customers
- Writing changelog entries for app store submissions
- Generating update notifications
- Creating internal release documentation
- Maintaining a public changelog/product updates page

## What This Skill Does

1. **Scans Git History**: Analyzes commits from a specific time period or between versions
2. **Categorizes Changes**: Groups commits into logical categories (features, improvements, bug fixes, breaking changes, security)
3. **Translates Technical → User-Friendly**: Converts developer commits into customer language
4. **Formats Professionally**: Creates clean, structured changelog entries
5. **Filters Noise**: Excludes internal commits (refactoring, tests, etc.)
6. **Follows Best Practices**: Applies changelog guidelines and your brand voice

## How to Use

### Basic Usage

From your project repository:

```
Create a changelog from commits since last release
```

```
Generate changelog for all commits from the past week
```

```
Create release notes for version 2.5.0
```

### With Specific Date Range

```
Create a changelog for all commits between March 1 and March 15
```

### With Custom Guidelines

```
Create a changelog for commits since v2.4.0, using my changelog 
guidelines from CHANGELOG_STYLE.md
```

## Example

**User**: "Create a changelog for commits from the past 7 days"

**Output**:
```markdown
# Updates - Week of March 10, 2024

## ✨ New Features

- **Team Workspaces**: Create separate workspaces for different 
  projects. Invite team members and keep everything organized.

- **Keyboard Shortcuts**: Press ? to see all available shortcuts. 
  Navigate faster without touching your mouse.

## 🔧 Improvements

- **Faster Sync**: Files now sync 2x faster across devices
- **Better Search**: Search now includes file contents, not just titles

## 🐛 Fixes

- Fixed issue where large images wouldn't upload
- Resolved timezone confusion in scheduled posts
- Corrected notification badge count
```

**Inspired by:** Manik Aggarwal's use case from Lenny's Newsletter

## Tips

- Run from your git repository root
- Specify date ranges for focused changelogs
- Use your CHANGELOG_STYLE.md for consistent formatting
- Review and adjust the generated changelog before publishing
- Save output directly to CHANGELOG.md

## Related Use Cases

- Creating GitHub release notes
- Writing app store update descriptions
- Generating email updates for users
- Creating social media announcement posts
```

Competitive ads extractor
```md
---
name: competitive-ads-extractor
description: Extracts and analyzes competitors' ads from ad libraries (Facebook, LinkedIn, etc.) to understand what messaging, problems, and creative approaches are working. Helps inspire and improve your own ad campaigns.
---

# Competitive Ads Extractor

This skill extracts your competitors' ads from ad libraries and analyzes what's working—the problems they're highlighting, use cases they're targeting, and copy/creative that's resonating.

## When to Use This Skill

- Researching competitor ad strategies
- Finding inspiration for your own ads
- Understanding market positioning
- Identifying successful ad patterns
- Analyzing messaging that works
- Discovering new use cases or pain points
- Planning ad campaigns with proven concepts

## What This Skill Does

1. **Extracts Ads**: Scrapes ads from Facebook Ad Library, LinkedIn, etc.
2. **Captures Screenshots**: Saves visual copies of all ads
3. **Analyzes Messaging**: Identifies problems, use cases, and value props
4. **Categorizes Ads**: Groups by theme, audience, or format
5. **Identifies Patterns**: Finds common successful approaches
6. **Provides Insights**: Explains why certain ads likely perform well

## How to Use

### Basic Extraction

```
Extract all current ads from [Competitor Name] on Facebook Ad Library
```

```
Scrape ads from [Company] and analyze their messaging
```

### Specific Analysis

```
Get all ads from [Competitor] focusing on their messaging 
about [specific problem]. What pain points are they highlighting?
```

### Competitive Set

```
Extract ads from these 5 competitors: [list]. 
Compare their approaches and tell me what's working.
```

### Specific Platform

```
Get LinkedIn ads from [Competitor] and analyze their 
B2B positioning strategy
```

## Example

**User**: "Extract ads from Notion on Facebook Ad Library and tell me what messaging is working for them."

**Process**:
```
Accessing Facebook Ad Library...
Searching for: Notion
Found: 23 active ads

Extracting screenshots...
[████████████████████] 100%

Saved to: competitor-ads/notion/
- ad-001-collaboration.png
- ad-002-productivity.png
- ad-003-templates.png
...

Analyzing messaging...
```

**Output**:
```
# Notion Ad Analysis

## Overview
- Total Ads: 23 active
- Primary Themes: Productivity (35%), Collaboration (30%), 
  Templates (20%), AI Features (15%)
- Ad Formats: Static images (60%), Video (40%)
- CTA Patterns: "Try for free", "Get started"

## Key Problems They're Highlighting

1. **Scattered Information** (8 ads)
   Copy: "Stop switching between 10 different tools"
   Why it works: Direct pain point many teams face

2. **Meeting Overload** (5 ads)
   Copy: "Replace unnecessary meetings with async updates"
   Why it works: Post-COVID remote work pain point

3. **Lost Documentation** (4 ads)
   Copy: "Never ask 'where is that doc?' again"
   Why it works: Universal workplace frustration

## Successful Creative Patterns

### Pattern 1: Before/After Split
- Shows chaotic tool landscape → Clean Notion workspace
- Used in 6 high-performing ads
- Visual metaphor is immediately clear

### Pattern 2: Feature Showcase
- GIF of actual product usage
- Shows specific feature in 5 seconds
- Used for new features (AI, templates)

### Pattern 3: Social Proof
- "Join 20M users" messaging
- Customer logos
- Used in 4 ads targeting enterprise

## Copy That's Working

Best Headlines:
1. "Your team's knowledge, finally in one place"
   → Benefit-focused, addresses pain directly
   
2. "The all-in-one workspace"
   → Clear positioning, broad appeal
   
3. "AI that actually helps you work"
   → Addresses AI skepticism, practical angle

Best Body Copy Patterns:
- Short sentences (under 10 words)
- Focus on outcomes not features
- Include specific numbers ("Cut meetings by 50%")

## Audience Targeting Insights

Based on ad variations:
- Startup founders: Solo productivity angle
- Team leads: Collaboration and alignment
- Enterprise: Security and compliance mentions
- Students: Free plan, templates, organization

## Recommendations for Your Ads

1. **Test the "tool sprawl" pain point**
   → Strong resonance based on their ad frequency

2. **Use product screenshots over abstract visuals**
   → All their top ads show actual UI

3. **Lead with the problem, not the solution**
   → "Tired of X?" performs better than "Introducing Y"

4. **Keep copy under 100 characters**
   → Their shortest ads seem most frequent

5. **Test before/after visual formats**
   → Proven pattern in their creative

## Files Saved
- All ads: ~/competitor-ads/notion/
- Analysis: ~/competitor-ads/notion/analysis.md
- Best performers: ~/competitor-ads/notion/top-10/
```

**Inspired by:** Sumant Subrahmanya's use case from Lenny's Newsletter

## What You Can Learn

### Messaging Analysis
- What problems they emphasize
- How they position against competition
- Value propositions that resonate
- Target audience segments

### Creative Patterns
- Visual styles that work
- Video vs. static image performance
- Color schemes and branding
- Layout patterns

### Copy Formulas
- Headline structures
- Call-to-action patterns
- Length and tone
- Emotional triggers

### Campaign Strategy
- Seasonal campaigns
- Product launch approaches
- Feature announcement tactics
- Retargeting patterns

## Best Practices

### Legal & Ethical
✓ Only use for research and inspiration
✓ Don't copy ads directly
✓ Respect intellectual property
✓ Use insights to inform original creative
✗ Don't plagiarize copy or steal designs

### Analysis Tips
1. **Look for patterns**: What themes repeat?
2. **Track over time**: Save ads monthly to see evolution
3. **Test hypotheses**: Adapt successful patterns for your brand
4. **Segment by audience**: Different messages for different targets
5. **Compare platforms**: LinkedIn vs Facebook messaging differs

## Advanced Features

### Trend Tracking
```
Compare [Competitor]'s ads from Q1 vs Q2. 
What messaging has changed?
```

### Multi-Competitor Analysis
```
Extract ads from [Company A], [Company B], [Company C]. 
What are the common patterns? Where do they differ?
```

### Industry Benchmarks
```
Show me ad patterns across the top 10 project management 
tools. What problems do they all focus on?
```

### Format Analysis
```
Analyze video ads vs static image ads from [Competitor]. 
Which gets more engagement? (if data available)
```

## Common Workflows

### Ad Campaign Planning
1. Extract competitor ads
2. Identify successful patterns
3. Note gaps in their messaging
4. Brainstorm unique angles
5. Draft test ad variations

### Positioning Research
1. Get ads from 5 competitors
2. Map their positioning
3. Find underserved angles
4. Develop differentiated messaging
5. Test against their approaches

### Creative Inspiration
1. Extract ads by theme
2. Analyze visual patterns
3. Note color and layout trends
4. Adapt successful patterns
5. Create original variations

## Tips for Success

1. **Regular Monitoring**: Check monthly for changes
2. **Broad Research**: Look at adjacent competitors too
3. **Save Everything**: Build a reference library
4. **Test Insights**: Run your own experiments
5. **Track Performance**: A/B test inspired concepts
6. **Stay Original**: Use for inspiration, not copying
7. **Multiple Platforms**: Compare Facebook, LinkedIn, TikTok, etc.

## Output Formats

- **Screenshots**: All ads saved as images
- **Analysis Report**: Markdown summary of insights
- **Spreadsheet**: CSV with ad copy, CTAs, themes
- **Presentation**: Visual deck of top performers
- **Pattern Library**: Categorized by approach

## Related Use Cases

- Writing better ad copy for your campaigns
- Understanding market positioning
- Finding content gaps in your messaging
- Discovering new use cases for your product
- Planning product marketing strategy
- Inspiring social media content
```

Connect apps
```md
---
name: connect-apps
description: Connect Claude to external apps like Gmail, Slack, GitHub. Use this skill when the user wants to send emails, create issues, post messages, or take actions in external services.
---

# Connect Apps

Connect Claude to 1000+ apps. Actually send emails, create issues, post messages - not just generate text about it.

## Quick Start

### Step 1: Install the Plugin

```
/plugin install composio-toolrouter
```

### Step 2: Run Setup

```
/composio-toolrouter:setup
```

This will:
- Ask for your free API key (get one at [platform.composio.dev](https://platform.composio.dev/?utm_source=Github&utm_content=AwesomeSkills))
- Configure Claude's connection to 1000+ apps
- Take about 60 seconds

### Step 3: Try It!

After setup, restart Claude Code and try:

```
Send me a test email at YOUR_EMAIL@example.com
```

If it works, you're connected!

## What You Can Do

| Ask Claude to... | What happens |
|------------------|--------------|
| "Send email to sarah@acme.com about the launch" | Actually sends the email |
| "Create GitHub issue: fix login bug" | Creates the issue |
| "Post to Slack #general: deploy complete" | Posts the message |
| "Add meeting notes to Notion" | Adds to Notion |

## Supported Apps

**Email:** Gmail, Outlook, SendGrid
**Chat:** Slack, Discord, Teams, Telegram
**Dev:** GitHub, GitLab, Jira, Linear
**Docs:** Notion, Google Docs, Confluence
**Data:** Sheets, Airtable, PostgreSQL
**And 1000+ more...**

## How It Works

1. You ask Claude to do something
2. Composio Tool Router finds the right tool
3. First time? You'll authorize via OAuth (one-time)
4. Action executes and returns result

## Troubleshooting

- **"Plugin not found"** → Make sure you ran `/plugin install composio-toolrouter`
- **"Need to authorize"** → Click the OAuth link Claude provides, then say "done"
- **Action failed** → Check you have permissions in the target app

---

<p align="center">
  <b>Join 20,000+ developers building agents that ship</b>
</p>

<p align="center">
  <a href="https://platform.composio.dev/?utm_source=Github&utm_content=AwesomeSkills">
    <img src="https://img.shields.io/badge/Get_Started_Free-4F46E5?style=for-the-badge" alt="Get Started"/>
  </a>
</p>
```
Connect
```md
---
name: connect
description: Connect Claude to any app. Send emails, create issues, post messages, update databases - take real actions across Gmail, Slack, GitHub, Notion, and 1000+ services.
---

# Connect

Connect Claude to any app. Stop generating text about what you could do - actually do it.

## When to Use This Skill

Use this skill when you need Claude to:

- **Send that email** instead of drafting it
- **Create that issue** instead of describing it
- **Post that message** instead of suggesting it
- **Update that database** instead of explaining how

## What Changes

| Without Connect | With Connect |
|-----------------|--------------|
| "Here's a draft email..." | Sends the email |
| "You should create an issue..." | Creates the issue |
| "Post this to Slack..." | Posts it |
| "Add this to Notion..." | Adds it |

## Supported Apps

**1000+ integrations** including:

- **Email:** Gmail, Outlook, SendGrid
- **Chat:** Slack, Discord, Teams, Telegram
- **Dev:** GitHub, GitLab, Jira, Linear
- **Docs:** Notion, Google Docs, Confluence
- **Data:** Sheets, Airtable, PostgreSQL
- **CRM:** HubSpot, Salesforce, Pipedrive
- **Storage:** Drive, Dropbox, S3
- **Social:** Twitter, LinkedIn, Reddit

## Setup

### 1. Get API Key

Get your free key at [platform.composio.dev](https://platform.composio.dev/?utm_source=Github&utm_content=AwesomeSkills)

### 2. Set Environment Variable

```bash
export COMPOSIO_API_KEY="your-key"
```

### 3. Install

```bash
pip install composio          # Python
npm install @composio/core    # TypeScript
```

Done. Claude can now connect to any app.

## Examples

### Send Email
```
Email sarah@acme.com - Subject: "Shipped!" Body: "v2.0 is live, let me know if issues"
```

### Create GitHub Issue
```
Create issue in my-org/repo: "Mobile timeout bug" with label:bug
```

### Post to Slack
```
Post to #engineering: "Deploy complete - v2.4.0 live"
```

### Chain Actions
```
Find GitHub issues labeled "bug" from this week, summarize, post to #bugs on Slack
```

## How It Works

Uses Composio Tool Router:

1. **You ask** Claude to do something
2. **Tool Router finds** the right tool (1000+ options)
3. **OAuth handled** automatically
4. **Action executes** and returns result

### Code

```python
from composio import Composio
from claude_agent_sdk.client import ClaudeSDKClient
from claude_agent_sdk.types import ClaudeAgentOptions
import os

composio = Composio(api_key=os.environ["COMPOSIO_API_KEY"])
session = composio.create(user_id="user_123")

options = ClaudeAgentOptions(
    system_prompt="You can take actions in external apps.",
    mcp_servers={
        "composio": {
            "type": "http",
            "url": session.mcp.url,
            "headers": {"x-api-key": os.environ["COMPOSIO_API_KEY"]},
        }
    },
)

async with ClaudeSDKClient(options) as client:
    await client.query("Send Slack message to #general: Hello!")
```

## Auth Flow

First time using an app:
```
To send emails, I need Gmail access.
Authorize here: https://...
Say "connected" when done.
```

Connection persists after that.

## Framework Support

| Framework | Install |
|-----------|---------|
| Claude Agent SDK | `pip install composio claude-agent-sdk` |
| OpenAI Agents | `pip install composio openai-agents` |
| Vercel AI | `npm install @composio/core @composio/vercel` |
| LangChain | `pip install composio-langchain` |
| Any MCP Client | Use `session.mcp.url` |

## Troubleshooting

- **Auth required** → Click link, authorize, say "connected"
- **Action failed** → Check permissions in target app
- **Tool not found** → Be specific: "Slack #general" not "send message"

---

<p align="center">
  <b>Join 20,000+ developers building agents that ship</b>
</p>

<p align="center">
  <a href="https://platform.composio.dev/?utm_source=Github&utm_content=AwesomeSkills">
    <img src="https://img.shields.io/badge/Get_Started_Free-4F46E5?style=for-the-badge" alt="Get Started"/>
  </a>
</p>
```

Domain name brainstormer
```md
---
name: domain-name-brainstormer
description: Generates creative domain name ideas for your project and checks availability across multiple TLDs (.com, .io, .dev, .ai, etc.). Saves hours of brainstorming and manual checking.
---

# Domain Name Brainstormer

This skill helps you find the perfect domain name for your project by generating creative options and checking what's actually available to register.

## When to Use This Skill

- Starting a new project or company
- Launching a product or service
- Creating a personal brand or portfolio site
- Rebranding an existing project
- Registering a domain for a side project
- Finding available alternatives when your first choice is taken

## What This Skill Does

1. **Understands Your Project**: Analyzes what you're building and who it's for
2. **Generates Creative Names**: Creates relevant, memorable domain options
3. **Checks Availability**: Verifies which domains are actually available across multiple TLDs
4. **Multiple Extensions**: Suggests .com, .io, .dev, .ai, .app, and more
5. **Provides Alternatives**: Offers variations if top choices are taken
6. **Branding Insights**: Explains why certain names work well

## How to Use

### Basic Brainstorming

```
I'm building a project management tool for remote teams. 
Suggest domain names.
```

```
Help me brainstorm domain names for a personal finance app
```

### Specific Preferences

```
I need a domain name for my AI writing assistant. 
Prefer short names with .ai or .io extension.
```

### With Keywords

```
Suggest domain names using the words "pixel" or "studio" 
for my design agency
```

## Example

**User**: "I'm building a tool for developers to share code snippets. Suggest creative domain names."

**Output**:
```
Analyzing your project...
Target audience: Developers
Key features: Code sharing, snippets, collaboration

🎯 Domain Name Suggestions

## Available (.com)
1. ✓ snippetbox.com - Clear, memorable, available!
   Why: Directly describes the product, easy to remember

2. ✓ codeclip.com - Short and snappy
   Why: Implies quick code sharing, only 8 characters

3. ✓ devpaste.com - Developer-focused
   Why: Familiar to devs (like pastebin), clear purpose

## Available (Alternative TLDs)
4. ✓ snippet.dev - Perfect extension for developers
   Why: .dev extension signals developer tool

5. ✓ codebox.io - Tech-forward
   Why: .io popular with tech startups, clean name

6. ✓ sharecode.app - Descriptive
   Why: .app extension, clearly states the action

## Premium/Taken (.com)
- codeshare.com (Taken, est. $2,500)
- snippets.com (Taken, premium domain)

## Recommendations

🏆 Top Pick: snippet.dev
- Perfect for developer audience
- Short and memorable  
- .dev extension adds credibility
- Available now!

🥈 Runner-up: snippetbox.com
- .com is universally recognized
- Slightly longer but descriptive
- Great brandability

Next steps:
1. Register your favorite before someone else does!
2. Want me to check more variations?
3. Need help with logo ideas for these names?
```

**Inspired by:** Ben Aiad's use case from Lenny's Newsletter

## Domain Naming Tips

### What Makes a Good Domain

✓ **Short**: Under 15 characters ideal
✓ **Memorable**: Easy to recall and spell
✓ **Pronounceable**: Can be said in conversation
✓ **Descriptive**: Hints at what you do
✓ **Brandable**: Unique enough to stand out
✓ **No hyphens**: Easier to share verbally

### TLD Guide

- **.com**: Universal, trusted, great for businesses
- **.io**: Tech startups, developer tools
- **.dev**: Developer-focused products
- **.ai**: AI/ML products
- **.app**: Mobile or web applications
- **.co**: Alternative to .com
- **.xyz**: Modern, creative projects
- **.design**: Creative/design agencies
- **.tech**: Technology companies

## Advanced Features

### Check Similar Variations

```
Check availability for "codebase" and similar variations 
across .com, .io, .dev
```

### Industry-Specific

```
Suggest domain names for a sustainable fashion brand, 
checking .eco and .fashion TLDs
```

### Multilingual Options

```
Brainstorm domain names in English and Spanish for 
a language learning app
```

### Competitor Analysis

```
Show me domain patterns used by successful project 
management tools, then suggest similar available ones
```

## Example Workflows

### Startup Launch
1. Describe your startup idea
2. Get 10-15 domain suggestions across TLDs
3. Review availability and pricing
4. Pick top 3 favorites
5. Register immediately

### Personal Brand
1. Share your name and profession
2. Get variations (firstname.com, firstnamelastname.dev, etc.)
3. Check social media handle availability too
4. Register consistent brand across platforms

### Product Naming
1. Describe product and target market
2. Get creative, brandable names
3. Check trademark conflicts
4. Verify domain and social availability
5. Test names with target audience

## Tips for Success

1. **Act Fast**: Good domains get taken quickly
2. **Register Variations**: Get .com and .io to protect brand
3. **Avoid Numbers**: Hard to communicate verbally
4. **Check Social Media**: Make sure @username is available too
5. **Say It Out Loud**: Test if it's easy to pronounce
6. **Check Trademarks**: Ensure no legal conflicts
7. **Think Long-term**: Will it still make sense in 5 years?

## Pricing Context

When suggesting domains, I'll note:
- Standard domains: ~$10-15/year
- Premium TLDs (.io, .ai): ~$30-50/year
- Taken domains: Market price if listed
- Premium domains: $hundreds to $thousands

## Related Tools

After picking a domain:
- Check logo design options
- Verify social media handles
- Research trademark availability
- Plan brand identity colors/fonts
- Set up website hosting options
- Create email addresses with your new domain
```

File organizer
```md
---
name: file-organizer
description: Intelligently organizes your files and folders across your computer by understanding context, finding duplicates, suggesting better structures, and automating cleanup tasks. Reduces cognitive load and keeps your digital workspace tidy without manual effort.
---

# File Organizer

This skill acts as your personal organization assistant, helping you maintain a clean, logical file structure across your computer without the mental overhead of constant manual organization.

## When to Use This Skill

- Your Downloads folder is a chaotic mess
- You can't find files because they're scattered everywhere
- You have duplicate files taking up space
- Your folder structure doesn't make sense anymore
- You want to establish better organization habits
- You're starting a new project and need a good structure
- You're cleaning up before archiving old projects

## What This Skill Does

1. **Analyzes Current Structure**: Reviews your folders and files to understand what you have
2. **Finds Duplicates**: Identifies duplicate files across your system
3. **Suggests Organization**: Proposes logical folder structures based on your content
4. **Automates Cleanup**: Moves, renames, and organizes files with your approval
5. **Maintains Context**: Makes smart decisions based on file types, dates, and content
6. **Reduces Clutter**: Identifies old files you probably don't need anymore

## How to Use

### From Your Home Directory

```
cd ~
```

Then run Claude Code and ask for help:

```
Help me organize my Downloads folder
```

```
Find duplicate files in my Documents folder
```

```
Review my project directories and suggest improvements
```

### Specific Organization Tasks

```
Organize these downloads into proper folders based on what they are
```

```
Find duplicate files and help me decide which to keep
```

```
Clean up old files I haven't touched in 6+ months
```

```
Create a better folder structure for my [work/projects/photos/etc]
```

## Instructions

When a user requests file organization help:

1. **Understand the Scope**
   
   Ask clarifying questions:
   - Which directory needs organization? (Downloads, Documents, entire home folder?)
   - What's the main problem? (Can't find things, duplicates, too messy, no structure?)
   - Any files or folders to avoid? (Current projects, sensitive data?)
   - How aggressively to organize? (Conservative vs. comprehensive cleanup)

2. **Analyze Current State**
   
   Review the target directory:
   ```bash
   # Get overview of current structure
   ls -la [target_directory]
   
   # Check file types and sizes
   find [target_directory] -type f -exec file {} \; | head -20
   
   # Identify largest files
   du -sh [target_directory]/* | sort -rh | head -20
   
   # Count file types
   find [target_directory] -type f | sed 's/.*\.//' | sort | uniq -c | sort -rn
   ```
   
   Summarize findings:
   - Total files and folders
   - File type breakdown
   - Size distribution
   - Date ranges
   - Obvious organization issues

3. **Identify Organization Patterns**
   
   Based on the files, determine logical groupings:
   
   **By Type**:
   - Documents (PDFs, DOCX, TXT)
   - Images (JPG, PNG, SVG)
   - Videos (MP4, MOV)
   - Archives (ZIP, TAR, DMG)
   - Code/Projects (directories with code)
   - Spreadsheets (XLSX, CSV)
   - Presentations (PPTX, KEY)
   
   **By Purpose**:
   - Work vs. Personal
   - Active vs. Archive
   - Project-specific
   - Reference materials
   - Temporary/scratch files
   
   **By Date**:
   - Current year/month
   - Previous years
   - Very old (archive candidates)

4. **Find Duplicates**
   
   When requested, search for duplicates:
   ```bash
   # Find exact duplicates by hash
   find [directory] -type f -exec md5 {} \; | sort | uniq -d
   
   # Find files with same name
   find [directory] -type f -printf '%f\n' | sort | uniq -d
   
   # Find similar-sized files
   find [directory] -type f -printf '%s %p\n' | sort -n
   ```
   
   For each set of duplicates:
   - Show all file paths
   - Display sizes and modification dates
   - Recommend which to keep (usually newest or best-named)
   - **Important**: Always ask for confirmation before deleting

5. **Propose Organization Plan**
   
   Present a clear plan before making changes:
   
   ```markdown
   # Organization Plan for [Directory]
   
   ## Current State
   - X files across Y folders
   - [Size] total
   - File types: [breakdown]
   - Issues: [list problems]
   
   ## Proposed Structure
   
   ```
   [Directory]/
   ├── Work/
   │   ├── Projects/
   │   ├── Documents/
   │   └── Archive/
   ├── Personal/
   │   ├── Photos/
   │   ├── Documents/
   │   └── Media/
   └── Downloads/
       ├── To-Sort/
       └── Archive/
   ```
   
   ## Changes I'll Make
   
   1. **Create new folders**: [list]
   2. **Move files**:
      - X PDFs → Work/Documents/
      - Y images → Personal/Photos/
      - Z old files → Archive/
   3. **Rename files**: [any renaming patterns]
   4. **Delete**: [duplicates or trash files]
   
   ## Files Needing Your Decision
   
   - [List any files you're unsure about]
   
   Ready to proceed? (yes/no/modify)
   ```

6. **Execute Organization**
   
   After approval, organize systematically:
   
   ```bash
   # Create folder structure
   mkdir -p "path/to/new/folders"
   
   # Move files with clear logging
   mv "old/path/file.pdf" "new/path/file.pdf"
   
   # Rename files with consistent patterns
   # Example: "YYYY-MM-DD - Description.ext"
   ```
   
   **Important Rules**:
   - Always confirm before deleting anything
   - Log all moves for potential undo
   - Preserve original modification dates
   - Handle filename conflicts gracefully
   - Stop and ask if you encounter unexpected situations

7. **Provide Summary and Maintenance Tips**
   
   After organizing:
   
   ```markdown
   # Organization Complete! ✨
   
   ## What Changed
   
   - Created [X] new folders
   - Organized [Y] files
   - Freed [Z] GB by removing duplicates
   - Archived [W] old files
   
   ## New Structure
   
   [Show the new folder tree]
   
   ## Maintenance Tips
   
   To keep this organized:
   
   1. **Weekly**: Sort new downloads
   2. **Monthly**: Review and archive completed projects
   3. **Quarterly**: Check for new duplicates
   4. **Yearly**: Archive old files
   
   ## Quick Commands for You
   
   ```bash
   # Find files modified this week
   find . -type f -mtime -7
   
   # Sort downloads by type
   [custom command for their setup]
   
   # Find duplicates
   [custom command]
   ```
   
   Want to organize another folder?
   ```

## Examples

### Example 1: Organizing Downloads (From Justin Dielmann)

**User**: "My Downloads folder is a mess with 500+ files. Help me organize it."

**Process**:
1. Analyzes Downloads folder
2. Finds patterns: work docs, personal photos, installers, random PDFs
3. Proposes structure:
   - Downloads/
     - Work/
     - Personal/
     - Installers/ (DMG, PKG files)
     - Archive/
     - ToSort/ (things needing decisions)
4. Asks for confirmation
5. Moves files intelligently based on content and names
6. Results: 500 files → 5 organized folders

### Example 2: Finding and Removing Duplicates

**User**: "Find duplicate files in my Documents and help me decide which to keep."

**Output**:
```markdown
# Found 23 Sets of Duplicates (156 MB total)

## Duplicate Set 1: "proposal.pdf"
- `/Documents/proposal.pdf` (2.3 MB, modified: 2024-03-15)
- `/Documents/old/proposal.pdf` (2.3 MB, modified: 2024-03-15)
- `/Desktop/proposal.pdf` (2.3 MB, modified: 2024-03-10)

**Recommendation**: Keep `/Documents/proposal.pdf` (most recent in correct location)
Delete the other 2 copies?

[Continue for all duplicates...]
```

### Example 3: Restructuring Projects Folder

**User**: "Review my ~/Projects directory and suggest improvements."

**Output**:
```markdown
# Analysis of ~/Projects

## Current Structure Issues
- Mix of active and archived projects (3+ years old)
- No consistent naming convention
- Some projects at root, others in random subfolders
- Duplicate folders (project-name, project-name-old, project-name-v2)

## Proposed Structure

```
Projects/
├── Active/
│   ├── client-work/
│   ├── side-projects/
│   └── learning/
├── Archive/
│   ├── 2022/
│   ├── 2023/
│   └── 2024/
└── Templates/
```

## Specific Changes
1. Move 12 projects not touched since 2022 → Archive/
2. Consolidate 4 duplicate project folders
3. Rename projects to consistent format: "client-name-project-name"
4. Create Archive for old work

Want me to implement this?
```

### Example 4: Organizing Photos by Date

**User**: "Organize my photo folders by year and month."

**Output**: Creates structure like:
```
Photos/
├── 2023/
│   ├── 01-January/
│   ├── 02-February/
│   └── ...
├── 2024/
│   ├── 01-January/
│   └── ...
└── Unsorted/
```

Then moves photos based on EXIF data or file modification dates.

## Common Organization Tasks

### Downloads Cleanup
```
Organize my Downloads folder - move documents to Documents, 
images to Pictures, keep installers separate, and archive files 
older than 3 months.
```

### Project Organization
```
Review my Projects folder structure and help me separate active 
projects from old ones I should archive.
```

### Duplicate Removal
```
Find all duplicate files in my Documents folder and help me 
decide which ones to keep.
```

### Desktop Cleanup
```
My Desktop is covered in files. Help me organize everything into 
my Documents folder properly.
```

### Photo Organization
```
Organize all photos in this folder by date (year/month) based 
on when they were taken.
```

### Work/Personal Separation
```
Help me separate my work files from personal files across my 
Documents folder.
```

## Pro Tips

1. **Start Small**: Begin with one messy folder (like Downloads) to build trust
2. **Regular Maintenance**: Run weekly cleanup on Downloads
3. **Consistent Naming**: Use "YYYY-MM-DD - Description" format for important files
4. **Archive Aggressively**: Move old projects to Archive instead of deleting
5. **Keep Active Separate**: Maintain clear boundaries between active and archived work
6. **Trust the Process**: Let Claude handle the cognitive load of where things go

## Best Practices

### Folder Naming
- Use clear, descriptive names
- Avoid spaces (use hyphens or underscores)
- Be specific: "client-proposals" not "docs"
- Use prefixes for ordering: "01-current", "02-archive"

### File Naming
- Include dates: "2024-10-17-meeting-notes.md"
- Be descriptive: "q3-financial-report.xlsx"
- Avoid version numbers in names (use version control instead)
- Remove download artifacts: "document-final-v2 (1).pdf" → "document.pdf"

### When to Archive
- Projects not touched in 6+ months
- Completed work that might be referenced later
- Old versions after migration to new systems
- Files you're hesitant to delete (archive first)

## Related Use Cases

- Setting up organization for a new computer
- Preparing files for backup/archiving
- Cleaning up before storage cleanup
- Organizing shared team folders
- Structuring new project directories
```

Image enhancer
```md
---
name: image-enhancer
description: Improves the quality of images, especially screenshots, by enhancing resolution, sharpness, and clarity. Perfect for preparing images for presentations, documentation, or social media posts.
---

# Image Enhancer

This skill takes your images and screenshots and makes them look better—sharper, clearer, and more professional.

## When to Use This Skill

- Improving screenshot quality for blog posts or documentation
- Enhancing images before sharing on social media
- Preparing images for presentations or reports
- Upscaling low-resolution images
- Sharpening blurry photos
- Cleaning up compressed images

## What This Skill Does

1. **Analyzes Image Quality**: Checks resolution, sharpness, and compression artifacts
2. **Enhances Resolution**: Upscales images intelligently
3. **Improves Sharpness**: Enhances edges and details
4. **Reduces Artifacts**: Cleans up compression artifacts and noise
5. **Optimizes for Use Case**: Adjusts based on intended use (web, print, social media)

## How to Use

### Basic Enhancement

```
Improve the image quality of screenshot.png
```

```
Enhance all images in this folder
```

### Specific Improvements

```
Upscale this image to 4K resolution
```

```
Sharpen this blurry screenshot
```

```
Reduce compression artifacts in this image
```

### Batch Processing

```
Improve the quality of all PNG files in this directory
```

## Example

**User**: "Improve the image quality of screenshot-2024.png"

**Output**:
```
Analyzing screenshot-2024.png...

Current specs:
- Resolution: 1920x1080
- Format: PNG
- Quality: Good, but slight blur

Enhancements applied:
✓ Upscaled to 2560x1440 (retina)
✓ Sharpened edges
✓ Enhanced text clarity
✓ Optimized file size

Saved as: screenshot-2024-enhanced.png
Original preserved as: screenshot-2024-original.png
```

**Inspired by:** Lenny Rachitsky's workflow from his newsletter - used for screenshots in his articles

## Tips

- Always keeps original files as backup
- Works best with screenshots and digital images
- Can batch process entire folders
- Specify output format if needed (PNG for quality, JPG for smaller size)
- For social media, mention the platform for optimal sizing

## Common Use Cases

- **Blog Posts**: Enhance screenshots before publishing
- **Documentation**: Make UI screenshots crystal clear
- **Social Media**: Optimize images for Twitter, LinkedIn, Instagram
- **Presentations**: Upscale images for large screens
- **Print Materials**: Increase resolution for physical media
- **Archiving**: Clean up old images before storage
```

Skill share
```md
---
name: skill-share
description: A skill that creates new Claude skills and automatically shares them on Slack using Rube for seamless team collaboration and skill discovery.
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill when you need to:
- **Create new Claude skills** with proper structure and metadata
- **Generate skill packages** ready for distribution
- **Automatically share created skills** on Slack channels for team visibility
- **Validate skill structure** before sharing
- **Package and distribute** skills to your team

Also use this skill when:
- **User says he wants to create/share his skill** 

This skill is ideal for:
- Creating skills as part of team workflows
- Building internal tools that need skill creation + team notification
- Automating the skill development pipeline
- Collaborative skill creation with team notifications

## Key Features

### 1. Skill Creation
- Creates properly structured skill directories with SKILL.md
- Generates standardized scripts/, references/, and assets/ directories
- Auto-generates YAML frontmatter with required metadata
- Enforces naming conventions (hyphen-case)

### 2. Skill Validation
- Validates SKILL.md format and required fields
- Checks naming conventions
- Ensures metadata completeness before packaging

### 3. Skill Packaging
- Creates distributable zip files
- Includes all skill assets and documentation
- Runs validation automatically before packaging

### 4. Slack Integration via Rube
- Automatically sends created skill information to designated Slack channels
- Shares skill metadata (name, description, link)
- Posts skill summary for team discovery
- Provides direct links to skill files

## How It Works

1. **Initialization**: Provide skill name and description
2. **Creation**: Skill directory is created with proper structure
3. **Validation**: Skill metadata is validated for correctness
4. **Packaging**: Skill is packaged into a distributable format
5. **Slack Notification**: Skill details are posted to your team's Slack channel

## Example Usage

```
When you ask Claude to create a skill called "pdf-analyzer":
1. Creates /skill-pdf-analyzer/ with SKILL.md template
2. Generates structured directories (scripts/, references/, assets/)
3. Validates the skill structure
4. Packages the skill as a zip file
5. Posts to Slack: "New Skill Created: pdf-analyzer - Advanced PDF analysis and extraction capabilities"
```

## Integration with Rube

This skill leverages Rube for:
- **SLACK_SEND_MESSAGE**: Posts skill information to team channels
- **SLACK_POST_MESSAGE_WITH_BLOCKS**: Shares rich formatted skill metadata
- **SLACK_FIND_CHANNELS**: Discovers target channels for skill announcements

## Requirements

- Slack workspace connection via Rube
- Write access to skill creation directory
- Python 3.7+ for skill creation scripts
- Target Slack channel for skill notifications
- Proper skill metadata for validation
```

Video downloader
```md
---
name: youtube-downloader
description: Download YouTube videos with customizable quality and format options. Use this skill when the user asks to download, save, or grab YouTube videos. Supports various quality settings (best, 1080p, 720p, 480p, 360p), multiple formats (mp4, webm, mkv), and audio-only downloads as MP3.
---

# YouTube Video Downloader

Download YouTube videos with full control over quality and format settings.

## Quick Start

The simplest way to download a video:

```bash
python scripts/download_video.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

This downloads the video in best available quality as MP4 to `/mnt/user-data/outputs/`.

## Options

### Quality Settings

Use `-q` or `--quality` to specify video quality:

- `best` (default): Highest quality available
- `1080p`: Full HD
- `720p`: HD
- `480p`: Standard definition
- `360p`: Lower quality
- `worst`: Lowest quality available

Example:
```bash
python scripts/download_video.py "URL" -q 720p
```

### Format Options

Use `-f` or `--format` to specify output format (video downloads only):

- `mp4` (default): Most compatible
- `webm`: Modern format
- `mkv`: Matroska container

Example:
```bash
python scripts/download_video.py "URL" -f webm
```

### Audio Only

Use `-a` or `--audio-only` to download only audio as MP3:

```bash
python scripts/download_video.py "URL" -a
```

### Custom Output Directory

Use `-o` or `--output` to specify a different output directory:

```bash
python scripts/download_video.py "URL" -o /path/to/directory
```

## Complete Examples

1. Download video in 1080p as MP4:
```bash
python scripts/download_video.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -q 1080p
```

2. Download audio only as MP3:
```bash
python scripts/download_video.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -a
```

3. Download in 720p as WebM to custom directory:
```bash
python scripts/download_video.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -q 720p -f webm -o /custom/path
```

## How It Works

The skill uses `yt-dlp`, a robust YouTube downloader that:
- Automatically installs itself if not present
- Fetches video information before downloading
- Selects the best available streams matching your criteria
- Merges video and audio streams when needed
- Supports a wide range of YouTube video formats

## Important Notes

- Downloads are saved to `/mnt/user-data/outputs/` by default
- Video filename is automatically generated from the video title
- The script handles installation of yt-dlp automatically
- Only single videos are downloaded (playlists are skipped by default)
- Higher quality videos may take longer to download and use more disk space
```

Webapp testing
```md
---
name: webapp-testing
description: Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing browser screenshots, and viewing browser logs.
license: Complete terms in LICENSE.txt
---

# Web Application Testing

To test local web applications, write native Python Playwright scripts.

**Helper Scripts Available**:
- `scripts/with_server.py` - Manages server lifecycle (supports multiple servers)

**Always run scripts with `--help` first** to see usage. DO NOT read the source until you try running the script first and find that a customized solution is abslutely necessary. These scripts can be very large and thus pollute your context window. They exist to be called directly as black-box scripts rather than ingested into your context window.

## Decision Tree: Choosing Your Approach

```
User task → Is it static HTML?
    ├─ Yes → Read HTML file directly to identify selectors
    │         ├─ Success → Write Playwright script using selectors
    │         └─ Fails/Incomplete → Treat as dynamic (below)
    │
    └─ No (dynamic webapp) → Is the server already running?
        ├─ No → Run: python scripts/with_server.py --help
        │        Then use the helper + write simplified Playwright script
        │
        └─ Yes → Reconnaissance-then-action:
            1. Navigate and wait for networkidle
            2. Take screenshot or inspect DOM
            3. Identify selectors from rendered state
            4. Execute actions with discovered selectors
```

## Example: Using with_server.py

To start a server, run `--help` first, then use the helper:

**Single server:**
```bash
python scripts/with_server.py --server "npm run dev" --port 5173 -- python your_automation.py
```

**Multiple servers (e.g., backend + frontend):**
```bash
python scripts/with_server.py \
  --server "cd backend && python server.py" --port 3000 \
  --server "cd frontend && npm run dev" --port 5173 \
  -- python your_automation.py
```

To create an automation script, include only Playwright logic (servers are managed automatically):
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True) # Always launch chromium in headless mode
    page = browser.new_page()
    page.goto('http://localhost:5173') # Server already running and ready
    page.wait_for_load_state('networkidle') # CRITICAL: Wait for JS to execute
    # ... your automation logic
    browser.close()
```

## Reconnaissance-Then-Action Pattern

1. **Inspect rendered DOM**:
   ```python
   page.screenshot(path='/tmp/inspect.png', full_page=True)
   content = page.content()
   page.locator('button').all()
   ```

2. **Identify selectors** from inspection results

3. **Execute actions** using discovered selectors

## Common Pitfall

❌ **Don't** inspect the DOM before waiting for `networkidle` on dynamic apps
✅ **Do** wait for `page.wait_for_load_state('networkidle')` before inspection

## Best Practices

- **Use bundled scripts as black boxes** - To accomplish a task, consider whether one of the scripts available in `scripts/` can help. These scripts handle common, complex workflows reliably without cluttering the context window. Use `--help` to see usage, then invoke directly. 
- Use `sync_playwright()` for synchronous scripts
- Always close the browser when done
- Use descriptive selectors: `text=`, `role=`, CSS selectors, or IDs
- Add appropriate waits: `page.wait_for_selector()` or `page.wait_for_timeout()`

## Reference Files

- **examples/** - Examples showing common patterns:
  - `element_discovery.py` - Discovering buttons, links, and inputs on a page
  - `static_html_automation.py` - Using file:// URLs for local HTML
  - `console_logging.py` - Capturing console logs during automation
  - `screenshot_capture.py` - Taking screenshots for inspection
  - `multi_server.py` - Managing multiple servers with `with_server.py`
```

Evaluate Repositery
```md
# Repository Evaluation Prompt (Awesome-Claude-Code · Full Version)

## Evaluation Context (Claude Code Ecosystem)

You are evaluating a repository intended for use in or alongside **Claude Code**, where certain features (such as hooks, commands, scripts, or automation) may execute implicitly or with elevated trust once enabled by a user.

In this ecosystem, risk commonly arises not from overtly malicious code, but from implicit execution surfaces, including:
- Hooks that execute automatically based on tool lifecycle events
- Custom commands that may invoke shell scripts
- Scripts that run in the user’s local environment
- Persistent state files that influence control flow
- Network access triggered indirectly by tooling

Your task is to perform a conservative, evidence-based, static review that:
- Identifies trust boundaries and implicit execution
- Distinguishes declared behavior from effective capability
- Surfaces red flags or areas requiring further manual inspection
- Avoids inferring author intent beyond what is observable

When uncertain, prefer explicit uncertainty over confident speculation.

---

## Instructions

Perform a static, read-only review of the repository named at the end of this prompt.

Do not run any code, install dependencies, or execute scripts.
Base your assessment solely on repository contents and documentation.

This evaluation supports curation and triage, not automated approval.

---

## Evaluation Criteria

For each category below:
- Assign a score from 1–10
- Provide concise justification
- Explicitly note uncertainty
- Separate red flags from speculation

### 1. Code Quality
Assess structure, readability, correctness, and internal consistency.

### 2. Security & Safety
Assess risks related to:
- Implicit execution (hooks, background behavior)
- File system access
- Network access
- Credential handling
- Tool escalation or privilege assumptions

### 3. Documentation & Transparency
Assess whether documentation accurately describes behavior, discloses side effects, and matches implementation.

### 4. Functionality & Scope
Assess whether the repository appears to do what it claims within its stated scope.

### 5. Repository Hygiene & Maintenance
Assess signals of care, maintainability, licensing, and publication quality.

---

## Claude-Code-Specific Checklist

Explicitly answer each item:
- Defines hooks (stop, lifecycle, or similar)
- Hooks execute shell scripts
- Commands invoke shell or external tools
- Writes persistent local state files
- Reads state to control execution flow
- Performs implicit execution without explicit confirmation
- Documents hook or command side effects
- Includes safe defaults
- Includes a clear disable or cancel mechanism

Briefly explain any checked item.

---

## Permissions & Side Effects Analysis

### A. Reported / Declared Permissions
From documentation or config:
- File system:
- Network:
- Execution / hooks:
- APIs / tools:

### B. Likely Actual Permissions (Inferred)
From static inspection:
- File system:
- Network:
- Execution / hooks:
- APIs / tools:

Mark items as confirmed, likely, or unclear.

### C. Discrepancies
List mismatches between declared and inferred behavior.

---

## Red Flag Scan

Check all that apply and justify:
- Malware or spyware indicators
- Undisclosed implicit execution
- Undocumented file or network activity
- Unsupported claims
- Supply-chain or trust risks

---

## Overall Assessment

### Overall Score
Score: X / 10

### Recommendation
Choose one:
- Recommend
- Recommend with caveats
- Needs further manual review
- Definitely reject

### Fast-Reject Heuristic
If "Definitely reject", specify which applies:
- Clear malicious behavior
- Undisclosed high-risk implicit execution
- Severe claim/behavior mismatch
- Unsafe defaults with no mitigation
- Other (explain)

---

## Possible Remedies / Improvement Suggestions

If applicable, list specific, minimal changes that could materially improve the submission or change the recommendation (e.g., documentation clarifications, safer defaults, permission scoping).

---

## Output Format

Use clear section headings corresponding to the sections above.
Keep the evaluation concise, precise, and evidence-based.

---

REPOSITORY:

IF PRESENT: <REPO>$ARGUMENTS</REPO>

ELSE: The repository you are currently working in.
```

PPTX genJS tutorial
```md
# PptxGenJS Tutorial

## Setup & Basic Structure

```javascript
const pptxgen = require("pptxgenjs");

let pres = new pptxgen();
pres.layout = 'LAYOUT_16x9';  // or 'LAYOUT_16x10', 'LAYOUT_4x3', 'LAYOUT_WIDE'
pres.author = 'Your Name';
pres.title = 'Presentation Title';

let slide = pres.addSlide();
slide.addText("Hello World!", { x: 0.5, y: 0.5, fontSize: 36, color: "363636" });

pres.writeFile({ fileName: "Presentation.pptx" });
```

## Layout Dimensions

Slide dimensions (coordinates in inches):
- `LAYOUT_16x9`: 10" × 5.625" (default)
- `LAYOUT_16x10`: 10" × 6.25"
- `LAYOUT_4x3`: 10" × 7.5"
- `LAYOUT_WIDE`: 13.3" × 7.5"

---

## Text & Formatting

```javascript
// Basic text
slide.addText("Simple Text", {
  x: 1, y: 1, w: 8, h: 2, fontSize: 24, fontFace: "Arial",
  color: "363636", bold: true, align: "center", valign: "middle"
});

// Character spacing (use charSpacing, not letterSpacing which is silently ignored)
slide.addText("SPACED TEXT", { x: 1, y: 1, w: 8, h: 1, charSpacing: 6 });

// Rich text arrays
slide.addText([
  { text: "Bold ", options: { bold: true } },
  { text: "Italic ", options: { italic: true } }
], { x: 1, y: 3, w: 8, h: 1 });

// Multi-line text (requires breakLine: true)
slide.addText([
  { text: "Line 1", options: { breakLine: true } },
  { text: "Line 2", options: { breakLine: true } },
  { text: "Line 3" }  // Last item doesn't need breakLine
], { x: 0.5, y: 0.5, w: 8, h: 2 });

// Text box margin (internal padding)
slide.addText("Title", {
  x: 0.5, y: 0.3, w: 9, h: 0.6,
  margin: 0  // Use 0 when aligning text with other elements like shapes or icons
});
```

**Tip:** Text boxes have internal margin by default. Set `margin: 0` when you need text to align precisely with shapes, lines, or icons at the same x-position.

---

## Lists & Bullets

```javascript
// ✅ CORRECT: Multiple bullets
slide.addText([
  { text: "First item", options: { bullet: true, breakLine: true } },
  { text: "Second item", options: { bullet: true, breakLine: true } },
  { text: "Third item", options: { bullet: true } }
], { x: 0.5, y: 0.5, w: 8, h: 3 });

// ❌ WRONG: Never use unicode bullets
slide.addText("• First item", { ... });  // Creates double bullets

// Sub-items and numbered lists
{ text: "Sub-item", options: { bullet: true, indentLevel: 1 } }
{ text: "First", options: { bullet: { type: "number" }, breakLine: true } }
```

---

## Shapes

```javascript
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 0.8, w: 1.5, h: 3.0,
  fill: { color: "FF0000" }, line: { color: "000000", width: 2 }
});

slide.addShape(pres.shapes.OVAL, { x: 4, y: 1, w: 2, h: 2, fill: { color: "0000FF" } });

slide.addShape(pres.shapes.LINE, {
  x: 1, y: 3, w: 5, h: 0, line: { color: "FF0000", width: 3, dashType: "dash" }
});

// With transparency
slide.addShape(pres.shapes.RECTANGLE, {
  x: 1, y: 1, w: 3, h: 2,
  fill: { color: "0088CC", transparency: 50 }
});

// Rounded rectangle (rectRadius only works with ROUNDED_RECTANGLE, not RECTANGLE)
// ⚠️ Don't pair with rectangular accent overlays — they won't cover rounded corners. Use RECTANGLE instead.
slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
  x: 1, y: 1, w: 3, h: 2,
  fill: { color: "FFFFFF" }, rectRadius: 0.1
});

// With shadow
slide.addShape(pres.shapes.RECTANGLE, {
  x: 1, y: 1, w: 3, h: 2,
  fill: { color: "FFFFFF" },
  shadow: { type: "outer", color: "000000", blur: 6, offset: 2, angle: 135, opacity: 0.15 }
});
```

Shadow options:

| Property | Type | Range | Notes |
|----------|------|-------|-------|
| `type` | string | `"outer"`, `"inner"` | |
| `color` | string | 6-char hex (e.g. `"000000"`) | No `#` prefix, no 8-char hex — see Common Pitfalls |
| `blur` | number | 0-100 pt | |
| `offset` | number | 0-200 pt | **Must be non-negative** — negative values corrupt the file |
| `angle` | number | 0-359 degrees | Direction the shadow falls (135 = bottom-right, 270 = upward) |
| `opacity` | number | 0.0-1.0 | Use this for transparency, never encode in color string |

To cast a shadow upward (e.g. on a footer bar), use `angle: 270` with a positive offset — do **not** use a negative offset.

**Note**: Gradient fills are not natively supported. Use a gradient image as a background instead.

---

## Images

### Image Sources

```javascript
// From file path
slide.addImage({ path: "images/chart.png", x: 1, y: 1, w: 5, h: 3 });

// From URL
slide.addImage({ path: "https://example.com/image.jpg", x: 1, y: 1, w: 5, h: 3 });

// From base64 (faster, no file I/O)
slide.addImage({ data: "image/png;base64,iVBORw0KGgo...", x: 1, y: 1, w: 5, h: 3 });
```

### Image Options

```javascript
slide.addImage({
  path: "image.png",
  x: 1, y: 1, w: 5, h: 3,
  rotate: 45,              // 0-359 degrees
  rounding: true,          // Circular crop
  transparency: 50,        // 0-100
  flipH: true,             // Horizontal flip
  flipV: false,            // Vertical flip
  altText: "Description",  // Accessibility
  hyperlink: { url: "https://example.com" }
});
```

### Image Sizing Modes

```javascript
// Contain - fit inside, preserve ratio
{ sizing: { type: 'contain', w: 4, h: 3 } }

// Cover - fill area, preserve ratio (may crop)
{ sizing: { type: 'cover', w: 4, h: 3 } }

// Crop - cut specific portion
{ sizing: { type: 'crop', x: 0.5, y: 0.5, w: 2, h: 2 } }
```

### Calculate Dimensions (preserve aspect ratio)

```javascript
const origWidth = 1978, origHeight = 923, maxHeight = 3.0;
const calcWidth = maxHeight * (origWidth / origHeight);
const centerX = (10 - calcWidth) / 2;

slide.addImage({ path: "image.png", x: centerX, y: 1.2, w: calcWidth, h: maxHeight });
```

### Supported Formats

- **Standard**: PNG, JPG, GIF (animated GIFs work in Microsoft 365)
- **SVG**: Works in modern PowerPoint/Microsoft 365

---

## Icons

Use react-icons to generate SVG icons, then rasterize to PNG for universal compatibility.

### Setup

```javascript
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const { FaCheckCircle, FaChartLine } = require("react-icons/fa");

function renderIconSvg(IconComponent, color = "#000000", size = 256) {
  return ReactDOMServer.renderToStaticMarkup(
    React.createElement(IconComponent, { color, size: String(size) })
  );
}

async function iconToBase64Png(IconComponent, color, size = 256) {
  const svg = renderIconSvg(IconComponent, color, size);
  const pngBuffer = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + pngBuffer.toString("base64");
}
```

### Add Icon to Slide

```javascript
const iconData = await iconToBase64Png(FaCheckCircle, "#4472C4", 256);

slide.addImage({
  data: iconData,
  x: 1, y: 1, w: 0.5, h: 0.5  // Size in inches
});
```

**Note**: Use size 256 or higher for crisp icons. The size parameter controls the rasterization resolution, not the display size on the slide (which is set by `w` and `h` in inches).

### Icon Libraries

Install: `npm install -g react-icons react react-dom sharp`

Popular icon sets in react-icons:
- `react-icons/fa` - Font Awesome
- `react-icons/md` - Material Design
- `react-icons/hi` - Heroicons
- `react-icons/bi` - Bootstrap Icons

---

## Slide Backgrounds

```javascript
// Solid color
slide.background = { color: "F1F1F1" };

// Color with transparency
slide.background = { color: "FF3399", transparency: 50 };

// Image from URL
slide.background = { path: "https://example.com/bg.jpg" };

// Image from base64
slide.background = { data: "image/png;base64,iVBORw0KGgo..." };
```

---

## Tables

```javascript
slide.addTable([
  ["Header 1", "Header 2"],
  ["Cell 1", "Cell 2"]
], {
  x: 1, y: 1, w: 8, h: 2,
  border: { pt: 1, color: "999999" }, fill: { color: "F1F1F1" }
});

// Advanced with merged cells
let tableData = [
  [{ text: "Header", options: { fill: { color: "6699CC" }, color: "FFFFFF", bold: true } }, "Cell"],
  [{ text: "Merged", options: { colspan: 2 } }]
];
slide.addTable(tableData, { x: 1, y: 3.5, w: 8, colW: [4, 4] });
```

---

## Charts

```javascript
// Bar chart
slide.addChart(pres.charts.BAR, [{
  name: "Sales", labels: ["Q1", "Q2", "Q3", "Q4"], values: [4500, 5500, 6200, 7100]
}], {
  x: 0.5, y: 0.6, w: 6, h: 3, barDir: 'col',
  showTitle: true, title: 'Quarterly Sales'
});

// Line chart
slide.addChart(pres.charts.LINE, [{
  name: "Temp", labels: ["Jan", "Feb", "Mar"], values: [32, 35, 42]
}], { x: 0.5, y: 4, w: 6, h: 3, lineSize: 3, lineSmooth: true });

// Pie chart
slide.addChart(pres.charts.PIE, [{
  name: "Share", labels: ["A", "B", "Other"], values: [35, 45, 20]
}], { x: 7, y: 1, w: 5, h: 4, showPercent: true });
```

### Better-Looking Charts

Default charts look dated. Apply these options for a modern, clean appearance:

```javascript
slide.addChart(pres.charts.BAR, chartData, {
  x: 0.5, y: 1, w: 9, h: 4, barDir: "col",

  // Custom colors (match your presentation palette)
  chartColors: ["0D9488", "14B8A6", "5EEAD4"],

  // Clean background
  chartArea: { fill: { color: "FFFFFF" }, roundedCorners: true },

  // Muted axis labels
  catAxisLabelColor: "64748B",
  valAxisLabelColor: "64748B",

  // Subtle grid (value axis only)
  valGridLine: { color: "E2E8F0", size: 0.5 },
  catGridLine: { style: "none" },

  // Data labels on bars
  showValue: true,
  dataLabelPosition: "outEnd",
  dataLabelColor: "1E293B",

  // Hide legend for single series
  showLegend: false,
});
```

**Key styling options:**
- `chartColors: [...]` - hex colors for series/segments
- `chartArea: { fill, border, roundedCorners }` - chart background
- `catGridLine/valGridLine: { color, style, size }` - grid lines (`style: "none"` to hide)
- `lineSmooth: true` - curved lines (line charts)
- `legendPos: "r"` - legend position: "b", "t", "l", "r", "tr"

---

## Slide Masters

```javascript
pres.defineSlideMaster({
  title: 'TITLE_SLIDE', background: { color: '283A5E' },
  objects: [{
    placeholder: { options: { name: 'title', type: 'title', x: 1, y: 2, w: 8, h: 2 } }
  }]
});

let titleSlide = pres.addSlide({ masterName: "TITLE_SLIDE" });
titleSlide.addText("My Title", { placeholder: "title" });
```

---

## Common Pitfalls

⚠️ These issues cause file corruption, visual bugs, or broken output. Avoid them.

1. **NEVER use "#" with hex colors** - causes file corruption
   ```javascript
   color: "FF0000"      // ✅ CORRECT
   color: "#FF0000"     // ❌ WRONG
   ```

2. **NEVER encode opacity in hex color strings** - 8-char colors (e.g., `"00000020"`) corrupt the file. Use the `opacity` property instead.
   ```javascript
   shadow: { type: "outer", blur: 6, offset: 2, color: "00000020" }          // ❌ CORRUPTS FILE
   shadow: { type: "outer", blur: 6, offset: 2, color: "000000", opacity: 0.12 }  // ✅ CORRECT
   ```

3. **Use `bullet: true`** - NEVER unicode symbols like "•" (creates double bullets)

4. **Use `breakLine: true`** between array items or text runs together

5. **Avoid `lineSpacing` with bullets** - causes excessive gaps; use `paraSpaceAfter` instead

6. **Each presentation needs fresh instance** - don't reuse `pptxgen()` objects

7. **NEVER reuse option objects across calls** - PptxGenJS mutates objects in-place (e.g. converting shadow values to EMU). Sharing one object between multiple calls corrupts the second shape.
   ```javascript
   const shadow = { type: "outer", blur: 6, offset: 2, color: "000000", opacity: 0.15 };
   slide.addShape(pres.shapes.RECTANGLE, { shadow, ... });  // ❌ second call gets already-converted values
   slide.addShape(pres.shapes.RECTANGLE, { shadow, ... });

   const makeShadow = () => ({ type: "outer", blur: 6, offset: 2, color: "000000", opacity: 0.15 });
   slide.addShape(pres.shapes.RECTANGLE, { shadow: makeShadow(), ... });  // ✅ fresh object each time
   slide.addShape(pres.shapes.RECTANGLE, { shadow: makeShadow(), ... });
   ```

8. **Don't use `ROUNDED_RECTANGLE` with accent borders** - rectangular overlay bars won't cover rounded corners. Use `RECTANGLE` instead.
   ```javascript
   // ❌ WRONG: Accent bar doesn't cover rounded corners
   slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 1, y: 1, w: 3, h: 1.5, fill: { color: "FFFFFF" } });
   slide.addShape(pres.shapes.RECTANGLE, { x: 1, y: 1, w: 0.08, h: 1.5, fill: { color: "0891B2" } });

   // ✅ CORRECT: Use RECTANGLE for clean alignment
   slide.addShape(pres.shapes.RECTANGLE, { x: 1, y: 1, w: 3, h: 1.5, fill: { color: "FFFFFF" } });
   slide.addShape(pres.shapes.RECTANGLE, { x: 1, y: 1, w: 0.08, h: 1.5, fill: { color: "0891B2" } });
   ```

---

## Quick Reference

- **Shapes**: RECTANGLE, OVAL, LINE, ROUNDED_RECTANGLE
- **Charts**: BAR, LINE, PIE, DOUGHNUT, SCATTER, BUBBLE, RADAR
- **Layouts**: LAYOUT_16x9 (10"×5.625"), LAYOUT_16x10, LAYOUT_4x3, LAYOUT_WIDE
- **Alignment**: "left", "center", "right"
- **Chart data labels**: "outEnd", "inEnd", "center"
- **Shadow angles**: 135 = bottom-right, 270 = upward
- **Icon libraries**: react-icons/fa (Font Awesome), react-icons/md (Material Design), react-icons/hi (Heroicons), react-icons/bi (Bootstrap Icons)
```

Frontend slides
```md
---
name: frontend-slides
description: Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. Use when the user wants to build a presentation, convert a PPT/PPTX to web, or create slides for a talk/pitch. Helps non-designers discover their aesthetic through visual exploration rather than abstract choices.
---

# Frontend Slides Skill

Create zero-dependency, animation-rich HTML presentations that run entirely in the browser. This skill helps non-designers discover their preferred aesthetic through visual exploration ("show, don't tell"), then generates production-quality slide decks.

## Core Philosophy

1. **Zero Dependencies** — Single HTML files with inline CSS/JS. No npm, no build tools.
2. **Show, Don't Tell** — People don't know what they want until they see it. Generate visual previews, not abstract choices.
3. **Distinctive Design** — Avoid generic "AI slop" aesthetics. Every presentation should feel custom-crafted.
4. **Production Quality** — Code should be well-commented, accessible, and performant.
5. **Viewport Fitting (CRITICAL)** — Every slide MUST fit exactly within the viewport. No scrolling within slides, ever. This is non-negotiable.

---

## CRITICAL: Viewport Fitting Requirements

**This section is mandatory for ALL presentations. Every slide must be fully visible without scrolling on any screen size.**

### The Golden Rule

```
Each slide = exactly one viewport height (100vh/100dvh)
Content overflows? → Split into multiple slides or reduce content
Never scroll within a slide.
```

### Content Density Limits

To guarantee viewport fitting, enforce these limits per slide:

| Slide Type | Maximum Content |
|------------|-----------------|
| Title slide | 1 heading + 1 subtitle + optional tagline |
| Content slide | 1 heading + 4-6 bullet points OR 1 heading + 2 paragraphs |
| Feature grid | 1 heading + 6 cards maximum (2x3 or 3x2 grid) |
| Code slide | 1 heading + 8-10 lines of code maximum |
| Quote slide | 1 quote (max 3 lines) + attribution |
| Image slide | 1 heading + 1 image (max 60vh height) |

**If content exceeds these limits → Split into multiple slides**

### Required CSS Architecture

Every presentation MUST include this base CSS for viewport fitting:

```css
/* ===========================================
   VIEWPORT FITTING: MANDATORY BASE STYLES
   These styles MUST be included in every presentation.
   They ensure slides fit exactly in the viewport.
   =========================================== */

/* 1. Lock html/body to viewport */
html, body {
    height: 100%;
    overflow-x: hidden;
}

html {
    scroll-snap-type: y mandatory;
    scroll-behavior: smooth;
}

/* 2. Each slide = exact viewport height */
.slide {
    width: 100vw;
    height: 100vh;
    height: 100dvh; /* Dynamic viewport height for mobile browsers */
    overflow: hidden; /* CRITICAL: Prevent ANY overflow */
    scroll-snap-align: start;
    display: flex;
    flex-direction: column;
    position: relative;
}

/* 3. Content container with flex for centering */
.slide-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    max-height: 100%;
    overflow: hidden; /* Double-protection against overflow */
    padding: var(--slide-padding);
}

/* 4. ALL typography uses clamp() for responsive scaling */
:root {
    /* Titles scale from mobile to desktop */
    --title-size: clamp(1.5rem, 5vw, 4rem);
    --h2-size: clamp(1.25rem, 3.5vw, 2.5rem);
    --h3-size: clamp(1rem, 2.5vw, 1.75rem);

    /* Body text */
    --body-size: clamp(0.75rem, 1.5vw, 1.125rem);
    --small-size: clamp(0.65rem, 1vw, 0.875rem);

    /* Spacing scales with viewport */
    --slide-padding: clamp(1rem, 4vw, 4rem);
    --content-gap: clamp(0.5rem, 2vw, 2rem);
    --element-gap: clamp(0.25rem, 1vw, 1rem);
}

/* 5. Cards/containers use viewport-relative max sizes */
.card, .container, .content-box {
    max-width: min(90vw, 1000px);
    max-height: min(80vh, 700px);
}

/* 6. Lists auto-scale with viewport */
.feature-list, .bullet-list {
    gap: clamp(0.4rem, 1vh, 1rem);
}

.feature-list li, .bullet-list li {
    font-size: var(--body-size);
    line-height: 1.4;
}

/* 7. Grids adapt to available space */
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(min(100%, 250px), 1fr));
    gap: clamp(0.5rem, 1.5vw, 1rem);
}

/* 8. Images constrained to viewport */
img, .image-container {
    max-width: 100%;
    max-height: min(50vh, 400px);
    object-fit: contain;
}

/* ===========================================
   RESPONSIVE BREAKPOINTS
   Aggressive scaling for smaller viewports
   =========================================== */

/* Short viewports (< 700px height) */
@media (max-height: 700px) {
    :root {
        --slide-padding: clamp(0.75rem, 3vw, 2rem);
        --content-gap: clamp(0.4rem, 1.5vw, 1rem);
        --title-size: clamp(1.25rem, 4.5vw, 2.5rem);
        --h2-size: clamp(1rem, 3vw, 1.75rem);
    }
}

/* Very short viewports (< 600px height) */
@media (max-height: 600px) {
    :root {
        --slide-padding: clamp(0.5rem, 2.5vw, 1.5rem);
        --content-gap: clamp(0.3rem, 1vw, 0.75rem);
        --title-size: clamp(1.1rem, 4vw, 2rem);
        --body-size: clamp(0.7rem, 1.2vw, 0.95rem);
    }

    /* Hide non-essential elements */
    .nav-dots, .keyboard-hint, .decorative {
        display: none;
    }
}

/* Extremely short (landscape phones, < 500px height) */
@media (max-height: 500px) {
    :root {
        --slide-padding: clamp(0.4rem, 2vw, 1rem);
        --title-size: clamp(1rem, 3.5vw, 1.5rem);
        --h2-size: clamp(0.9rem, 2.5vw, 1.25rem);
        --body-size: clamp(0.65rem, 1vw, 0.85rem);
    }
}

/* Narrow viewports (< 600px width) */
@media (max-width: 600px) {
    :root {
        --title-size: clamp(1.25rem, 7vw, 2.5rem);
    }

    /* Stack grids vertically */
    .grid {
        grid-template-columns: 1fr;
    }
}

/* ===========================================
   REDUCED MOTION
   Respect user preferences
   =========================================== */
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        transition-duration: 0.2s !important;
    }

    html {
        scroll-behavior: auto;
    }
}
```

### Overflow Prevention Checklist

Before generating any presentation, mentally verify:

1. ✅ Every `.slide` has `height: 100vh; height: 100dvh; overflow: hidden;`
2. ✅ All font sizes use `clamp(min, preferred, max)`
3. ✅ All spacing uses `clamp()` or viewport units
4. ✅ Content containers have `max-height` constraints
5. ✅ Images have `max-height: min(50vh, 400px)` or similar
6. ✅ Grids use `auto-fit` with `minmax()` for responsive columns
7. ✅ Breakpoints exist for heights: 700px, 600px, 500px
8. ✅ No fixed pixel heights on content elements
9. ✅ Content per slide respects density limits

### When Content Doesn't Fit

If you find yourself with too much content:

**DO:**
- Split into multiple slides
- Reduce bullet points (max 5-6 per slide)
- Shorten text (aim for 1-2 lines per bullet)
- Use smaller code snippets
- Create a "continued" slide

**DON'T:**
- Reduce font size below readable limits
- Remove padding/spacing entirely
- Allow any scrolling
- Cram content to fit

### Testing Viewport Fit

After generating, recommend the user test at these sizes:
- Desktop: 1920×1080, 1440×900, 1280×720
- Tablet: 1024×768, 768×1024 (portrait)
- Mobile: 375×667, 414×896
- Landscape phone: 667×375, 896×414

---

## Phase 0: Detect Mode

First, determine what the user wants:

**Mode A: New Presentation**
- User wants to create slides from scratch
- Proceed to Phase 1 (Content Discovery)

**Mode B: PPT Conversion**
- User has a PowerPoint file (.ppt, .pptx) to convert
- Proceed to Phase 4 (PPT Extraction)

**Mode C: Existing Presentation Enhancement**
- User has an HTML presentation and wants to improve it
- Read the existing file, understand the structure, then enhance

---

## Phase 1: Content Discovery (New Presentations)

Before designing, understand the content. Ask via AskUserQuestion:

### Step 1.1: Presentation Context

**Question 1: Purpose**
- Header: "Purpose"
- Question: "What is this presentation for?"
- Options:
  - "Pitch deck" — Selling an idea, product, or company to investors/clients
  - "Teaching/Tutorial" — Explaining concepts, how-to guides, educational content
  - "Conference talk" — Speaking at an event, tech talk, keynote
  - "Internal presentation" — Team updates, strategy meetings, company updates

**Question 2: Slide Count**
- Header: "Length"
- Question: "Approximately how many slides?"
- Options:
  - "Short (5-10)" — Quick pitch, lightning talk
  - "Medium (10-20)" — Standard presentation
  - "Long (20+)" — Deep dive, comprehensive talk

**Question 3: Content**
- Header: "Content"
- Question: "Do you have the content ready, or do you need help structuring it?"
- Options:
  - "I have all content ready" — Just need to design the presentation
  - "I have rough notes" — Need help organizing into slides
  - "I have a topic only" — Need help creating the full outline

If user has content, ask them to share it (text, bullet points, images, etc.).

---

## Phase 2: Style Discovery (Visual Exploration)

**CRITICAL: This is the "show, don't tell" phase.**

Most people can't articulate design preferences in words. Instead of asking "do you want minimalist or bold?", we generate mini-previews and let them react.

### How Users Choose Presets

Users can select a style in **two ways**:

**Option A: Guided Discovery (Default)**
- User answers mood questions
- Skill generates 3 preview files based on their answers
- User views previews in browser and picks their favorite
- This is best for users who don't have a specific style in mind

**Option B: Direct Selection**
- If user already knows what they want, they can request a preset by name
- Example: "Use the Bold Signal style" or "I want something like Dark Botanical"
- Skip to Phase 3 immediately

**Available Presets:**
| Preset | Vibe | Best For |
|--------|------|----------|
| Bold Signal | Confident, high-impact | Pitch decks, keynotes |
| Electric Studio | Clean, professional | Agency presentations |
| Creative Voltage | Energetic, retro-modern | Creative pitches |
| Dark Botanical | Elegant, sophisticated | Premium brands |
| Notebook Tabs | Editorial, organized | Reports, reviews |
| Pastel Geometry | Friendly, approachable | Product overviews |
| Split Pastel | Playful, modern | Creative agencies |
| Vintage Editorial | Witty, personality-driven | Personal brands |
| Neon Cyber | Futuristic, techy | Tech startups |
| Terminal Green | Developer-focused | Dev tools, APIs |
| Swiss Modern | Minimal, precise | Corporate, data |
| Paper & Ink | Literary, thoughtful | Storytelling |

### Step 2.0: Style Path Selection

First, ask how the user wants to choose their style:

**Question: Style Selection Method**
- Header: "Style"
- Question: "How would you like to choose your presentation style?"
- Options:
  - "Show me options" — Generate 3 previews based on my needs (recommended for most users)
  - "I know what I want" — Let me pick from the preset list directly

**If "Show me options"** → Continue to Step 2.1 (Mood Selection)

**If "I know what I want"** → Show preset picker:

**Question: Pick a Preset**
- Header: "Preset"
- Question: "Which style would you like to use?"
- Options:
  - "Bold Signal" — Vibrant card on dark, confident and high-impact
  - "Dark Botanical" — Elegant dark with soft abstract shapes
  - "Notebook Tabs" — Editorial paper look with colorful section tabs
  - "Pastel Geometry" — Friendly pastels with decorative pills

(If user picks one, skip to Phase 3. If they want to see more options, show additional presets or proceed to guided discovery.)

### Step 2.1: Mood Selection (Guided Discovery)

**Question 1: Feeling**
- Header: "Vibe"
- Question: "What feeling should the audience have when viewing your slides?"
- Options:
  - "Impressed/Confident" — Professional, trustworthy, this team knows what they're doing
  - "Excited/Energized" — Innovative, bold, this is the future
  - "Calm/Focused" — Clear, thoughtful, easy to follow
  - "Inspired/Moved" — Emotional, storytelling, memorable
- multiSelect: true (can choose up to 2)

### Step 2.2: Generate Style Previews

Based on their mood selection, generate **3 distinct style previews** as mini HTML files in a temporary directory. Each preview should be a single title slide showing:

- Typography (font choices, heading/body hierarchy)
- Color palette (background, accent, text colors)
- Animation style (how elements enter)
- Overall aesthetic feel

**Preview Styles to Consider (pick 3 based on mood):**

| Mood | Style Options |
|------|---------------|
| Impressed/Confident | "Bold Signal", "Electric Studio", "Dark Botanical" |
| Excited/Energized | "Creative Voltage", "Neon Cyber", "Split Pastel" |
| Calm/Focused | "Notebook Tabs", "Paper & Ink", "Swiss Modern" |
| Inspired/Moved | "Dark Botanical", "Vintage Editorial", "Pastel Geometry" |

**IMPORTANT: Never use these generic patterns:**
- Purple gradients on white backgrounds
- Inter, Roboto, or system fonts
- Standard blue primary colors
- Predictable hero layouts

**Instead, use distinctive choices:**
- Unique font pairings (Clash Display, Satoshi, Cormorant Garamond, DM Sans, etc.)
- Cohesive color themes with personality
- Atmospheric backgrounds (gradients, subtle patterns, depth)
- Signature animation moments

### Step 2.3: Present Previews

Create the previews in: `.claude-design/slide-previews/`

```
.claude-design/slide-previews/
├── style-a.html   # First style option
├── style-b.html   # Second style option
├── style-c.html   # Third style option
└── assets/        # Any shared assets
```

Each preview file should be:
- Self-contained (inline CSS/JS)
- A single "title slide" showing the aesthetic
- Animated to demonstrate motion style
- ~50-100 lines, not a full presentation

Present to user:
```
I've created 3 style previews for you to compare:

**Style A: [Name]** — [1 sentence description]
**Style B: [Name]** — [1 sentence description]
**Style C: [Name]** — [1 sentence description]

Open each file to see them in action:
- .claude-design/slide-previews/style-a.html
- .claude-design/slide-previews/style-b.html
- .claude-design/slide-previews/style-c.html

Take a look and tell me:
1. Which style resonates most?
2. What do you like about it?
3. Anything you'd change?
```

Then use AskUserQuestion:

**Question: Pick Your Style**
- Header: "Style"
- Question: "Which style preview do you prefer?"
- Options:
  - "Style A: [Name]" — [Brief description]
  - "Style B: [Name]" — [Brief description]
  - "Style C: [Name]" — [Brief description]
  - "Mix elements" — Combine aspects from different styles

If "Mix elements", ask for specifics.

---

## Phase 3: Generate Presentation

Now generate the full presentation based on:
- Content from Phase 1
- Style from Phase 2

### File Structure

For single presentations:
```
presentation.html    # Self-contained presentation
assets/              # Images, if any
```

For projects with multiple presentations:
```
[presentation-name].html
[presentation-name]-assets/
```

### HTML Architecture

Follow this structure for all presentations:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Presentation Title</title>

    <!-- Fonts (use Fontshare or Google Fonts) -->
    <link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=...">

    <style>
        /* ===========================================
           CSS CUSTOM PROPERTIES (THEME)
           Easy to modify: change these to change the whole look
           =========================================== */
        :root {
            /* Colors */
            --bg-primary: #0a0f1c;
            --bg-secondary: #111827;
            --text-primary: #ffffff;
            --text-secondary: #9ca3af;
            --accent: #00ffcc;
            --accent-glow: rgba(0, 255, 204, 0.3);

            /* Typography - MUST use clamp() for responsive scaling */
            --font-display: 'Clash Display', sans-serif;
            --font-body: 'Satoshi', sans-serif;
            --title-size: clamp(2rem, 6vw, 5rem);
            --subtitle-size: clamp(0.875rem, 2vw, 1.25rem);
            --body-size: clamp(0.75rem, 1.2vw, 1rem);

            /* Spacing - MUST use clamp() for responsive scaling */
            --slide-padding: clamp(1.5rem, 4vw, 4rem);
            --content-gap: clamp(1rem, 2vw, 2rem);

            /* Animation */
            --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
            --duration-normal: 0.6s;
        }

        /* ===========================================
           BASE STYLES
           =========================================== */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
            scroll-snap-type: y mandatory;
            height: 100%;
        }

        body {
            font-family: var(--font-body);
            background: var(--bg-primary);
            color: var(--text-primary);
            overflow-x: hidden;
            height: 100%;
        }

        /* ===========================================
           SLIDE CONTAINER
           CRITICAL: Each slide MUST fit exactly in viewport
           - Use height: 100vh (NOT min-height)
           - Use overflow: hidden to prevent scroll
           - Content must scale with clamp() values
           =========================================== */
        .slide {
            width: 100vw;
            height: 100vh; /* EXACT viewport height - no scrolling */
            height: 100dvh; /* Dynamic viewport height for mobile */
            padding: var(--slide-padding);
            scroll-snap-align: start;
            display: flex;
            flex-direction: column;
            justify-content: center;
            position: relative;
            overflow: hidden; /* Prevent any content overflow */
        }

        /* Content wrapper that prevents overflow */
        .slide-content {
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            max-height: 100%;
            overflow: hidden;
        }

        /* ===========================================
           RESPONSIVE BREAKPOINTS
           Adjust content for different screen sizes
           =========================================== */
        @media (max-height: 600px) {
            :root {
                --slide-padding: clamp(1rem, 3vw, 2rem);
                --content-gap: clamp(0.5rem, 1.5vw, 1rem);
            }
        }

        @media (max-width: 768px) {
            :root {
                --title-size: clamp(1.5rem, 8vw, 3rem);
            }
        }

        @media (max-height: 500px) and (orientation: landscape) {
            /* Extra compact for landscape phones */
            :root {
                --title-size: clamp(1.25rem, 5vw, 2rem);
                --slide-padding: clamp(0.75rem, 2vw, 1.5rem);
            }
        }

        /* ===========================================
           ANIMATIONS
           Trigger via .visible class (added by JS on scroll)
           =========================================== */
        .reveal {
            opacity: 0;
            transform: translateY(30px);
            transition: opacity var(--duration-normal) var(--ease-out-expo),
                        transform var(--duration-normal) var(--ease-out-expo);
        }

        .slide.visible .reveal {
            opacity: 1;
            transform: translateY(0);
        }

        /* Stagger children */
        .reveal:nth-child(1) { transition-delay: 0.1s; }
        .reveal:nth-child(2) { transition-delay: 0.2s; }
        .reveal:nth-child(3) { transition-delay: 0.3s; }
        .reveal:nth-child(4) { transition-delay: 0.4s; }

        /* ... more styles ... */
    </style>
</head>
<body>
    <!-- Progress bar (optional) -->
    <div class="progress-bar"></div>

    <!-- Navigation dots (optional) -->
    <nav class="nav-dots">
        <!-- Generated by JS -->
    </nav>

    <!-- Slides -->
    <section class="slide title-slide">
        <h1 class="reveal">Presentation Title</h1>
        <p class="reveal">Subtitle or author</p>
    </section>

    <section class="slide">
        <h2 class="reveal">Slide Title</h2>
        <p class="reveal">Content...</p>
    </section>

    <!-- More slides... -->

    <script>
        /* ===========================================
           SLIDE PRESENTATION CONTROLLER
           Handles navigation, animations, and interactions
           =========================================== */

        class SlidePresentation {
            constructor() {
                // ... initialization
            }

            // ... methods
        }

        // Initialize
        new SlidePresentation();
    </script>
</body>
</html>
```

### Required JavaScript Features

Every presentation should include:

1. **SlidePresentation Class** — Main controller
   - Keyboard navigation (arrows, space)
   - Touch/swipe support
   - Mouse wheel navigation
   - Progress bar updates
   - Navigation dots

2. **Intersection Observer** — For scroll-triggered animations
   - Add `.visible` class when slides enter viewport
   - Trigger CSS animations efficiently

3. **Optional Enhancements** (based on style):
   - Custom cursor with trail
   - Particle system background (canvas)
   - Parallax effects
   - 3D tilt on hover
   - Magnetic buttons
   - Counter animations

### Code Quality Requirements

**Comments:**
Every section should have clear comments explaining:
- What it does
- Why it exists
- How to modify it

```javascript
/* ===========================================
   CUSTOM CURSOR
   Creates a stylized cursor that follows mouse with a trail effect.
   - Uses lerp (linear interpolation) for smooth movement
   - Grows larger when hovering over interactive elements
   =========================================== */
class CustomCursor {
    constructor() {
        // ...
    }
}
```

**Accessibility:**
- Semantic HTML (`<section>`, `<nav>`, `<main>`)
- Keyboard navigation works
- ARIA labels where needed
- Reduced motion support

```css
@media (prefers-reduced-motion: reduce) {
    .reveal {
        transition: opacity 0.3s ease;
        transform: none;
    }
}
```

**CSS Function Negation:**
- Never negate CSS functions directly — `-clamp()`, `-min()`, `-max()` are silently ignored by browsers with no console error
- Always use `calc(-1 * clamp(...))` instead. See STYLE_PRESETS.md → "CSS Gotchas" for details.

**Responsive & Viewport Fitting (CRITICAL):**

**See the "CRITICAL: Viewport Fitting Requirements" section above for complete CSS and guidelines.**

Quick reference:
- Every `.slide` must have `height: 100vh; height: 100dvh; overflow: hidden;`
- All typography and spacing must use `clamp()`
- Respect content density limits (max 4-6 bullets, max 6 cards, etc.)
- Include breakpoints for heights: 700px, 600px, 500px
- When content doesn't fit → split into multiple slides, never scroll

---

## Phase 4: PPT Conversion

When converting PowerPoint files:

### Step 4.1: Extract Content

Use Python with `python-pptx` to extract:

```python
from pptx import Presentation
from pptx.util import Inches, Pt
import json
import os
import base64

def extract_pptx(file_path, output_dir):
    """
    Extract all content from a PowerPoint file.
    Returns a JSON structure with slides, text, and images.
    """
    prs = Presentation(file_path)
    slides_data = []

    # Create assets directory
    assets_dir = os.path.join(output_dir, 'assets')
    os.makedirs(assets_dir, exist_ok=True)

    for slide_num, slide in enumerate(prs.slides):
        slide_data = {
            'number': slide_num + 1,
            'title': '',
            'content': [],
            'images': [],
            'notes': ''
        }

        for shape in slide.shapes:
            # Extract title
            if shape.has_text_frame:
                if shape == slide.shapes.title:
                    slide_data['title'] = shape.text
                else:
                    slide_data['content'].append({
                        'type': 'text',
                        'content': shape.text
                    })

            # Extract images
            if shape.shape_type == 13:  # Picture
                image = shape.image
                image_bytes = image.blob
                image_ext = image.ext
                image_name = f"slide{slide_num + 1}_img{len(slide_data['images']) + 1}.{image_ext}"
                image_path = os.path.join(assets_dir, image_name)

                with open(image_path, 'wb') as f:
                    f.write(image_bytes)

                slide_data['images'].append({
                    'path': f"assets/{image_name}",
                    'width': shape.width,
                    'height': shape.height
                })

        # Extract notes
        if slide.has_notes_slide:
            notes_frame = slide.notes_slide.notes_text_frame
            slide_data['notes'] = notes_frame.text

        slides_data.append(slide_data)

    return slides_data
```

### Step 4.2: Confirm Content Structure

Present the extracted content to the user:

```
I've extracted the following from your PowerPoint:

**Slide 1: [Title]**
- [Content summary]
- Images: [count]

**Slide 2: [Title]**
- [Content summary]
- Images: [count]

...

All images have been saved to the assets folder.

Does this look correct? Should I proceed with style selection?
```

### Step 4.3: Style Selection

Proceed to Phase 2 (Style Discovery) with the extracted content in mind.

### Step 4.4: Generate HTML

Convert the extracted content into the chosen style, preserving:
- All text content
- All images (referenced from assets folder)
- Slide order
- Any speaker notes (as HTML comments or separate file)

---

## Phase 5: Delivery

### Final Output

When the presentation is complete:

1. **Clean up temporary files**
   - Delete `.claude-design/slide-previews/` if it exists

2. **Open the presentation**
   - Use `open [filename].html` to launch in browser

3. **Provide summary**
```
Your presentation is ready!

📁 File: [filename].html
🎨 Style: [Style Name]
📊 Slides: [count]

**Navigation:**
- Arrow keys (← →) or Space to navigate
- Scroll/swipe also works
- Click the dots on the right to jump to a slide

**To customize:**
- Colors: Look for `:root` CSS variables at the top
- Fonts: Change the Fontshare/Google Fonts link
- Animations: Modify `.reveal` class timings

Would you like me to make any adjustments?
```

---

## Style Reference: Effect → Feeling Mapping

Use this guide to match animations to intended feelings:

### Dramatic / Cinematic
- Slow fade-ins (1-1.5s)
- Large scale transitions (0.9 → 1)
- Dark backgrounds with spotlight effects
- Parallax scrolling
- Full-bleed images

### Techy / Futuristic
- Neon glow effects (box-shadow with accent color)
- Particle systems (canvas background)
- Grid patterns
- Monospace fonts for accents
- Glitch or scramble text effects
- Cyan, magenta, electric blue palette

### Playful / Friendly
- Bouncy easing (spring physics)
- Rounded corners (large radius)
- Pastel or bright colors
- Floating/bobbing animations
- Hand-drawn or illustrated elements

### Professional / Corporate
- Subtle, fast animations (200-300ms)
- Clean sans-serif fonts
- Navy, slate, or charcoal backgrounds
- Precise spacing and alignment
- Minimal decorative elements
- Data visualization focus

### Calm / Minimal
- Very slow, subtle motion
- High whitespace
- Muted color palette
- Serif typography
- Generous padding
- Content-focused, no distractions

### Editorial / Magazine
- Strong typography hierarchy
- Pull quotes and callouts
- Image-text interplay
- Grid-breaking layouts
- Serif headlines, sans-serif body
- Black and white with one accent

---

## Animation Patterns Reference

### Entrance Animations

```css
/* Fade + Slide Up (most common) */
.reveal {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.6s var(--ease-out-expo),
                transform 0.6s var(--ease-out-expo);
}

.visible .reveal {
    opacity: 1;
    transform: translateY(0);
}

/* Scale In */
.reveal-scale {
    opacity: 0;
    transform: scale(0.9);
    transition: opacity 0.6s, transform 0.6s var(--ease-out-expo);
}

/* Slide from Left */
.reveal-left {
    opacity: 0;
    transform: translateX(-50px);
    transition: opacity 0.6s, transform 0.6s var(--ease-out-expo);
}

/* Blur In */
.reveal-blur {
    opacity: 0;
    filter: blur(10px);
    transition: opacity 0.8s, filter 0.8s var(--ease-out-expo);
}
```

### Background Effects

```css
/* Gradient Mesh */
.gradient-bg {
    background:
        radial-gradient(ellipse at 20% 80%, rgba(120, 0, 255, 0.3) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 20%, rgba(0, 255, 200, 0.2) 0%, transparent 50%),
        var(--bg-primary);
}

/* Noise Texture */
.noise-bg {
    background-image: url("data:image/svg+xml,..."); /* Inline SVG noise */
}

/* Grid Pattern */
.grid-bg {
    background-image:
        linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
    background-size: 50px 50px;
}
```

### Interactive Effects

```javascript
/* 3D Tilt on Hover */
class TiltEffect {
    constructor(element) {
        this.element = element;
        this.element.style.transformStyle = 'preserve-3d';
        this.element.style.perspective = '1000px';
        this.bindEvents();
    }

    bindEvents() {
        this.element.addEventListener('mousemove', (e) => {
            const rect = this.element.getBoundingClientRect();
            const x = (e.clientX - rect.left) / rect.width - 0.5;
            const y = (e.clientY - rect.top) / rect.height - 0.5;

            this.element.style.transform = `
                rotateY(${x * 10}deg)
                rotateX(${-y * 10}deg)
            `;
        });

        this.element.addEventListener('mouseleave', () => {
            this.element.style.transform = 'rotateY(0) rotateX(0)';
        });
    }
}
```

---

## Troubleshooting

### Common Issues

**Fonts not loading:**
- Check Fontshare/Google Fonts URL
- Ensure font names match in CSS

**Animations not triggering:**
- Verify Intersection Observer is running
- Check that `.visible` class is being added

**Scroll snap not working:**
- Ensure `scroll-snap-type` on html/body
- Each slide needs `scroll-snap-align: start`

**Mobile issues:**
- Disable heavy effects at 768px breakpoint
- Test touch events
- Reduce particle count or disable canvas

**Performance issues:**
- Use `will-change` sparingly
- Prefer `transform` and `opacity` animations
- Throttle scroll/mousemove handlers

---

## Related Skills

- **learn** — Generate FORZARA.md documentation for the presentation
- **frontend-design** — For more complex interactive pages beyond slides
- **design-and-refine:design-lab** — For iterating on component designs

---

## Example Session Flow

1. User: "I want to create a pitch deck for my AI startup"
2. Skill asks about purpose, length, content
3. User shares their bullet points and key messages
4. Skill asks about desired feeling (Impressed + Excited)
5. Skill generates 3 style previews
6. User picks Style B (Neon Cyber), asks for darker background
7. Skill generates full presentation with all slides
8. Skill opens the presentation in browser
9. User requests tweaks to specific slides
10. Final presentation delivered

---

## Conversion Session Flow

1. User: "Convert my slides.pptx to a web presentation"
2. Skill extracts content and images from PPT
3. Skill confirms extracted content with user
4. Skill asks about desired feeling/style
5. Skill generates style previews
6. User picks a style
7. Skill generates HTML presentation with preserved assets
8. Final presentation delivered
```

Card animation
```html
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Card Transform</title>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Courier+Prime:wght@400;700&family=Rajdhani:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  background: #0d0d0f;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  font-family: 'Rajdhani', sans-serif;
}

body::before {
  content: '';
  position: fixed; inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.018) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.018) 1px, transparent 1px);
  background-size: 52px 52px;
  pointer-events: none;
}
body::after {
  content: '';
  position: fixed; inset: 0;
  background: radial-gradient(ellipse 70% 70% at 50% 50%, transparent 40%, rgba(0,0,0,0.75) 100%);
  pointer-events: none;
}

/* ═══════════════════════════════════════════════
   SCENE
   ═══════════════════════════════════════════════ */
.scene {
  position: relative;
  width: 500px;
  height: 520px;
}

/* ═══════════════════════════════════════════════
   Z-INDEX MAP
   ─────────────────────────────────────────────
   1   → .card-wrap          (travels up/down)
   20  → .machine-back       (solid block below slot — hides card as it enters)
   30  → .slot-window        (the gap — always visible but very thin)
   40  → .machine-front      (solid block above slot — hides card if it went up too far)
   50  → .machine-base       (bottom ledge)
   60  → .status-text
   ═══════════════════════════════════════════════ */

/* ── CARD ── */
.card-wrap {
  position: absolute;
  top: 28px;
  left: 50%;
  transform: translateX(-50%);
  width: 324px;
  height: 204px;
  z-index: 1;
  animation: cardSlide 5.5s cubic-bezier(0.42, 0, 0.18, 1) infinite;
  animation-delay: 0.8s;
  will-change: transform;
}

.card {
  width: 100%; height: 100%;
  border-radius: 14px;
  position: relative;
  overflow: hidden;
  animation: cardBg 5.5s cubic-bezier(0.42,0,0.18,1) infinite;
  animation-delay: 0.8s;
}

/* Noise grain */
.card::before {
  content: '';
  position: absolute; inset: 0;
  border-radius: 14px;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='180' height='180' filter='url(%23n)' opacity='0.045'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 20;
  animation: grainMode 5.5s cubic-bezier(0.42,0,0.18,1) infinite;
  animation-delay: 0.8s;
}

/* Specular highlight */
.card::after {
  content: '';
  position: absolute; inset: 0;
  border-radius: 14px;
  background: linear-gradient(
    125deg,
    rgba(255,255,255,0) 15%,
    rgba(255,255,255,0.22) 42%,
    rgba(255,255,255,0.38) 50%,
    rgba(255,255,255,0.14) 58%,
    rgba(255,255,255,0) 80%
  );
  pointer-events: none;
  z-index: 19;
  animation: sheenAnim 5.5s ease-in-out infinite;
  animation-delay: 0.8s;
}

/* ── DECO CIRCLES ── */
.deco { position: absolute; border-radius: 50%; pointer-events: none; }
.deco.a {
  width: 210px; height: 210px; top: -65px; right: -55px;
  animation: decoA 5.5s ease infinite; animation-delay: 0.8s;
}
.deco.b {
  width: 145px; height: 145px; top: 10px; right: -12px;
  animation: decoB 5.5s ease infinite; animation-delay: 0.8s;
}

/* ── BANK NAME ── */
.bank-name {
  position: absolute; top: 20px; left: 24px;
  font-family: 'Archivo Black', sans-serif;
  font-size: 10px; letter-spacing: 0.32em;
  text-transform: uppercase; z-index: 10;
  animation: colDark 5.5s ease infinite; animation-delay: 0.8s;
}

/* ── EMV CHIP — NEVER CHANGES COLOR ── */
.chip {
  position: absolute; top: 58px; left: 24px;
  width: 44px; height: 34px; border-radius: 5px; z-index: 10;
  background: linear-gradient(
    135deg,
    #b87e1e 0%, #f0c040 12%, #d4962a 25%,
    #f5d060 38%, #c08020 50%, #e8b840 63%,
    #ae6e10 75%, #eec030 88%, #c89028 100%
  );
  box-shadow:
    0 1px 6px rgba(0,0,0,0.38),
    0 0 0 1px rgba(155,105,15,0.58),
    inset 0 1px 0 rgba(255,225,90,0.48),
    inset 0 -1px 0 rgba(70,45,0,0.28);
}
.chip::before {
  content: ''; position: absolute; inset: 5px;
  border: 1px solid rgba(100,65,0,0.3); border-radius: 3px;
}
.chip::after {
  content: ''; position: absolute;
  top: 50%; left: 0; right: 0; height: 1px;
  background: rgba(80,50,0,0.18); transform: translateY(-50%);
}
.chip-vline {
  position: absolute; top: 0; bottom: 0; width: 1px;
  background: rgba(80,50,0,0.14);
}
.chip-vline.l { left: 33%; }
.chip-vline.r { right: 33%; }

/* ── CONTACTLESS ── */
.nfc {
  position: absolute; top: 58px; left: 80px;
  width: 30px; height: 30px; z-index: 10;
  display: flex; align-items: center; justify-content: center;
  animation: nfcCol 5.5s ease infinite; animation-delay: 0.8s;
}
.nfc svg { width: 22px; height: 22px; }

/* ── CARD NUMBER ── */
.num {
  position: absolute; bottom: 50px; left: 24px;
  font-family: 'Courier Prime', monospace;
  font-size: 14px; font-weight: 700; letter-spacing: 0.2em;
  display: flex; gap: 12px; z-index: 10;
  animation: colDark 5.5s ease infinite; animation-delay: 0.8s;
}

/* ── HOLDER ── */
.holder {
  position: absolute; bottom: 22px; left: 24px;
  font-family: 'Rajdhani', sans-serif;
  font-size: 10px; font-weight: 500; letter-spacing: 0.22em;
  text-transform: uppercase; z-index: 10;
  animation: colDark 5.5s ease infinite; animation-delay: 0.8s;
}

/* ── EXPIRY ── */
.expiry {
  position: absolute; bottom: 22px; right: 72px;
  font-family: 'Courier Prime', monospace;
  font-size: 10px; font-weight: 700; letter-spacing: 0.1em; z-index: 10;
  animation: colDark 5.5s ease infinite; animation-delay: 0.8s;
}
.exp-lbl {
  font-family: 'Rajdhani', sans-serif; font-size: 7px;
  letter-spacing: 0.15em; text-transform: uppercase;
  opacity: 0.5; display: block; margin-bottom: 1px;
}

/* ── NETWORK ── */
.network {
  position: absolute; bottom: 18px; right: 22px;
  font-family: 'Archivo Black', sans-serif;
  font-size: 17px; font-style: italic; letter-spacing: -0.02em; z-index: 10;
  animation: colNetwork 5.5s ease infinite; animation-delay: 0.8s;
}


/* ═══════════════════════════════════════════════
   TERMINAL — split into front / slot / back layers
   ═══════════════════════════════════════════════ */

/* 
  GEOMETRY (all measured from scene top):
  - Machine front top: 230px  
  - Machine front bottom / slot top: 270px
  - Slot height: 16px  → slot bottom: 286px
  - Machine back top: 286px  → extends to bottom of scene
*/

/* FRONT PANEL (above slot) */
.t-front {
  position: absolute;
  left: 50%; transform: translateX(-50%);
  top: 228px;
  width: 420px;
  height: 58px;   /* sits above slot */
  z-index: 40;
  border-radius: 14px 14px 0 0;
  background: linear-gradient(180deg, #2d2d31 0%, #262628 60%, #222224 100%);
  box-shadow:
    0 -2px 0 rgba(255,255,255,0.06),
    inset 0 1px 0 rgba(255,255,255,0.07);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
}
.t-front::before, .t-front::after {
  content: ''; position: absolute; top: 8px; bottom: 8px; width: 2px;
  border-radius: 2px;
  background: linear-gradient(180deg, rgba(255,255,255,0.07), transparent);
}
.t-front::before { left: 11px; }
.t-front::after  { right: 11px; }

.led-row { display: flex; align-items: center; gap: 7px; }
.led {
  width: 7px; height: 7px; border-radius: 50%;
  animation: ledCol 5.5s ease-in-out infinite; animation-delay: 0.8s;
}
@keyframes ledCol {
  0%,18%  { background:#152515; box-shadow: none; }
  25%,56% { background:#ff6600; box-shadow: 0 0 6px #ff6600, 0 0 14px rgba(255,100,0,0.35); }
  60%,72% { background:#00cc55; box-shadow: 0 0 6px #00cc55, 0 0 14px rgba(0,200,70,0.35); }
  80%,100%{ background:#152515; box-shadow: none; }
}
.led-lbl {
  font-size: 8px; font-weight: 500; letter-spacing: 0.3em;
  text-transform: uppercase; color: rgba(255,255,255,0.17);
}
.brand {
  font-family: 'Archivo Black', sans-serif; font-size: 8px;
  letter-spacing: 0.35em; text-transform: uppercase;
  color: rgba(255,255,255,0.1);
}

/* SLOT GAP */
.t-slot {
  position: absolute;
  left: 50%; transform: translateX(-50%);
  top: 286px;
  width: 420px;
  height: 16px;
  z-index: 30;
  display: flex;
  align-items: center;
  justify-content: center;
}
.slot-inner {
  width: 296px; height: 12px;
  background: #020204;
  border-radius: 3px;
  position: relative;
  overflow: hidden;
  box-shadow:
    inset 0 3px 10px rgba(0,0,0,1),
    0 1px 0 rgba(255,255,255,0.05),
    0 -1px 0 rgba(0,0,0,0.7);
}
.slot-glow {
  position: absolute; inset: 0;
  opacity: 0;
  animation: slotGlow 5.5s ease-in-out infinite; animation-delay: 0.8s;
}
@keyframes slotGlow {
  0%,18%  { opacity:0; background:linear-gradient(90deg,transparent,rgba(255,90,0,0.2),transparent); }
  28%     { opacity:1; background:linear-gradient(90deg,transparent,rgba(255,110,0,0.35),transparent); }
  52%     { opacity:1; background:linear-gradient(90deg,transparent,rgba(255,60,0,0.25),transparent); }
  62%     { opacity:1; background:linear-gradient(90deg,transparent,rgba(0,200,80,0.28),transparent); }
  75%,100%{ opacity:0; }
}

/* BACK PANEL (below slot — the key layer that hides the card) */
.t-back {
  position: absolute;
  left: 50%; transform: translateX(-50%);
  top: 302px;   /* starts right after slot bottom */
  bottom: 50px;
  width: 420px;
  z-index: 20;
  background: linear-gradient(180deg, #222224 0%, #1c1c1e 50%, #181819 100%);
  border-radius: 0 0 14px 14px;
  box-shadow:
    0 12px 44px rgba(0,0,0,0.95),
    inset 0 -1px 0 rgba(0,0,0,0.5);
}

/* BASE LEDGE */
.t-base {
  position: absolute;
  left: 50%; transform: translateX(-50%);
  bottom: 40px;
  width: 440px; height: 10px;
  z-index: 50;
  background: linear-gradient(180deg, #171718, #101011);
  border-radius: 0 0 8px 8px;
  box-shadow: 0 10px 32px rgba(0,0,0,1);
}

/* STATUS */
.status-txt {
  position: absolute;
  bottom: 12px; left: 50%; transform: translateX(-50%);
  z-index: 60;
  font-size: 9px; font-weight: 600;
  letter-spacing: 0.45em; text-transform: uppercase;
  white-space: nowrap;
  transition: color 0.4s;
  color: rgba(255,255,255,0.15);
}

/* TITLE */
.title {
  position: absolute;
  top: 4px; left: 50%; transform: translateX(-50%);
  z-index: 60; white-space: nowrap;
  font-family: 'Archivo Black', sans-serif;
  font-size: 9px; letter-spacing: 0.5em; text-transform: uppercase;
  color: rgba(255,255,255,0.07);
}


/* ═══════════════════════════════════════════════
   ANIMATION KEYFRAMES
   ═══════════════════════════════════════════════
   Card height: 204px
   Card starts at top: 28px  → card bottom at rest: 232px
   Slot top: 286px, slot bottom: 302px
   Machine back starts at 302px (z=20, hides card below that)

   For card to FULLY vanish:
   card top must reach ≥ 302px (machine-back top)
   card top starts at 28px → need translateY = 302 - 28 = 274px
   Add a few px buffer → 280px
*/
@keyframes cardSlide {
  0%        { transform: translateX(-50%) translateY(0); }
  13%       { transform: translateX(-50%) translateY(0); }
  /* glide down — fully hidden inside machine */
  44%       { transform: translateX(-50%) translateY(280px); }
  56%       { transform: translateX(-50%) translateY(280px); }
  /* glide back up */
  82%       { transform: translateX(-50%) translateY(0); }
  100%      { transform: translateX(-50%) translateY(0); }
}

/* Color flips while card is completely hidden (at ~50% of timeline) */
@keyframes cardBg {
  0%,  48.9% {
    background: linear-gradient(148deg, #ffffff 0%, #eeeeee 38%, #f7f7f7 58%, #ffffff 100%);
    box-shadow:
      0 0 0 1px rgba(0,0,0,0.07),
      0 4px 14px rgba(0,0,0,0.12),
      0 18px 44px rgba(0,0,0,0.16);
  }
  49%, 100% {
    background: linear-gradient(148deg, #1a1a1a 0%, #0e0e0e 32%, #1f1f1f 58%, #131313 100%);
    box-shadow:
      0 0 0 1px rgba(255,255,255,0.06),
      0 4px 14px rgba(0,0,0,0.55),
      0 18px 44px rgba(0,0,0,0.65);
  }
}

@keyframes grainMode {
  0%,   48.9% { mix-blend-mode: multiply; opacity: 1; }
  49%,  100%  { mix-blend-mode: screen;   opacity: 0.2; }
}
@keyframes colDark {
  0%,   48.9% { color: #1a1a1a; }
  49%,  100%  { color: rgba(255,255,255,0.86); }
}
@keyframes colNetwork {
  0%,   48.9% { color: #1c3a88; }
  49%,  100%  { color: rgba(255,255,255,0.65); }
}
@keyframes nfcCol {
  0%,   48.9% { color: rgba(26,26,26,0.5); }
  49%,  100%  { color: rgba(255,255,255,0.36); }
}
@keyframes decoA {
  0%,  48.9% {
    background: radial-gradient(circle, rgba(190,215,255,0.22) 0%, transparent 70%);
    border: 1px solid rgba(170,200,245,0.14);
  }
  49%, 100% {
    background: radial-gradient(circle, rgba(255,255,255,0.04) 0%, transparent 70%);
    border: 1px solid rgba(255,255,255,0.05);
  }
}
@keyframes decoB {
  0%,  48.9% {
    background: radial-gradient(circle, rgba(165,195,250,0.14) 0%, transparent 70%);
    border: 1px solid rgba(150,185,238,0.09);
  }
  49%, 100% {
    background: radial-gradient(circle, rgba(255,255,255,0.025) 0%, transparent 70%);
    border: 1px solid rgba(255,255,255,0.035);
  }
}
@keyframes sheenAnim {
  0%,12%  { opacity:0; }
  16%     { opacity:1; }
  22%     { opacity:0; }
  42%,58% { opacity:0; }
  64%     { opacity:0; }
  72%     { opacity:1; }
  80%     { opacity:0; }
  100%    { opacity:0; }
}
</style>
</head>
<body>

<div class="scene">

  <div class="title">Card Transformation</div>

  <!-- ══ CARD ══ -->
  <div class="card-wrap">
    <div class="card">
      <div class="deco a"></div>
      <div class="deco b"></div>
      <div class="bank-name">Nova Bank</div>
      <div class="chip">
        <div class="chip-vline l"></div>
        <div class="chip-vline r"></div>
      </div>
      <div class="nfc">
        <svg viewBox="0 0 24 24" fill="none">
          <path d="M12 3C7 3 3.5 6.5 3 11" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" opacity="0.9"/>
          <path d="M12 7C9 7 6.8 9 6.3 11.8" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" opacity="0.62"/>
          <path d="M12 11C10.9 11 10 12 10 13.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" opacity="0.36"/>
          <circle cx="12" cy="14.5" r="1.3" fill="currentColor"/>
        </svg>
      </div>
      <div class="num">
        <span>4562</span><span>••••</span><span>••••</span><span>8341</span>
      </div>
      <div class="holder">A. MARTIN</div>
      <div class="expiry">
        <span class="exp-lbl">Valid Thru</span>09/28
      </div>
      <div class="network">VISA</div>
    </div>
  </div>

  <!-- ══ TERMINAL ══ -->
  <!-- front panel (above slot) -->
  <div class="t-front">
    <div class="led-row">
      <div class="led"></div>
      <span class="led-lbl">Processing</span>
    </div>
    <div class="brand">NovaTerm Pro</div>
  </div>

  <!-- slot opening -->
  <div class="t-slot">
    <div class="slot-inner">
      <div class="slot-glow"></div>
    </div>
  </div>

  <!-- back panel (below slot — hides card) -->
  <div class="t-back"></div>

  <!-- base ledge -->
  <div class="t-base"></div>

  <!-- status label -->
  <div class="status-txt" id="stEl">INSERT CARD</div>

</div>

<script>
const el = document.getElementById('stEl');
const steps = [
  { t: 0,    msg: 'INSERT CARD', col: 'rgba(255,255,255,0.15)' },
  { t: 700,  msg: 'READING ···', col: '#e07830' },
  { t: 2400, msg: 'PROCESSING',  col: '#cc5522' },
  { t: 3400, msg: 'APPROVED  ✓', col: '#33cc66' },
  { t: 4800, msg: 'INSERT CARD', col: 'rgba(255,255,255,0.15)' },
];
function run() {
  steps.forEach(({ t, msg, col }) => {
    setTimeout(() => { el.textContent = msg; el.style.color = col; }, t);
  });
}
setTimeout(() => { run(); setInterval(run, 5500); }, 800);
</script>
</body>
</html>
```

🧠 Le Manuel Ultime : Comment Coder une IA Conversationnelle de A à Z

Ce document est un plan directeur exhaustif destiné à comprendre, structurer et coder une Intelligence Artificielle (IA) conversationnelle. Il est conçu pour être à la fois un cours magistral pour un humain et un cahier des charges compréhensible par une autre IA (voir la dernière section) pour générer un projet fonctionnel.

PARTIE 1 : Comprendre les Différents Types d'IA

Avant de coder, il faut savoir ce que l'on code. L'IA n'est pas magique, c'est un ensemble de mathématiques et de logique. Voici les grands types d'IA existants :

1. IA Basée sur les Règles (Rule-Based AI / Systèmes Experts)

Concept : Ce n'est pas vraiment "intelligent". Le programme suit des instructions strictes : SI l'utilisateur dit X, ALORS répondre Y.

Fonctionnement : Utilise des expressions régulières (Regex) et des arbres de décision.

Avantages : 100% prévisible, aucune hallucination, très rapide.

Inconvénients : Incapable de comprendre le contexte ou les nuances. Si l'utilisateur fait une faute d'orthographe, l'IA est perdue.

2. Machine Learning Classique (Apprentissage Automatique)

Concept : L'IA apprend à partir de données sans être explicitement programmée pour chaque règle.

Sous-types : * Apprentissage Supervisé : On donne à l'IA des exemples (Ex: 1000 phrases étiquetées "Salutation", 1000 étiquetées "Question").

Apprentissage Non-Supervisé : L'IA trouve des modèles par elle-même (Clustering).

Application NLP : Classification d'intentions (Intent Matching) via des algorithmes comme Naive Bayes ou SVM couplés à TF-IDF (Term Frequency-Inverse Document Frequency).

3. Deep Learning (Apprentissage Profond)

Concept : Utilisation de Réseaux de Neurones Artificiels inspirés du cerveau humain, avec plusieurs "couches" (layers) cachées.

Architectures courantes :

RNN (Réseaux de Neurones Récurrents) / LSTM : Ancienne norme pour le texte, bons pour mémoriser des séquences courtes mais oublient vite le contexte lointain.

CNN (Réseaux de Neurones Convolutifs) : Surtout pour l'image, mais parfois utilisés pour extraire des caractéristiques d'un texte.

4. Les Modèles Fondateurs et Transformeurs (L'ère moderne des LLMs)

Concept : Basés sur l'architecture "Transformer" (inventée par Google en 2017 avec le papier Attention Is All You Need). C'est ce qui fait tourner ChatGPT, Gemini, Claude.

Le Mécanisme Clé - L'Attention : Permet à l'IA de peser l'importance de chaque mot par rapport à tous les autres mots de la phrase, peu importe leur distance.

IA Générative : Au lieu de choisir une réponse dans une base de données, elle prédit le mot suivant avec des probabilités.

5. Apprentissage par Renforcement (Reinforcement Learning - RL)

Concept : L'IA apprend par essais et erreurs avec un système de récompenses et de punitions (comme dresser un chien).

Application : RLHF (Reinforcement Learning from Human Feedback) : des humains notent les réponses de l'IA pour l'aligner sur des comportements éthiques et utiles.

PARTIE 2 : Architecture d'une "Mini-IA" Indépendante (Le Plan des Fichiers)

Pour créer une IA conversationnelle fonctionnelle from scratch (sans juste faire des appels à l'API d'OpenAI), nous allons concevoir une IA par Classification d'Intentions avec un Réseau de Neurones Feed-Forward. C'est le meilleur compromis pour une "mini-IA" performante, rapide, et tournant sur un ordinateur classique.

Voici l'arborescence complète du projet que l'IA devra générer :

/mon_ia_conversationnelle
│
├── main.py                 # Le point d'entrée, l'interface utilisateur (CLI ou API)
├── config.py               # Le cerveau des paramètres (variables ultra utiles)
├── data.json               # La base de connaissances (intents, patterns, responses)
├── nlp_utils.py            # La boîte à outils de traitement du langage naturel
├── train.py                # Le script pour entraîner le réseau de neurones
├── model.py                # L'architecture mathématique du Réseau de Neurones (PyTorch)
├── memory.py               # Le gestionnaire de contexte et d'historique
└── chat.py                 # La boucle de prédiction (Inférence) de l'IA


Rôles des Fichiers :

data.json : Contient les intentions. Ex: un tag "salutation" avec des patterns ("bonjour", "salut") et des réponses associées.

nlp_utils.py : Tokenisation (découper les phrases), Stemming (trouver la racine des mots), et création du "Bag of Words" (sac de mots).

model.py : Le code PyTorch définissant les couches d'entrée, cachées, et de sortie du cerveau.

train.py : Convertit le texte en nombres, les passe dans le modèle, calcule l'erreur, et ajuste les poids (Backpropagation).

chat.py : Prend l'input utilisateur, le traite, demande au modèle de prédire l'intention, et pioche la réponse correspondante.

PARTIE 3 : Les Variables "Ultra Utiles" (Explications Critiques)

Dans le fichier config.py et dans le code en général, on retrouve des variables fondamentales. Si on ne les maîtrise pas, l'IA ne fonctionnera pas.

1. Variables de Structure (NLP & Deep Learning)

VOCAB_SIZE (Taille du vocabulaire) : Le nombre total de mots uniques que votre IA connaît. Si l'utilisateur utilise un mot hors vocabulaire (OOV - Out of Vocabulary), l'IA le transformera souvent en <UNK> (Unknown).

EMBEDDING_DIM (Dimension de plongement) : Pour qu'une IA comprenne le sens d'un mot, elle le transforme en un vecteur (une liste de nombres). Par exemple, [0.2, -0.5, 0.9]. La taille de ce vecteur est l'Embedding Dim. Plus il est grand, plus l'IA saisit de nuances, mais plus elle est lente.

HIDDEN_DIM / HIDDEN_SIZE (Taille de la couche cachée) : Le nombre de "neurones" dans le cerveau de votre modèle. Pour une petite IA, 8 ou 16 suffisent. Pour un LLM, on parle de dizaines de milliers.

2. Variables d'Entraînement (Hyperparamètres)

EPOCHS (Époques) : Le nombre de fois que l'IA va lire l'intégralité de vos données d'entraînement (data.json). Si EPOCHS = 1000, elle va réviser 1000 fois. Trop bas : elle n'apprend rien (Underfitting). Trop haut : elle apprend par cœur et perd sa logique (Overfitting).

LEARNING_RATE (Taux d'apprentissage - ex: 0.001) : La vitesse à laquelle l'IA corrige ses erreurs. S'il est trop grand, l'IA saute par-dessus la bonne réponse. S'il est trop petit, l'entraînement prend une éternité.

BATCH_SIZE (Taille du lot) : Combien d'exemples l'IA analyse-t-elle à la fois avant de corriger ses poids. BATCH_SIZE = 8 est classique pour une petite IA.

3. Variables de Génération (Pour les LLMs avancés)

TEMPERATURE (Température) : Contrôle la créativité.

0.0 = Strict, déterministe, logique, choisit toujours le mot le plus probable.

1.0 = Créatif, aléatoire, prend des risques (peut halluciner).

TOP_P (Nucleus Sampling) : Alternative à la température. L'IA ne considère que le sous-ensemble de mots dont la somme des probabilités atteint la valeur P (ex: 0.9). Évite à l'IA de sortir des mots complètement absurdes.

CONTEXT_WINDOW (Fenêtre de contexte) : La mémoire à court terme de l'IA mesurée en "Tokens" (morceaux de mots). Si le contexte est de 4096 tokens, l'IA oubliera le début de la conversation une fois cette limite dépassée.

PARTIE 4 : Morceaux de Code Incontournables & Algorithmes de Base

Voici les "briques Lego" que 90% des IA utilisent sous le capot.

1. Le Bag of Words (Sac de mots) - Le pilier de l'IA classique

L'IA ne lit pas de texte, elle lit des mathématiques. Le Bag of Words convertit une phrase en un tableau de 0 et de 1.

# Exemple de logique NLP dans nlp_utils.py
import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np

stemmer = PorterStemmer()

def tokenize(sentence):
    """Sépare la phrase en tableau de mots"""
    return nltk.word_tokenize(sentence)

def stem(word):
    """Trouve la racine du mot (ex: marchant -> march)"""
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, words):
    """
    phrase = ["bonjour", "comment", "tu", "vas"]
    mots_connus = ["bonjour", "salut", "je", "tu", "vas", "bien", "comment"]
    bag   =       [   1,         0,       0,    1,    1,      0,        1   ]
    """
    sentence_words = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1.0
    return bag


2. Le Réseau de Neurones de Base (PyTorch)

Voici comment construire le cerveau. C'est un modèle "Feed-Forward" (propagation avant). Il prend le "Bag of words", le fait passer par des couches linéaires (multiplications matricielles) avec une fonction d'activation ReLU (qui empêche les valeurs négatives, ajoutant de la non-linéarité pour des calculs complexes).

# Extrait de model.py
import torch
import torch.nn as nn

class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        # Couche d'entrée vers couche cachée 1
        self.l1 = nn.Linear(input_size, hidden_size) 
        # Couche cachée 1 vers couche cachée 2
        self.l2 = nn.Linear(hidden_size, hidden_size) 
        # Couche cachée 2 vers la sortie (prédiction des intentions)
        self.l3 = nn.Linear(hidden_size, num_classes)
        # Fonction d'activation
        self.relu = nn.ReLU()
    
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        # Pas d'activation softmax ici car PyTorch l'inclut dans sa fonction de perte CrossEntropy
        return out


3. Le Mécanisme de l'Attention (La révolution des LLM)

Bien que notre Mini-IA n'en ait pas besoin, il est capital de comprendre ce code. Voici le cœur des IA modernes comme ChatGPT : l'Attention Multi-Têtes.
L'idée est de créer trois vecteurs pour chaque mot : Query (Requête), Key (Clé) et Value (Valeur).

# Concept simplifié de l'Attention (Self-Attention)
import torch
import torch.nn.functional as F
import math

def attention(query, key, value):
    # 1. Produit matriciel entre Requête et Clé pour voir "quels mots sont liés entre eux"
    scores = torch.matmul(query, key.transpose(-2, -1))
    
    # 2. Mise à l'échelle (pour éviter des gradients explosifs)
    d_k = query.size(-1)
    scores = scores / math.sqrt(d_k)
    
    # 3. Softmax : transforme les scores en pourcentages (probabilités de 0 à 1)
    attention_weights = F.softmax(scores, dim=-1)
    
    # 4. On applique ces poids aux Valeurs réelles des mots
    output = torch.matmul(attention_weights, value)
    
    return output, attention_weights


4. La Boucle d'Inférence (Parler à l'IA)

Une fois le modèle entraîné, voici la boucle qui maintient l'IA "en vie" en attendant vos messages.

# Extrait de chat.py
def chat_loop():
    print("L'IA est prête ! (Tapez 'quitter' pour arrêter)")
    while True:
        sentence = input("Vous: ")
        if sentence == "quitter":
            break
            
        # 1. Tokeniser la phrase de l'utilisateur
        sentence_tokenized = tokenize(sentence)
        
        # 2. Convertir en tableau de nombres (Bag of Words)
        X = bag_of_words(sentence_tokenized, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X)
        
        # 3. Faire la prédiction avec le modèle
        output = model(X)
        _, predicted = torch.max(output, dim=1)
        
        # 4. Trouver l'intention correspondante
        tag = tags[predicted.item()]
        
        # 5. Vérifier la certitude (probabilité)
        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        
        # 6. Répondre
        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    print(f"IA: {random.choice(intent['responses'])}")
        else:
            print("IA: Je ne suis pas sûr de bien comprendre...")


PARTIE 5 : Gestion de la Mémoire (Le Secret d'une Vraie Conversation)

Une IA basique traite chaque message indépendamment. Pour qu'elle s'en souvienne, il faut créer une classe de mémoire.

# Extrait de memory.py
class ConversationMemory:
    def __init__(self, max_history=5):
        self.history = []
        self.max_history = max_history
        
    def add_message(self, role, content):
        self.history.append({"role": role, "content": content})
        # Garder seulement les X derniers messages pour ne pas saturer l'IA
        if len(self.history) > self.max_history * 2: # *2 car questions+réponses
            self.history.pop(0)
            
    def get_context_string(self):
        """Assemble l'historique pour le donner à l'IA avant sa réponse"""
        context = ""
        for msg in self.history:
            context += f"{msg['role']}: {msg['content']} | "
        return context


PARTIE 6 : LE META-PROMPT DE GÉNÉRATION (À COPIER-COLLER À UNE IA)

Voici le texte exact que vous devez fournir à une intelligence artificielle (comme un LLM de codage) pour qu'elle lise les instructions ci-dessus et génère le code complet, prêt à l'emploi.

INSTRUCTIONS POUR L'IA GÉNÉRATRICE :

"Tu es un ingénieur en Machine Learning et développement logiciel de niveau Senior. Ton objectif est de générer le code source complet et fonctionnel pour une mini-IA conversationnelle basée sur la classification d'intentions en Python (utilisant PyTorch et NLTK).

Je veux que tu me génères les fichiers suivants dans des blocs de code séparés et clairement identifiés :

data.json : Un fichier JSON contenant au moins 5 intentions différentes (salutation, au_revoir, identite, blague, meteo) avec des patterns et des responses.

nlp_utils.py : Un script contenant les fonctions tokenize, stem, et bag_of_words utilisant nltk.

model.py : Une classe PyTorch NeuralNet (Réseau de Neurones Feed-Forward avec 3 couches linéaires et des activations ReLU).

train.py : Le script complet qui charge le JSON, prépare les données d'entraînement (X_train, y_train), instancie le modèle, définit la CrossEntropyLoss et l'optimiseur Adam, exécute la boucle d'entraînement sur 1000 EPOCHS, et sauvegarde le modèle dans data.pth.

chat.py : La boucle interactive infinie qui charge data.pth, attend les inputs de l'utilisateur dans le terminal, utilise le modèle pour prédire l'intention, vérifie que la probabilité est supérieure à 75%, et affiche une réponse aléatoire parmi celles du JSON.

L'architecture et la logique doivent suivre scrupuleusement les explications fournies dans le 'Plan Directeur IA' que nous venons de conceptualiser. Le code doit être abondamment commenté en français. Ne génère rien d'autre que les fichiers requis, avec un code propre, sans erreurs, et prêt à être exécuté (en supposant que j'ai fait pip install torch torchvision nltk)."

Conclusion et Étapes pour le Déploiement

Une fois que l'IA aura généré ces fichiers grâce au Meta-Prompt :

Créez un dossier vide sur votre PC.

Copiez-collez les codes générés dans les fichiers correspondants.

Ouvrez un terminal dans ce dossier.

Installez les dépendances : pip install torch nltk numpy

Téléchargez les données de tokenization nltk (lancez python et tapez : import nltk; nltk.download('punkt'))

Lancez l'entraînement : python train.py (Cela va créer un fichier data.pth qui est le "cerveau" entraîné).

Lancez le chat : python chat.py

Félicitations, vous avez l'architecture et la logique mathématique complète pour créer, comprendre et déployer votre propre Intelligence Artificielle conversationnelle.