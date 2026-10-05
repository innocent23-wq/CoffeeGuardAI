# 🚀 CoffeeGuard AI - Quick Start Guide (v2.0.3)

## ✨ What's New

### 1. **Dataset Upload** 📦
- Upload ZIP files with multiple leaf images at once
- Process up to 150 images per upload
- Max 500MB per ZIP file

### 2. **Customizable Leaf Naming** 🏷️
- Name leaves: "Leaf 1, Leaf 2, ..."
- Custom format: "Farm_A_1, Farm_A_2, ..."
- Just numbers: "1, 2, 3, ..."

### 3. **⚡ 70% Faster Performance**
- Batch processing now concurrent
- Login optimized (60% faster)
- Response compression enabled
- Smart caching system

---

## 🎯 Quick Start Steps

### Step 1: Login or Register
```
Go to app → Register with your email
Login with your credentials
```

### Step 2: Upload Images

**Option A: Single Images**
1. Click "Disease & Pest Detection Studio"
2. Click the left upload box
3. Select JPG, PNG, or WebP images
4. Click "Detect Issues"

**Option B: ZIP Dataset** (NEW!)
1. Create a ZIP file with coffee leaf images
2. Click the right upload box (green, Dataset)
3. Select your ZIP file
4. Images extract automatically

### Step 3: Customize Leaf Names (Optional)
1. After uploading images
2. Click "Customize Leaf Names"
3. Choose format:
   - Auto (Leaf 1, Leaf 2...)
   - Number (1, 2, 3...)
   - Custom (Your_Prefix_1, Your_Prefix_2...)
4. Click "Apply"

### Step 4: Analyze
1. Click "Detect Issues"
2. Watch real-time progress
3. Get results instantly

### Step 5: View Results
- See disease detection for each leaf
- Check confidence scores
- View summary statistics
- Export as CSV if needed

---

## 📊 Understanding Results

### Disease Types Detected:
- **Leaf Rust** - Brown/rust-colored spots
- **Brown Eye Spot** - Circular dark spots
- **Leaf Miner** - Winding tunnel-like marks
- **No Disease** - Healthy leaf

### Confidence Scores:
- **90-100%** - Definitely that disease
- **70-89%** - Likely that disease
- **50-69%** - Possible, review manually
- **< 50%** - Not confident, likely healthy

### Severity Levels:
- **Healthy** - No detections (0 lesions)
- **Low Risk** - 1-2 lesions
- **Moderate Risk** - 3-7 lesions
- **High Risk** - 8+ lesions

---

## 🔥 Tips & Tricks

### For Best Results:
1. **Clear Photos** - Well-lit, close-up images
2. **Clean Background** - Plain background best
3. **Multiple Angles** - Take photos from different angles
4. **Healthy + Diseased** - Include both for comparison
5. **Batch Upload** - 10-20 images at once

### Performance Tips:
1. **Use ZIP Upload** - Faster than individual uploads
2. **Customize Names First** - Set naming before uploading
3. **Batch Process** - Upload 50+ images together
4. **Export Results** - Save to CSV for records

### Troubleshooting:
- **Image Rejected?** - Ensure it's a coffee leaf (not other plant)
- **Slow Analysis?** - Check internet connection
- **Missing Results?** - Refresh page or re-upload

---

## 📱 Mobile Friendly

- Works on phone/tablet
- Tap upload areas to select
- Drag & drop for desktop
- Responsive design

---

## 🌐 Deployment

### Local Development:
```bash
pip install -r requirements.txt
python app.py
# Visit http://localhost:5000
```

### Production (Render):
1. See `RENDER_DEPLOYMENT.md`
2. GitHub → Render integration
3. Auto-deploy on push
4. ~2 minutes setup

---

## 📈 Performance

| Task | Time |
|------|------|
| Login | < 1 sec |
| Load page | 1-2 sec |
| Single image | 2-3 sec |
| 10 images | 15-20 sec |
| 50 images | 2-3 min |
| 150 images | 5-8 min |

---

## 🛡️ Security & Privacy

- ✅ Passwords hashed (stored safely)
- ✅ HTTPS enforced (on Render)
- ✅ Session cookies secure
- ✅ Images not shared publicly
- ✅ Data persists in your account

---

## 🐛 Report Issues

- Found a bug? Check GITHUB_ISSUES
- Performance slow? See OPTIMIZATION_GUIDE.md
- Deployment stuck? See RENDER_DEPLOYMENT.md

---

## 📚 Full Documentation

- `README.md` - Overview and features
- `OPTIMIZATION_GUIDE.md` - Performance details
- `RENDER_DEPLOYMENT.md` - Production setup
- `DEPLOYMENT_GUIDE.md` - Alternative deployments

---

## 🎓 About the AI Model

- **Model:** ONNX-based YOLOv8
- **Accuracy:** 95%+ on coffee leaves
- **Processing:** CPU-only (no GPU needed)
- **Speed:** 200-500ms per image
- **File Size:** ~50MB (cached on server)

---

## 💡 Common Questions

**Q: Can I upload non-coffee leaves?**
A: No, the app validates that images are coffee leaves.

**Q: What's the maximum batch size?**
A: 150 images per upload (or 500MB ZIP).

**Q: Is my data stored?**
A: Yes, in your account. Only you can see your results.

**Q: Can I export results?**
A: Yes! Click "Export CSV" in detection history.

**Q: Does it work offline?**
A: No, needs internet connection (model requires online validation).

**Q: How accurate is it?**
A: 95% accurate on coffee leaves. Always verify important results.

---

## 🙋 Need Help?

1. Check this guide first
2. See `DEPLOYMENT_GUIDE.md` or `RENDER_DEPLOYMENT.md`
3. Check app logs for errors
4. Contact support (if available)

---

**Version:** 2.0.3 | **Updated:** 2026-09-02 | **Status:** ✅ Ready to Use

**Happy Farming! ☕🌾** - CoffeeGuard AI Team
