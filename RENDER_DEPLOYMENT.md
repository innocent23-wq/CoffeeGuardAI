# CoffeeGuard AI - Render Deployment Guide

## Quick Start on Render.com

This guide will help you deploy CoffeeGuard AI to Render.com for fast, reliable hosting.

### Step 1: Prepare Your Repository

1. **Clone or fork the CoffeeGuard repository** on GitHub
2. **Ensure these files are in the root directory:**
   - `Procfile` - Gunicorn configuration
   - `requirements.txt` - Python dependencies
   - `app.py` - Flask application
   - `.env.example` - Environment variables template

### Step 2: Create a Render Service

1. Go to [Render.com](https://render.com) and sign in with GitHub
2. Click "New +" → "Web Service"
3. Connect your GitHub repository containing CoffeeGuard
4. Fill in the details:
   - **Name:** `coffeeguard-ai`
   - **Environment:** Python
   - **Build Command:** `pip install -r requirements.txt && python -c 'import onnxruntime'`
   - **Start Command:** `gunicorn --workers=4 --worker-class=sync --timeout=60 --bind=0.0.0.0:$PORT app:app`
   - **Python Version:** 3.11

### Step 3: Configure Environment Variables

In the Render dashboard, add these environment variables:

| Variable | Value | Notes |
|----------|-------|-------|
| `SECRET_KEY` | Generate a long random string | Keep secure! |
| `SESSION_COOKIE_SECURE` | `true` | Enable secure cookies |
| `FLASK_ENV` | `production` | Production mode |
| `HF_HUB_OFFLINE` | `1` | Use offline model cache |
| `EMAIL_USER` | Your email | For notifications (optional) |
| `EMAIL_PASS` | Your app password | Google App Password (optional) |
| `PYTHONUNBUFFERED` | `true` | Real-time logging |
| `PYTHONDONTWRITEBYTECODE` | `true` | Save memory |

### Step 4: Configure Disk Storage (Optional)

For persistent model cache:

1. Click "Disks" in your service
2. Create a disk with:
   - **Name:** `model_cache`
   - **Size:** 5 GB (or more if needed)
   - **Mount Path:** `/opt/render/project/src/.model_cache`

This keeps the ONNX model cached between deployments, avoiding re-downloads.

### Step 5: Deploy

1. Click "Deploy" to start the initial build
2. Monitor the build logs - it should complete in 2-5 minutes
3. Once deployed, visit your Render URL

## Performance Optimizations Applied

### ✅ Automatic Optimizations Included:

- **Response Compression** - Flask-Compress reduces response size by ~70%
- **Smart Caching** - Static assets cached for days, HTML pages never cached
- **Async Email** - Welcome emails sent in background (non-blocking)
- **Batch Processing** - Concurrent image analysis for speed
- **Connection Pooling** - Efficient database queries
- **Lazy Loading** - Frontend optimizations for faster page loads
- **Gunicorn Workers** - 4 concurrent workers for handling multiple requests

### 📊 Expected Performance:

- **Page Load Time:** < 2 seconds
- **Login Time:** < 1 second
- **Single Image Detection:** 2-3 seconds
- **Batch (10 images):** 10-15 seconds
- **Concurrent Requests:** Support 15-20 simultaneous users

## Health Monitoring

Render will automatically monitor your app's health. The app provides these endpoints:

- `/health` - Full health check (used by Render)
- `/ping` - Quick ping (returns "pong")
- `/status` - Detailed application status

If your app crashes, Render will automatically restart it.

## Dataset Upload Feature

Users can now:
- Upload individual images or ZIP datasets
- Customize leaf naming (Leaf 1-150, or custom prefix)
- Batch process up to 150 images per upload
- Get instant detection results with disease confidence scores

### Supported File Formats:
- **Individual Images:** JPG, PNG, WebP, BMP, TIFF (max 10MB each)
- **Datasets:** ZIP files (max 500MB)

## Optimization Tips

### 1. Reduce Database Queries
- Login uses a single query for all user data
- Dashboard stats cached for 5 minutes per user

### 2. Image Processing
- Images scaled down before detection (improves speed)
- ONNX Runtime uses CPU only (no GPU needed/required)

### 3. Frontend Optimization
- CSS/JS minified and gzipped
- Lazy loading for images
- Minimal re-renders

### 4. Cost Optimization on Render
- Use **free tier** if load is < 100 requests/hour
- Scale to **Starter Plan** for production
- Model cache disk (~$5/month) saves bandwidth

## Troubleshooting

### Build Fails with "Memory Error"
- The build doesn't install PyTorch (intentionally, to save memory)
- If you need it, use a paid Render plan with more RAM

### App Crashes After 30s
- Check if `MODEL_AVAILABLE` shows false in logs
- Verify the ONNX model file (`decafia_best.onnx`) exists
- Check `/status` endpoint for detailed info

### Slow Initial Request
- First request after deploy warms up the model (normal)
- Subsequent requests are fast (< 1 second)

### Email Not Sending
- Verify `EMAIL_USER` and `EMAIL_PASS` are correct
- Use Google App Password (not Gmail password)
- Check email logs in app (if enabled)

## Example Render Environment Setup

Here's a template for your `.env` on Render:

```bash
SECRET_KEY=your-super-secret-key-generate-with-secrets.token_urlsafe(32)
SESSION_COOKIE_SECURE=true
FLASK_ENV=production
HF_HUB_OFFLINE=1
EMAIL_USER=your-email@gmail.com
EMAIL_PASS=your-app-specific-password
PYTHONUNBUFFERED=true
PYTHONDONTWRITEBYTECODE=true
```

## Next Steps

1. **Test the App:** Visit your Render URL and log in
2. **Upload Images:** Test batch upload with 5-10 leaf images
3. **Monitor Performance:** Check Render dashboard for metrics
4. **Scale as Needed:** Upgrade plan if traffic increases

## Support & Updates

- Check app logs: Render Dashboard → Logs
- View health status: `https://your-app.onrender.com/status`
- See all endpoints: `/help` endpoint (if available)

---

**Happy Farming! ☕🌾** - CoffeeGuard AI Team
