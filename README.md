# Master Humans 🧍

Site parodique façon Uber Eats pour l'installation **Master Humans** — *« C'est bon d'être traité comme un produit. »*

Détournement satirique d'une interface de livraison de repas, accessible via QR code depuis l'affiche.

---

## 🚀 Déploiement sur Render (gratuit)

Le site est entièrement **statique** (un seul `index.html`, aucune base de données, aucun backend). Le déploiement est immédiat.

### 1. Mettre le projet sur GitHub

```bash
git init
git add .
git commit -m "Master Humans - site parodique"
git branch -M main
git remote add origin https://github.com/TON-PSEUDO/master-humans.git
git push -u origin main
```

### 2. Déployer sur Render

1. Va sur https://render.com et connecte ton compte GitHub.
2. Clique **New +** → **Static Site**.
3. Sélectionne le dépôt `master-humans`.
4. Renseigne :
   - **Name** : `master-humans` (ou ce que tu veux)
   - **Branch** : `main`
   - **Build Command** : *(laisser vide)*
   - **Publish Directory** : `.`
5. Clique **Create Static Site**.

En ~1 minute, Render te donne une URL publique du type :

```
https://master-humans.onrender.com
```

> 💡 Le `render.yaml` inclus configure tout automatiquement si tu utilises l'option **Blueprint** (New + → Blueprint) au lieu de Static Site.

### 3. Générer le QR code de l'affiche

Une fois l'URL Render obtenue, lance le script avec cette URL :

```bash
python3 make_poster.py "https://master-humans.onrender.com"
```

Le script remplace le QR de l'affiche par un nouveau pointant vers le site en ligne.

---

## ⚠️ Note pour l'expo (Render gratuit)

Le plan **Static Site gratuit de Render ne s'endort pas** (contrairement aux Web Services gratuits). Ton site reste donc accessible en permanence, sans délai de réveil. Parfait pour une expo.

Teste l'URL + le QR sur 2-3 téléphones avant l'ouverture.

---

## 📁 Contenu

- `index.html` — le site complet (HTML/CSS/JS, autonome)
- `render.yaml` — config de déploiement Render
- `README.md` — ce fichier
