import kagglehub

# Download latest version
path = kagglehub.dataset_download("pratyushpuri/wearable-health-devices-performance-analysis")

print("Path to dataset files:", path)