# Fleet Command – APK

## Cloud build (no Android Studio)
1. Push this folder to a GitHub repo.
2. Actions tab → "Build APK" → run (also runs on push).
3. Download the `fleet-command-apk` artifact → `app-debug.apk`, install on the phone.

## Local build
Needs Node 18+, JDK 17, Android SDK.

    npm install
    npx cap add android && npx cap sync android
    cd android && ./gradlew assembleDebug

APK: android/app/build/outputs/apk/debug/app-debug.apk
(or `npx cap open android` → Build > Build APK in Android Studio)

Edit the game in `www/index.html`, then `npx cap sync android`.

## Web version (laptop + phone browser, WebRTC works)
Repo Settings → Pages → Source: **GitHub Actions**. Push to `main`; the "Deploy Pages" workflow
publishes `www/` at `https://<user>.github.io/<repo>/`. Open it on the laptop (host) and phone (guest); the guest just types the room ID.

## Invite links
- The host shows `https://<user>.github.io/<repo>/#ROOM` (needs the Pages deploy above).
- On Android, that page has an **Open in app** button (deep link `fleetcommand://join/ROOM`); if the app isn’t installed it stays in the browser.
- Tapping the https link in a chat opens the browser first. Opening the app directly from the https link needs Android App Links (assetlinks.json on the domain root + a fixed signing key), which github.io project pages can’t serve.
