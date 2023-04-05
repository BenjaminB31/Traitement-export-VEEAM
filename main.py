import os
import re
from bs4 import BeautifulSoup

# Variable contenant le nom de la VM
var_nom = "vm"

# Variable contenant le fichier VEEAM
var_fichier = "backups.html"

# ----------------------------------------------------------------

# Ouvrir le fichier HTML
with open(var_fichier, "r") as file:
    html = file.read()

# Ajouter un saut de ligne après chaque balise </tr>
html = html.replace("</tr>", "</tr>\n")

# Supprimer un saut de ligne avant chaque balise </td>
html = html.replace("\n</td>", "</td>")

html = html.splitlines()

var1 = "</td><td style=\"padding: 2px 3px 2px 3px;vertical-align: top;border: 1px solid #a7a9ac;font-family: Tahoma;font-size: 12px;\" nowrap=\"nowrap\"><span style="

# Rechercher les lignes contenant "</td><td" et effacer celles qui ne contiennent pas la variable spécifiée
new_html = []
for line in html:
    if var1 in line:
        if var_nom in line:
            new_html.append(line)
        else:
            continue
    else:
        new_html.append(line)

# Rejoindre les lignes du fichier HTML en une seule chaîne de caractères
html = "\n".join(new_html)

# Supprimer les sauts de ligne inutiles
html = re.sub('\n\s*\n', '\n', html)

# Ajouter des indentations pour améliorer la lisibilité
html = re.sub(r'>\s*<', '>\n<', html)

# Écrire les modifications dans le fichier
with open(var_nom + ".html", "w") as file:
    file.write(html)
