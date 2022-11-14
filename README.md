# Workload Identity GCP

This repo show how you can configure and start use Workload Identity Provider GCP

```yaml
name: "Workload name"
jobs:
  run:
    name: "Example Job name"
    permissions:
      id-token: write
      contents: read
    runs-on: ubuntu-latest
    steps:
      - name: "Auth in GCP"
        id: auth
        uses: "google-github-actions/auth@v1"
        with:
          token_format: "access_token"
          workload_identity_provider: ${{ secrets.GCP_WORKLOAD_IDENTITY_PROVIDER_NAME }}
          service_account: ${{ secrets.GCP_WORKLOAD_IDENTITY_SA_EMAIL }}
          access_token_lifetime: "900s" # Default 3600s

      - name: "Docker login"
        run: |
          echo '${{ steps.auth.outputs.access_token }}' | docker login -u oauth2accesstoken --password-stdin https://eu.gcr.io
```

**Important permissions:**

```yaml
permissions:
  id-token: write
  contents: read
```
