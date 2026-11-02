# Adds fleetcommand://join/<ROOM> deep link to the main activity
p='android/app/src/main/AndroidManifest.xml'
s=open(p).read()
f='<intent-filter><action android:name="android.intent.action.VIEW"/><category android:name="android.intent.category.DEFAULT"/><category android:name="android.intent.category.BROWSABLE"/><data android:scheme="fleetcommand" android:host="join"/></intent-filter>'
assert '</activity>' in s
open(p,'w').write(s.replace('</activity>',f+'</activity>',1))
