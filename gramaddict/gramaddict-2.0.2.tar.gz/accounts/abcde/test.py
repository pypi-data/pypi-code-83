tested_ig_version = "185.0.1.39.120"
tested_ig_version_splitted = tested_ig_version.split(".")
running_ig_version = "185.0.1.39.116"
print(f"Instagram version: {running_ig_version}")
running_ig_version_splitted = running_ig_version.split(".")

for n in range(len(running_ig_version_splitted)):
    if int(running_ig_version_splitted[n]) > int(tested_ig_version_splitted[n]):
        print(
            f"You have a newer version of IG then the one we tested! (Tested version: {running_ig_version})"
        )
        break
    else:
        if int(running_ig_version_splitted[n]) == int(tested_ig_version_splitted[n]):
            continue
        break