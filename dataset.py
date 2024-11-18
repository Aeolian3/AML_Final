import kagglehub

# Download latest version
path = kagglehub.dataset_download("msarmi9/food101tiny")

print("Path to dataset files:", path)
