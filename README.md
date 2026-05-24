<div align="center">

```
██████╗  █████╗ ██████╗ ██╗  ██╗██╗███████╗██╗   ██╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██║██╔════╝╚██╗ ██╔╝
██████╔╝███████║██████╔╝█████╔╝ ██║█████╗   ╚████╔╝ 
██╔═══╝ ██╔══██║██╔══██╗██╔═██╗ ██║██╔══╝    ╚██╔╝  
██║     ██║  ██║██║  ██║██║  ██╗██║██║        ██║   
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝  
```

### 🚗 *Find. Park. Go.* — Smart Parking, Zero Hassle.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1.1-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com)
[![Vercel](https://img.shields.io/badge/Deployed_on-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://vercel.com)

<br/>

> **Parkify** is a full-stack parking management system where users book spots in seconds  
> and admins manage lots, track revenue, and monitor occupancy — all in one sleek dashboard.

<br/>

[🚀 Live Demo](#) · [🐛 Report Bug](https://github.com/24f1001022/parkify/issues) · [✨ Request Feature](https://github.com/24f1001022/parkify/issues)

---

</div>

<br/>

## 🗺️ What Is Parkify?

Imagine driving around a crowded mall for 20 minutes looking for parking. **Parkify kills that problem.**

Users open the app → search by location or pincode → book a spot in one click → drive straight in. Admins get a real-time dashboard with revenue charts, occupancy heatmaps, and full lot management. No clipboard, no phone calls, no chaos.

<br/>

## ✨ Features at a Glance

```
┌─────────────────────────────────┐   ┌─────────────────────────────────┐
│          👤  USER SIDE          │   │         🛠️  ADMIN SIDE          │
├─────────────────────────────────┤   ├─────────────────────────────────┤
│  🔐  Secure Login / Signup      │   │  🏢  Add / Edit / Delete Lots   │
│  🔍  Search by Location/Pincode │   │  📍  Manage Individual Spots    │
│  🅿️  Reserve Parking Spots     │   │  📊  Revenue Analytics Chart    │
│  🚘  View Booking History       │   │  📈  Occupancy Bar Chart        │
│  💸  Real-time Cost Tracking    │   │  👥  View All Users             │
│  🔓  Release Parking & Pay      │   │  🔎  Search by User / Location  │
│  👤  Edit Profile               │   │  🗑️  Delete Spots Safely        │
└─────────────────────────────────┘   └─────────────────────────────────┘
```

<br/>

## 🧱 Tech Stack

| Layer | Technology |
|-------|-----------|
| 🐍 Backend | Flask 3.1 + Python 3.10+ |
| 🗄️ Database | SQLite + SQLAlchemy ORM |
| 🎨 Frontend | Jinja2 + Bootstrap 5 + Chart.js |
| 🔐 Auth | Werkzeug password hashing + Flask sessions |
| ☁️ Deployment | Vercel (Serverless) |

<br/>

## 🚀 Getting Started

### ⚡ Option A — Clone & Run in 60 Seconds

```bash
# 1. Clone the repo
git clone https://github.com/24f1001022/parkify.git
cd parkify

# 2. Create & activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create your .env file
echo "SECRET_KEY=your-secret-key-here" > .env
echo "SQLALCHEMY_DATABASE_URI=sqlite:///parkify.db" >> .env
echo "SQLALCHEMY_TRACK_MODIFICATIONS=False" >> .env

# 5. Run it!
python run.py
```

🎉 Open your browser at **http://127.0.0.1:5000**

---

### 🐳 Option B — One-liner Setup (Mac/Linux)

```bash
git clone https://github.com/24f1001022/parkify.git && cd parkify && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && cp .env.example .env && python run.py
```

---

### 🪟 Option C — Windows PowerShell Step by Step

```powershell
# Clone
git clone https://github.com/24f1001022/parkify.git
cd parkify

# Virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install packages
pip install -r requirements.txt

# Environment file
python -c "open('.env','w').write('SECRET_KEY=parkify-dev-key\nSQLALCHEMY_DATABASE_URI=sqlite:///parkify.db\nSQLALCHEMY_TRACK_MODIFICATIONS=False\n')"

# Launch
python run.py
```

<br/>

## 🔑 Default Admin Login

```
📧 Email    :  admin@parkify.com
🔒 Password :  admin
```

> ⚠️ Change the password after first login in production!

<br/>

## 🗂️ Project Structure

```
parkify/
│
├── 📄 app.py                  ← Flask app + config initialization
├── 📄 run.py                  ← Entry point (python run.py)
├── 📄 config.py               ← Legacy config reference
├── 📄 requirements.txt        ← Python dependencies
├── 📄 vercel.json             ← Vercel deployment config
├── 📄 .env                    ← Environment variables (never commit this!)
│
├── 📁 api/
│   └── 📄 index.py            ← Vercel serverless handler
│
├── 📁 models/
│   └── 📄 models.py           ← SQLAlchemy DB models
│
├── 📁 routes/
│   └── 📄 routes.py           ← All URL routes + auth decorators
│
├── 📁 controller/
│   ├── 📄 user_controller.py  ← User logic (login, book, release)
│   └── 📄 admin_controller.py ← Admin logic (lots, search, summary)
│
└── 📁 templates/              ← Jinja2 HTML templates
    ├── layout.html            ← Base layout
    ├── navbar.html            ← Navigation bar
    ├── login.html / signup.html
    ├── user_dashbord.html     ← User home
    ├── admin_dashbord.html    ← Admin home
    ├── booking_page.html
    ├── release_parking.html
    └── ...
```

<br/>

## 🗄️ Database Models

```
┌──────────────┐       ┌─────────────────┐       ┌──────────────┐
│     User     │       │   ParkingLot    │       │ ParkingSpot  │
├──────────────┤       ├─────────────────┤       ├──────────────┤
│ id (PK)      │       │ id (PK)         │       │ id (PK)      │
│ email        │       │ location_name   │  1:N  │ lot_id (FK)  │
│ passhash     │       │ address         │──────▶│ status (A/O) │
│ full_name    │       │ pincode         │       └──────┬───────┘
│ pin_code     │       │ price/hr        │              │ 1:N
│ address      │       │ max_spots       │              ▼
│ is_admin     │       └─────────────────┘       ┌──────────────┐
└──────┬───────┘                                 │ Reservation  │
       │ 1:N                                     ├──────────────┤
       └────────────────────────────────────────▶│ id (PK)      │
                                                 │ user_id (FK) │
                                                 │ spot_id (FK) │
                                                 │ vehicle_no   │
                                                 │ parked_at    │
                                                 │ left_at      │
                                                 │ total_cost   │
                                                 └──────────────┘
```

<br/>

## ☁️ Deploy to Vercel

```bash
# 1. Install Vercel CLI
npm i -g vercel

# 2. Login
vercel login

# 3. Deploy
vercel --prod
```

Or connect via **[vercel.com](https://vercel.com)** → Import GitHub repo → Add env vars → Deploy.

**Required environment variables on Vercel:**

| Variable | Value |
|----------|-------|
| `SECRET_KEY` | `your-strong-secret-key` |
| `SQLALCHEMY_DATABASE_URI` | `sqlite:////tmp/parkify.db` |
| `SQLALCHEMY_TRACK_MODIFICATIONS` | `False` |

> 💡 For persistent data on Vercel, use [Neon](https://neon.tech) (free PostgreSQL)  
> and replace the URI with `postgresql://user:pass@host/dbname`

<br/>

## 🐛 Bugs Fixed in This Version

| # | Bug | Status |
|---|-----|--------|
| 1 | Missing `.env` file — app crashed on startup | ✅ Fixed |
| 2 | Circular import double-loading Flask app | ✅ Fixed |
| 3 | Typo `SQLALCHEMY_TRACK_MODIFICATONS` | ✅ Fixed |
| 4 | `release_parking` null check AFTER attribute access | ✅ Fixed |
| 5 | Missing `return` in release parking else branch | ✅ Fixed |
| 6 | `moredetails` crashed if no reservation found | ✅ Fixed |
| 7 | Jinja2 `Available` unquoted — UndefinedError | ✅ Fixed |
| 8 | No cascade delete on Lot → Spot → Reservation | ✅ Fixed |
| 9 | `edit_lot` redirected to `add_lot` on error | ✅ Fixed |
| 10 | HTTP method `'Post'` (case-sensitive Flask bug) | ✅ Fixed |

<br/>

## 🔮 Future Roadmap

- [ ] 📱 Mobile app (React Native)
- [ ] 💳 Online payments (Razorpay / Stripe)
- [ ] 🔔 Email / SMS booking notifications
- [ ] 🧠 AI-based parking demand prediction
- [ ] 🗺️ Map view with GPS integration
- [ ] 🌐 Multi-language support

<br/>

## 🤝 Contributing

Contributions are welcome! Here's how:

```bash
# Fork the repo, then:
git clone https://github.com/YOUR_USERNAME/parkify.git
git checkout -b feature/your-amazing-feature
# make your changes
git commit -m "feat: add your amazing feature"
git push origin feature/your-amazing-feature
# open a Pull Request on GitHub
```

<br/>

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

<br/>

---

<div align="center">

**Built with ❤️ by [Safwan Humayun](https://github.com/24f1001022)**

*If Parkify saved you time, drop a ⭐ on the repo — it means the world!*

```
🚗 ════════════════════════════════════════════ 🅿️
```

</div>
