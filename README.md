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
