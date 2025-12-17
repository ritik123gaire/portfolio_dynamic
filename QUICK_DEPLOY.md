# 🚀 Quick Deploy to ritikgaire.com.np - Railway Method

## What You Need:
- GitHub account
- Railway account (sign up at railway.app)
- Your domain DNS access

---

## Step-by-Step Deployment (10 minutes)

### 1️⃣ Push to GitHub

```powershell
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Ready for deployment"

# Create repository on GitHub (go to github.com → New Repository)
# Name it: portfolio or ritikgaire-portfolio

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/ritik123gaire/portfolio.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 2️⃣ Deploy on Railway

1. **Sign up**: Go to https://railway.app/ → Sign in with GitHub

2. **Create Project**:
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your portfolio repository

3. **Add PostgreSQL** (Recommended):
   - Click "+ New" → "Database" → "Add PostgreSQL"
   - Railway will automatically connect it to your app

4. **Environment Variables**:
   Click on your web service → Variables → Add these:
   ```
   DJANGO_SECRET_KEY = generate-random-50-char-string-here
   DEBUG = False
   ALLOWED_HOSTS = ritikgaire.com.np,www.ritikgaire.com.np,*.railway.app
   ```

   To generate SECRET_KEY, run in terminal:
   ```powershell
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

5. **Deploy**:
   - Railway will automatically deploy
   - Wait for build to complete (~2-3 minutes)
   - You'll get a URL like: `yourapp.railway.app`

### 3️⃣ Configure Your Domain (ritikgaire.com.np)

**In Railway:**
1. Go to your web service → Settings → Networking
2. Click "Add Custom Domain"
3. Enter: `ritikgaire.com.np`
4. Railway will show you DNS records to add

**In Your Domain Registrar (where you bought ritikgaire.com.np):**
1. Go to DNS Management
2. Add CNAME record:
   - **Type**: CNAME
   - **Name**: `@` (for root domain) or `www` (for www.ritikgaire.com.np)
   - **Value**: The CNAME target Railway provides
   - **TTL**: 3600

3. If your registrar doesn't support CNAME for root domain, add A record instead:
   - Railway will show you the IP address to use

4. Wait 5-60 minutes for DNS propagation

### 4️⃣ Verify Deployment

Visit your site:
- Railway URL: `https://yourapp.railway.app`
- Your domain: `https://ritikgaire.com.np` (after DNS propagates)

**Admin Panel:**
- URL: `https://ritikgaire.com.np/admin/`
- Create superuser (see below)

---

## 🔐 Create Admin User on Railway

**Option 1: Using Railway CLI**
```powershell
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Connect to your project
railway link

# Run command
railway run python manage.py createsuperuser
```

**Option 2: Using Railway Dashboard**
1. Go to your project → Select web service
2. Click "..." → "Service Settings" → "Variables"
3. Add a one-time command variable:
   - Click "New Variable"
   - Raw Editor → Add:
   ```
   RAILWAY_RUN_COMMAND=python manage.py createsuperuser
   ```
4. Redeploy the service
5. Remove the variable after superuser is created

**Option 3: Create via Django Admin (after first deploy)**
Use Railway's shell feature to run:
```bash
python manage.py createsuperuser
```

---

## ✅ Post-Deployment Checklist

- [ ] Site loads at Railway URL
- [ ] Custom domain (ritikgaire.com.np) points to site
- [ ] HTTPS works (automatic with Railway)
- [ ] Admin panel accessible
- [ ] Created superuser account
- [ ] Uploaded profile picture
- [ ] Added project images
- [ ] Tested contact form
- [ ] All static files loading (CSS, JS, images)

---

## 🔧 Common Issues & Solutions

**Issue: Static files not loading**
```powershell
# Locally, test collectstatic
python manage.py collectstatic --noinput
```
Railway runs this automatically, but verify in build logs.

**Issue: Database errors**
- Make sure PostgreSQL is added in Railway
- Check DATABASE_URL is set automatically

**Issue: Domain not working**
- DNS can take up to 24 hours (usually 5-60 minutes)
- Use `nslookup ritikgaire.com.np` to check DNS
- Clear browser cache

**Issue: Admin login not working**
- Verify superuser was created
- Try creating via Railway shell

---

## 📊 Monitoring

Railway Dashboard shows:
- Deployment status
- Build logs
- Application logs
- Resource usage
- Metrics

---

## 💰 Cost

**Railway Free Tier:**
- $5 credit per month (no credit card needed)
- Enough for hobby projects
- Auto-sleeps after inactivity

**Paid Plan:** $5/month if you need more

---

## 🎯 You're Done!

Your portfolio will be live at:
- **https://ritikgaire.com.np** ✨
- Fully managed by Django admin panel
- Automatic HTTPS
- Professional and scalable

**Next Steps:**
1. Share your portfolio link
2. Update content via admin panel
3. Monitor visitor traffic
4. Keep building amazing projects!

---

Need help? Check DEPLOYMENT_GUIDE.md for alternative deployment methods.
