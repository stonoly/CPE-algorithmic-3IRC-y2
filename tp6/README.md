# TP6 - Tableaux associatifs


### Contexte:
Vinyl Records Co. gère un catalogue de disques vinyle. Chaque disque est identifié par une référence catalogue à 13 chiffres, et possède un titre, un artiste, une année de publication et un prix. L’application doit répondre à deux familles de requêtes :
- Requêtes ponctuelles : ”Quel est le prix du disque 9782070360024 ?”
- Requêtes par plage : ”Quels disques ont été publiés entre 1965 et 1975 ?”

Global: 

`printTree.py`

## Exercice 1 - Tables de hachage
> On indexe le catalogue par référence dans une table de hachage de taille m = 1009 (nombre premier) avec adressage ouvert par sondage linéaire. La fonction de hachage est : h(k) = k mod m, où k est la valeur numérique de la référence.
### Question 1: 
> Insérez les 4 clés suivantes dans la table. Donnez les alvéoles occupées et indiquez les collisions éventuelles
>
| Référence (k) | h(k) | Alvéole finale | Sondages supp. | Collision ? |
|---------------|------|----------------|----------------|-------------|
| 9782070360024 |_970_ |_970_           |_0_             |_NO_         |
| 9782070360033 |_979_ |_979_           |_0_             |_NO_         |
| 9782070361039 |_976_ |_976_           |_0_             |_NO_         |
| 9782207258002 |_855_ |_855_           |_0_             |_NO_         |

### Question 2: 
> On suppose que la table contient n = 700 éléments

> A. Calculez le facteur de charge $\alpha$ 

$
\alpha = n / m \\
n = 700 \\
m = 1009 \\
\alpha = 700 / 1009 \\
\alpha = 0,6937561943
$

> B. En sondage linéaire, le nombre moyen de sondes pour une recherche infructueuse est approximé par : $E[\mathrm{sondes}] = \frac{1}{2} \times \left( 1 + \frac{1}{(1-\alpha)^2} \right)$ Donnez la valeur numérique et commentez ce résultat.

$E[\mathrm{sondes}] = \frac{1}{2} \times \left( 1 + \frac{1}{(1-0,6937561943)^2} \right)$

$E[\mathrm{sondes}] = \frac{773081}{528081} \approx 1.463943978$


