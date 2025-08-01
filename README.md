# 💰 Calculateur de Salaire Net – PLF 2025 🇲🇦

Application Django simple permettant de calculer le salaire net au Maroc en 2025, selon les règles fiscales (CNSS, AMO, Mutuelle, IR brut/net, charges familiales).

## 🔧 Fonctionnalités
- Saisie du salaire de base, primes/congés, indemnités exonérées, et charges familiales
- Calcul automatique du :
  - Salaire brut et brut imposable
  - CNSS, AMO, mutuelle
  - Frais professionnels
  - IR brut, IR net
  - Salaire net
- Export des résultats en PDF et Excel
- Historique des calculs

## ⚙️ Technologies
- Python 3.10+
- Django
- OpenPyXL
- ReportLab

## ▶️ Lancer le projet en local

```bash
python manage.py runserver
