# Deployment Guide - ritikgaire.com.np

## Quick Deployment Options

### 🚀 Recommended: Railway (Easiest & Free Tier)
**Best for**: Quick deployment, free hosting, automatic HTTPS
**Time**: ~10 minutes

### 🐳 DigitalOcean/VPS (Full Control)
**Best for**: Production-grade, custom configuration
**Cost**: $4-6/month

### 🌐 Render (Alternative Free Option)
**Best for**: Similar to Railway, good free tier

---

## Option 1: Railway (RECOMMENDED) ⭐

Railway offers free hosting with automatic HTTPS and is perfect for Django apps.

### Step 1: Prepare Your Project

Already done! Your project is ready.

### Step 2: Create Railway Account
1. Go to https://railway.app/
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"

### Step 3: Connect Your Repository
1. Push your code to GitHub:
```powershell
git init
git add .
git commit -m "Initial commit - Django portfolio"
git branch -M main
git remote add origin https://github.com/ritik123gaire/portfolio.git
git push -u origin main
```

2. Select your repository in Railway

### Step 4: Configure Environment Variables
In Railway dashboard, add these variables:
```
DJANGO_SECRET_KEY=your-super-secret-key-here-change-this
DEBUG=False
ALLOWED_HOSTS=ritikgaire.com.np,*.railway.app
DATABASE_URL=postgresql://... (Railway provides this automatically if you add PostgreSQL)
```

### Step 5: Point Your Domain
1. In Railway, go to Settings → Domains
2. Add custom domain: `ritikgaire.com.np`
3. Railway will give you a CNAME record
4. Go to your domain registrar's DNS settings
5. Add CNAME record:
   - Name: `@` or `www`
   - Value: (the value Railway provides)
   - TTL: 3600

**Railway will automatically handle HTTPS certificates!**

---

## Option 2: DigitalOcean/VPS (Production Grade)

### Requirements:
- DigitalOcean account ($4/month droplet)
- Basic Linux knowledge

### Step 1: Create Droplet
1. Create Ubuntu 22.04 droplet
2. SSH into your server

### Step 2: Server Setup
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install python3-pip python3-venv nginx postgresql -y

# Install Gunicorn
pip3 install gunicorn

# Clone your repository
git clone https://github.com/ritik123gaire/portfolio.git
cd portfolio

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
pip install gunicorn psycopg2-binary
```

### Step 3: Configure PostgreSQL
```bash
sudo -u postgres psql
CREATE DATABASE portfolio_db;
CREATE USER portfolio_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE portfolio_db TO portfolio_user;
\q
```

### Step 4: Configure Nginx
Create `/etc/nginx/sites-available/portfolio`:
```nginx
server {
    listen 80;
    server_name ritikgaire.com.np www.ritikgaire.com.np;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /home/yourusername/portfolio;
    }
    
    location /media/ {
        root /home/yourusername/portfolio;
    }

    location / {
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_pass http://unix:/home/yourusername/portfolio/portfolio.sock;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/portfolio /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

### Step 5: Create Gunicorn Service
Create `/etc/systemd/system/gunicorn.service`:
```ini
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=yourusername
Group=www-data
WorkingDirectory=/home/yourusername/portfolio
ExecStart=/home/yourusername/portfolio/venv/bin/gunicorn \
          --workers 3 \
          --bind unix:/home/yourusername/portfolio/portfolio.sock \
          portfolio_project.wsgi:application

[Install]
WantedBy=multi-user.target
```

Start service:
```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

### Step 6: SSL Certificate (HTTPS)
```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d ritikgaire.com.np -d www.ritikgaire.com.np
```

### Step 7: DNS Configuration
Point your domain to DigitalOcean:
1. Go to your domain registrar (where you bought ritikgaire.com.np)
2. Update nameservers to DigitalOcean's:
   - ns1.digitalocean.com
   - ns2.digitalocean.com
   - ns3.digitalocean.com
3. In DigitalOcean, add A record pointing to your droplet IP

---

## Option 3: Render.com (Free Alternative)

### Step 1: Create Account
1. Go to https://render.com/
2. Sign up with GitHub

### Step 2: Deploy
1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Configure:
   - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - Start Command: `gunicorn portfolio_project.wsgi:application`
4. Add environment variables (same as Railway)

### Step 3: Custom Domain
1. In Render dashboard, go to Settings → Custom Domain
2. Add `ritikgaire.com.np`
3. Update your DNS with provided CNAME

---

## Production Settings Checklist

Before deploying, ensure:

✅ DEBUG = False
✅ SECRET_KEY is secure and not in code
✅ ALLOWED_HOSTS configured
✅ Static files collected
✅ Database migrations applied
✅ HTTPS enabled
✅ Environment variables secured

---

## Which Option Should You Choose?

### Choose Railway/Render if:
- You want quick deployment
- You're okay with free tier limitations
- You want automatic HTTPS
- You don't need advanced server control

### Choose DigitalOcean/VPS if:
- You need full control
- You expect high traffic
- You want to learn server management
- You need custom configurations

---

## Need Help?

1. **Railway**: Simplest option, recommended for beginners
2. **DigitalOcean**: Best for production, more control
3. **Render**: Good middle ground

Choose based on your needs and budget!
