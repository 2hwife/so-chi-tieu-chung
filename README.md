# Sổ Chi Tiêu Chung

Build source for the Android debug APK of the shared family expense book (Capacitor wrapper around www/index.html, which talks to the shared Supabase expenses table).

Pushing to main (or running the workflow manually) builds app-debug.apk on GitHub Actions and uploads it as an artifact named app-debug. The app icon is regenerated at build time by tools/generate_icons.py, so no binary image assets are stored here.
