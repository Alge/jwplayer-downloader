import requests
import shutil
import sys

file_name = "w688591160"
file_extension = "mp2t"
first_id = 1

def get_url(file_id):
    return f"https://cdn03.abiliteam.com/stream13.abiliteam.com/ability400/mp4:74775_cam1.mp4/media_w688591160_{file_id}.ts"

i = first_id
while True:
    print(f"Started to download part {i}", end=" ")
    url = get_url(i)
    r = requests.get(url, stream=True)
    print(r.status_code, end=" ")
    if r.status_code == 200:
        with open(f"output/{file_name}-{i}.{file_extension}", 'wb') as f:
            r.raw.decode_content = True
            f.write(r.raw.data)
        print("- done")

    else:
        print("\ngot non ok status code back, probably done (or there was an error). Stopping")
        break

    i += 1


