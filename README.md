# 🎰 Martingale Limbo Simulator

**Simulation réaliste de la stratégie Martingale appliquée au jeu Limbo.**  
Testez la vraie viabilité de cette stratégie avec différentes balances, multiplicateurs et conditions de faillite.

---

## 📌 Qu'est-ce que la Martingale ?

> La Martingale est une stratégie de pari simple : **doubler la mise après chaque perte** jusqu'à enfin gagner — et récupérer toutes ses pertes avec un petit gain.

Cette stratégie repose sur **l’illusion** que la victoire finit toujours par arriver **avant que vous ne manquiez d’argent**.

---

## 🧠 Comment fonctionne ce simulateur ?

- Vous choisissez une **mise de départ**, un **multiplicateur cible** (ex: x2) et une **balance initiale**.
- À chaque tour :
  - Un **résultat aléatoire** est généré (comme dans Limbo).
  - Si le résultat ≥ multiplicateur cible → **vous gagnez**.
  - Sinon → vous **doublez la mise** et continuez.
- La simulation s'arrête si :
  - Vous atteignez la limite de mises consécutives,
  - Vous manquez d’argent,
  - Ou le nombre de tours est atteint.

---

## 🧪 Résultats typiques

- Plus la **balance initiale est élevée**, plus vous **gagnez souvent**.
- Mais dès que vous perdez une seule fois avec une longue série de pertes → 💥 **faillite**.
- Ce simulateur permet de visualiser la **fréquence et la gravité** de ces échecs.

---

## ⚠️ Les illusions de la Martingale

> **Oui**, vous pouvez gagner **plus de 90 % du temps**.
>
> Mais...
>
> **Une seule défaite** peut effacer **des centaines de gains.**
>
> Vous ne jouez pas contre un casino : **vous jouez contre les probabilités à long terme.**

---
