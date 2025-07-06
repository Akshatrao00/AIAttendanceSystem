import os

print("\n🔍 DEBUGGING FACE.PY LOCATION ISSUE")
print("📂 Current working directory:", os.getcwd())

print("\n📁 Checking if 'known_faces' folder exists...")

folder_name = "known_faces"
full_path = os.path.join(os.getcwd(), folder_name)

if os.path.exists(full_path):
    print(f"✅ Folder FOUND at: {full_path}")
else:
    print(f"❌ Folder NOT FOUND at: {full_path}")

print("\n📄 Listing contents of current directory:")
for item in os.listdir():
    print("➡️", item)

print("\n✅ DONE.")

