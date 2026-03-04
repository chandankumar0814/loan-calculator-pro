# 💰 Loan Calculator Pro — PWA

An offline-capable Progressive Web App for calculating and comparing **Flat Rate** and **Reducing Balance** loans with full **Down Payment** support.

## ✨ Features

- **Down Payment** — toggle on/off with quick preset pills (5%, 10%, 20%, 25%, 30%, 50%)
- **LTV Meter** — visual Loan-to-Value ratio bar with colour-coded health indicator
- **Flat Rate Calculator** — EMI, Total Interest, Effective APR
- **Reducing Balance Calculator** — with stacked bar chart over tenure
- **Comparison Tab** — side-by-side with Grand Total (DP + loan repayment)
- **Amortization Schedule** — full month-by-month table with CSV export (includes DP metadata)
- **Guide** — all formulas, explanations, and tips
- **Installable PWA** — works 100% offline after first load

## 🚀 Deploy to GitHub Pages

1. Create a new GitHub repository
2. Upload all files: `index.html`, `sw.js`, `manifest.json`, `README.md`
3. Run icon generator (see below) and upload the `icons/` folder
4. Go to **Settings → Pages → Deploy from branch → main → / (root)**
5. Visit `https://yourusername.github.io/your-repo-name`

## 🖼️ Generate Icons

```bash
pip install Pillow
python generate-icons.py
```

## 📁 File Structure

```
/
├── index.html            ← Main app (all-in-one)
├── sw.js                 ← Service Worker (offline caching)
├── manifest.json         ← PWA manifest
├── generate-icons.py     ← Icon generator script (run once)
├── README.md
└── icons/
    ├── icon-72.png
    ├── icon-96.png
    ├── icon-128.png
    ├── icon-144.png
    ├── icon-152.png
    ├── icon-192.png
    ├── icon-384.png
    └── icon-512.png
```

## 📐 Formulas

### Flat Rate
```
Loan Amount = Asset Price − Down Payment
Monthly Interest = Loan × R / 12 / 100
EMI = (Loan / N) + Monthly Interest
Total Interest = Monthly Interest × N
Grand Total = Down Payment + Loan + Total Interest
```

### Reducing Balance
```
r = R / 12 / 100
EMI = Loan × r × (1+r)^N / ((1+r)^N − 1)
Grand Total = Down Payment + EMI × N
```

## 🔒 Privacy
All calculations are done 100% in the browser. No data is ever sent to any server.
