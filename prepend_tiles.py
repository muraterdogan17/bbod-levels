import os, json

# Path to your levels folder
levels_path = "levels"

# The 19 "0" values to prepend
zeros = ["0"] * 19

for filename in os.listdir(levels_path):
    if filename.endswith(".json"):
        full_path = os.path.join(levels_path, filename)
        with open(full_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Check if "tiles" exists and is a list
        if "tiles" in data and isinstance(data["tiles"], list):
            data["tiles"] = zeros + data["tiles"]

            with open(full_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"✅ Updated {filename}")
        else:
            print(f"⚠️ Skipped {filename} — no 'tiles' list found.")

