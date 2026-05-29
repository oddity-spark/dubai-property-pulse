import json
from urllib.request import Request, urlopen
from pathlib import Path

api_url = "https://data.dubai/o/dda/data-services/dataset-download?datasetId=470061&page=1&pageSize=30&sortDir=desc"

request = Request(
    api_url,
    headers={
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "x-csrf-token": "",
    },
)

with urlopen(request, timeout=30) as response:
    data = json.load(response)

csv_files = []

for folder in data["data"]["metadata"]:
    for file_info in folder["files"]:
        if file_info["file_extension"] == "csv":
            csv_files.append(file_info)

print("CSV files available:")
for i, file_info in enumerate(csv_files):
    size_mb = file_info["file_size"] / (1024 * 1024)
    print(f"{i}: {file_info['file_name']} - {size_mb:.2f} MB")

# Download the smaller CSV file only
file_to_download = csv_files[1]

output_path = Path("data_raw") / file_to_download["file_name"]

print(f"\nDownloading: {file_to_download['file_name']}")
print(f"Saving to: {output_path}")

download_request = Request(
    file_to_download["file_url"],
    headers={"User-Agent": "Mozilla/5.0"},
)

with urlopen(download_request, timeout=300) as response:
    output_path.write_bytes(response.read())

print("Download complete.")