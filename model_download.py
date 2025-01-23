from huggingface_hub import snapshot_download

snapshot_download(
    repo_id= 'meta-llama/Llama-3.1-8B-Instruct',
    revision= 'main',
    local_dir= '/Path/to/your/model',
    token= 'XXXXXX'
)