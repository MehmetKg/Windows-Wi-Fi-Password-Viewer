import subprocess

try:
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], encoding='utf-8', errors='backslashreplace').split('\n')
except subprocess.CalledProcessError as e:
    print(f"Hata: Wi-Fi profilleri alınamadı.\n{e}")
    exit()

profiles = []
for line in data:
    if "All User Profile" in line:
        profile_name = line.split(":")[1].strip()
        profiles.append(profile_name)

for profile in profiles:
    try:
        result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], encoding='utf-8', errors='backslashreplace').split('\n')
        password = None
        for line in result:
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                break
        if password:
            print(f"SSID: {profile}, Password: {password}")
        else:
            print(f"SSID: {profile}, Password: Bulunamadı")
    except subprocess.CalledProcessError as e:
        print(f"Profil alınırken hata oluştu: {profile}\n{e}")
