import json
data = None
with open("data/adopt_your_spot_geocoded.json", "r") as f:
    data = json.load(f)


def normalize_tokens(text):
    text = text.lower()
    text = text.replace(",", " ")
    text = text.replace(".", " ")
    text = text.replace("/", " ")
    tokens = text.split()
    result = []
    for t in tokens:
        if t.endswith("ss") or t.endswith("us") or t.endswith("es") or t.endswith("os") or t.endswith("as") or t.endswith("is"):
            result.append(t)
        elif t.endswith("s"):
            result.append(t[:-1])
        else:
            result.append(t)
    return result


def search_text(text, search):
    normalized = normalize_tokens(text)
    for phrase in search:
        if phrase in normalized:
            return True
        elif " " in phrase and phrase in text:
            return True
    return False

name_counts = {}
reason_counts = {}

for entry in data:
    if "name_keywords" not in entry:
        entry["name_keywords"] = {}

    def add_key(key, text, search):
        found = search_text(text, search)
        entry["name_keywords"][key] = found
        if found:
            if key not in name_counts:
                name_counts[key] = 0
            name_counts[key] += 1
    add_key("tree", entry["name"], ["tree", "trees"])
    add_key("station", entry["name"], [
            "station", "subway", "train", "bus", "buses", "track", "rail"])
    add_key("sidewalk", entry["name"], ["sidewalk", "side walk", "path"])
    add_key("house", entry["name"], ["house", "houses", "home", "homes"])
    add_key("apartment", entry["name"], [
            "apartment", "condo", "condos", "building"])
    add_key("block", entry["name"], ["block"])
    add_key("park", entry["name"], ["park", "playground"])
    add_key("intersection", entry["name"], ["intersection", "corner"])
    add_key("underpass/overpass", entry["name"],
            ["underpass", "overpass", "bridge", "tunnel"])
    add_key("garden", entry["name"], [
            "garden", "flower", "grass", "lawn", "planter"])
    add_key("fountain", entry["name"], ["fountain"])
    add_key("vacant", entry["name"], ["abandon", "abandoned",
            "vacant", "unoccupied", "neglect", "neglected"])
    add_key("construction", entry["name"], ["construction"])
    add_key("drain", entry["name"], [
            "grate", "grates", "drain", "basin", "gutter"])
    add_key("shop", entry["name"], [
            "business", "businesses", "shop", "restaurant", "store", "stores"])
    add_key("beach", entry["name"], ["beach", "beaches"])
    add_key("school", entry["name"], ["school", "preschool", "kindergarden"])
    add_key("bench", entry["name"], ["bench", "benches"])

    if "reason_keywords" not in entry:
        entry["reason_keywords"] = {}

    def add_key(key, text, search):
        found = search_text(text, search)
        entry["reason_keywords"][key] = found
        if found:
            if key not in reason_counts:
                reason_counts[key] = 0
            reason_counts[key] += 1
    add_key(
        "live", entry["Can you tell us why you have selected this spot?"], ["live", "living", "lived", "lives"])
    add_key("walk", entry["Can you tell us why you have selected this spot?"], [
            "walk", "stroll", "walking", "walked", "strolling", "strolled"])
    add_key("run", entry["Can you tell us why you have selected this spot?"], [
            "run", "jog", "jogging", "running", "jogger", "runner", "jogged", "ran"])
    add_key(
        "dog", entry["Can you tell us why you have selected this spot?"], ["dog", "pet"])
    add_key(
        "sunset", entry["Can you tell us why you have selected this spot?"], ["sunset"])
    add_key("child", entry["Can you tell us why you have selected this spot?"], [
            "child", "children", "kid"])
    add_key(
        "play", entry["Can you tell us why you have selected this spot?"], ["play", "playing"])
    add_key("tired", entry["Can you tell us why you have selected this spot?"], [
            "tired", "sick", "frustrated", "frustrating"])
    add_key("hope", entry["Can you tell us why you have selected this spot?"], [
            "hope", "wish"])
    add_key("everyday", entry["Can you tell us why you have selected this spot?"], [
            "every day", "everyday", "daily"])
    add_key("near", entry["Can you tell us why you have selected this spot?"], [
            "near", "nearby"])
    add_key("beautiful", entry["Can you tell us why you have selected this spot?"], [
            "beautiful", "beauty", "pretty"])
    add_key("pride", entry["Can you tell us why you have selected this spot?"], [
            "pride", "proud"])
    add_key("help", entry["Can you tell us why you have selected this spot?"], [
            "help", "contribute", "contributing", "give back"])
    add_key("community", entry["Can you tell us why you have selected this spot?"], [
            "community", "shared", "share"])
    add_key("neighborhood", entry["Can you tell us why you have selected this spot?"], [
            "neighborhood"])
    add_key("neglect", entry["Can you tell us why you have selected this spot?"], [
            "abandoned", "abandon", "vacant", "unoccupied", "neglect", "neglected"])
    add_key("busy", entry["Can you tell us why you have selected this spot?"], [
            "busy", "traffic", "pedestrian"])
    add_key("flood", entry["Can you tell us why you have selected this spot?"], [
            "flood", "flooded", "flooding"])
    add_key("family", entry["Can you tell us why you have selected this spot?"], [
            "family", "parent", "relative", "relatives"])
    add_key(
        "care", entry["Can you tell us why you have selected this spot?"], ["care"])
    add_key(
        "rats", entry["Can you tell us why you have selected this spot?"], ["rat"])
    add_key("environment", entry["Can you tell us why you have selected this spot?"], [
            "environment", "nature", "animal", "wild", "wildlife"])
    add_key("already", entry["Can you tell us why you have selected this spot?"], [
        "already"])

with open("data/adopt_your_spot_geocoded.json", "w") as f:
    json.dump(data, f, indent=4)

print("names:")
for k, n in sorted(name_counts.items(), key=lambda x: x[1], reverse=True):
    print(k, n)
print("reasons:")
for k, n in sorted(reason_counts.items(), key=lambda x: x[1], reverse=True):
    print(k, n)
