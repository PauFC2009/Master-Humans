#!/usr/bin/env python3
"""
Remplace le QR code de l'affiche Master Humans par un QR pointant vers une URL.

Prérequis :
    pip install qrcode pillow

Usage :
    1. Place l'affiche d'origine dans ce dossier, nommée : affiche_source.png
       (ou modifie la variable SRC ci-dessous avec le bon nom)
    2. Lance :
       python3 make_poster.py "https://master-humans.onrender.com"

Le résultat est enregistré dans : affiche_master_humans.png
"""
import sys
import os
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image

# ---- Paramètres ----
URL = sys.argv[1] if len(sys.argv) > 1 else "https://master-humans.onrender.com"

# Chemins RELATIFS au dossier du script (mets l'affiche source à côté de ce fichier)
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "affiche_source.png")          # <-- ton affiche d'origine
OUT = os.path.join(HERE, "affiche_master_humans.png")   # <-- résultat

# Bounding box du QR d'origine (carré blanc), mesuré sur l'affiche 1024x1536.
# Si ton affiche a une autre résolution, ajuste ces valeurs proportionnellement.
BX0, BY0, BX1, BY1 = 47, 1377, 140, 1471
PAD = 3
QX0, QY0, QX1, QY1 = BX0 - PAD, BY0 - PAD, BX1 + PAD, BY1 + PAD
side = QX1 - QX0

# ---- Vérif ----
if not os.path.exists(SRC):
    print(f"[ERREUR] Affiche introuvable : {SRC}")
    print("Place ton affiche d'origine dans ce dossier sous le nom 'affiche_source.png',")
    print("ou modifie la variable SRC dans le script.")
    sys.exit(1)

# ---- Génération ----
poster = Image.open(SRC).convert("RGB")

# Adapte le bbox si la résolution diffère de 1024x1536
W, H = poster.size
if (W, H) != (1024, 1536):
    sx, sy = W / 1024.0, H / 1536.0
    QX0, QY0 = int((BX0 - PAD) * sx), int((BY0 - PAD) * sy)
    QX1, QY1 = int((BX1 + PAD) * sx), int((BY1 + PAD) * sy)
    side = QX1 - QX0

qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=10, border=2)
qr.add_data(URL)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
qr_img = qr_img.resize((side, QY1 - QY0), Image.NEAREST)

poster.paste(qr_img, (QX0, QY0))
poster.save(OUT, quality=95)
print("OK ->", OUT)
print("URL encodée :", URL)
